from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests 
import json

def search_question_stack(request,question):
    if request.method == "GET":
        try:
            
            url = 'https://api.stackexchange.com/2.2/search/advanced?title='+question+'&site=stackoverflow'

            r = requests.get(url)
            all_questions = r.json()

            # print(len(all_questions['items']),all_questions)

            if len(all_questions['items']):
                return JsonResponse({"status": True, "data":all_questions["items"]})
            else:
                return JsonResponse({"status": False})
        except Exception as e:
            return JsonResponse({"status": False})


