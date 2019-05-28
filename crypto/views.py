from django.shortcuts import render

# Create your views here.

def home(request):
	import requests
	import json

	# crypto prices
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,BCH,ETH,OMG,XRP,GNO,REP,DAS&tsyms=THB,USD")
	price = json.loads(price_request.content)


	# crypto news
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)

	return render(request, 'home.html', {'api': api, 'price': price} )


def prices(request):
	import requests
	import json

	if request.method == 'POST':
		quote = request.POST['quote'].upper()

		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=THB")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote': quote, 'crypto': crypto } )

	else:
		notfound = "Please enter valid crypto currency symbol at the top right above.."
		return render(request, 'prices.html', {'notfound': notfound})
		

		


