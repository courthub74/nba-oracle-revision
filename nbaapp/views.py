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


#PHILADELPHIA 76ERS
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


#TORONTO RAPTORS
def tor(request):
    import requests
    import json

    # RAPTORS General Info 134864
    torreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Toronto_Raptors")
    tor_info = json.loads(torreq.content)

    # RAPTORS Last Game 134864
    torlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134864")
    tor_last = json.loads(torlast.content)

    # RAPTORS Next Game 134864
    tornext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134864")
    tor_next = json.loads(tornext.content)

    return render(request, "teams/eastern/toronto.html", {'tor_info': tor_info, 'tor_last': tor_last, 'tor_next': tor_next})


#WASHINGTON WIZARDS
def was(request):
    import requests
    import json

    # WIZARDS General Info 134884
    wasreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Washington_Wizards")
    was_info = json.loads(wasreq.content)

    # WIZARDS Last Game 134884
    waslast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134884")
    was_last = json.loads(waslast.content)

    # WIZARDS Next Game 134884
    wasnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134884")
    was_next = json.loads(wasnext.content)

    return render(request, "teams/eastern/washington.html", {'was_info': was_info, 'was_last': was_last, 'was_next': was_next})


###################################################################################

#WESTERN CONFERENCE

###################################################################################

#DALLAS MAVERICKS
def dal(request):
    import requests
    import json 

    # MAVERICKS General Info 134875
    dalreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Dallas%20Mavericks")
    dal_info = json.loads(dalreq.content)

    # MAVERICKS Last Game 134875
    dallast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134875")
    dal_last = json.loads(dallast.content)

    # MAVERICKS Next Game 134875
    dalnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134875")
    dal_next = json.loads(dalnext.content)

    return render(request, "teams/western/dallas.html", {'dal_info': dal_info, 'dal_last': dal_last, 'dal_next': dal_next})


#DENVER NUGGETS
def den(request):
    import requests
    import json 

    # NUGGETS General Info 134885
    denreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Denver_Nuggets")
    den_info = json.loads(denreq.content)

    # NUGGETS Last Game 134885
    denlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134885")
    den_last = json.loads(denlast.content)
    
    # NUGGETS Next Game 134885
    dennext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134885")
    den_next = json.loads(dennext.content)

    return render(request, "teams/western/denver.html", {'den_info': den_info, 'den_last': den_last, 'den_next': den_next})


#GOLDEN STATE WARRIORS
def gsw(request):
    import requests
    import json 

    # NUGGETS General Info 134885
    gswreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Golden%20State%20Warriors")
    gsw_info = json.loads(gswreq.content)

    # NUGGETS Last Game 134885
    gswlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134865")
    gsw_last = json.loads(gswlast.content)

    # NUGGETS Next Game 134885
    gswnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134865")
    gsw_next = json.loads(gswnext.content)

    return render(request, "teams/western/goldenstate.html", {'gsw_info': gsw_info, 'gsw_last': gsw_last, 'gsw_next': gsw_next})


#GOLDEN STATE WARRIORS
def gsw(request):
    import requests
    import json 

    # WARRIORS General Info 134865
    gswreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Golden%20State%20Warriors")
    gsw_info = json.loads(gswreq.content)

    # WARRIORS Last Game 134865
    gswlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134865")
    gsw_last = json.loads(gswlast.content)

    # WARRIORS Next Game 134865
    gswnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134865")
    gsw_next = json.loads(gswnext.content)

    return render(request, "teams/western/goldenstate.html", {'gsw_info': gsw_info, 'gsw_last': gsw_last, 'gsw_next': gsw_next})


#HOUSTON ROCKETS
def hou(request):
    import requests
    import json 

    # ROCKETS General Info 134876
    houreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Houston%20Rockets")
    hou_info = json.loads(houreq.content)

    # ROCKETS Last Game 134876
    houlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134876")
    hou_last = json.loads(houlast.content)

    # ROCKETS Next Game 134876
    hounext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134876")
    hou_next = json.loads(hounext.content)

    return render(request, "teams/western/houston.html", {'hou_info': hou_info, 'hou_last': hou_last, 'hou_next': hou_next})


#LOS ANGELES CLIPPERS
def lac(request):
    import requests
    import json 

    # CLIPPERS General Info 134866
    lacreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Los%20Angeles%20Clippers")
    lac_info = json.loads(lacreq.content)

    # CLIPPERS last game info 134866
    laclast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134866")
    lac_last = json.loads(laclast.content)

    # CLIPPERS next game info 134866
    lacnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134866")
    lac_next = json.loads(lacnext.content)

    return render(request, "teams/western/laclippers.html", {'lac_info': lac_info, 'lac_last': lac_last, 'lac_next': lac_next})


#LOS ANGELES LAKERS
def lal(request):
    import requests
    import json 

    # LAKERS General Info 134867
    lalreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Los_Angeles_Lakers")
    lal_info = json.loads(lalreq.content)

    # LAKERS last game info 134867
    lallast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134867")
    lal_last = json.loads(lallast.content)

    # LAKERS next game info 134867
    lalnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134867")
    lal_next = json.loads(lalnext.content)

    return render(request, "teams/western/lalakers.html", {'lal_info': lal_info, 'lal_last': lal_last, 'lal_next': lal_next})


#MEMPHIS GRIZZLIES
def mem(request):
    import requests
    import json 

    # GRIZZLIES General Info 134877
    memreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Memphis_Grizzlies")
    mem_info = json.loads(memreq.content)

    # GRIZZLIES last game info 134877
    memlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134877")
    mem_last = json.loads(memlast.content)

    # GRIZZLIES next game info 134877
    memnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134877")
    mem_next = json.loads(memnext.content)

    return render(request, "teams/western/memphis.html", {'mem_info': mem_info, 'mem_last': mem_last, 'mem_next': mem_next})


#MINNESOTA TIMBERWOLVES
def min(request):
    import requests
    import json 

    # T-WOLVES General Info 134886
    minreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Memphis_Grizzlies")
    min_info = json.loads(minreq.content)

    # T-WOLVES Last Game Info
    minlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134886")
    min_last = json.loads(minlast.content)

    # T-WOLVES Next Game Info
    minnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134886")
    min_next = json.loads(minnext.content)

    return render(request, "teams/western/minnesota.html", {'min_info': min_info, 'min_last': min_last, 'min_next': min_next})


#NEW ORLEANS PELICANS
def nola(request):
    import requests
    import json 

    # PELICANS General Info 134878
    nolareq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=New%20Orleans%20Pelicans")
    nola_info = json.loads(nolareq.content)

    # PELICANS Last Game 134878
    nolalast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134878")
    nola_last = json.loads(nolalast.content)

    # PELICANS Next Game 134878
    nolanext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134878")
    nola_next = json.loads(nolanext.content)

    return render(request, "teams/western/neworleans.html", {'nola_info': nola_info, 'nola_last': nola_last, 'nola_next': nola_next})


#OKLAHOMA CITY THUNDER
def okc(request):
    import requests
    import json 

    # PELICANS General Info 134878
    okcreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Oklahoma_City_Thunder")
    okc_info = json.loads(okcreq.content)

    # PELICANS Last Game 134878
    okclast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134887")
    okc_last = json.loads(okclast.content)

    # PELICANS Next Game 134878
    okcnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134887")
    okc_next = json.loads(okcnext.content)

    return render(request, "teams/western/okcthunder.html", {'okc_info': okc_info, 'okc_last': okc_last, 'okc_next': okc_next})


#PORTLAND TRAILBLAZERS
def por(request):
    import requests
    import json 

    # PELICANS General Info 134878
    porreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Portland_Trail_Blazers")
    por_info = json.loads(porreq.content)

    # PELICANS Last Game 134878
    porlast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134888")
    por_last = json.loads(porlast.content)

    # PELICANS Next Game 134878
    pornext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134888")
    por_next = json.loads(pornext.content)

    return render(request, "teams/western/portland.html", {'por_info': por_info, 'por_last': por_last, 'por_next': por_next})


#SAN ANTONIO SPURS
def sas(request):
    import requests
    import json 

    # SPURS General Info 134879
    sasreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=San_Antonio_Spurs")
    sas_info = json.loads(sasreq.content)

    # SPURS Last Game 134879
    saslast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134879")
    sas_last = json.loads(saslast.content)

    # SPURS Next Game 134879
    sasnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134879")
    sas_next = json.loads(sasnext.content)

    return render(request, "teams/western/sanantonio.html", {'sas_info': sas_info, 'sas_last': sas_last, 'sas_next': sas_next})


#SACRAMENTO KINGS
def sac(request):
    import requests
    import json 

    # KINGS General Info 134869
    sacreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Sacramento_Kings")
    sac_info = json.loads(sacreq.content)

    # KINGS Last Game 134869
    saclast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134869")
    sac_last = json.loads(saclast.content)

    # KINGS Next Game 134869
    sacnext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134869")
    sac_next = json.loads(sacnext.content)

    return render(request, "teams/western/sacramento.html", {'sac_info': sac_info, 'sac_last': sac_last, 'sac_next': sac_next})


#PHOENIX SUNS
def pho(request):
    import requests
    import json 

    # SUNS General Info 134868
    phoreq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Phoenix_Suns")
    pho_info = json.loads(phoreq.content)

    # KINGS Last Game 134869
    pholast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134868")
    pho_last = json.loads(pholast.content)

    # KINGS Next Game 134869
    phonext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134868")
    pho_next = json.loads(phonext.content)

    return render(request, "teams/western/phoenix.html", {'pho_info': pho_info, 'pho_last': pho_last, 'pho_next': pho_next})


#UTAH JAZZ
def uta(request):
    import requests
    import json 

    # JAZZ General Info 134889
    utareq = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/searchteams.php?t=Utah_jazz")
    uta_info = json.loads(utareq.content)

    # JAZZ Last Game 134889
    utalast = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134889")
    uta_last = json.loads(utalast.content)

    # JAZZ Next Game 134889
    utanext = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134889")
    uta_next = json.loads(utanext.content)

    return render(request, "teams/western/utah.html", {'uta_info': uta_info, 'uta_last': uta_last, 'uta_next': uta_next})



