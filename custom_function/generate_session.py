import requests
import json
from datetime import datetime


def generate_cookis(zip_code):

    result = {}
    session = requests.Session()
    # GET request for product page which will generate cookies
    response_1 = session.get('https://www.ruralking.com/extreme-shock-collars')

    # GET request which get stores based on zip code
    response_2 = session.get(
        'https://www.ruralking.com//rest/V1/search-for-stores'
        '/{zip_code}'.format(zip_code=zip_code)
    )
    stores_info = json.loads(response_2.content)
    comparable_store = stores_info[0].get('store_number')

    # POST request for choosing store
    headers = {
        'x-requested-with': 'XMLHttpRequest'
    }

    data = [
        ('store', str(comparable_store))
    ]

    response_3 = session.post(
        'https://www.ruralking.com/widget/store/save',
        data=data,
        headers=headers
    )

    if json.loads(response_3.content).get('success') == 1:
        for cookie in session.cookies:
            if cookie.name == "PHPSESSID":
                result.update({
                    'cookies': {
                        cookie.name: cookie.value
                    },
                    'expiry': {
                        'expires_at': datetime.fromtimestamp(cookie.expires)
                    }
                })

    return result
