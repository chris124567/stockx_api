#!/usr/bin/env python3
"""Searches (completely) for a given brand then formats the output to a csv
file."""

import os
import csv
import json

import stockx.api
from util import die, JSON_ERRORS

JSON_OUT_DIR = "json_out"
BRAND = "supreme"


def all_brand_search_results(brand):
    """This function gathers all results for a given brand (or rather, StockX
    tag) and writes the JSON output to a file.

    I just chose to save the output to a file instead of a variable so I
    do not have to redownload 10 MB of output every time I run the csv
    output part of the program.
    """
    brand_list = stockx.api.search_tag_all(brand)
    brand_list_json = json.dumps(brand_list)
    with open(JSON_OUT_DIR + "/" + brand, "w+") as json_out:
        json_out.write(brand_list_json)


def write_csv(brand):
    """This function writes the output for every product listed in the JSON to <brand>.csv.

    The CSV includes: StockX ID, StockX URL, StockX Ticker, Title,
    Release Date, Brand, Category, Colorway, Gender, Retail Price,
    averageDeadstockPrice, and StockX's Price Premium (their
    calculations are usually averageDeadstockPrice/retailPrice but
    sometimes it differs so I am unsure how they actually calculate it)
    """
    with open(brand + ".csv", "w+") as csvfile:
        filewriter = csv.writer(
            csvfile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([
            'id', 'url', 'tickerSymbol', 'title', 'releaseDate', 'brand',
            'category', 'colorway', 'gender', 'retailPrice',
            'averageDeadstockPrice', 'pricePremium'
        ])
        with open(JSON_OUT_DIR + "/" + brand, "r") as supreme_json:
            try:
                results_json = json.load(supreme_json)
            except JSON_ERRORS:
                die()
            for product in results_json:
                try:
                    filewriter.writerow([
                        product["id"],
                        "https://stockx.com/%s" % (product["urlKey"]),
                        product["tickerSymbol"], product["title"],
                        product["releaseDate"], product["brand"],
                        product["category"], product["colorway"],
                        product["gender"], product["retailPrice"],
                        product["market"]["averageDeadstockPrice"],
                        product["market"]["pricePremium"]
                    ])
                except JSON_ERRORS:
                    die()


os.mkdir(JSON_OUT_DIR)
all_brand_search_results(BRAND)
write_csv(BRAND)
