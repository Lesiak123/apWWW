from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
# Create your views here.
from .models import Candidate, Voivodeship, VotingResult, District
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie


def index(request):
    voivodeship_list = Voivodeship.objects.order_by('Nr')
    candidates = Candidate.objects.order_by('Name')
    template = loader.get_template('PKW/index.html')
    context = {
        'voivodeship_list': voivodeship_list,
        'candidates': candidates,
    }
    return HttpResponse(template.render(context,request))

@require_POST
def loginView(request):
    user = authenticate(username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/PKW")
    else:
        return HttpResponseForbidden("Bad username or password.")

def editing_byinh(request):
    if request.method == 'GET':
        lb = request.GET['lower']
        ub = request.GET['upper']
        data = serializers.serialize('json',District.objects.filter(Inhabitants__range=[lb,ub]))
        return HttpResponse(data)

def editing_byvoiv(request):
    if request.method == 'GET':
        vname = request.GET['name']
        data = serializers.serialize('json', District.objects.filter(voivodeship__Name=vname))
        return HttpResponse(data)

def editing_bytype(request):
    if request.method == 'GET':
        tName = request.GET['name']
        data = serializers.serialize('json', District.objects.filter(Type=tName))
        return HttpResponse(data)

def editing_save(request):
    if request.method == 'GET':
        dn = request.GET['dn']
        last_edit = District.objects.filter(Name=dn).values('last_edit_date')
        return HttpResponse(last_edit[0]['last_edit_date'])
    if request.method == 'POST':
        v1 = request.POST['v1']
        v2 = request.POST['v2']
        rel_v = int(v1) + int(v2)
        dn = request.POST['dn']
        dis = District.objects.get(Name=dn)
        dis.votes_for_first = v1
        dis.relevant_votes = rel_v
        dis.save()
        return HttpResponse();