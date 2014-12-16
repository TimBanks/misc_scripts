#!/usr/bin/python

import pymongo
import datetime
import sys
import getopt
import argparse

from pymongo import MongoClient

#client connect string
client = MongoClient('mongodb://user:pass@mongo-host:port')

db = client.ip_list

def read_list(args):


#parses the portion of the variable we will print and then escapes the other text we will print with it
    w = args.dc +"/"+ args.dc + ".list"


#opens the file and adds it to an array.  Also drops the newline character.  Return lines allows the list to be used later
    with open(w) as f:

    lines = f.read().splitlines()

    f.close()
    return lines


def add_ip(lines):
    for ip in lines:
        post = {"block": ip, "status": "unused"}


def main(args):
    lines = read_list(args)

    posts = args.dc +"_list"
    post_id = posts.insert(add_ip(lines))
    print post_id



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add free IPs to database')
    parser.add_argument("dc",choices=['iad', 'ord', 'dfw', 'lon', 'hkg', 'sjc', 'syd'], help='Enter the 3-letter code for one of the datacenters')

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    main(args)
