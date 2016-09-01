# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST, require_GET
from .models import Candidate, Voivodeship, District
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.renderers import JSONRenderer
from .serializers import DistrictSerializer, CandidateSerializer, VoivodeshipSerializer
from django.views.decorators.csrf import csrf_exempt


@require_GET
def listDistricts(request):
    districts = District.objects.all()
    serializer = DistrictSerializer(districts, many=True)
    content = JSONRenderer().render(serializer.data)
    response = HttpResponse(content, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response


@require_GET
def listVoivodeships(request):
    voivodeships = Voivodeship.objects.all()
    serializer = VoivodeshipSerializer(voivodeships, many=True)
    content = JSONRenderer().render(serializer.data)
    response = HttpResponse(content, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response


@require_GET
def listCandidates(request):
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    content = JSONRenderer().render(serializer.data)
    response = HttpResponse(content, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response


@require_GET
def editing_byinh(request):
	lb = request.GET['lower']
	ub = request.GET['upper']
	data = serializers.serialize('json',District.objects.filter(Inhabitants__range=[lb,ub]))
	response = HttpResponse(data)
	response["Access-Control-Allow-Origin"] = "*"
	return response;


@require_GET
def editing_byvoiv(request):
	vname = request.GET['name']
	data = serializers.serialize('json', District.objects.filter(voivodeship__Name=vname))
	response = HttpResponse(data)
	response["Access-Control-Allow-Origin"] = "*"
	return response;


@require_GET
def editing_bytype(request):
	tName = request.GET['name']
	data = serializers.serialize('json', District.objects.filter(Type=tName))
	response = HttpResponse(data)
	response["Access-Control-Allow-Origin"] = "*"
	return response;

@csrf_exempt
def editing_save(request):
	if request.method == 'GET':
		dn = request.GET['dn']
		last_edit = District.objects.filter(Name=dn).values('last_edit_date')
		response = HttpResponse(last_edit[0]['last_edit_date'])
		response["Access-Control-Allow-Origin"] = "*"
		return response
	if request.method == 'POST':
		v1 = request.POST['v1']
		v2 = request.POST['v2']
		rel_v = int(v1) + int(v2)
		dn = request.POST['dn']
		dis = District.objects.get(Name=dn)
		dis.votes_for_first = v1
		dis.relevant_votes = rel_v
		dis.save()
		response = HttpResponse();
		response["Access-Control-Allow-Origin"] = "*"
		return HttpResponse();
