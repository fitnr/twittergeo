# Twittergeo

Export geotagged tweets to GeoJSON.

## Install

Open your terminal and run:

````bash
pip install twittergeo
````

([Don't have Pip?](https://pip.pypa.io/en/stable/installing.html))

## Use

To use the tool, you'll need a application registered with Twitter. Instructions from Twitter: [https://apps.twitter.com](https://apps.twitter.com).

When your application is set, you'll get two keys, which need to be added to a config file.

### Setting up a config file

You'll need a `bots.yaml` (or `.json`) file with you keys, because copying and pasting them is boring, and environment variabled don't work if you have several applications. Save a config file like so:

````yaml
apps:
    twittergeo:
        consumer_key: ...
        consumer_secret: ...

````

Call the file bots.yaml and save it in your home directory. `twittergeo` will find it automatically. Or use a custom file:

````bash
$ twittergeo --search "some words" --config configfile.yaml -o some_words.geojson
````

### Smaller files

Use the `--lite` option to get smaller files. The only properties saved will be the tweet's `text` and `id` and the user's `screen_name` and `userid`.

````bash
$ twittergeo --search "some words" --lite > some_words.geojson
````

### Get more tweets

By default, Twitter returns only 15 tweets, which is pretty weak. Use the `--count` parameter to request more. Note that Twittergeo will return `count` tweets, but that may include non-geotagged tweets, so your files will likely be much shorter. The Twitter API doesn't have a way request only geotagged tweets.

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
usage: twittergeo [-h] [-c path] [--app APP] [-u screen_name | -f search]
                  [--lite] [--count COUNT] [--geocode LAT,LON,RADIUS]
                  [--since ID] [--max ID] [-o OUTPUT]

Pull Twitter searches into GeoJSON

optional arguments:
  -h, --help            show this help message and exit
  -c path, --config path
                        jsom or yaml config file
  --app APP             Twitter app to read in config (default: twittergeo)
  -u screen_name, --user screen_name
                        User timeline to search
  -f search, --search search
                        Search string
  --lite                Output minimal information about tweets
  --count COUNT         Maximum number of tweets to return (default: 500)
  --geocode LAT,LON,RADIUS
                        optional geocode parameter when searching
  --since ID            Fetch tweets since this ID
  --max ID              Fetch tweets before this ID
  -o OUTPUT, --output OUTPUT
                        output file (default: stdout)
````