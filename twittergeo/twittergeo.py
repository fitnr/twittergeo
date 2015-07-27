#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of twittergeo.
# https://github.com/fitnr/twittergeo

# Licensed under the GNU General Public License v3 (GPLv3) license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>


def geojson(tweet, lite=None):
    '''
    Converts a tweepy Status object into a GeoJSON point TeatureClass

    tweet : a tweepy Status object
    lite (boolean) : If true, include only a small part of the tweet metadata
    '''
    feature = {}

    if tweet.geo:

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [tweet.geo['coordinates'][1], tweet.geo['coordinates'][0]]
            }
        }

        if lite:
            feature['properties'] = {
                "screen_name": tweet.user.screen_name,
                "userid": tweet.user.id,
                "text": tweet.text,
                "id": tweet.id,
                "source": tweet.source
            }

        else:
            feature['properties'] = tweet._json

    return feature
