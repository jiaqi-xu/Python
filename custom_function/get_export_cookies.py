'''
Export cookies list from chrome:
e.g.
input = [
{
    "domain": ".staples.com",
    "expirationDate": 1584211044,
    "hostOnly": False,
    "httpOnly": False,
    "name": "__gads",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "ID=b12d13738eb2067b:T=1521139044:S=ALNI_Ma6_OEpzNntiOsoBhJ6dkR5eFKSRg",
    "id": 1
},
{
    "domain": ".staples.com",
    "expirationDate": 1552675230.177658,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_abck",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "70457BAE3BE810DE7C940BBB029091BDD803334C72720000CCBDAA5A7D13C03A~0~AvHbX5+GO+Q1UJkqNfctnyK5UNQNIc9hPQ4rLZiXIcA=~-1~-1",
    "id": 2
}]


'''
def get_cookies(exported_cookies_list):
    cookies = {}
    for cookie in exported_cookies_list:
        cookie_key = cookie.get("name")
        cookie_value = cookie.get("value")
        cookies.update({
            cookie_key: cookie_value
        })

    return cookies

