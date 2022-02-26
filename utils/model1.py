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

efficiencies_list = [9.9167,2.0000,0.7657,0.5108,0.2734,0.0980,0.2581,0.0971,0.0980,0.1261,0.1575,0.1000,0.1261,0.0980,0.1176,0.0980,
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
metrics = "HashRate, DiffMean, FeeTotUSD, FeeTotNtv"
frequency = "1d"
start_time = "2018-11-25"
end_time = "2018-11-25"




logging.info("Getting prices...")
df_diffmean = client.get_asset_metrics(
    assets=asset_with_ref_rates,
    metrics=metrics,
    frequency=frequency,
    start_time=start_time,
    end_time=end_time
).to_dataframe()

###
def average_efficiency(hashrate, miner_fees, difficulty, btc_difficulty, electricity_cost_kwh):
    print("Hashrate: ", hashrate)
    gigahashes_per_day = hashrate*60*60*24*1000/1000
    mining_revenue_per_gigahash = miner_fees/gigahashes_per_day
    print("Gigahashes per day: ", gigahashes_per_day)
    print("Mining revenue per gigahash", mining_revenue_per_gigahash)
    print("Miner fees: ", miner_fees)
    difficulty_factor = difficulty/btc_difficulty
    print("Difficulty: ", difficulty_factor)
    electricity_cost_joule = electricity_cost_kwh/3600000
    print(electricity_cost_joule)
    profitability_threshold = (mining_revenue_per_gigahash*difficulty_factor)/electricity_cost_joule
    print("Prof threshold: ", profitability_threshold)
    usable_miners = [x for x in efficiencies_list if x <= profitability_threshold]
    #print(profitability_threshold)

    if usable_miners == []:
        usable_miners = [1000000]
        print("0 div")
    return sum(usable_miners)/len(usable_miners)

def coin_watts_annualised(hashrate, miner_fees, difficulty, btc_difficulty, electricity_cost_kwh):
    efficiency = average_efficiency(hashrate, miner_fees, difficulty, btc_difficulty, electricity_cost_kwh)
    return efficiency*hashrate*1.1*60*60*24*365.25/10**12

##
btc_diff = df_diffmean.iloc[2]['DiffMean']
ass = df_diffmean.iloc[2]
print(ass['asset'], coin_watts_annualised(ass['HashRate'], ass['FeeTotUSD'], ass['DiffMean'], btc_diff, 0.05)/10**9)
print(ass['FeeTotNtv'])
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