# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from books.models import Book

# Create your views here.

def books(request):
	ua = request.META.get('HTTP_USER_AGENT', 'unknow')
	return HttpResponse('Your browser is %s' % ua)

def search_books(request):
	books = []
	if request.GET.get('q'):
		q = request.GET['q']
		books = Book.objects.filter(title__icontains = q)
	return render_to_response('search_books.html', {'books':books})
