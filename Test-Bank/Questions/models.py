from django.db import models

answers = ( 
    ("A", "A"), 
    ("B", "B"), 
    ("C", "C"), 
    ("D", "D"), 
)
class MCQ(models.Model):
    question = models.TextField(max_length = 1000)
    A = models.TextField(max_length = 1000)
    B = models.TextField(max_length = 1000)
    C = models.TextField(max_length = 1000)
    D = models.TextField(max_length = 1000)
    answer = models.CharField(max_length = 1,choices = answers,default = 'A')