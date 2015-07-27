# Twittergeo

Export geotagged tweets to GeoJSON.

## Install

Open your terminal and run:

````bash
pip install twittergeo
````

([Don't have Pip?](https://pip.pypa.io/en/stable/installing.html))

## Usage

To use the tool, you'll need a application registered with Twitter. Instructions from Twitter: [https://apps.twitter.com](https://apps.twitter.com).

Now that you have an application, you'll need the consumer key and the consumer secret. Enter them on the command line: 

````bash
$ KEY=<paste in the key>
$ SECRET=<paste in the secret>
````

And here's the command to download a GeoJSON of geotagged tweets:

````bash
$ twittergeo --user example_username --consumer-secret $SECRET --consumer-key $KEY -o example_username.geojson
````

### Setting up a config file

Pasting in your consumer key and secret every time is boring. Save a config file like so:

````yaml
apps:
    twittergeo:
        consumer_key: ...
        consumer_secret: ...

````

Call the file bots.yaml and save it in your home directory, and `twittergeo` will find it automatically. Or use a custom file:

````bash
$ twittergeo --search "some words" --config bots.yaml -o some_words.geojson
````

To download a search:
````bash
$ twittergeo --search "some words" --consumer-secret $SECRET --consumer-key $KEY > some_words.geojson
````

### Smaller files

Use the `--lite` option to get smaller files. The only properties saved will be the tweet's text and ID, and the user's screen_name and userid.

````bash
$ twittergeo --search "some words" --lite > some_words.geojson
````

### Get more tweets

By default, Twitter returns only 15 tweets, which is pretty weak. Use the `--count` parameter to request more. Note that Twittergeo will return `count` tweets, but ignore non-geotagged tweets, so your files will likely be much shorter. The Twitter API doesn't have a way request only geotagged tweets.

````bash
$ twittergeo --search "some words" --count 100 > some_words.geojson
````

### Geocode parameter

When using the search option, you can request tweets close to a particular point. The format to use is `latitude,longitude,radius`, where radius is either in miles (`mi`) or kilometers (`km`).

````bash
$ twittergeo --search "some words" --geocode 37.781157,-122.398720,1mi -o some_words_a.geojson
$ twittergeo --search "some words" --geocode 37.781157,-74.2644,10km -o some_words_b.geojson
````

### Options

````
usage: twittergeo [-h] [-c path] [--consumer-key key]
                  [--consumer-secret secret] [-u user | -f search] [--lite]
                  [--count COUNT] [--geocode GEOCODE] [-o OUTPUT]

Pull Twitter searches into GeoJSON

optional arguments:
  -h, --help            show this help message and exit
  -c path, --config path
                        path to config file to parse (json or yaml)
  --consumer-key key    Twitter consumer key
  --consumer-secret secret
                        Twitter consumer secret
  -u user, --user user  User timeline to search
  -f search, --search search
                        Search string
  --lite                Output minimal information about tweets
  --count COUNT         Maximum number of tweets to return
  --geocode GEOCODE     optional geocode parameter when searching
  -o OUTPUT, --output OUTPUT
                        output file (default is stdout)
````