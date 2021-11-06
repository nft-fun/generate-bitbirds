import requests

r = requests.get('https://api.opensea.io/api/v1/events?collection_slug=bit-birds&event_type=successful&limit=20')
jsonResponse = r.json()

for i in range(20):
    print('\n\n----{}----'.format(i))
    name = jsonResponse['asset_events'][i]['asset']['name']
    timestamp = jsonResponse['asset_events'][i]['created_date']
    amount = int(jsonResponse['asset_events'][i]['total_price'])
    eth = amount / 1000000000000000000
    winner = jsonResponse['asset_events'][i]['winner_account']['address']
    winner_username = jsonResponse['asset_events'][i]['winner_account']['user']['username']

    print('Name: {}\nTime: {}\nAmount: {} ETH\nWinner: {}\nUsername: {}'.format(name, timestamp, eth, winner, winner_username))

print('\n\n---Done---')
