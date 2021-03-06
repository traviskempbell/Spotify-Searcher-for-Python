'''
SpotifySearcher

November 13, 2015

Copyright (c) 2015, Travis Kempbell

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''

import json
import urllib2

class SpotifySearcher(object):
    def __init__(self):
        self.tracks = []
        self.artists = []
        self.albums = []
        self.playlists = []

    def search(self, search_string, search_type, limit):
        self.reset()
        if limit < 0:
            limit = 0
            print "**Limit values must be greater than 0**\n"
        if limit > 50:
            limit = 50
            print "**Limit values must be less than 50**\n"
        url = "https://api.spotify.com/v1/search?q=%s&type=%s&market=US&limit=%d" % (search_string, search_type, limit)
        return json.loads(urllib2.urlopen(url).read())

    def find_tracks(self, request, limit=10):
        print "\nSearching top %d tracks on Spotify for: %s\n" % (limit, request)
        data = self.search(request.replace(' ', '+'), "track", limit)
        if 'tracks' in data:
            tracks = []
            for track in data['tracks']['items']:
                tracks.append(track)
            for track in tracks:
                newTrack = Track(track['album'], track['name'], track['uri'], track['external_urls'], track['popularity'],
                            track['explicit'], track['preview_url'], track['track_number'], track['disc_number'], track['href'],
                            track['artists'], track['duration_ms'], track['external_ids'], track['type'], track['id'], track['available_markets'])
                self.tracks.append(newTrack)
        print "%d tracks found for: %s" % (len(self.tracks), request)

    def find_artists(self, request, limit=10):
        print "\nSearching top %d artists on Spotify for: %s\n" % (limit, request)
        data = self.search(request.replace(' ', '+'), "artist", limit)
        if 'artists' in data:
            artists = []
            for artist in data['artists']['items']:
                artists.append(artist)
            for artist in artists:
                newArtist = Artist(artist['genres'], artist['name'], artist['external_urls'], artist['popularity'], artist['uri'], artist['href'],
                            artist['followers'], artist['images'], artist['type'], artist['id'])
                self.artists.append(newArtist)
        print "%d artists found for: %s" % (len(self.artists), request)

    def find_albums(self, request, limit=10):
        print "\nSearching top %d albums on Spotify for: %s\n" % (limit, request)
        data = self.search(request.replace(' ', '+'), "album", limit)
        if 'albums' in data:
            albums = []
            for album in data['albums']['items']:
                albums.append(album)
            for album in albums:
                newAlbum = Album(album['album_type'], album['name'], album['external_urls'], album['uri'], album['href'],
                            album['images'], album['type'], album['id'], album['available_markets'])
                self.albums.append(newAlbum)
        print "%d albums found for: %s" % (len(self.albums), request)


    def find_playlists(self, request, limit=10):
        print "\nSearching top %d playlists on Spotify for: %s\n" % (limit, request)
        data = self.search(request.replace(' ', '+'), "playlist", limit)
        if 'playlists' in data:
            playlists = []
            for playlist in data['playlists']['items']:
                playlists.append(playlist)
            for playlist in playlists:
                newPlaylist = Playlist(playlist['name'], playlist['collaborative'], playlist['external_urls'], playlist['uri'], playlist['public'],
                            playlist['owner'], playlist['tracks'], playlist['href'], playlist['snapshot_id'], playlist['images'], playlist['type'], playlist['id'])
                self.playlists.append(newPlaylist)
        print "%d playlists found for: %s" % (len(self.playlists), request)

    def reset(self):
        self.__init__()


class Track(object):
    def __init__(self, album, name, uri, external_urls, popularity, explicit, preview_url, track_number, disc_number, href, artists, duration_ms, external_ids, typeinf, idinf, available_markets):
        self.album = album
        self.name = name
        self.uri = uri
        self.external_urls = external_urls
        self.popularity = popularity
        self.explicit = explicit
        self.preview_url = preview_url
        self.track_number = track_number
        self.disc_number = disc_number
        self.href = href
        self.artists = artists
        self.duration_ms = duration_ms
        self.external_ids = external_ids
        self.type = typeinf
        self.id = idinf
        self.available_markets = available_markets

class Artist(object):
    def __init__(self, genres, name, external_urls, popularity, uri, href, followers, images, typeinf, idinf):
        self.genres = genres
        self.name = name
        self.external_urls = external_urls
        self.popularity = popularity
        self.uri = uri
        self.href = href
        self.followers = followers
        self.images = images
        self.type = typeinf
        self.id = idinf

class Album(object):
    def __init__(self, album_type, name, external_urls, uri, href, images, typeinf, idinf, available_markets):
        self.album_type = album_type
        self.name = name
        self.external_urls = external_urls
        self.uri = uri
        self.href = href
        self.images = images
        self.type = typeinf
        self.id = idinf
        self.available_markets = available_markets

class Playlist(object):
    def __init__(self, name, collaborative, external_urls, uri, public, owner, tracks, href, snapshot_id, images, typeinf, idinf):
        self.name = name
        self.collaborative = collaborative
        self.external_urls = external_urls
        self.uri = uri
        self.public = public
        self.owner = owner
        self.tracks = tracks
        self.href = href
        self.snapshot_id = snapshot_id
        self.images = images
        self.type = typeinf
        self.id = idinf