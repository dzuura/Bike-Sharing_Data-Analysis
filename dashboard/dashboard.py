import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
bike_data = pd.read_csv('https://raw.githubusercontent.com/dzuura/Bike-Sharing_Data-Analysis/main/dashboard/bike_data.csv')

# Title dashboard
st.title("Bike Sharing Dashboard")

# Sidebar filter
st.sidebar.header("Filter Data")
selected_month = st.sidebar.selectbox("Pilih Bulan", bike_data['month_hour'].unique())
selected_season = st.sidebar.selectbox("Pilih Musim", bike_data['season_hour'].unique())

# Filter data berdasarkan pilihan di sidebar
filtered_data = bike_data[(bike_data['month_hour'] == selected_month) & (bike_data['season_hour'] == selected_season)]

# Tampilkan statistik umum
st.header(f"Statistik Penyewaan untuk Bulan {selected_month} dan Musim {selected_season}")
st.write(filtered_data[['count_day', 'casual_day', 'registered_day']].describe())

# Visualisasi penyewaan sepeda
st.subheader("Grafik Jumlah Penyewaan Sepeda Berdasarkan Hari")
plt.figure(figsize=(10, 6))
sns.barplot(data=filtered_data, x='weekday_day', y='count_day', palette='coolwarm')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Jumlah Penyewaan')
plt.title('Penyewaan Sepeda Berdasarkan Hari')
st.pyplot(plt)

# Visualisasi penyewaan sepeda berdasarkan kondisi cuaca
st.subheader("Pengaruh Kondisi Cuaca Terhadap Penyewaan Sepeda")
plt.figure(figsize=(10, 6))
sns.boxplot(data=filtered_data, x='weather_day', y='count_day', palette='viridis')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan')
plt.title('Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
st.pyplot(plt)
