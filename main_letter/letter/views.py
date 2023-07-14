from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .services import search_letter


class MainLetterView(View):
    template_name = "letter/index.html"

    def post(self, request):
        message = request.POST.get('message')

        letter = search_letter(message)
        response = (f"\nYour request:\n{message}\n \nLetter what are you looking for: {letter}\n" 
                    if letter 
                    else 
                    f"\nYour request:\n{message}\n \nSorry, there are no unique letters here.\n")
        return JsonResponse({"response": response})

    def get(self, request):
        return render(request, "letter/index.html")
