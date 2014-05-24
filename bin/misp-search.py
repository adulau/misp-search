#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import argparse
import json

from pymisp import PyMISP

argParser = argparse.ArgumentParser(description='misp-search - search MISP from command line')
argParser.add_argument('-a', action='store_true', help='Add an event based on file attributes (default: False)', default=False)
argParser.add_argument('-u', type=str, help='URL of the MISP instance', required=True)
argParser.add_argument('-k', type=str, help='MISP API key', required=True)
argParser.add_argument('-c', type=str, help='MISP SSL certificate file', required=True)
argParser.add_argument('-o', type=str, help='Output format: json (default) or event_id', default='json')
argParser.add_argument('-q', type=str, action='append', help='One or more value(s) to query', required=True)
argParser.add_argument('-d', action='store_true', help='Debug mode', default=False)

args = argParser.parse_args()

misp = PyMISP(args.u , args.k, args.c, "json")


for q in args.q:
    r = misp.search(q)
    if r.status_code == 200:
        if args.o == "event_id":
            response = json.loads(r.text)
            for event in response['response']['Event']:
                print "%s,%s" % (event['id'],q)
        else:
            print r.text
    else:
        if args.d:
            print "Query %s -> HTTP error code %d " % (q,r.status_code)
