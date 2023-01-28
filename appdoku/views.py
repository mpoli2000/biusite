from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Tablero
from .forms import TableroForm

from dokusan import solvers, generators, renderers
from dokusan.boards import BoxSize, Sudoku

def grid_2_grid_i(grid):
    grid_i=[]
    i=0
    for fila in grid:
        grid_i_row=[]
        for item in fila:
            grid_i_row.append((str(i),str(item)))
            i+=1
        grid_i.append(grid_i_row)
    return grid_i

def grid2cluster(grid):
    grid_cluster=[]
    for f in range(3):
        for c in range(3):
            cluster=[]
            for i in range(9):
                cluster.append(grid[3*f+i//3][3*c+i%3])
            grid_cluster.append(cluster)
    return grid_cluster          

def print_lst(lst):
    for r in lst:
        print(r)
    print("\n")

#--------------------------------------------------------

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
                            final_sudoku = str(sudoku),
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


def tablero(request, tablero_id):
    tablero = Tablero.objects.get(id = tablero_id)
    sudoku_lst=[]
    for fila in range(9):
        sudoku_lst.append(list(tablero.final_sudoku[fila*9:(fila+1)*9]))

    sudoku_cluster = grid2cluster(grid_2_grid_i(sudoku_lst))

    return render(request, 'appdoku/tablero.html', {'tablero': tablero, 'sudoku_lst': sudoku_lst, 'sudoku_cluster': sudoku_cluster})


def grilla(request):
    return render(request, 'appdoku/grilla.html')


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