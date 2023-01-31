from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Tablero
from .forms import TableroForm, SudokuForm

from dokusan import solvers, generators, renderers, stats
from dokusan.boards import BoxSize, Sudoku

import json

def grid_2_grid_i(grid):
    grid_i=[]
    i=0
    for fila in grid:
        grid_i_row=[]
        for item in fila:
            grid_i_row.append(("id_"+str(i),str(item)))
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


def sudoku_dic(sudoku_initial_str, sudoku_solution_str):
    sudoku_d={}
    for i in range(81):
        sudoku_d[str(i)]={}
        sudoku_d[str(i)]['row'] = i//9
        sudoku_d[str(i)]['column']= i%9
        sudoku_d[str(i)]['box']= i//27*3 + (i%9)//3
        sudoku_d[str(i)]['initial_value'] = sudoku_initial_str[i]
        sudoku_d[str(i)]['solution_value'] = sudoku_solution_str[i]
        sudoku_d[str(i)]['user_value'] = sudoku_initial_str[i]
    return sudoku_d

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
            
            if cd['level']=='1':
                avg_rank = 150
            elif cd['level']=='2':
                avg_rank = 300
            elif cd['level']=='3':
                avg_rank = 450
            else:
                avg_rank=150
            
            while stats.rank(sudoku := generators.random_sudoku(avg_rank)) < avg_rank:
                continue
            print(f"initial_sudoku:{sudoku}, nivel complejidad (0-500): {stats.rank(sudoku)}")

            solution = solvers.backtrack(sudoku)
            print(f'solution_sudoku: {solution}')

            sd = sudoku_dic(str(sudoku), str(solution))
            sd_sorted_by_box = sorted(sd.items(), key= lambda item: item[1]['box']) 
            sd_json=json.dumps(sd_sorted_by_box, indent=2)
            
            print(f'len sudoku_json: {len(sd_json)}')
            print(sd_json[:100])

            tablero = Tablero(name="sudoku",
                            level = cd['level'],
                            size = cd['size'],
                            initial_sudoku = str(sudoku),
                            final_sudoku = str(solution),
                            user_sudoku = str(sudoku),
                            )
            tablero.save()
            #assert False
            # return HttpResponseRedirect('?submitted=True')
            return redirect("/appdoku/tablero/"+str(tablero.id))
        else:
            print(form.errors)
    else:
        form = TableroForm()

        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'appdoku/generar.html', {'form': form,'submitted': submitted})


def tablero(request, tablero_id):

    if request.method == 'POST':
        form = SudokuForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # print(cd)

            tablero = Tablero.objects.get(id = tablero_id)
            sudoku_solution_str = tablero.final_sudoku

            sudoku_user_str=''
            for i in range(81):
                value = cd["id_"+str(i)]
                if value in ['1','2','3','4','5','6','7','8','9']:
                    sudoku_user_str += cd["id_"+str(i)]
                elif value == '?':
                    sudoku_user_str += sudoku_solution_str[i]
                else:
                    sudoku_user_str+='0'

            tablero.user_sudoku = sudoku_user_str
            tablero.save()

        else:
            print(form.errors)

        return redirect("/appdoku/tablero/"+str(tablero_id))
    
    else:
        form = SudokuForm()
        tablero = Tablero.objects.get(id = tablero_id)
        
        sudoku_initial_str = tablero.initial_sudoku
        sudoku_solution_str = tablero.final_sudoku
        sudoku_user_str = tablero.user_sudoku

        # print(f'{sudoku_initial_str}', len(sudoku_initial_str))
        # print(f'{sudoku_user_str}', len(sudoku_user_str))
        # print(f'{sudoku_solution_str}', len(sudoku_solution_str))

        sudoku4template = []
        for i in range(81):
            if sudoku_initial_str[i] != '0':
                sudoku4template.append((i, 'id_'+str(i), str(i//27*3+(i%9)//3), sudoku_initial_str[i], 'P'))
            else:
                if sudoku_user_str[i] != '0':
                    if sudoku_user_str[i]==sudoku_solution_str[i]:
                        sudoku4template.append((i, 'id_'+str(i), str(i//27*3+(i%9)//3), sudoku_user_str[i], 'S'))
                    else:
                        sudoku4template.append((i, 'id_'+str(i), str(i//27*3+(i%9)//3), sudoku_user_str[i], 'D'))
                else:
                    sudoku4template.append((i, 'id_'+str(i), str(i//27*3+(i%9)//3), sudoku_initial_str[i], 'N'))

        sudoku4template_sorted = sorted(sudoku4template, key=lambda item: (item[2],item[0]))
        sudoku_cluster = []
        for fila in range(9):
            sudoku_cluster.append(sudoku4template_sorted[fila*9:(fila+1)*9])
        # print(sudoku_cluster)


        # for box in sudoku_cluster1:
        #     print(box) 

        # sudoku_lst=[]
        # for fila in range(9):
        #     sudoku_lst.append(list(tablero.initial_sudoku[fila*9:(fila+1)*9]))

        # sudoku_cluster = grid2cluster(grid_2_grid_i(sudoku_lst))
        # print(sudoku_cluster)
        
    return render(request, 'appdoku/tablero.html', {'form': form, 'tablero': tablero, 'sudoku_cluster': sudoku_cluster})

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