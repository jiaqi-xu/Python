import pymongo
from copy import deepcopy

db = pymongo.MongoClient()['swift']

site = db.sites.find_one({'name': 'google.com'})
fields = [f for f in db.fields.find({'site': site['_id']})]
map(lambda a: a.pop('_id'), fields)
map(lambda a: a.pop('site'), fields)

rc = site['request_config']

def fix_headers(rc, c):
    for k in rc['*']['headers']:
        rc['*']['headers'][k] = rc['*']['headers'][k].replace('google.com', c)

for child_site in [
    'google.ca', 'google.co.uk', 'google.de', 'google.fr', 'google.com.co',
    'google.com.br', 'google.co.jp', 'google.ec', 'google.cl',
    'google.es', 'google.it', 'google.com.au',
    'google.nl', 'google.ch', 'google.cz', 'google.com.ar', 'google.com.bo',
    'google.com.mx', 'google.com.pe'

]:
    cs = db.sites.find_one({'name': child_site})
    rc2 = deepcopy(rc)
    fix_headers(rc2, child_site)
    cs['request_config'] = rc2
    print db.sites.save(cs), cs['name']
    print db.fields.remove({'site': cs['_id']})
    for f in fields:
        fn = deepcopy(f)
        fn['site'] = cs['_id']
        db.fields.insert_one(fn)
