import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("tracks.csv")

# Clean
df.dropna(subset=['genre', 'artist_name', 'popularity', 'danceability', 'energy',
                  'valence', 'tempo', 'speechiness', 'liveness'], inplace=True)

st.set_page_config(page_title="Spotify Data Dashboard", layout="wide")
st.title("🎧 Spotify Music Data Analytics Dashboard")
st.markdown("Analyze genres, artists, and audio features using interactive charts.")

# Sidebar Filters
genre_list = df['genre'].value_counts().head(20).index.tolist()
selected_genre = st.sidebar.selectbox("🎼 Filter by Genre", genre_list)

filtered_df = df[df['genre'] == selected_genre]

# --- Section 1: Top Artists ---
st.subheader(f"🎤 Top Artists in {selected_genre}")
top_artists = filtered_df['artist_name'].value_counts().head(10)
fig1 = px.bar(top_artists, x=top_artists.values, y=top_artists.index,
              orientation='h', color=top_artists.values,
              labels={'x': 'Track Count', 'y': 'Artist'},
              color_continuous_scale='viridis')
st.plotly_chart(fig1, use_container_width=True)

# --- Section 2: Popularity Distribution ---
st.subheader("📈 Popularity Score Distribution")
fig2 = px.histogram(filtered_df, x='popularity', nbins=30, title='Track Popularity',
                    color_discrete_sequence=['#636EFA'])
st.plotly_chart(fig2, use_container_width=True)

# --- Section 3: Feature Correlation Heatmap ---
st.subheader("🧠 Feature Correlation")
features = filtered_df[['popularity', 'acousticness', 'danceability', 'energy',
                        'instrumentalness', 'liveness', 'loudness', 'speechiness', 
                        'tempo', 'valence']]
corr = features.corr()

fig3 = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale="RdBu_r")
st.plotly_chart(fig3, use_container_width=True)
