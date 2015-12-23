#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of twittergeo.
# https://github.com/fitnr/twittergeo

# Licensed under the GNU General Public License v3 (GPLv3) license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from tweepy import Cursor

def twittergeo(method, count=None, lite=None, **kwargs):
    count = count or 100
    geojson = collection()

    for tweet in Cursor(method, **kwargs).items(count):
        feat = feature(tweet, lite=lite)

        if feat:
            geojson['features'].append(feat)

    return geojson


def collection():
    return {
        "type": "FeatureCollection",
        "features": []
    }


def feature(tweet, lite=None):
    '''
    Converts a tweepy Status object into a GeoJSON point TeatureClass

    tweet : a tweepy Status object
    lite (boolean) : If true, include only a small part of the tweet metadata
    '''
    feat = {}

    if hasattr(tweet, 'geo'):

        feat = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [tweet.geo['coordinates'][1], tweet.geo['coordinates'][0]]
            }
        }

        if lite:
            feat['properties'] = {
                "screen_name": tweet.user.screen_name,
                "userid": tweet.user.id,
                "text": tweet.text,
                "id": tweet.id,
                "source": tweet.source
            }

        else:
            feat['properties'] = tweet._json

    return feat
