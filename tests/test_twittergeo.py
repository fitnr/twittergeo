#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of twittergeo.
# https://github.com/fitnr/twittergeo

# Licensed under the GNU General Public License v3 (GPLv3) license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

import unittest
import json
import tweepy
import twittergeo
import requests

validate_endpoint = 'http://geojsonlint.com/validate'

TWEET = {
    'follow_request_sent': None, 'has_extended_profile': False, 'profile_use_background_image': True, 'default_profile_image': True,
    'id': 61043461, 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'verified': False, 'profile_text_color': '333333',
    'profile_image_url_https': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', 'profile_sidebar_fill_color': 'DDEEF6',
    'entities': {
        'description': {'urls': []}}, 'followers_count': 114, 'profile_sidebar_border_color': 'C0DEED',
    'id_str': '61043461', 'profile_background_color': 'C0DEED', 'listed_count': 22, 'is_translation_enabled': False, 'utc_offset': -14400,
    'statuses_count': 654785, 'description': '', 'friends_count': 0, 'location': '',
    'profile_link_color': '0084B4', 'profile_image_url': 'http://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', 'following': None, 'geo_enabled': True,
    'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'screen_name': 'googuns_prod', 'lang': 'en', 'profile_background_tile': False,
    'favourites_count': 0, 'name': 'GooGuns', 'notifications': None, 'url': None, 'created_at': 'Tue Jul 28 22:49:22 +0000 2009', 'contributors_enabled': False,
    'time_zone': 'Eastern Time (US & Canada)', 'protected': False, 'default_profile': True, 'is_translator': False,
    'text': '047adb82b3000000',
    'source': '<a href="http://www.google.com/" rel="nofollow">Google</a>',
    'geo': {
        'type': 'Point', 'coordinates': [29.10438635, -64.47487041]
    },
    'user': {
        'follow_request_sent': None, 'has_extended_profile': False, 'profile_use_background_image': True, 'default_profile_image': True, 'id': 61043461,
        'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'verified': False, 'profile_text_color': '333333',
        'profile_image_url_https': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', 'profile_sidebar_fill_color': 'DDEEF6',
        'entities': {'description': {'urls': []}}, 'followers_count': 114, 'profile_sidebar_border_color': 'C0DEED', 'id_str': '61043461', 'profile_background_color': 'C0DEED', 'listed_count': 22,
        'is_translation_enabled': False, 'utc_offset': -14400, 'statuses_count': 654785, 'description': '', 'friends_count': 0, 'location': '', 'profile_link_color': '0084B4',
        'profile_image_url': 'http://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', 'following': None, 'geo_enabled': True,
        'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'screen_name': 'googuns_prod', 'lang': 'en', 'profile_background_tile': False, 'favourites_count': 0,
        'name': 'GooGuns', 'notifications': None, 'url': None, 'created_at': 'Tue Jul 28 22:49:22 +0000 2009', 'contributors_enabled': False, 'time_zone': 'Eastern Time (US & Canada)',
        'protected': False, 'default_profile': True, 'is_translator': False
    }
}


class TestCase(unittest.TestCase):

    api = tweepy.API()
    status = tweepy.Status.parse(api, TWEET)

    def test_basics(self):
        assert twittergeo
        assert twittergeo.feature
        assert twittergeo.collection

    def test_feature(self):
        feature = twittergeo.feature(self.status)

        assert feature['type'] == 'Feature'
        assert feature['geometry']['type'] == 'Point'
        assert feature['geometry']['coordinates'] == [-64.47487041, 29.10438635]

        assert feature['properties']['friends_count'] == 0
        assert feature['properties']['user']['screen_name'] == 'googuns_prod'

    def test_feature_lite(self):
        feature = twittergeo.feature(self.status, lite=True)

        assert feature['properties']['screen_name'] == 'googuns_prod'

    def test_collection(self):
        collection = twittergeo.collection()

        collection['features'] = [twittergeo.feature(self.status)]

        request = requests.post(validate_endpoint, data=json.dumps(collection))

        assert request.ok == True
