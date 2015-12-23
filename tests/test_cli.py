#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of twittergeo.
# https://github.com/fitnr/twittergeo

# Licensed under the GNU General Public License v3 (GPLv3) license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

import unittest
import sys
from os import path, remove
import json
import tweepy
import twittergeo.cli
import mock


TIMELINE = [
    {
        "id": 1235,
        "id_str": "1235",
        "in_reply_to_user_id": None,
        "retweeted": False,
        "entities": {},
        "user": {"screen_name": "Random"},
        "text": "Lorem ipsum dolor sit amet",
        "geo": {
            "coordinates": [1, 1]
        }
    },
    {
        "id": 1234,
        "id_str": "1234",
        "in_reply_to_user_id": 1,
        "retweeted": False,
        "entities": {},
        "user": {"screen_name": "Random"},
        "text": "Quas doloremque velit deleniti unde commodi voluptatum incidunt.",
        "geo": {
            "coordinates": [1, 2]
        }
    },
    {
        "id": 1233,
        "id_str": "1233",
        "retweeted": True,
        "in_reply_to_user_id": None,
        "entities": {},
        "user": {"screen_name": "Random"},
        "text": "Sunt, culpa blanditiis, nostrum doloremque illum excepturi quam.",
        "geo": {
            "coordinates": [2, 1]
        }
    },
]


def fake_timeline():
    return [tweepy.Status.parse(tweepy.api, t) for t in TIMELINE]


class CliTestCase(unittest.TestCase):

    def setUp(self):
        self.sink = 'test-result.json'
        self.config = path.join(path.dirname(__file__), 'fixtures', 'bots.yaml')

    @mock.patch.object(tweepy.Cursor, 'items', return_value=fake_timeline())
    def testCliUserTimeline(self, *_):
        sys.argv = ['twittergeo', '-u', 'foo', '-c', self.config, '-o', self.sink]

        twittergeo.cli.main()

        with open(self.sink) as f:
            result = json.load(f)

        remove(self.sink)

        assert isinstance(result, dict)
        assert result['type'] == 'FeatureCollection'

    @mock.patch.object(tweepy.Cursor, 'items', return_value=fake_timeline())
    def testCliSearch(self, *_):
        sys.argv = ['twittergeo', '-f', 'foo', '-c', self.config, '-o', self.sink]

        twittergeo.cli.main()

        with open(self.sink) as f:
            result = json.load(f)

        remove(self.sink)

        assert isinstance(result, dict)

        assert result['type'] == 'FeatureCollection'


if __name__ == '__main__':
    unittest.main()
