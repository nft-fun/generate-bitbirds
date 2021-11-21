import requests
import time
import json

# Query opensea API for most recent sale events
import csv
from datetime import datetime

now = datetime.now().strftime('%Y%m%d%H%M%S')

# !!! KEY !!!!
headers = {'X-API-KEY':'------Need to insert your own-------','Accept':'application/json'}


url = 'https://api.opensea.io/api/v1/events?collection_slug=bit-birds&event_type=successful&limit=100'
r = requests.get(url, headers=headers)

jsonResponse = r.json()

concat_addresses = ''
unique_count = 0
overall_count = 0

with open('./recipients/{}_most_recent.csv'.format(now), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow( ['Address'] 
    + ['Bird'] 
    + ['Time'] 
    + ['Time'] 
    + ['Amount'] 
    + ['OS Username'])

    while unique_count < 30:
        print('\n\n----{}----'.format(overall_count))
        name = jsonResponse['asset_events'][overall_count]['asset']['name']
        timestamp = jsonResponse['asset_events'][overall_count]['created_date']
        amount = int(jsonResponse['asset_events'][overall_count]['total_price'])
        eth = amount / 1000000000000000000
        winner = jsonResponse['asset_events'][overall_count]['winner_account']['address']
        winner_username = jsonResponse['asset_events'][overall_count]['winner_account']['user']['username']

        print('Name: {}\nTime: {}\nAmount: {} ETH\nWinner: {}\nUsername: {}\n'.format(name, timestamp, eth, winner, winner_username))
        
        # Will be -1 if winner is not found within the concatenated string concat_addresses
        if concat_addresses.find(winner) == -1:
            concat_addresses = concat_addresses + winner
            unique_count += 1
            print('Unique #{}'.format(unique_count))

            writer.writerow([winner, name, timestamp, eth, winner_username])

        else:
            print('Not unique')
        
        overall_count += 1

print('\n\n---Done---\nUnique count: {}\n\n\n'.format(unique_count))
