from ast import Return
from asyncore import write
import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# created request (argument) in function idx 
def idx(request):
    response = HttpResponse()
    response.writelines("<p>Hello world!</p>")
    response.writelines("<p>Hello world!</p>")
    response.writelines("<p>Hello world!</p>")
    response.writelines("<p>Hello world!</p>")

    return response














