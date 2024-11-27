from django.shortcuts import render
from django.http import JsonResponse
from .models import Question

def get_question(request):
    questions = Question.objects.all()
    question_list = [
        {
            'id': q.id,
            'text': q.text,
            'options': [q.opiton1, q.option2, q.option3, q.option4],
            'correct':[q.opiton1, q.option2, q.option3, q.option4][q.correct_answer -1]
        }
        for q in questions
    ]
    return JsonResponse({'questions': question_list})