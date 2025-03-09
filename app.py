import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

st.sidebar.header("Filter Data")
season_filter = st.sidebar.selectbox("Pilih Musim:", ["Semua"] + sorted(day_df['season'].unique().tolist()))
hour_filter = st.sidebar.slider("Pilih Jam:", int(hour_df['hr'].min()), int(hour_df['hr'].max()), (int(hour_df['hr'].min()), int(hour_df['hr'].max())))

if season_filter != "Semua":
    day_df = day_df[day_df['season'] == season_filter]
    hour_df = hour_df[hour_df['season'] == season_filter]

hour_df = hour_df[(hour_df['hr'] >= hour_filter[0]) & (hour_df['hr'] <= hour_filter[1])]

st.title("Dashboard Analisis Penggunaan Sepeda")

st.subheader("Tren Penggunaan Sepeda Sepanjang Hari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=hour_df, x='hr', y='cnt', ci=None, ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Pengguna")
st.pyplot(fig)

st.subheader("Pengaruh Musim terhadap Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=day_df, x='season', y='cnt', ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Pengguna")
st.pyplot(fig)

day_df["keterangan"] = pd.cut(day_df["cnt"], bins=[0, 4000, 6000, 8000, 10000],
                                   labels=["Rendah", "Sedang", "Tinggi", "Sangat Tinggi"])

st.subheader("Clustering Kategori Penggunaan Sepeda")
st.dataframe(day_df[["dteday", "cnt", "keterangan"]])

st.subheader("Visualisasi Kategori Penggunaan Sepeda")
fig, ax = plt.subplots()
day_df["usage_category"].value_counts().plot(kind="bar", ax=ax)
ax.set_title("Distribusi Kategori Penggunaan Sepeda")
ax.set_xlabel("Kategori")
ax.set_ylabel("Jumlah Hari")
st.pyplot(fig)

st.subheader("Insights")
st.write("1. Jam penggunaan sepeda tertinggi ada pada jam sibuk, yaitu 07:00 dan 16:00-18:00.")
st.write("2. Musim memiliki hubungan terkait banyaknya penggunaan sepeda, penggunaan sepeda tertinggi berada pada musim yang hangat seperti Summer dan Fall.")
st.write("3. Penggunaan sepeda dapat diclustering untuk mengetahui berapa kali penggunaan sepeda dikatakan rendah, sedang, tinggi, dan sangat tinggi tiap harinya.")