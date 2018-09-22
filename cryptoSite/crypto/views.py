from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    #Price Api
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    #news Api
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request,'crypto/home.html' , {'api':api, 'price':price})


def prices(request):
    if request.method == 'POST':
        import json
        import requests
        quote = request.POST['quote']
        quote = quote.upper()
        quote_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto= json.loads(quote_request.content)


        return render(request, 'crypto/prices.html', {'quote':quote, 'crypto':crypto})
    else:
        return render(request, 'crypto/prices.html',{})
