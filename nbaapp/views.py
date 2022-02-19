from urllib import request
from django.shortcuts import render
import requests
import json

#HOME
def home(request):
    return render(request, "home.html", {})

###################################################################################

#TEAMS (API Request)

###################################################################################

#EASTERN CONFERENCE

###################################################################################

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

    return render(request, "teams/eastern/atlanta.html", {'atl_info': atl_info, 'atl_last': atl_last, 'atl_next': atl_next})


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

    return render(request, "teams/eastern/boston.html", {'bos_info': bos_info, 'bos_last': bos_last, 'bos_next': bos_next})


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


    return render(request, "teams/eastern/brooklyn.html", {'bklyn_info':bklyn_info, 'bklyn_last': bklyn_last, 'bklyn_next': bklyn_next})


#CHARLOTTE HORNETS
def char(request):
    import requests 
    import json 

    # HORNETS General Info 134881
    charreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Charlotte%20Hornets")
    char_info = json.loads(charreq.content)

    # HORNETS Last Game Info 134881
    charlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134881")
    char_last = json.loads(charlast.content)

    # HORNETS Next Game Info 134881
    charnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134881")
    char_next = json.loads(charnext.content)

    return render(request, "teams/eastern/charlotte.html", {'char_info': char_info, 'char_last': char_last, 'char_next': char_next})


#CHICAGO BULLS
def chi(request):
    import requests
    import json 

    # BULLS General Info 134870
    chireq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Chicago%20Bulls")
    chi_info = json.loads(chireq.content)

    # BULLS Last Game Info 134870
    chilast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134870")
    chi_last = json.loads(chilast.content)

    # BULLS Next Game Info 134870
    chinext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134870")
    chi_next = json.loads(chinext.content)

    return render(request, "teams/eastern/chicago.html", {'chi_info': chi_info, 'chi_last': chi_last, 'chi_next': chi_next})


#CLEVELAND CAVALIERS
def cle(request):
    import requests
    import json 

    # CAVALIERS General Info 134871
    clereq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Cleveland%20Cavaliers")
    cle_info = json.loads(clereq.content)

    # CAVALIERS Last Game 134871
    clelast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134871")
    cle_last = json.loads(clelast.content)

    # CAVALIERS Next Game 134871
    clenext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134871")
    cle_next = json.loads(clenext.content)

    return render(request, "teams/eastern/cleveland.html", {'cle_info': cle_info, 'cle_last': cle_last, 'cle_next': cle_next})


#DETROIT PISTONS
def det(request):
    import requests
    import json 

    # PISTONS General Info 134872
    detreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Detroit%20Pistons")
    det_info = json.loads(detreq.content)
    # PISTONS Last Game 134872
    detlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134872")
    det_last = json.loads(detlast.content)
    # PISTONS Next Game 134872
    detnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134872")
    det_next = json.loads(detnext.content)

    return render(request, "teams/eastern/detroit.html", {'det_info': det_info, 'det_last': det_last, 'det_next': det_next})

#INDIANA PACERS
def ind(request):
    import requests
    import json

    # PACERS General Info 134873
    indreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Indiana%20Pacers")
    ind_info = json.loads(indreq.content)

    # PACERS Last Game Info
    indlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134873")
    ind_last = json.loads(indlast.content)
    # PACERS Next Game Info
    indnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134873")
    ind_next = json.loads(indnext.content)

    return render(request, "teams/eastern/indiana.html", {'ind_info': ind_info, 'ind_last': ind_last, 'ind_next': ind_next})



    