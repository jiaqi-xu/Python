def key_lookup(dct, key, default=None, sep='.'):
    """
    simplify json dictionary lookup
    ie.
        print key_lookup(
            resp.json(),
            'productDetail.softhardProductdetails.0.fbmMerchants'
        )

    :param dct: nested/single key lookup object
    :type dct/list/tuple:
    :param key: list or single of key(s)/index(es) to lookup by
    :type key: str/list/tuple
    :param default: return value if key not found
    :type default: any
    :param sep: seperator use to divide keys in string
    :type sep: string
    :returns: any

    """

    if isinstance(key, (list, tuple)):
        for k in key:
            val = key_lookup(dct, k, default=default, sep=sep)
            if val is not None:
                return val
        return

    try:
        key = key.split(sep, 1)
        try:
            key[0] = int(key[0])
        except ValueError:
            pass

        if len(key) > 1:
            return key_lookup(dct[key[0]], key[1], default=default, sep=sep)

        return dct[key[0]]
    except (IndexError, TypeError, KeyError):
        return default