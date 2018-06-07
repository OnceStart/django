# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

# Create your views here.

def hello(request):
	current_date = datetime.datetime.now()
	return render_to_response('hello.html', locals())
