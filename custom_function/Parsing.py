import re

PRICE_RE = re.compile(r'([+-.]?\d\d*(\.\d\d?)?)')
COMMA_CENT_SEP_RE = re.compile(r',(\d{2})(?:\b|$)')
WHITESPACE_PRICE_RE = re.compile(r'\s+')


def _generate_res(*re_strings):
    return tuple(re.compile(s, flags=re.IGNORECASE) for s in re_strings)


TRUE_RES = _generate_res(
    r'((((\d+\s?\-)?\s?\d+)\s?)|(next\s?))(business )?(day|week|month)s?',
    r'[1-9]+\d* (?:left|remain)',
    r'\bavail\b',
    r'\byes\b',
    r'^y$',
    r'add\s?to\s?cart',
    r'available online',
    r'available',
    r'buy\s?now',
    r'delivery: most areas',
    r'expected (to )?(deliver[y]?|ship)',
    r'free 2-day shipping',
    r'in[-\s_]stock',
    r'instock',
    r'limited (availability|quantit(y|ies))',
    r'low stock',
    r'on order',
    r'online',
    r'pre[\s-]?order',
    r'ready for delivery',
    r'scheduled delivery',
    r'ships by (?:mon|tue|wed|thu|fri)',
    r'ships in 24 hours',
    r'ships same day',
    r'ships today',
    r'special order',
    r'true',
    r'usually available in',
    r'usually ships (with)?in',
    r'within 24 hours',
)


FALSE_RES = _generate_res(
    r'\bno\b',
    r'\bre-order\b',
    r'\bunavail\b',
    r'^n$',
    r'available soon',
    r'back[-\s_]?order(?!ed\.[\s]*Due in stock)',
    r'coming soon',
    r'discontinued',
    r'expected (?:to )?(arriv|soon)',
    r'false',
    r'in[\-\s_]stores?[\-\s_]only',
    r'no longer available',
    r'not[\s_-]*available',
    r'not currently available',
    r'not in stock',
    r'offline',
    r'only 0+ left',
    r'please check back',
    r'sold[-\s_]?out',
    r'taking orders for this product',
    r'this product is not available',
    r'unavailable',
    r'out[\s_-]*of[\s_-]*stock',
    r'retired'
)


def check_availability(avail):
    if not isinstance(avail, (list, tuple)):
        avail = avail,

    for a in avail:
        if isinstance(a, bool):
            return a

        try:
            if int(float(a)) == float(a):
                return int(float(a)) > 0
        except (ValueError, TypeError):
            pass

        if a is None:
            return None

        if not isinstance(a, basestring):
            raise TypeError('Invalid availability type {0}'.format(type(a)))

        if any(false_re.search(a) for false_re in FALSE_RES):
            return False

        if any(true_re.search(a) for true_re in TRUE_RES):
            return True


def convert_price_to_float(price):
    """
    This method will tries its best to return a float from the string given
    It will TRUNCATE to two decimal places where a decimal exists
    """

    if price is None:
        return None

    elif isinstance(price, (float, int)):
        return float(price)

    elif isinstance(price, basestring):
        price = WHITESPACE_PRICE_RE.sub(' ', price).strip()
        if not price:
            return None

        if 'free' in price.lower():
            return 0.0

        if price == '.':
            return None

        # Handle commas as cent separators
        price = COMMA_CENT_SEP_RE.sub(r'.\1', price)

        for token in [',', '$', '!', '/', '\t', '\n', '\r']:
            price = price.replace(token, '')

        try:
            return float(PRICE_RE.search(price).group(1))
        except:
            raise PriceNotFoundException(price)

    else:
        raise InvalidPriceTypeException(price)


class PriceNotFoundException(Exception):

    def __init__(self, price_str):
        msg = u'Could not find price in \'{0}\''
        if isinstance(price_str, unicode):
            msg = msg.format(price_str).encode('utf-8')
        else:
            msg = msg.encode('utf-8').format(price_str)
        Exception.__init__(self, msg)


class InvalidPriceTypeException(Exception):

    def __init__(self, price):
        msg = u'Invalid price type: {0}'.format(type(price))
        Exception.__init__(self, msg.encode('utf-8'))