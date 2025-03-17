from django.shortcuts import render

# Aqui irão ficar as viws (controladores) ref ao sistema


def index(request):
    return render(
        request,
        'sistema/index.html',
    )
   


