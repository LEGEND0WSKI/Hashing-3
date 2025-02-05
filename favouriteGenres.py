# Time:
# Space:
# leetcode:
# Issues:



from collections import defaultdict

def favorite_genre(user_map, genre_map):
    song2genre = defaultdict(list)
    for genre in genre_map:
        songs = genre_map[genre]
        for song in songs:
            song2genre[song] = genre
            
            
    res = defaultdict(str)
    
    for user in user_map:
        songs = user_map[user]
        
    
user_songs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma": ["song5", "song6", "song7"]
}

song_genres = {
    "Rock": ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno": ["song2", "song4"],
    "Pop": ["song5", "song6"],
    "Jazz": ["song8", "song9"]
}

res = favorite_genre(user_songs, song_genres)
print(res)print("Hello World!")