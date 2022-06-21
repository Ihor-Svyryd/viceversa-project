from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    result = len(user_text.split())
    words_count ="There are " + str(result) + " words."
    reverse_text = user_text[::-1]
    return render(request, 'reverse.html', {'user_text': user_text,'revers_text':reverse_text,'words_count': words_count})