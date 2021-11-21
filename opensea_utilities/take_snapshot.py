import requests
import time
import json
import csv
from datetime import datetime

now = datetime.now().strftime('%Y%m%d%H%M%S')

# !!! KEY !!!!
headers = {'X-API-KEY':'------Need to insert your own----','Accept':'application/json'}

with open('./snapshots/{}_snap.csv'.format(now), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow( ['Name'] 
    + ['Num sales'] 
    + ['Last sale'] 
    + ['Price'] 
    + ['Buyer address'] 
    + ['Buyer username'] 
    + ['Tx'] 
    + ['Token ID'])


    for x in range(30):
        print('\n\n\n\n\n---x {}---\n\n\n\n'.format(x))
        time.sleep(0.6)
        offset = x * 50
        url = 'https://api.opensea.io/api/v1/assets?collection=bit-birds&order_direction=asc&limit=50&offset={}'.format(offset)
        r = requests.get(url, headers=headers)
        jsonResponse = r.json()

        for i in range(50):
            print('\n\n---i {}---'.format(i))
            # print(json.dumps(jsonResponse))
            name = jsonResponse['assets'][i]['name']
            num_sales = jsonResponse['assets'][i]['num_sales']

            last_sale = 'n/a'
            eth = 'n/a'
            buyer_address = 'n/a'
            txid = 'n/a'
            buyer_username = 'n/a'

            if jsonResponse['assets'][i]['last_sale'] is not None:
                last_sale = jsonResponse['assets'][i]['last_sale']['event_timestamp']
                price = int(jsonResponse['assets'][i]['last_sale']['total_price'])
                eth = price / 1000000000000000000
                buyer_address = jsonResponse['assets'][i]['last_sale']['transaction']['from_account']['address']
                txid = jsonResponse['assets'][i]['last_sale']['transaction']['transaction_hash']
                if jsonResponse['assets'][i]['last_sale']['transaction']['from_account']['user'] is not None:
                    buyer_username = jsonResponse['assets'][i]['last_sale']['transaction']['from_account']['user']['username']


            token_id = jsonResponse['assets'][i]['token_id']

            print('Name: {}\nNum sales: {}\nLast sale: {}\nPrice: {} ETH\nBuyer: {}\nBuyer username: {}'.format(name, num_sales, last_sale, eth, buyer_address, buyer_username))

            writer.writerow([name, num_sales, last_sale, eth, buyer_address, buyer_username, txid, token_id])

print('\n\n\n---Done---\n\n\n')
