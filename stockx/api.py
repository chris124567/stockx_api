"""This file queries the StockX API for search results."""
import requests

from http_util import HEADERS
from util import JSON_ERRORS


def search_tag_all(tag):
    """This returns all of the results for a given StockX tag in a list.

    Essentially, it keeps calling the individual search pages and adding
    their results together until we get 0 results.
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
    """This function returns the JSON of an individual results page of a given
    StockX tag's search results."""
    search_url = "https://stockx.com/api/browse?_tags=%s&page=%d" % (tag, page)
    try:
        response_json = requests.get(search_url, headers=HEADERS).json()
    except (JSON_ERRORS, requests.exceptions.RequestException):
        return None
    return response_json
