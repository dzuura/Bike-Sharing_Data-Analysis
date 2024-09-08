import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dashboard
st.title("Bike Sharing Dashboard")

# Load data
data = pd.read_csv('https://raw.githubusercontent.com/dzuura/Bike-Sharing_Data-Analysis/main/dashboard/bike_data.csv')

# Sidebar untuk memilih filter
st.sidebar.header("Filter Data")
season_filter = st.sidebar.selectbox("Pilih Musim", data['season_hour'].unique())
workingday_filter = st.sidebar.selectbox("Pilih Hari Kerja", data['workingday_hour'].unique())

# Filter data berdasarkan pilihan musim dan hari kerja
filtered_data = data[(data['season_hour'] == season_filter) & (data['workingday_hour'] == workingday_filter)]

# Statistik Rata-rata Penyewaan Sepeda
st.subheader(f"Rata-rata Penyewaan Sepeda untuk Musim {season_filter} dan Hari Kerja {workingday_filter}")
avg_rentals = filtered_data['count_day'].mean()
st.write(f"Rata-rata Penyewaan: {avg_rentals:.2f} sepeda")

# Visualisasi Penyewaan Sepeda per Hari dalam Seminggu
st.subheader("Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
plt.figure(figsize=(10, 6))
sns.barplot(data=filtered_data, x='weekday_day', y='count_day', palette='coolwarm')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Jumlah Penyewaan')
plt.title('Penyewaan Sepeda per Hari')
st.pyplot(plt)

# Visualisasi Penyewaan Sepeda Berdasarkan Musim
st.subheader("Tren Penyewaan Sepeda Berdasarkan Musim")
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='month_hour', y='count_day', hue='season_hour', palette='viridis')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan')
plt.title('Tren Penyewaan Sepeda Berdasarkan Musim')
st.pyplot(plt)

# Visualisasi Pengaruh Hari Kerja terhadap Penyewaan
st.subheader("Pengaruh Hari Kerja terhadap Penyewaan Sepeda")
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='workingday_hour', y='count_day', palette='Set2')
plt.xlabel('Hari Kerja (0 = Libur, 1 = Hari Kerja)')
plt.ylabel('Jumlah Penyewaan')
plt.title('Penyewaan Sepeda Berdasarkan Hari Kerja')
st.pyplot(plt)
