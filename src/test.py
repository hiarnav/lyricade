from datetime import time
from main import *
import librosa


ARTISTS = ['Phoebe Bridgers', 'Eminem', 'Coldplay', 'Julien Baker', 'Drake', 'Lucy Dacus', 'Justin Bieber', 'John Mayer', 'Beyonce', 'Issac Gracie', 'Billie Marten', 'Novo Amor', 'Adam Melchor', 'Hozier', 'Khalid', 'Iron  Wine', 'Ben Howard', 'Katy Perry', 'Cardi B', 'Rihanna', 'Ariana Grande', 'James Bay', 'Dua Lipa', 'Nicki Minaj', 'BTS', 'Ed Sheeran', 'Angelo De Augustine', 'Selena Gomez', 'Maroon 5', 'Taylor Swift', 'Post Malone', 'Charlie Puth', 'Billie Eilish', 'Lady Gaga']
GENRES = ['indie-pop', 'anime', 'folk', 'brazil', 'chill', 'guitar', 'acoustic', 'metalcore', 'groove', 'ambient', 'afrobeat', 'gospel', 'garage', 'singer-songwriter', 'j-rock', 'drum-and-bass', 'black-metal', 'iranian', 'blues', 'study', 'british', 'dub', 'goth', 'idm', 'detroit-techno', 'deep-house', 'dance', 'edm', 'grindcore', 'electronic', 'dancehall', 'chicago-house', 'electro', 'pop', 'opera', 'j-dance', 'alt-rock', 'club', 'rockabilly', 'children', 'hardstyle', 'death-metal', 'disco', 'breakbeat', 'country', 'swedish', 'progressive-house', 'show-tunes', 'emo', 'party', 'grunge', 'hip-hop', 'soul', 'piano', 'punk-rock', 'j-pop', 'comedy', 'industrial', 'cantopop', 'kids', 'indian', 'alternative', 'k-pop', 'turkish', 'bluegrass', 'minimal-techno', 'trance', 'dubstep', 'reggae', 'rock-n-roll', 'power-pop', 'french', 'honky-tonk', 'sad', 'house', 'hardcore', 'ska', 'latin', 'happy', 'rock', 'punk', 'pop-film', 'spanish', 'techno', 'new-age', 'synth-pop', 'german', 'funk', 'trip-hop', 'sleep', 'latino', 'classical', 'psych-rock', 'r-n-b', 'metal', 'hard-rock', 'disney', 'world-music', 'mpb', 'malay', 'jazz', 'salsa', 'j-idol', 'mandopop']

def start_generation(artist, genre, explicit, file_path):
    y, sr = librosa.load(file_path, sr=None)
    duration_sec = librosa.get_duration(y=y, sr=sr)
    prompts = create_prompts(y, sr, artist, genre, explicit, duration_sec)
    segments = []
    for prompt in prompts:
        segments.append(prompt)
    lyrics = process_librosa_input(segments[0])
    return lyrics

def main():

    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_name = input("Enter the name of your audio file (e.g., drake.mp3): ")
    file_path = os.path.join(script_dir, file_name)

    artist = input("Artist")
    
    genre = input("Genre")

    explicit = int(input("Explicit"))

    if explicit:
        explicit = 2.826916
    else:
        explicit = 	-0.353742	

    lyrics = start_generation(artist, genre, explicit, file_path)
    print(lyrics)


if __name__ == "__main__":
   main()

