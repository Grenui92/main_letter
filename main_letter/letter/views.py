from django.shortcuts import render

def give_letter(request):
    return render(request, 'letter/index.html')
