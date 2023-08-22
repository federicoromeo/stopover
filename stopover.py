import json
import requests

def GET():

    # open credentials.txt to get the apikey
    with open('credentials.txt') as f:
        apikey = f.readline().strip()

    url = 'https://api.flightapi.io/onewaytrip'
    headers = {
        'api_key': apikey,
        'departure_airport_code': 'BGY',
        'arrival_airport_code': 'ROM',
        'departure_date': '2023-10-10',
        'number_of_adults': '1',
        'number_of_childrens': '0',
        'number_of_infants': '0',
        'cabin_class': 'Economy',
        'currency': 'EUR'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        with open('response.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
    else:
        print('Request failed with status code:', response.status_code)

def currency_code2currency(currency_code):
    return {"EUR":"€", "USD":"$"}[currency_code]

def analyze():

    with open('response.json') as f:
        data = json.load(f)

    for leg in data["legs"]:

        if leg["stopoversCount"] == 1:

            stopover_at = leg["segments"][0]["arrivalAirportCode"]
            id = leg["id"]
            for trip in data["trips"]:
                if trip["legIds"][0] == id:
                    price_id = trip["id"]
                    break
                
            for fare in data["fares"]:
                if fare["tripId"] == price_id:
                    price = fare["price"]["amount"]
                    currency_code = fare["price"]["currencyCode"]
                    currency = currency_code2currency(currency_code)
                    #print(stopover_at, price, currency)
                    break
            
            flight_code = leg["segments"][0]["designatorCode"]
            segment_duration = leg["segments"][0]["durationMinutes"]
            stopover_duration = leg["stopoverDuration"]

            print(f"{leg['departureAirportCode']} -> {leg['arrivalAirportCode']}  with stopover at {stopover_at}   [{price} {currency}]")

analyze()