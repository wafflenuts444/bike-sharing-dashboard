import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Sidebar filters
st.sidebar.header("Filter Data")
season_filter = st.sidebar.selectbox("Pilih Musim:", ["Semua"] + sorted(day_df['season'].unique().tolist()))
hour_filter = st.sidebar.slider("Pilih Jam:", int(hour_df['hr'].min()), int(hour_df['hr'].max()), (int(hour_df['hr'].min()), int(hour_df['hr'].max())))

# Apply filters
if season_filter != "Semua":
    day_df = day_df[day_df['season'] == season_filter]
    hour_df = hour_df[hour_df['season'] == season_filter]

hour_df = hour_df[(hour_df['hr'] >= hour_filter[0]) & (hour_df['hr'] <= hour_filter[1])]

# Title
st.title("Dashboard Analisis Penggunaan Sepeda")

# Visualization 1: Tren Penggunaan Sepeda Sepanjang Hari
st.subheader("Tren Penggunaan Sepeda Sepanjang Hari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=hour_df, x='hr', y='cnt', ci=None, ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Pengguna")
st.pyplot(fig)

# Visualization 2: Pengaruh Musim terhadap Penggunaan Sepeda
st.subheader("Pengaruh Musim terhadap Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=day_df, x='season', y='cnt', ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Pengguna")
st.pyplot(fig)

# Insights
st.subheader("Insights")
st.write("1. Tren penggunaan sepeda menunjukkan puncak pada jam-jam tertentu, terutama pada jam sibuk pagi dan sore hari.")
st.write("2. Musim memiliki pengaruh terhadap jumlah pengguna, dengan musim tertentu menunjukkan tingkat penggunaan yang lebih tinggi.")

# Run the app by using `streamlit run app.py` in the terminal
