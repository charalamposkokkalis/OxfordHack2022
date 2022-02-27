from coinmetrics.api_client import CoinMetricsClient
import requests
from os import environ
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import logging
from datetime import date, datetime, timedelta
from coinmetrics.api_client import CoinMetricsClient
import json
import logging
from pytz import timezone as timezone_conv
from datetime import timezone as timezone_info
from statistics import *

####################################################

#miner fees = amount paid per day
#hashes per day = 60*60*24*hashrate
#difficulty = expected number of hashes to get success

#how to calculate miner_fees?

efficiencies_list = [0.0971,0.0980,0.1261,0.1575,0.1000,0.1261,0.0980,0.1176,0.0980,
0.1306,0.1444,0.1364,0.1667,0.1102,0.1471,0.0917,0.1043,0.2568,0.1640,0.0925,0.0949,0.0526,0.0913,0.0943,0.0970,
0.0985,0.1100,0.1100,0.0863,0.0875,0.1052,0.0825,0.0857,0.0931,0.0960,0.0636,0.0650,0.0688,0.0850,0.0450,0.0477,
0.0550,0.0650,0.0813,0.0788,0.0746,0.1035,0.0773,0.0750,0.0488,0.0551,0.0395,0.0395,0.0450,0.0450,0.0423,0.0550,
0.0600,0.0457,0.0620,0.0800,0.0600,0.0494,0.0970,0.0467,0.0500,0.0579,0.0568,0.0650,0.0643,0.0450,0.0550,0.0400,
0.0500,0.0431,0.0380,0.0460,0.0295,0.0342,0.0375,0.0540,0.0420,0.0520,0.0450,0.0520,0.0380,0.0957,0.0361,0.0305]


 


######################################################################







sns.set_theme()
sns.set(rc={'figure.figsize':(12,8)})
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
try:
    api_key = environ["CM_API_KEY"]
    logging.info("Using API key found in environment")
except KeyError:
    api_key = ""
    logging.info("API key not found. Using community client")


client = CoinMetricsClient(api_key)

''' 
assets = ['btc', 'eth']
asset_mapping = {i: assets[i] for i in range(len(assets))}
print(asset_mapping)


asset_catalog = client.catalog_assets(assets=assets)
full_asset_catalog = client.catalog_full_assets(assets=assets)

print(f"Asset Catalog metadata includes: {list(asset_catalog[0].keys())}")
i=0


print("*** catalog endpoint ***")
for i in range(len(asset_catalog)):
    asset_metadata = asset_catalog[i]
    asset_name = asset_metadata['asset']

    
    for i in range (len(asset_metadata['metrics'])):
        if asset_metadata['metrics'][i]['metric'] =='HashRate':
            print("Hash Rate index is ", i)
            print(asset_metadata['metrics'][i])
        if asset_metadata['metrics'][i]['metric'] =='DiffMean':
            print("Difficulty index is ", i)
            print(asset_metadata['metrics'][i])

        if asset_metadata['metrics'][i]['metric'] =='FeeTotUSD':
            print("Miner Fee index is ", i)
            print(asset_metadata['metrics'][i])
'''


   
# Get all assets that have a reference rate 
assets_refrate = client.catalog_metrics("HashRate")
# Get list of assets with daily ref rate 
# uncomment the top line to look at *every* asset with reference rates
asset_with_ref_rates = assets_refrate[0]["frequencies"][0]["assets"]
print(asset_with_ref_rates)
#asset_with_ref_rates = ['btc', 'eth', 'bnb', 'ada', 'doge', 'xrp']
#Query API for prices, daily CM reference rates as dataframe
metrics = "HashRate, DiffMean, FeeTotUSD, FeeTotNtv, PriceUSD"
frequency = "1d"
start_time = "2022-02-25"
end_time = "2022-02-25"




logging.info("Getting prices...")
df_diffmean = client.get_asset_metrics(
    assets=asset_with_ref_rates,
    metrics=metrics,
    frequency=frequency,
    start_time=start_time,
    end_time=end_time
).to_dataframe()

#ass = df_diffmean.iloc[2]

#difficulty = ass['DiffMean']
#price = ass['PriceUSD']
#print(ass['BlkUncRwd'])
#print((10**9/(2**32*difficulty))*block_reward*(price/0.05)*3.6*10**6)


value_list = {'BCH': (0,6.25,600,520954.2979996533,24.35), 'BSV': (1,6.25,600,396136.5814224482,85.14), 'BTC': (2,6.25,600,186294129.77324116,38786.6), 'DASH': (3,2.88,150,4129,92.26), 'DOGE': (4,10000,60,337,0.13), 'ETC': (5,0.125,13,23,28.31), 'ETH': (6,2.31137,13,1000,2785.9), 'LTC': (7,12.5,150,389,106.83), 'VTC': (8,25,150,25/1000,0.2654), 'XMR': (9,0.8,120,3.18/1000,155.44), 'ZEC': (10,6.25,75,8.38/1000,106.63)}

def average_efficiency(tag):
    ass = df_diffmean.iloc[value_list[tag][0]]
    profitability_threshold = value_list[tag][1]*3600000*value_list[tag][4]/(1000*value_list[tag][2]*value_list[tag][3]*0.05)
    #print(tag, ' ', ass['PriceUSD'])
    usable_miners = [x for x in efficiencies_list if x <= profitability_threshold]
    if usable_miners == []:
        usable_miners = [10000000000000]
        print("0 div")
    return sum(usable_miners)/len(usable_miners)

def coin_watts_annualised(tag):
    efficiency = average_efficiency(tag)
    print(tag, ' efficiency: ', efficiency)
    return efficiency*value_list[tag][3]*1.1*60*60*24*365.25/(3.6*10**12)

print('BCH')
print(coin_watts_annualised('BCH'))
print('BSV')
print(coin_watts_annualised('BSV'))
print('BTC')
print(coin_watts_annualised('BTC'))
print('DASH')
print(coin_watts_annualised('DASH'))
print('DOGE')
print(coin_watts_annualised('DOGE'))
print('ETC')
print(coin_watts_annualised('ETC'))
print('ETH')
print(coin_watts_annualised('ETH'))
print('LTC')
print(coin_watts_annualised('LTC'))
print('VTC')
print(coin_watts_annualised('VTC'))
print('XMR')
print(coin_watts_annualised('XMR'))
print('ZEC')
print(coin_watts_annualised('ZEC'))

'''
def average_efficiency(difficulty, block_reward, price, electricity_cost_kwh):
    profitability_threshold = (10**9/(2**32*difficulty))*block_reward*(price/electricity_cost_kwh)*3.6*10**6
    print("Prof threshold: ", profitability_threshold)
    print('Difficulty: ', difficulty)
    print('Price: ', price)
    usable_miners = [x for x in efficiencies_list if x <= profitability_threshold]
    if usable_miners == []:
        usable_miners = [1000000]
        print("0 div")
    return sum(usable_miners)/len(usable_miners)

def coin_watts_annualised(hashrate, difficulty, block_reward, price, electricity_cost_kwh):
    efficiency = average_efficiency(difficulty, block_reward, price, electricity_cost_kwh)
    print('Efficiency: ', efficiency)
    return efficiency*hashrate*1.1*60*60*24*365.25/(3.6*10**12)

'''



'''
ass = df_diffmean.iloc[2]
print(ass['asset'], coin_watts_annualised(ass['HashRate'], ass['DiffMean'], 6.25, ass['PriceUSD'], 0.05), 'GWh')


print(asset_with_ref_rates)


print(6.25*3600000*ass['PriceUSD']/(1000*10*60*ass['HashRate']*0.05))

# BCH: 6.25
# BSV: 6.25
# BTC: 6.25
# DASH: 2.88
# DOGE: 10000
# ETC: 0.125
# ETH: 2.31137
# LTC: 12.5
# VTC: 25
# XMR: 0.8
# ZEC: 6.25


['bch', 'bsv', 'btc', 'btg', 'dash', 'doge', 'etc', 'eth', 'ltc', 'vtc', 'xmr', 'zec']


'''
'''
print(df_diffmean.iloc[2]['HashRate'])
btc_diff = df_diffmean.iloc[2]['DiffMean']
for i in range(12):
    ass = df_diffmean.iloc[i]
    print(ass['asset'], coin_watts_annualised(ass['HashRate'], ass['FeeTotUSD'], ass['DiffMean'], btc_diff, 0.05)/10**9)


client = CoinMetricsClient("<cm_api_key>")

# or to use community API:
client = CoinMetricsClient()

#print(type(client.catalog_assets(assets=['btc'], metrics = ['HashRate'])))

response = requests.get('https://api.coinmetrics.io/v4/catalog/metrics?pretty=true&api_key=<your_key>').json()
print(response)
'''