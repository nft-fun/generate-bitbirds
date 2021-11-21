import csv
import pandas as pd
from datetime import datetime


file_path = "./snapshots/20211121125737_snap.csv" 

data = pd.read_csv(file_path, sep=',')  

# print(data)

d = data.sort_values(by=["Last sale"], ascending=True)
now = datetime.now().strftime('%Y%m%d%H%M%S')

# print(d)

concat_addresses = ''

with open('./recipients/{}_oldest.csv'.format(now), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow( ['Address'] 
    + ['Bird'] 
    + ['Time'] 
    + ['Time'] 
    + ['Amount']
    + ['Winner username'])

    overall_count = 0
    unique_count = 0

    while unique_count < 50:
        print('\n\n---{}---'.format(overall_count))
        bird = d.values[overall_count][0]
        num_sales = d.values[overall_count][1]
        sale_time = d.values[overall_count][2]
        eth_price = d.values[overall_count][3]
        buyer = d.values[overall_count][4]
        buyer_username = d.values[overall_count][5]
        print('Bird: {}\nNum sales: {}\nSale time: {}\nEth price: {}\nBuyer address: {}\nBuyer username: {}\n'.format(bird,num_sales,sale_time,eth_price,buyer,buyer_username))


        # Will be -1 if winner is not found within the concatenated string concat_addresses
        if concat_addresses.find(buyer) == -1:
            concat_addresses = concat_addresses + buyer
            unique_count += 1
            print('Unique #{}\n\n'.format(unique_count))

            writer.writerow([buyer, bird, sale_time, eth_price, buyer_username])
        else:
            print('Not unique\n\n')
        
        overall_count += 1
