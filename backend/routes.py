from flask import current_app,jsonify,request
from flask_cors import CORS, cross_origin
from app import create_app,db
from models import Articles,articles_schema
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
from datetime import date, datetime, timedelta

from solutions import *


#set up coinmetrics
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
#get date (yesterday: last available data)
# Create an application instance
app = create_app()
CORS(app)


@app.route("/")
def home():

    return 


# Define a route to fetch the avaialable articles
@app.route("/articles", methods=["GET"], strict_slashes=False)
def articles():

	articles = Articles.query.all()
	results = articles_schema.dump(articles)

	return jsonify(results)


@app.route("/coins", methods=["GET"])
def coins():
	yesterday = datetime.now() - timedelta(1)
	d1 = yesterday.strftime("%Y-%m-%d")

	metrics = "PriceUSD"
	frequency = "1d"
	start_time = d1
	end_time = d1

	asset_with_ref_rates = ['bch', 'bsv', 'btc', 'btg', 'dash', 'doge', 'etc', 'eth', 'ltc', 'vtc', 'xmr', 'zec']

	df_diffmean = client.get_asset_metrics(
    	assets=asset_with_ref_rates,
    	metrics=metrics,
    	frequency=frequency,
    	start_time=start_time,
    	end_time=end_time).to_dataframe()

	rates = {}

	for i in range(12):
		ass=df_diffmean.iloc[i]
		rates[ass['asset']] = ass['PriceUSD']

	return jsonify(rates)

solutions = []
comparisons = []

@app.route("/portfolio", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type'])
def portfolio():
    vals = request.get_json(force=True)['vals']
    x = out(vals)
    solutions = x[0]
    comparisons = x[1]
    return {'out':x}

# change debug to False when in prod
if __name__ == "__main__":
	app.run(debug=True, port=5000)
