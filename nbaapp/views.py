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

    # ATLANTA Last Game 134880
    atllast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134880")
    atl_last = json.loads(atllast.content)

    # ATLANTA Next Game 134880
    atlnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134880")
    atl_next = json.loads(atlnext.content)

    return render(request, "teams/atlanta.html", {'atl_info': atl_info, 'atl_last': atl_last, 'atl_next': atl_next})


#BOSTON CELTICS
def bos(request):
    import requests
    import json 

    #BOSTON General Info 134860
    bosreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Boston%20Celtics")
    bos_info = json.loads(bosreq.content)

    #BOSTON Last Game 134860
    boslast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134860")
    bos_last = json.loads(boslast.content)

    #BOSTON Next Game 134860
    bosnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134860")
    bos_next = json.loads(bosnext.content)

    return render(request, "teams/boston.html", {'bos_info': bos_info, 'bos_last': bos_last, 'bos_next': bos_next})

#BROOKLYN NETS
def bklyn(request):
    import requests
    import json

    # NETS General Info 134861
    bklynreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Brooklyn%20Nets")
    bklyn_info = json.loads(bklynreq.content)

    # NETS Last Game 134861
    bklynlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134861")
    bklyn_last = json.loads(bklynlast.content)

    # NETS Next Game 134861
    bklynnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134861")
    bklyn_next = json.loads(bklynnext.content)


    return render(request, "teams/brooklyn.html", {'bklyn_info':bklyn_info, 'bklyn_last': bklyn_last, 'bklyn_next': bklyn_next})








