#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of twittergeo.
# https://github.com/fitnr/twittergeo

# Licensed under the GNU General Public License v3 (GPLv3) license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from . import twittergeo
import argparse
import json
from twitter_bot_utils.api import API
from tweepy import Cursor

def main():
    parser = argparse.ArgumentParser('twittergeo', description='Pull Twitter searches into GeoJSON')

    parser.add_argument('-c', '--config', metavar='path', default=None, type=str, help='path to config file to parse (json or yaml)')
    parser.add_argument('--consumer-key', type=str, metavar='key', help='Twitter consumer key')
    parser.add_argument('--consumer-secret', type=str, metavar='secret', help='Twitter consumer secret')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u', '--user', type=str, metavar='user', dest='screen', help='User timeline to search')
    group.add_argument('-f', '--search', type=str, metavar='search', dest='q', help='Search string')

    parser.add_argument('--lite', action='store_true', help='Output minimal information about tweets')
    parser.add_argument('--count', type=int, default=100, help='Maximum number of tweets to return')
    parser.add_argument('--geocode', type=str, help='optional geocode parameter when searching')

    parser.add_argument('-o', '--output', type=str, help='output file (default is stdout)')

    arguments = parser.parse_args()

    twitter = API(app='twittergeo', config_file=arguments.config)

    kwargs = {k:v for k, v in vars(arguments).items() if k in ('q', 'screen', 'geocode') and v is not None}

    if 'screen' in kwargs:
        kwargs['screen_name'] = kwargs.pop('screen')

    if getattr(arguments, 'screen'):
        method = twitter.user_timeline

    if getattr(arguments, 'q'):
        method = twitter.search

    geojson = twittergeo.collection()

    for tweet in Cursor(method, **kwargs).items(arguments.count):
        feature = twittergeo.feature(tweet, lite=arguments.lite)

        if feature:
            geojson['features'].append(feature)

    if arguments.output:
        with open(arguments.output, 'w') as f:
            json.dump(geojson, f)
    else:
        print(json.dumps(geojson))

if __name__ == '__main__':
    main()
