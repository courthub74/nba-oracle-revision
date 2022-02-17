from urllib import request
from django.shortcuts import render
import requests
import json

#HOME
def home(request):
    return render(request, "home.html", {})

###################################################################################

#TEAMS (API Request)

#ATLANTA HAWKS
def atl(request):
    import requests
    import json

    # ATLANTA General Info 134880
    atlreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Atlanta%20Hawks")
    atl_info = json.loads(atlreq.content)

    return render(request, "teams/atlanta.html", {'atl_info': atl_info})


#BOSTON CELTICS
def bos(request):
    import requests
    import json 

    #BOSTON General Info 134860
    bosreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Boston%20Celtics")
    bos_info = json.loads(bosreq.content)

    return render(request, "teams/boston.html", {'bos_info': bos_info})








