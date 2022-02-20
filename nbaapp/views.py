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

#MIAMI HEAT
def mia(request):
    import requests
    import json

    # HEAT General Info 134882
    miareq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Miami_Heat")
    mia_info = json.loads(miareq.content)

    # Last Game Info HEAT 134882
    mialast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134882")
    mia_last = json.loads(mialast.content)

    # Next Game Info HEAT 134882
    mianext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134882")
    mia_next = json.loads(mianext.content)

    return render(request, "teams/eastern/miami.html", {'mia_info': mia_info, 'mia_last': mia_last, 'mia_next': mia_next})


#MILWAUKEE BUCKS
def mil(request):
    import requests
    import json

    # HEAT General Info 134882
    milreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Milwaukee_Bucks")
    mil_info = json.loads(milreq.content)

    # Last Game Info HEAT 134882
    millast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134874")
    mil_last = json.loads(millast.content)

    # Next Game Info HEAT 134882
    milnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134874")
    mil_next = json.loads(milnext.content)

    return render(request, "teams/eastern/milwaukee.html", {'mil_info': mil_info, 'mil_last': mil_last, 'mil_next': mil_next})


#NEW YORK KNICKS
def nyc(request):
    import requests
    import json

    # KNICKS General Info 134862
    nycreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=new_york_knicks")
    nyc_info = json.loads(nycreq.content)

    # KNICKS Last Game 134862
    nyclast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134862")
    nyc_last = json.loads(nyclast.content)

    # KNICKS Next Game 134862
    nycnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134862")
    nyc_next = json.loads(nycnext.content)

    return render(request, "teams/eastern/newyork.html", {'nyc_info': nyc_info, 'nyc_last': nyc_last, 'nyc_next': nyc_next})


#ORLANDO MAGIC
def orl(request):
    import requests
    import json

    # KNICKS General Info 134862
    orlreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Orlando_Magic")
    orl_info = json.loads(orlreq.content)

    # KNICKS Last Game 134862
    orllast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134883")
    orl_last = json.loads(orllast.content)

    # KNICKS Next Game 134862
    orlnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134883")
    orl_next = json.loads(orlnext.content)

    return render(request, "teams/eastern/orlando.html", {'orl_info': orl_info, 'orl_last': orl_last, 'orl_next': orl_next})


#ORLANDO MAGIC
def phi(request):
    import requests
    import json

    #SIXERS General Info 134863
    phireq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=philadelphia_76ers")
    phi_info = json.loads(phireq.content)

    #SIXERS Last Game 134863
    philast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134863")
    phi_last = json.loads(philast.content)

    #SIXERS Next Game 134863
    phinext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134863")
    phi_next = json.loads(phinext.content)

    return render(request, "teams/eastern/philadelphia.html", {'phi_info': phi_info, 'phi_last': phi_last, 'phi_next': phi_next})



    