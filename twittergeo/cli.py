#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of twittergeo.
# https://github.com/fitnr/twittergeo

# Licensed under the GNU General Public License v3 (GPLv3) license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

import argparse
import json
from twitter_bot_utils import API

from .twittergeo import twittergeo


def main():
    parser = argparse.ArgumentParser('twittergeo', description='Pull Twitter searches into GeoJSON')

    parser.add_argument('-c', '--config', dest='config_file', metavar='path', default=None, type=str, help='jsom or yaml config file')
    parser.add_argument('--app', default='twittergeo', type=str, help='Twitter app to read in config (default: %(default)s)')
    parser.add_argument('--consumer-key', type=str, help=argparse.SUPPRESS)
    parser.add_argument('--consumer-secret', type=str, help=argparse.SUPPRESS)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u', '--user', type=str, dest='screen_name', metavar='screen_name', help='User timeline to search')
    group.add_argument('-f', '--search', type=str, dest='search', metavar='search', help='Search string')

    parser.add_argument('--lite', action='store_true', help='Output minimal information about tweets')
    parser.add_argument('--count', type=int, default=100, help='Maximum number of tweets to return (default: %(default)s)')

    parser.add_argument('--geocode', type=str, metavar='LAT,LON,RADIUS', help='optional geocode parameter when searching')

    parser.add_argument('--since', metavar='ID', type=int, help='Fetch tweets since this ID')
    parser.add_argument('--max', metavar='ID', type=int, help='Fetch tweets before this ID')

    parser.add_argument('-o', '--output', type=str, help='output file (default: stdout)', default='/dev/stdout')

    arguments = parser.parse_args()

    twitter = API(arguments)

    if getattr(arguments, 'screen_name'):
        method = twitter.user_timeline

    if getattr(arguments, 'search'):
        method = twitter.search

    keys = ('search', 'screen_name', 'geocode', 'since_id', 'max_id')
    kwargs = {k: v for k, v in vars(arguments).items() if k in keys and v is not None}

    geojson = twittergeo(method, arguments.count, arguments.lite, **kwargs)

    with open(arguments.output, 'w') as f:
        json.dump(geojson, f)

if __name__ == '__main__':
    main()
