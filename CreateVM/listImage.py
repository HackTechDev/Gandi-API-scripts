#!/usr/bin/python3

import pprint
import xmlrpc.client

pp = pprint.PrettyPrinter(indent=4)

api = xmlrpc.client.ServerProxy('https://rpc.gandi.net/xmlrpc/')

apikey = 'API KEY'

images = api.hosting.image.list(apikey, {'datacenter_id': 1})
debian_images = [x for x in images if x['label'].lower().startswith('debian')]


for image in debian_images:
    disk_id = image['disk_id']
    pp.pprint( image['label'] + " : " +str(disk_id))
