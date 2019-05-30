from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Retruns a list of APIView features"""

        an_api_view = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to traditional Django View',
            'Gives you the most control over yout logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_api_view': an_api_view})