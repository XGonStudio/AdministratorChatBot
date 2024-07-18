import base64 as decoder
import os
from pathlib import Path
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework import status
from dotenv import load_dotenv
from .models import Business

load_dotenv()


def path_to_photo(filename):
    return Path(__file__).resolve().parent.parent/'static'/'media'/'photos'/filename


class MainInformationAPI(APIView):
    def get(self, request):
        bmodel = Business.objects.first()
        logo_path = path_to_photo(bmodel.logo)
        with open(logo_path, 'rb') as logo_file:
            logo = decoder.b64encode(logo_file.read()).decode('utf-8')
            data = {
                'logo': logo,
                'business_name': bmodel.name,
                'business_short_info': bmodel.short_info,
            }
            return JsonResponse(data, status=status.HTTP_200_OK)


def index(request):
    return render(request, 'main/homepage.html')


class ContactsView(View):
    def get(self, request):
        template = 'main/contact.html'
        return render(request, template_name=template)
