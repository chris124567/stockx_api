"""
This file queries the StockX API for search results.
"""

import json
import requests

from http_util import HEADERS
from util import JSON_ERRORS


def search_tag_all(tag):
    """
    This returns all of the results for a given StockX tag in a list.  Essentially, it keeps calling the individual search pages and adding their results together until we get 0 results.
    """
    current_page = 0
    total = float("inf")

    all_results = []
    while total > 0:
        response_json = search_tag(tag, current_page)
        try:
            total = response_json["Pagination"]["total"]
            for product in response_json["Products"]:
                all_results.append(product)
        except JSON_ERRORS:
            break
        current_page += 1

    return all_results


def search_tag(tag, page):
    """
    This function returns the JSON of an individual results page of a given StockX tag's search results.
    """
    search_url = "https://stockx.com/api/browse?_tags=%s&page=%d" % (tag,
                                                                     page)
    try:
        response = requests.get(search_url, headers=HEADERS)
    except requests.exceptions.RequestException:
        return None
    try:
        response_json = json.loads(response.text)
    except JSON_ERRORS:
        return None
    return response_json
