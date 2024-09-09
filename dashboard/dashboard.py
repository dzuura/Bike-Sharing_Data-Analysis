import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dashboard
st.title("Bike Sharing Dashboard")

# Load dataset
final_df = pd.read_csv('final_df.csv')

# Mapping hari
days_of_week = {0: 'Senin', 1: 'Selasa', 2: 'Rabu', 3: 'Kamis', 4: 'Jumat', 5: 'Sabtu', 6: 'Minggu'}
final_df['weekday_hour'] = final_df['weekday_hour'].map(days_of_week)

# Sidebar filter
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", ['Winter', 'Spring', 'Summer', 'Fall'])
selected_weekday = st.sidebar.selectbox("Pilih Hari dalam Seminggu", final_df['weekday_hour'].unique())
selected_workingday = st.sidebar.selectbox("Pilih Hari Kerja", [0, 1], format_func=lambda x: 'Hari Libur' if x == 0 else 'Hari Kerja')

# Filter dataset berdasarkan sidebar selections
filtered_data = final_df[
    (final_df['season_hour'] == selected_season) &
    (final_df['weekday_hour'] == selected_weekday) &
    (final_df['workingday_hour'] == selected_workingday)
]

# Visualisasi Penyewaan Sepeda Berdasarkan Hari dalam Seminggu
st.subheader("Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
rental_per_hari = final_df.groupby('weekday_hour')['count_day'].mean()

plt.figure(figsize=(8, 5))
plt.bar(rental_per_hari.index, rental_per_hari)
plt.xlabel('Hari', fontsize=12)
plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
plt.title('Rata-rata Penyewaan Sepeda per Hari', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
st.pyplot(plt)

# Visualisasi Tren Penyewaan Sepeda Berdasarkan Musim
st.subheader("Tren Penyewaan Sepeda Berdasarkan Musim")
rental_per_musim = final_df.groupby('season_hour')['count_day'].mean()

plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")
palette = sns.color_palette("coolwarm", 4)
sns.barplot(x=['Winter', 'Spring', 'Summer', 'Fall'], y=rental_per_musim, palette=palette)
plt.xlabel('Musim', fontsize=12)
plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
plt.title('Rata-rata Penyewaan Sepeda per Musim', fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--')
st.pyplot(plt)

# Visualisasi Pengaruh Hari Kerja terhadap Penyewaan Sepeda
st.subheader("Pengaruh Hari Kerja terhadap Penyewaan Sepeda")
rental_hari_kerja = final_df.groupby('workingday_hour')['count_day'].mean()

plt.figure(figsize=(8, 5))
sns.barplot(x=['Hari Libur', 'Hari Kerja'], y=rental_hari_kerja, palette='viridis')
plt.xlabel('Tipe Hari', fontsize=12)
plt.ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
plt.title('Pengaruh Hari Kerja terhadap Penyewaan Sepeda', fontsize=14, fontweight='bold')
st.pyplot(plt)

