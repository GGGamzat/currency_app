import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


response = requests.get(url='https://v6.exchangerate-api.com/v6/57103832bca2b0605120abcf/latest/USD').json()
currencies = response.get('conversion_rates')


@api_view(['GET'])
def rates_view(request):
    fr = request.GET.get('from', '')
    to = request.GET.get('to', '')
    value = request.GET.get('value', '')

    try:
        value = float(value)
    except:
        return Response({"error": "Incorrect value"})

    if fr not in currencies or to not in currencies:
        return Response({"error": "Incorrect Currency"})

    converted_amount = round((currencies[to] / currencies[fr]) * value, 2)
    return Response({'result': converted_amount})