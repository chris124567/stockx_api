"""This file allows us to extract the JSON embedded in the HTML of a given
product (it's in a script and is assigned to the variable window.preLoaded)"""

import re
import json

import requests

from http_util import HEADERS


def get_product_html(product_url):
    """Downloads the content of a given product's web page and returns the
    text."""
    try:
        response = requests.get(product_url, headers=HEADERS)
    except requests.exceptions.RequestException:
        response = None
    return response.text


def find_product_json(html_text):
    """Uses regular expression to find the embedded JSON text within the
    product page."""
    regex = r"window\.preLoaded\s*=\s*(.*)"  # regex to find the json embedded in the html
    match = re.findall(regex, html_text)
    if match is not None:
        json_text = match[0]
        json_text = json_text.replace(";", "")  # get rid of semicolons
    else:
        json_text = None
    return json_text


def product_json_load(json_text):
    """Loads the product page's embedded JSON."""
    try:
        product_json = json.loads(json_text)
    except ValueError:
        product_json = None
    return product_json


def product_json_all(product_url):
    """Puts the previous functions all together."""
    html_text = get_product_html(product_url)
    if html_text:
        json_text = find_product_json(html_text)
        if json_text:
            product_json = product_json_load(json_text)
            if product_json:
                return product_json
    return None
