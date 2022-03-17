from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>hello django</h1>')

def about(request):
    return HttpResponse('<h1>A propos</h1><p>Nous aimons merch</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1><p>Liste des elements</p>')

def contact(request):
    return HttpResponse('<h1>Nous contacter</h1><p>Page de contact<p>')