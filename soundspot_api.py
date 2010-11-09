""" Soundspot API

Examples of API usage.
This is an alpha version. API will be changed.
Please send feature requests and questions to alex at extensibl.com
"""

import urllib, urllib2
import urlparse
from urllib2 import Request
from urllib2 import HTTPError, URLError

# CONSTANTS
BASE_URL = 'http://soundspot.fm'

## Autocomplete
URL_AC_VENUES = '/api/ac/venues'
URL_AC_ARTISTS = '/api/ac/artists'

## Search
URL_SEARCH = '/api/search'

## Operations with gigs
URL_GIG_ADD = '/api/gig/add'

## Get venue or artist details
URL_ARTIST_GET = '/api/artist/get'
URL_VENUE_GET = '/api/venue/get'
# END CONSTANTS


def api_ac_venues(q, limit = 10, offset = 0):
    """  Autocomplete for venues
    
    Args:
        q - autocomplete string
        limit - integer, range 1..100
        offset - integer >= 0
    
    Example:
        >>> api_ac_venues('Al')
        u"Alliance Francaise de Melbourne, St Kilda\nAlbert Park Yacht Club\nAlbany Bowling Club\nAlbany Town Hall Theatre"

    """
    url = urlparse.urljoin(BASE_URL, URL_AC_VENUES)
    data = urllib.urlencode({ 'q': q, 'limit': limit, 'offset': offset }) 
    return urllib2.urlopen(Request(url, data)).read() # make POST request


def api_ac_artists(q, limit = 10, offset = 0, url = ''):
    """  Autocomplete for artists
    
    Args:
        q - autocomplete string
        limit - integer, range 1..100
        offset - integer >= 0
    
    Example:
        >>> api_ac_artists('Al')
        "Zen Burger\nZebyah"

    """
    url = urlparse.urljoin(BASE_URL, URL_AC_ARTISTS)
    data = urllib.urlencode({ 'q': q, 'limit': limit, 'offset': offset })
    return urllib2.urlopen(Request(url, data)).read() # make POST request


def api_search(venue = '', artist = '', date = '', limit = 10, offset = 0):
    """  Gigs search
    
    Args:
        venue - venue name
        artist - artist name
        date - date (mm/dd/yyyy)
        limit - integer, range 1..100
        offset - integer >= 0
    
    Example:
        >>> api_search(artist = 'Lisa Mitchell')
        [{"name": null, 
          "artist": {"name": "Lisa Mitchell"}, 
          "price": "$62.50", 
          "venue": {"map": [-31.937647999999999, 115.792209], 
                    "name": "Quarry Amphitheatre, Floreat"}, 
                    "kw_venue": ["quarry", "amphitheatre,", "floreat"], 
          "date": "Wednesday 10 November", 
          "state": "WA", 
          "time": "6pm", 
          "genre": "Rock & Pop", 
          "datetime_parsed": "2010-11-10T18:00:00", 
          "_id": "4cd5d69c10f12168fb000df0", 
          "kw_musician": ["lisa", "mitchell"]}]
          
    """
    url = urlparse.urljoin(BASE_URL, URL_SEARCH)
    data = urllib.urlencode({'venue' : venue, 
                             'artist': artist, 
                             'date': date,
                             'limit' : limit, 'offset': offset})
    return urllib2.urlopen(Request(url, data)).read()

def api_get_venue(object_id = '', name = ''):
    """ Get venue by its name and/or object id
    
    Example:
        >>> api_get_venue(name = 'The Plenary, Melbourne Exhibition and Convention Centre, Southbank')
        {u'_id': ObjectId('4cd04973312f917a1c000080'), u'name': u'The Plenary, Melbourne Exhibition and Convention Centre, Southbank', u'kw_venue': [u'the', u'plenary,', u'melbourne', u'exhibition', u'and', u'convention', u'centre,', u'southbank']}
    
    """
    url = urlparse.urljoin(BASE_URL, URL_VENUE_GET)
    data = urllib.urlencode({'object_id' : object_id, 'name': name})
    return urllib2.urlopen(Request(url, data)).read() 


def api_get_artist(object_id = '', name = ''):
    """ Get artist by its name and/or object id
    
    Example:
        >>> api_get_venue(name = 'The Plenary, Melbourne Exhibition and Convention Centre, Southbank')
        {u'_id': ObjectId('4cd04980312f917a1c001d86'), u'kw_musician': [u'chris', u'klondike', u'masuak', u'&', u'the', u'north'], u'name': u'Chris Klondike Masuak & The North'}
        
    """
    url = urlparse.urljoin(BASE_URL, URL_ARTIST_GET)
    data = urllib.urlencode({'object_id' : object_id, 'name': name})
    return urllib2.urlopen(Request(url, data)).read() 

def api_get_gig(object_id = '', name = ''):
    """ Get gig by its name and/or object id
    
    Example:
        >>> api_get_venue(name = 'The Plenary, Melbourne Exhibition and Convention Centre, Southbank')
        {u'name': None, u'artist': {u'name': u'Breaking Orbit'}, u'price': u'$12', u'venue': {u'name': u'Glacier, Frankston'}, u'kw_venue': [u'glacier,', u'frankston'], u'genre': u'Rock & Pop', u'state': u'VIC', u'time': u'8pm', u'date': u'Monday 4 October', u'datetime_parsed': datetime.datetime(2010, 10, 4, 20, 0), u'_id': ObjectId('4cd04973312f917a1c000003'), u'kw_musician': [u'breaking', u'orbit']}
        
    """
    url = urlparse.urljoin(BASE_URL, URL_GIG_GET)
    data = urllib.urlencode({'object_id' : object_id, 'name': name})
    return urllib2.urlopen(Request(url, data)).read() 
    
if __name__ == '__main__':

    import doctest
    doctest.testmod()
