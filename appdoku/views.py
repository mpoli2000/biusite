from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Tablero
from .forms import TableroForm

from dokusan import solvers, generators, renderers
from dokusan.boards import BoxSize, Sudoku

def index(request):
    latest_tablero_list = Tablero.objects.order_by('-created')[:20]
    context = {'latest_tablero_list': latest_tablero_list,}
    return render(request, 'appdoku/index.html', context)

def generar(request):
    # pub_date = timezone.now() - datetime.timedelta(hours=3)
    # context = {'pub_date': pub_date}
    # return render(request,'appdoku/generar.html', context)
    
    submitted = False
    if request.method == 'POST':
        form = TableroForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            sudoku = generators.random_sudoku(avg_rank=150)
            print(type(sudoku), sudoku, len(str(sudoku)))
            print(renderers.colorful(sudoku))

            tablero = Tablero(name="sudoku",
                            level = cd['level'],
                            size = cd['size'],
                            initial_sudoku = str(sudoku),
                            )
            tablero.save()
            #assert False
            return HttpResponseRedirect('?submitted=True')
        else:
            print(form.errors)
    else:
        form = TableroForm()

        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'appdoku/generar.html', {'form': form,'submitted': submitted})


# def crear_juegos(request):
#     usuario = request.user
#     if request.method == 'POST':
#         nivel_partida = request.POST['nivel']
#         sudoku = generators.random_sudoku(avg_rank=150)
#         print(type(sudoku), sudoku, len(str(sudoku)))
#         print(renderers.colorful(sudoku))
#         juego = MiJuego(user_id = usuario.id,
#                         fecha = datetime.date(2022, 10, 19),
#                         nombre = request.POST['nombre'],
#                         descripcion = request.POST['descripcion'],
#                         nivel = request.POST['nivel'],
#                         sudoku_inicial = str(sudoku),
#                         sudoku_final = str(sudoku),
#                         numeros = 10,
#                         ceros = 71,
#                         progreso = 0,
#                         movimientos = 0,
#                         )
#         juego.save()
#         return redirect('/listar_juegos')
#     return render(request, 'juegos/crear_juegos.html')