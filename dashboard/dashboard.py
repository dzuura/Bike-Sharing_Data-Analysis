import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
bike_data = pd.read_csv('https://raw.githubusercontent.com/dzuura/Bike-Sharing_Data-Analysis/main/dashboard/bike_data.csv')

# Sidebar filters
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", ['Winter', 'Spring', 'Summer', 'Fall'])
selected_weekday = st.sidebar.selectbox("Pilih Hari dalam Seminggu", bike_data['weekday_hour'].unique())
selected_workingday = st.sidebar.selectbox("Pilih Hari Kerja", [0, 1], format_func=lambda x: 'Hari Libur' if x == 0 else 'Hari Kerja')

# Filter dataset based on the sidebar selections
filtered_data = bike_data[
    (bike_data['season_hour'] == selected_season) &
    (bike_data['weekday_hour'] == selected_weekday) &
    (bike_data['workingday_hour'] == selected_workingday)
]

# 1. Penyewaan Sepeda Berdasarkan Hari dalam Seminggu
st.subheader("Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
rentals_by_day = bike_data.groupby('weekday_hour')['count_day'].mean()

plt.figure(figsize=(8, 5))
plt.bar(rentals_by_day.index, rentals_by_day)
plt.xlabel('Hari', fontsize=12)
plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
plt.title('Rata-rata Penyewaan Sepeda per Hari', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
st.pyplot(plt)

# 2. Tren Penyewaan Sepeda Berdasarkan Musim
st.subheader("Tren Penyewaan Sepeda Berdasarkan Musim")
rentals_by_season = bike_data.groupby('season_hour')['count_day'].mean()

plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")
palette = sns.color_palette("coolwarm", 4)
sns.barplot(x=['Winter', 'Spring', 'Summer', 'Fall'], y=rentals_by_season, palette=palette)
plt.xlabel('Musim', fontsize=12)
plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
plt.title('Rata-rata Penyewaan Sepeda per Musim', fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--')
st.pyplot(plt)

# 3. Pengaruh Hari Kerja terhadap Penyewaan Sepeda
st.subheader("Pengaruh Hari Kerja terhadap Penyewaan Sepeda")
rentals_by_workingday = bike_data.groupby('workingday_hour')['count_day'].mean()

plt.figure(figsize=(8, 5))
sns.barplot(x=['Hari Libur', 'Hari Kerja'], y=rentals_by_workingday, palette='viridis')
plt.xlabel('Tipe Hari', fontsize=12)
plt.ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
plt.title('Pengaruh Hari Kerja terhadap Penyewaan Sepeda', fontsize=14, fontweight='bold')
st.pyplot(plt)

