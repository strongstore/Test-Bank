from django.shortcuts import render
from .models import MCQ

def questions(request):
    questions = MCQ.objects.all()
    context = {
        "questions": questions
    }
    return render(request, 'questions/index.html', context)
