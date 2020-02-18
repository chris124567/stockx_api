"""The variables in this file are used to give the impression that we are a
legitimate web browser visiting StockX (we are not using the official API)"""

# https://techblog.willshouse.com/2012/01/03/most-common-user-agents/ - always updated and contains most common user agents
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"

# headers chrome uses
HEADERS = {
    'authority':
    'stockx.com',
    'pragma':
    'no-cache',
    'cache-control':
    'no-cache',
    'upgrade-insecure-requests':
    '1',
    'user-agent':
    USER_AGENT,
    'sec-fetch-user':
    '?1',
    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site':
    'same-origin',
    'sec-fetch-mode':
    'navigate',
    'accept-encoding':
    'gzip, deflate, br',
    'accept-language':
    'en-US,en;q=0.9',
}
