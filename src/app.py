#!/usr/bin/env python
# coding: utf-8

# # Explore here

# In[7]:


import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener client_id y client_secret de las variables de entorno
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")




# In[ ]:


import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# id=4dpARuHxo51G3z768sgnrY (Adele)
adele_uri = 'spotify:artist:4dpARuHxo51G3z768sgnrY'

# Autentic Spotify usando las credenciales
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

results = spotify.artist_top_tracks(adele_uri)

tracks_adele = []
for track in results['tracks'][:10]:
    track_name = track['name']
    track_popularity = track['popularity']
    track_duration = track['duration_ms'] / 1000 / 60  # Convertir milisegundos a minutos

    tracks_adele.append({
        'name': track_name,
        'popularity': track_popularity,
        'duration_minutes': track_duration
    })

for track in tracks_adele:
    print(f"Song: {track['name']}")
    print(f"Popularity: {track['popularity']}")
    print(f"Duration: {track['duration_minutes']:.2f} minutes")
    print("\n")




# In[17]:


import pandas as pd

df_tracks_adele=pd.DataFrame(tracks_adele)
df_tracks_adele
df_tracks_adele_sorted = df_tracks_adele.sort_values(by='popularity', ascending=True)
df_tracks_adele_sorted


# Podríamos decir que una canción que dure poco tiempo puede ser más popular que otra que dure más? Analízalo graficando un scatter plot y argumenta tu respuesta.

# In[ ]:






# In[20]:


import matplotlib.pyplot as plt

popularity = df_tracks_adele_sorted['popularity']
duration_minutes = df_tracks_adele_sorted['duration_minutes'] 

plt.figure(figsize=(8, 5))
plt.scatter(duration_minutes, popularity, color='skyblue')  
plt.xlabel('Duración (minutos)')
plt.ylabel('Popularidad')
plt.title('Duración vs Popularidad de las canciones de Adele')

# Mostrar el gráfico
plt.show()


# Viendo este gráfico no se puede decir que exista una relación entre duración y popularidad. Los valores están muy dispersos. Quizás si extraemos la popularidad y el año de liberación de la canción podríamos ver más tendencia, porque lo lógico, si se mantiene la calidad del artista es que la popularidad aumente con la visibildad.
