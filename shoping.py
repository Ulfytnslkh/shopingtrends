import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Konfigurasi Dasar ===
st.set_page_config(page_title="Dashboard Shopping Trends", layout="wide")
st.title("🛍️ Dashboard Analisis Data Shopping Trends")

# === Informasi Anggota Kelompok ===
st.markdown("### 👥 Anggota Kelompok ")
st.markdown("""
- 📛 Nama 1: Ulfiyatun Solekha (23.11.5708)
- 📛 Nama 2: Laila Nuraini (23.11.5740)
""")

st.info("***Dashboard ini dirancang untuk memberikan gambaran menyeluruh mengenai perilaku belanja konsumen berdasarkan data historis yang telah dikumpulkan. Melalui eksplorasi data(EDA), pengguna dapat memahami pola-pola penting seperti distribusi usia konsumen, dominasi gender, preferensi metode pembayaran, dan karakteristik pembelian lainnya. Dengan visualisasi yang interaktif dan informatif, dashboard ini membantu dalam pengambilan keputusan strategis terkait pemasaran, segmentasi pelanggan, hingga optimalisasi layanan. Tidak hanya menyajikan data, dashboard ini juga dilengkapi dengan fitur prediksi metode pembayaran secara manual, memungkinkan pengguna mengeksplorasi kemungkinan perilaku konsumen baru berdasarkan input profil tertentu.***")
st.markdown("---")

# Load data .sav
df = pickle.load(open('shopping_data.sav', 'rb'))

# === Gaya Visual ===
sns.set_style("whitegrid")

# === Statistik Ringkas ===
st.subheader("📊 Statistik Ringkas")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Data", len(df))
with col2:
    st.metric("Umur Rata-rata", round(df['Age'].mean(), 1))
with col3:
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        st.metric("Rasio Gender", f"{gender_counts.iloc[0]} : {
                  gender_counts.iloc[1]}")

st.markdown("---")

# === Tata Letak Visualisasi ===
col1, col2 = st.columns(2)

with col1:
    if 'Gender' in df.columns:
        st.subheader("👨‍👩‍👧‍👦 Distribusi Gender")
        fig1, ax1 = plt.subplots()
        sns.countplot(data=df, x='Gender', palette='pastel', ax=ax1)
        ax1.set_xlabel("Gender")
        ax1.set_ylabel("Jumlah")
        st.pyplot(fig1)
        st.info("***Visualisasi ini menampilkan distribusi jumlah konsumen berdasarkan jenis kelamin mereka. Dari grafik ini kita dapat memahami kelompok gender mana yang lebih dominan dalam aktivitas belanja. Informasi ini sangat penting untuk menentukan target pasar secara lebih spesifik. Misalnya, jika jumlah pembeli perempuan jauh lebih banyak dibandingkan laki-laki, maka strategi pemasaran bisa difokuskan pada kebutuhan dan preferensi perempuan. Sebaliknya, jika jumlahnya seimbang, strategi pemasaran bisa dibuat lebih umum atau disesuaikan dengan segmen lain seperti usia atau kategori produk.***")

with col2:
    if 'Payment Method' in df.columns:
        st.subheader("💳 Metode Pembayaran yang Digunakan")
        payment_count = df['Payment Method'].value_counts()
        fig2, ax2 = plt.subplots()
        ax2.pie(payment_count, labels=payment_count.index,
                autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel"))
        ax2.axis("equal")
        st.pyplot(fig2)
        st.success("***Grafik ini menunjukkan bagaimana persebaran metode pembayaran yang digunakan oleh para konsumen saat melakukan pembelian. Pie chart memberikan gambaran proporsi masing-masing metode, seperti penggunaan kartu kredit, debit, atau metode lainnya. Dengan memahami metode pembayaran yang paling sering digunakan, bisnis dapat meningkatkan kenyamanan transaksi dengan lebih menekankan metode populer tersebut. Selain itu, informasi ini juga penting dalam menyusun kebijakan promosi, seperti cashback khusus untuk metode pembayaran tertentu yang paling banyak digunakan.***")

# === Baris Kedua Visualisasi ===
col3, col4 = st.columns(2)

with col3:
    if 'Age' in df.columns:
        st.subheader("📈 Distribusi Usia Konsumen")
        fig3, ax3 = plt.subplots()
        sns.histplot(df['Age'], kde=True, bins=20, color="skyblue", ax=ax3)
        ax3.set_xlabel("Usia")
        ax3.set_ylabel("Jumlah Konsumen")
        st.pyplot(fig3)
        st.warning("***Grafik ini memperlihatkan distribusi usia para pembeli dalam dataset. Dengan menggunakan histogram, kita bisa melihat usia berapa yang paling sering melakukan transaksi belanja. Distribusi ini dapat mengarahkan bisnis untuk memahami kelompok usia mana yang paling aktif dalam kegiatan konsumsi. Misalnya, jika mayoritas konsumen berusia antara 25 hingga 35 tahun, maka kampanye pemasaran, desain produk, bahkan pendekatan komunikasi dapat disesuaikan untuk usia produktif tersebut. Hal ini krusial dalam merancang user experience dan campaign yang lebih personal dan efektif.***")

with col4:
    st.subheader("📋 Statistik Deskriptif")
    st.dataframe(df.describe(include='all'))
    st.caption("***Tabel statistik deskriptif menyajikan ringkasan data dari seluruh variabel dalam dataset, termasuk nilai rata-rata (mean), minimum, maksimum, standar deviasi, serta jumlah data (count) untuk masing-masing kolom. Tabel ini memberikan gambaran menyeluruh mengenai karakteristik data sebelum dilakukan analisis lebih lanjut. Misalnya, dengan melihat nilai maksimum dan minimum dari 'Purchase Amount', kita bisa mengetahui rentang belanja konsumen. Sementara itu, standar deviasi pada kolom usia bisa menunjukkan apakah umur konsumen tersebar merata atau cenderung terkonsentrasi pada kelompok usia tertentu.***")

# === Footer ===
st.info("****Kesimpulan****")
st.info("***Berdasarkan hasil visualisasi dan analisis data pada dashboard ini, dapat disimpulkan bahwa pola belanja konsumen dipengaruhi oleh faktor-faktor seperti usia, gender, dan jenis produk yang dibeli. Konsumen dengan usia produktif (sekitar 20–35 tahun) tampak mendominasi tren belanja. Gender tertentu juga memiliki kecenderungan berbeda dalam jumlah transaksi, serta preferensi terhadap metode pembayaran.Dengan memahami pola ini, pelaku bisnis dapat menyesuaikan strategi pemasaran, pengembangan produk, dan kebijakan layanan agar lebih tepat sasaran. Selain itu, fitur prediksi memungkinkan adanya simulasi perilaku konsumen, yang sangat bermanfaat untuk memproyeksikan kebutuhan pasar dan mengambil keputusan berbasis data.***")
st.markdown("---")
