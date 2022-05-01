import requests

name = input("Enter card name: ")
#SR01-EN009 - Raiza the Storm Monarch - 1.39
response = requests.get('http://yugiohprices.com/api/price_for_print_tag/' + name)
response_name = requests.get('http://yugiohprices.com/api/get_card_prices/Raiza the Storm Monarch')
card = response.json()
card2 = response_name.json()

print(card['data']['price_data']['price_data']['data']['prices']['average'])
print(card2['data'][0]['price_data']['data']['prices']['average'])
