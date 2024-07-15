import base64 as decoder
import os
from pathlib import Path
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from dotenv import load_dotenv

load_dotenv()


def path_to_photo(filename):
    return Path(__file__).resolve().parent.parent/'static'/'media'/'photos'/filename


class MainInformationAPI(APIView):
    def get(self, request):
        logo_path = path_to_photo(os.getenv("LOGO_NAME"))
        with open(logo_path, 'rb') as logo_file:
            logo = decoder.b64encode(logo_file.read()).decode('utf-8')
            data = {
                'logo': logo,
                'business_name': os.getenv('BUSINESS_NAME'),
                'business_short_info': os.getenv('BUSINESS_SHORT_INFO'),
            }
            return JsonResponse(data, status=status.HTTP_200_OK)


def index(request):
    return render(request, 'main/homepage.html')
