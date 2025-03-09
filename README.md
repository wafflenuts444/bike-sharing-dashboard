# Dashboard Bike Sharing

Dashboard ini digunakan untuk menganalisis penggunaan sepeda berdasarkan dataset yang tersedia.

## Setup Environment - Anaconda

```sh
conda create --name bike-sharing-env python=3.9
conda activate bike-sharing-env
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

```sh
mkdir bike_sharing_dashboard
cd bike_sharing_dashboard
python -m venv env
source env/bin/activate  # Untuk MacOS/Linux
# Atau gunakan perintah berikut untuk Windows
# env\Scripts\activate
pip install -r requirements.txt
```

## Menjalankan Streamlit App

```sh
streamlit run app.py
```
