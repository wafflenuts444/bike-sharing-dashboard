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

# Clustering Kategori Penggunaan Sepeda
day_df["usage_category"] = pd.cut(day_df["cnt"], bins=[0, 4000, 6000, 8000, 10000],
                                   labels=["Rendah", "Sedang", "Tinggi", "Sangat Tinggi"])

st.subheader("Clustering Kategori Penggunaan Sepeda")
st.dataframe(day_df[["dteday", "cnt", "usage_category"]])

# Visualisasi Clustering
st.subheader("Visualisasi Kategori Penggunaan Sepeda")
fig, ax = plt.subplots()
day_df["usage_category"].value_counts().plot(kind="bar", ax=ax)
ax.set_title("Distribusi Kategori Penggunaan Sepeda")
ax.set_xlabel("Kategori")
ax.set_ylabel("Jumlah Hari")
st.pyplot(fig)

# Insights
st.subheader("Insights")
st.write("1. Jam penggunaan sepeda tertinggi ada pada jam sibuk, yaitu 07:00 dan 16:00-18:00.")
st.write("2. Musim memiliki hubungan terkait banyaknya penggunaan sepeda, penggunaan sepeda tertinggi berada pada musim yang hangat seperti Summer dan Fall.")
st.write("3. Pengguna sepeda dapat dikelompokkan ke dalam beberapa kategori berdasarkan jumlah pengguna harian, yang membantu dalam analisis pola penggunaan.")

# Run the app by using `streamlit run app.py` in the terminal
