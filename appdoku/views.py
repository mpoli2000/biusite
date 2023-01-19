from django.shortcuts import render
from django.http import HttpResponse

from .models import Tablero


def index(request):
    latest_tablero_list = Tablero.objects.order_by('-fecha_pub')[:5]
    context = {'latest_tablero_list': latest_tablero_list,}
    return render(request, 'appdoku/index.html', context)



# def listar_juegos(request):
#     usuario = request.user
#     juegos = MiJuego.objects.filter(user_id = usuario.id)
#     return render(request, 'juegos/listar_juegos.html', {'juegos': juegos})


