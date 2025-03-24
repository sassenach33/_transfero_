from django.shortcuts import render

# Aqui irão ficar as viws (controladores) ref ao App sistema
# A função index informa oque vai acontecer quando ela for chamada.
def index(request):
    return render(
        request,
        'sistema/index.html',
    )
   


