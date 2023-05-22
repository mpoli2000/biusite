from django.db import models

class Tablero(models.Model):

    LEVEL_CHOICES = (
        ('1', 'bajo'),
        ('2', 'medio'),
        ('3', 'alto'),
    )

    SIZE_CHOICES =(
        ('3', '3x3'),
    )

    name = models.CharField(max_length=50, blank=True)
    level = models.CharField(max_length=1, default='2', choices=LEVEL_CHOICES)
    size = models.CharField(max_length=1, default='3', choices=SIZE_CHOICES)
    initial_sudoku = models.CharField(max_length=81, default='0')
    final_sudoku = models.CharField(max_length=81, default='0')
    user_sudoku = models.CharField(max_length=81, default='0')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'name: {self.name} - level: {self.level} - size: {self.size} - initial_sudoku: {self.initial_sudoku} - final_sudoku: {self.final_sudoku} - created: {self.created}'
