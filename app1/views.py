from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(r):
    return HttpResponse(
        "<h1 align='center'>Welcome to Home Page</h1></br>"
        "<p>This site is only testing purpos</P></br>"
        )