import os
import json
import requests
import pandas as pd
import time

from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

etherscan_key = os.getenv('ETHERSCAN_KEY')
address = os.getenv('ETH_ADDRESS').lower()

url = 'https://api.etherscan.io/api'

test_qty = 5

concat_tx_check = ''
unique_tx_count = 0
repeat_tx_count = 0
unique_list = ''
repeat_list = ''

# ------
# ------
# Beginning normal transaction export
# ------
# ------
print('\n-----\n-----\n-----\nBeginning NORMAL Transaction export\n-----\n-----\n-----')
normal_tx = '?module=account&action=txlist&address={}&startblock=0&endblock=99999999&sort=asc&apikey={}'.format(
    address, etherscan_key)


r = requests.get('{}{}'.format(url, normal_tx))
print('HTTP Response code: {}\n\n'.format(r))
normal_tx_reponse_json = r.json()

entries = len(normal_tx_reponse_json['result'])
print('{} normal transactions'.format(entries))


for i in range(len(normal_tx_reponse_json['result'])):

# for i in range(test_qty):
    time.sleep(0.10)

    # ------ Raw response data points ------
    print('\n---Normal TX {}---\n'.format(i))
    block_number = normal_tx_reponse_json['result'][i]['blockNumber']
    timestamp = normal_tx_reponse_json['result'][i]['timeStamp']
    tx_hash = normal_tx_reponse_json['result'][i]['hash']
    nonce = normal_tx_reponse_json['result'][i]['nonce']
    block_hash = normal_tx_reponse_json['result'][i]['blockHash']
    transaction_index = normal_tx_reponse_json['result'][i]['transactionIndex']
    from_address = normal_tx_reponse_json['result'][i]['from']
    to_address = normal_tx_reponse_json['result'][i]['to']
    value = normal_tx_reponse_json['result'][i]['value']
    # Gas limit offered up by our transaction
    gas = normal_tx_reponse_json['result'][i]['gas']
    gas_price = normal_tx_reponse_json['result'][i]['gasPrice']
    is_error = normal_tx_reponse_json['result'][i]['isError']
    txreceipt_status = normal_tx_reponse_json['result'][i]['txreceipt_status']
    tx_input = normal_tx_reponse_json['result'][i]['input']
    contract_address = normal_tx_reponse_json['result'][i]['contractAddress']
    # Seems to be the sum of gas used by the block up to the index of our transaction
    cumulative_gas_used = normal_tx_reponse_json['result'][i]['cumulativeGasUsed']
    # Gas used by our transaction
    gas_used = normal_tx_reponse_json['result'][i]['gasUsed']
    confirmations = normal_tx_reponse_json['result'][i]['confirmations']



    if concat_tx_check.find(tx_hash) == -1:
        concat_tx_check = concat_tx_check + tx_hash
        unique_tx_count += 1
        print('Unique tx #{}'.format(unique_tx_count))
        unique_list = '{}\n{}'.format(unique_list,tx_hash)
    else:
        repeat_tx_count +=1
        print('Repeat tx #{}'.format(repeat_tx_count))
        repeat_list = '{}\n{}'.format(repeat_list,tx_hash)



    # Prints raw data points
    print('Raw:\n timeStamp: {}\n tx_hash: {}\n nonce: {}\n from: {}\n to: {}\n value: {}\n gas (gas limit): {}\n gas_price: {}\n isError (0=good 1=error): {}\n txreceipt_status: {}\n contractAddress: {}\n cumulativeGasUsed: {}\n gasUsed (gas usage): {}\n confirmations: {}'.format(
        timestamp,
        tx_hash,
        nonce,
        from_address,
        to_address,
        value,
        gas,
        gas_price,
        is_error,
        txreceipt_status,
        contract_address,
        cumulative_gas_used,
        gas_used,
        confirmations)
        )

    # ------- Cleaned and augmented data points -------

    tx_datetime = datetime.utcfromtimestamp(int(timestamp))
    price_date = tx_datetime.strftime('%Y-%m-%d')
    # print(price_date)

    price_url = '{}?module=stats&action=ethdailyprice&startdate={}&enddate={}&sort=asc&apikey={}'.format(
        url, price_date, price_date, etherscan_key)

    # price_url = 'https://api.cryptowat.ch/assets/eth'

    # print(price_url)

    r_price = requests.get('{}'.format(price_url))
    price_response_json = r_price.json()
    # print('\n\nPrice response: {}'.format(json.dumps(price_response_json)))

    hist_eth_date = price_response_json['result'][0]['UTCDate']
    hist_eth_price = price_response_json['result'][0]['value']

    if from_address == address:
        in_out = 'TX_SENDER'
    elif from_address != address and to_address == address:
        in_out = 'TX_RECIPIENT'
    else:
        in_out = 'NEITHER-ABNORMAL'

    eth_value = int(value) / 10 ** 18
    usd_value = round(float(hist_eth_price) * eth_value, 2)

    gas_summary = '{} / {}'.format(gas, gas_used)
    gwei_gas = int(gas_used) * int(gas_price)
    eth_gas = gwei_gas / 10 ** 18
    hist_usd_gas = round(float(hist_eth_price) * eth_gas, 2)

    # Prints cleaned and augmented data points
    print('\nPretty:\n Transaction datetime (yyyy-mm-dd UTC): {}\n Eth price on {}: ${}\n Sender or receiver?: {}\n eth_value: {}\n ETH/USD Value transferred (not including gas): ${}\n Gas limit/used: {}\n GWEI Gas: {}\n ETH Gas: {}\n Estimated USD fee: ${}'.format(
        tx_datetime,
        hist_eth_date,
        hist_eth_price,
        in_out,
        eth_value,
        usd_value,
        gas_summary,
        gwei_gas,
        eth_gas,
        hist_usd_gas)
    )


# print(json.dumps(normal_tx_reponse_json))
print('\n\n------End Normal TX-------')


print('\n\nUnique tx count: {}\nRepeat tx count: {}\n\nUnique tx list: {}\n\nRepeat tx list: {}\n\n'.format(unique_tx_count, repeat_tx_count, unique_list, repeat_list))

# ------
# ------
# Beginning internal transaction export
# ------
# ------
print('\n-----\n-----\n-----\nBeginning INTERNAL Transaction export\n-----\n-----\n-----')


i = 0

internal_tx = '?module=account&action=txlistinternal&address={}&startblock=0&endblock=99999999&sort=asc&apikey={}'.format(
    address, etherscan_key)

print('\n\nInternal Transactions Export URL:\n{}{}'.format(url, internal_tx))

r_internal = requests.get('{}{}'.format(url, internal_tx))
print('HTTP Response code: {}\n\n'.format(r_internal))
internal_tx_response_json = r_internal.json()

entries = len(internal_tx_response_json['result'])
print('{} internal transactions'.format(entries))


for i in range(len(internal_tx_response_json['result'])):

# for i in range(test_qty):

    time.sleep(0.10)

    # ------ Raw response data points ------
    print('\n\n\n---Internal TX {}---\n'.format(i))
    block_number = internal_tx_response_json['result'][i]['blockNumber']
    timestamp = internal_tx_response_json['result'][i]['timeStamp']
    tx_hash = internal_tx_response_json['result'][i]['hash']
    from_address = internal_tx_response_json['result'][i]['from']
    to_address = internal_tx_response_json['result'][i]['to']
    value = internal_tx_response_json['result'][i]['value']
    contract_address = internal_tx_response_json['result'][i]['contractAddress']
    tx_type = internal_tx_response_json['result'][i]['type']
    gas = internal_tx_response_json['result'][i]['gas']    # Gas limit offered up by the transaction
    gas_used = internal_tx_response_json['result'][i]['gasUsed']    # Gas used by the transaction
    trace_id = internal_tx_response_json['result'][i]['traceId']
    is_error = internal_tx_response_json['result'][i]['isError']
    err_code = internal_tx_response_json['result'][i]['errCode']


    if concat_tx_check.find(tx_hash) == -1:
        concat_tx_check = concat_tx_check + tx_hash
        unique_tx_count += 1
        print('Unique tx #{}'.format(unique_tx_count))
        unique_list = '{}\n{}'.format(unique_list,tx_hash)
    else:
        repeat_tx_count +=1
        print('Repeat tx #{}'.format(repeat_tx_count))
        repeat_list = '{}\n{}'.format(repeat_list,tx_hash)

    # Prints raw data points
    print('Raw:\n block_number: {}\n timestamp: {}\n tx_hash: {}\n from: {}\n to: {}\n value: {}\n contract_address: {}\n tx_type: {}\n gas: {}\n gas_used: {}\n trace_id: {}\n is_error: {}\n err_code: {}\n'.format(
        block_number,
        timestamp,
        tx_hash,
        from_address,
        to_address,
        value,
        contract_address,
        tx_type,
        gas,
        gas_used,
        trace_id,
        is_error,
        err_code)
    )

    # ------- Cleaned and augmented data points -------

    tx_datetime = datetime.utcfromtimestamp(int(timestamp))
    price_date = tx_datetime.strftime('%Y-%m-%d')
    # print(price_date)

    price_url = '{}?module=stats&action=ethdailyprice&startdate={}&enddate={}&sort=asc&apikey={}'.format(url,price_date,price_date,etherscan_key)
    # print(price_url)

    r_price = requests.get('{}'.format(price_url))
    price_response_json = r_price.json()
    # print('\n\nPrice response: {}'.format(json.dumps(price_response_json)))

    hist_eth_date = price_response_json['result'][0]['UTCDate']
    hist_eth_price = price_response_json['result'][0]['value']

    if from_address == address:
        in_out = 'TX_SENDER'
    elif from_address != address and to_address == address:
        in_out = 'TX_RECIPIENT'
    else:
        in_out = 'NEITHER-ABNORMAL'


    eth_value = int(value) / 10 ** 18
    usd_value = round(float(hist_eth_price) * eth_value,2)

    gas_summary = '{} / {}'.format(gas,gas_used)
    gwei_gas = int(gas_used) * int(gas_price)
    eth_gas = gwei_gas / 10 ** 18
    hist_usd_gas = round(float(hist_eth_price) * eth_gas,2)

    # Prints cleaned and augmented data points
    print('\nPretty:\n Transaction datetime (yyyy-mm-dd UTC): {}\n Eth price on {}: ${}\n Sender or receiver?: {}\n eth_value: {}\n ETH/USD Value transferred (not including gas): ${}\n Gas limit/used: {}\n GWEI Gas: {}\n ETH Gas: {}\n Estimated USD fee: ${}'.format(
    tx_datetime,
    hist_eth_date,
    hist_eth_price,
    in_out,
    eth_value,
    usd_value,
    gas_summary,
    gwei_gas,
    eth_gas,
    hist_usd_gas)
    )


# print(json.dumps(internal_tx_response_json))
print('\n\n------End Internal TX-------')


print('\n\nUnique tx count: {}\nRepeat tx count: {}\n\nUnique tx list: {}\n\nRepeat tx list: {}\n\n'.format(unique_tx_count, repeat_tx_count, unique_list, repeat_list))

# ------
# ------
# Beginning ERC20 transaction export
# ------
# ------
print('\n-----\n-----\n-----\nBeginning ERC Transaction export\n-----\n-----\n-----')


i = 0

erc20_tx = '?module=account&action=tokentx&address={}&startblock=0&endblock=99999999&sort=asc&apikey={}'.format(
    address, etherscan_key)

print('\n\nERC20 Transactions Export URL:\n{}{}'.format(url, erc20_tx))

r_erc20 = requests.get('{}{}'.format(url, erc20_tx))
print('HTTP Response code: {}\n\n'.format(r_erc20))
erc20_tx_response_json = r_erc20.json()

entries = len(erc20_tx_response_json['result'])
print('{} erc20 transactions'.format(entries))


for i in range(len(erc20_tx_response_json['result'])):

# for i in range(test_qty):

    time.sleep(0.10)

    # ------ Raw response data points ------
    print('\n\n\n---ERC20 TX {}---\n'.format(i))
    block_number = erc20_tx_response_json['result'][i]['blockNumber']
    timestamp = erc20_tx_response_json['result'][i]['timeStamp']
    tx_hash = erc20_tx_response_json['result'][i]['hash']
    nonce = erc20_tx_response_json['result'][i]['nonce']
    from_address = erc20_tx_response_json['result'][i]['from']
    contract_address = erc20_tx_response_json['result'][i]['contractAddress']
    to_address = erc20_tx_response_json['result'][i]['to']
    value = erc20_tx_response_json['result'][i]['value']
    token_name = erc20_tx_response_json['result'][i]['tokenName']
    token_symbol = erc20_tx_response_json['result'][i]['tokenSymbol']
    token_decimal = erc20_tx_response_json['result'][i]['tokenDecimal']
    gas = erc20_tx_response_json['result'][i]['gas']    # Gas limit offered up by the transaction
    gas_price = erc20_tx_response_json['result'][i]['gasPrice']
    gas_used = erc20_tx_response_json['result'][i]['gasUsed']    # Gas used by the transaction
    confirmations = erc20_tx_response_json['result'][i]['confirmations']


    if concat_tx_check.find(tx_hash) == -1:
        concat_tx_check = concat_tx_check + tx_hash
        unique_tx_count += 1
        print('Unique tx #{}'.format(unique_tx_count))
        unique_list = '{}\n{}'.format(unique_list,tx_hash)
    else:
        repeat_tx_count +=1
        print('Repeat tx #{}'.format(repeat_tx_count))
        repeat_list = '{}\n{}'.format(repeat_list,tx_hash)



#     # Prints raw data points
    print('Raw:\n block_number: {}\n timestamp: {}\n tx_hash: {}\n nonce: {}\n from: {}\n contract_address: {}\n to: {}\n value: {}\n token_name: {}\n token_symbol: {}\n token_decimal: {}\n gas: {}\n gas_price: {}\n gas_used: {}\n confirmations: {}\n'.format(
        block_number,
        timestamp,
        tx_hash,
        nonce,
        from_address,
        contract_address,
        to_address,
        value,
        token_name,
        token_symbol,
        token_decimal,
        gas,
        gas_price,
        gas_used,
        confirmations)
    )

    # ------- Cleaned and augmented data points -------

    tx_datetime = datetime.utcfromtimestamp(int(timestamp))
    price_date = tx_datetime.strftime('%Y-%m-%d')
    # print(price_date)

    price_url = '{}?module=stats&action=ethdailyprice&startdate={}&enddate={}&sort=asc&apikey={}'.format(url,price_date,price_date,etherscan_key)
    # print(price_url)

    r_price = requests.get('{}'.format(price_url))
    price_response_json = r_price.json()
    # print('\n\nPrice response: {}'.format(json.dumps(price_response_json)))

    hist_eth_date = price_response_json['result'][0]['UTCDate']
    hist_eth_price = price_response_json['result'][0]['value']

    if from_address == address:
        in_out = 'TX_SENDER'
    elif from_address != address and to_address == address:
        in_out = 'TX_RECIPIENT'
    else:
        in_out = 'NEITHER-ABNORMAL'

    token_value = int(value) / 10 ** int(token_decimal)

    gas_summary = '{} / {}'.format(gas,gas_used)
    gwei_gas = int(gas_used) * int(gas_price)
    eth_gas = gwei_gas / 10 ** 18
    hist_usd_gas = round(float(hist_eth_price) * eth_gas,2)

    # Prints cleaned and augmented data points
    print('\nPretty:\n Transaction datetime (yyyy-mm-dd UTC): {}\n Eth price on {}: ${}\n Sender or receiver?: {}\n token_value: {} {}\n Gas limit/used: {}\n GWEI Gas: {}\n ETH Gas: {}\n Estimated USD fee: ${}'.format(
    tx_datetime,
    hist_eth_date,
    hist_eth_price,
    in_out,
    token_value,
    token_symbol,
    gas_summary,
    gwei_gas,
    eth_gas,
    hist_usd_gas)
    )


# print(json.dumps(erc20_tx_response_json))
print('\n\n------End erc20 TX-------')

print('\n\nUnique tx count: {}\nRepeat tx count: {}\n\nUnique tx list: {}\n\nRepeat tx list: {}\n\n'.format(unique_tx_count, repeat_tx_count, unique_list, repeat_list))






# ------
# ------
# Beginning erc721 transaction export
# ------
# ------




print('\n-----\n-----\n-----\nBeginning ERC721 Transaction export\n-----\n-----\n-----')


i = 0

erc721_tx = '?module=account&action=tokennfttx&address={}&startblock=0&endblock=99999999&sort=asc&apikey={}'.format(
    address, etherscan_key)

print('\n\nERC721 Transactions Export URL:\n{}{}'.format(url, erc721_tx))

r_erc721 = requests.get('{}{}'.format(url, erc721_tx))
print('HTTP Response code: {}\n\n'.format(r_erc721))
erc721_tx_response_json = r_erc721.json()

entries = len(erc721_tx_response_json['result'])
print('{} erc721 transactions'.format(entries))


for i in range(len(erc721_tx_response_json['result'])):

# for i in range(test_qty):

    time.sleep(0.10)

    # ------ Raw response data points ------
    print('\n\n\n---erc721 TX {}---\n'.format(i))
    block_number = erc721_tx_response_json['result'][i]['blockNumber']
    timestamp = erc721_tx_response_json['result'][i]['timeStamp']
    tx_hash = erc721_tx_response_json['result'][i]['hash']
    nonce = erc721_tx_response_json['result'][i]['nonce']
    from_address = erc721_tx_response_json['result'][i]['from']
    contract_address = erc721_tx_response_json['result'][i]['contractAddress']
    to_address = erc721_tx_response_json['result'][i]['to']
    token_id = erc721_tx_response_json['result'][i]['tokenID']
    token_name = erc721_tx_response_json['result'][i]['tokenName']
    token_symbol = erc721_tx_response_json['result'][i]['tokenSymbol']
    token_decimal = erc721_tx_response_json['result'][i]['tokenDecimal']
    gas = erc721_tx_response_json['result'][i]['gas']    # Gas limit offered up by the transaction
    gas_price = erc721_tx_response_json['result'][i]['gasPrice']
    gas_used = erc721_tx_response_json['result'][i]['gasUsed']    # Gas used by the transaction
    confirmations = erc721_tx_response_json['result'][i]['confirmations']




    if concat_tx_check.find(tx_hash) == -1:
        concat_tx_check = concat_tx_check + tx_hash
        unique_tx_count += 1
        print('Unique tx #{}'.format(unique_tx_count))
        unique_list = '{}\n{}'.format(unique_list,tx_hash)
    else:
        repeat_tx_count +=1
        print('Repeat tx #{}'.format(repeat_tx_count))
        repeat_list = '{}\n{}'.format(repeat_list,tx_hash)




#     # Prints raw data points
    print('Raw:\n block_number: {}\n timestamp: {}\n tx_hash: {}\n nonce: {}\n from: {}\n contract_address: {}\n to: {}\n token_id: {}\n token_name: {}\n token_symbol: {}\n token_decimal: {}\n gas: {}\n gas_price: {}\n gas_used: {}\n confirmations: {}\n'.format(
        block_number,
        timestamp,
        tx_hash,
        nonce,
        from_address,
        contract_address,
        to_address,
        token_id,
        token_name,
        token_symbol,
        token_decimal,
        gas,
        gas_price,
        gas_used,
        confirmations)
    )

    # ------- Cleaned and augmented data points -------

    tx_datetime = datetime.utcfromtimestamp(int(timestamp))
    price_date = tx_datetime.strftime('%Y-%m-%d')
    # print(price_date)

    price_url = '{}?module=stats&action=ethdailyprice&startdate={}&enddate={}&sort=asc&apikey={}'.format(url,price_date,price_date,etherscan_key)
    # print(price_url)

    r_price = requests.get('{}'.format(price_url))
    price_response_json = r_price.json()
    # print('\n\nPrice response: {}'.format(json.dumps(price_response_json)))

    hist_eth_date = price_response_json['result'][0]['UTCDate']
    hist_eth_price = price_response_json['result'][0]['value']

    if from_address == address:
        in_out = 'TX_SENDER'
    elif from_address != address and to_address == address:
        in_out = 'TX_RECIPIENT'
    else:
        in_out = 'NEITHER-ABNORMAL'

    # token_value = int(value) / 10 ** int(token_decimal)

    gas_summary = '{} / {}'.format(gas,gas_used)
    gwei_gas = int(gas_used) * int(gas_price)
    eth_gas = gwei_gas / 10 ** 18
    hist_usd_gas = round(float(hist_eth_price) * eth_gas,2)

    # Prints cleaned and augmented data points
    print('\nPretty:\n Transaction datetime (yyyy-mm-dd UTC): {}\n Eth price on {}: ${}\n Sender or receiver?: {}\n Token ID: {}\n Token Name [Symbol]: {} [{}]\n Gas limit/used: {}\n GWEI Gas: {}\n ETH Gas: {}\n Estimated USD fee: ${}'.format(
    tx_datetime,
    hist_eth_date,
    hist_eth_price,
    in_out,
    token_id,
    token_name,
    token_symbol,
    gas_summary,
    gwei_gas,
    eth_gas,
    hist_usd_gas)
    )


# print(json.dumps(erc721_tx_response_json))
print('\n\n------End erc721 TX-------')

print('\n\nUnique tx count: {}\nRepeat tx count: {}\n\nUnique tx list: {}\n\nRepeat tx list: {}\n\n'.format(unique_tx_count, repeat_tx_count, unique_list, repeat_list))





# ------
# ------
# Beginning erc1155 transaction export
# ------
# ------





print('\n-----\n-----\n-----\nBeginning ERC1155 Transaction export\n-----\n-----\n-----')

opensea_count = 0
erc1155_count = 0
payout_count = 0
erc1155_continue = True

while erc1155_continue == True:
    time.sleep(0.6)
    print('\n\n----Opensea TX {}\n'.format(opensea_count))

    opensea_url = 'https://api.opensea.io/api/v1/events?account_address={}&limit=1&offset={}'.format(address,opensea_count)
    print(opensea_url)
    headers = {'X-API-KEY':os.getenv('OPENSEA_KEY'),'Accept':'application/json'}

    # print(headers)

    r_erc1155 = requests.get(opensea_url, headers=headers)

    print('HTTP Response code: {}\n'.format(r_erc1155))
    erc1155_tx_response_json = r_erc1155.json()

    # print(json.dumps(erc1155_tx_response_json))

    if len(erc1155_tx_response_json['asset_events']) != 0:

        nft_type = erc1155_tx_response_json['asset_events'][0]['asset']['asset_contract']['schema_name']
        nft_name = erc1155_tx_response_json['asset_events'][0]['asset']['name']
        collection_name = erc1155_tx_response_json['asset_events'][0]['asset']['collection']['name']
        nft_url = erc1155_tx_response_json['asset_events'][0]['asset']['permalink']
        event_type = erc1155_tx_response_json['asset_events'][0]['event_type']
        print('\nName: {}\n Collection: {}\n Type: {}\n Event type: {}\n\nURL: \n {}\n\n'.format(nft_name, collection_name, nft_type, event_type, nft_url))

        if nft_type == 'ERC1155':

            if event_type == 'transfer' or event_type == 'successful' or event_type == 'approve':
                print('transfer, successful, or approve path... event_type: {}'.format(erc1155_tx_response_json['asset_events'][0]['event_type']))

                tx_hash = erc1155_tx_response_json['asset_events'][0]['transaction']['transaction_hash']
                print(tx_hash)
                erc1155_count += 1


                if concat_tx_check.find(tx_hash) == -1:
                    concat_tx_check = concat_tx_check + tx_hash
                    unique_tx_count += 1
                    print('Unique tx #{}'.format(unique_tx_count))
                    unique_list = '{}\n{}'.format(unique_list,tx_hash)
                else:
                    repeat_tx_count +=1
                    print('Repeat tx #{}'.format(repeat_tx_count))
                    repeat_list = '{}\n{}'.format(repeat_list,tx_hash)

            elif erc1155_tx_response_json['asset_events'][0]['event_type'] == 'payout':
                print('payout path... probably the buyer of a bid or auction that was accepted by another party. event_type: {}'.format(erc1155_tx_response_json['asset_events'][0]['event_type']))
                erc1155_count += 1
                payout_count += 1


        opensea_count += 1

    else:
        print('hit the else path - should be done')
        erc1155_continue = False

print('\n\n\n\n\n\n----------Exited while loop-----------\n\nSummary:\n ERC1155 count: {}\n Opensea count: {}\n Payout count: {}\n\n\n'.format(erc1155_count,opensea_count, payout_count))

print('Unique tx count: {}\nRepeat tx count: {}\n\nUnique tx list: {}\n\nRepeat tx list: {}'.format(unique_tx_count, repeat_tx_count, unique_list, repeat_list))


