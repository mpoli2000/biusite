from django.db import models

class Tablero(models.Model):
    fecha_pub = models.DateTimeField('date published')
    nivel = models.IntegerField(default=1)
    sudoku_inicial = models.CharField(max_length=81)
    sudoku_final = models.CharField(max_length=81)

    def __str__(self):
        return f'fecha: {self.fecha_pub} - nivel: {self.nivel}'
