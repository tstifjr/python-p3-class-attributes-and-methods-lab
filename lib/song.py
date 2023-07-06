class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) :
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if not (genre in cls.genres):
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist) :
        if not (artist in cls.artists):
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre) :
        keys = [key for key , value in cls.genre_count.items()]

        if genre in keys :
            cls.genre_count[genre] += 1
        else :
            cls.genre_count[genre] = 1

        # for g in cls.genres :
        #    print(g)
        #    if (g in keys and g == genre):
        #        cls.genre_count[g] += 1
        #    elif not g in keys : 
        #        cls.genre_count[g] = 1
            

        # if cls.genre_count.get(genre) == None :
        #     cls.genre_count[genre] = 1
        # else :
        #     cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist) == None :
            cls.artist_count[artist] = 1
        else :
            cls.artist_count[artist] += 1

# Song("99 Problems", "Jay Z", "Rap")
# Song("Halo", "Beyonce", "Pop")
# Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# Song("Sara Smile", "Hall and Oates", "Pop")
# out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")