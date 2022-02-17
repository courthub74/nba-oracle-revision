from django.shortcuts import render

#HOME
def home(request):
    return render(request, "home.html", {})

###################################################################################

#TEAMS

#ATLANTA HAWKS
def hawks(request):
    import requests
    import json 

# ATLANTA General Info 134880





