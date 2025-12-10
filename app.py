import streamlit as st

# --- 1. SETUP HALAMAN ---
st.set_page_config(
    page_title="Dukun Saham Pro 🔮",
    page_icon="🚀",
    layout="centered"
)

# --- 2. SIDEBAR MENU (Pusat Navigasi) ---
st.sidebar.title("🎛️ Menu Dukun")
pilihan_menu = st.sidebar.radio(
    "Mau ngapain hari ini?",
    ["🚀 Kalkulator IPO (Gorengan)", 
     "📈 Kalkulator Saham Listing (BBRI dkk)", 
     "📚 Tutorial: Cari Data IPO", 
     "📖 Tutorial: Cari Data Saham Listing"]
)

st.sidebar.divider()
st.sidebar.info("💡 **Tips Mentor:**\nJangan trading pake uang dapur!")

# ==============================================================================
# FITUR 1: KALKULATOR IPO (Kodingan Lama yang Dipindah)
# ==============================================================================
if pilihan_menu == "🚀 Kalkulator IPO (Gorengan)":
    st.title("🚀 Dukun IPO Calculator")
    st.markdown("### Alat Bantu Hitung Valuasi Saham Baru (IPO)")
    st.divider()

    st.header("📝 Masukkan Data Prospektus")
    col1, col2 = st.columns(2)

    # Input Data
    with col1:
        ticker = st.text_input("Kode Saham (Contoh: SUPA)", "SUPA").upper()
        saham_publik = st.number_input("Jml Saham Publik (Lembar)", min_value=1, value=4406612300)
    with col2:
        harga_ipo = st.number_input("Harga Penawaran (Rp)", min_value=1, value=695)
        total_saham = st.number_input("Total Saham Beredar (Lembar)", min_value=1, value=33897017650)

    st.subheader("Keuangan Awal")
    ekuitas_awal = st.number_input("Total Ekuitas Awal (Rupiah)", min_value=1, value=4368337000000, format="%d")

    st.divider()
    
    if st.button("🔥 TERAWANG IPO!", type="primary", use_container_width=True):
        # Rumus IPO
        dana_ipo = saham_publik * harga_ipo
        ekuitas_baru = ekuitas_awal + dana_ipo
        bvps = ekuitas_baru / total_saham
        market_cap = harga_ipo * total_saham
        pbv = harga_ipo / bvps if bvps > 0 else 0

        # Hasil
        st.success(f"📊 Hasil Analisis IPO: {ticker}")
        c1, c2, c3 = st.columns(3)
        c1.metric("Dana IPO Masuk", f"Rp {dana_ipo/1_000_000_000:,.1f} M")
        c2.metric("Ekuitas Baru", f"Rp {ekuitas_baru/1_000_000_000:,.1f} M")
        c3.metric("Harga Modal (BVPS)", f"Rp {bvps:,.2f}")
        
        st.subheader("Vonis Mentor:")
        # Vonis Market Cap
        if market_cap < 500_000_000_000:
            st.info(f"💰 Market Cap: **ENTENG** (Rp {market_cap/1_000_000_000:,.1f} M). Potensi ARA tinggi.")
        elif market_cap < 10_000_000_000_000:
            st.warning(f"💰 Market Cap: **SEDANG** (Rp {market_cap/1_000_000_000:,.1f} M).")
        else:
            st.error(f"💰 Market Cap: **GAJAH** (Rp {market_cap/1_000_000_000_000:,.1f} T). Berat, susah ARA.")

        # Vonis PBV
        if pbv < 1:
            st.success(f"🏷️ PBV: **{pbv:.2f}x (MURAH)**. Cek kesehatannya!")
        elif pbv <= 2:
            st.success(f"🏷️ PBV: **{pbv:.2f}x (WAJAR)**. Aman buat masuk.")
        elif pbv <= 4:
            st.warning(f"🏷️ PBV: **{pbv:.2f}x (PREMIUM)**. Mahal dikit, oke kalau brand bagus.")
        else:
            st.error(f"🏷️ PBV: **{pbv:.2f}x (MAHAL BANGET)**. Hati-hati sangkut.")

# ==============================================================================
# FITUR 2: KALKULATOR SAHAM LISTING (Buat BBRI, BUMI, DATA)
# ==============================================================================
elif pilihan_menu == "📈 Kalkulator Saham Listing (BBRI dkk)":
    st.title("📈 Bedah Saham Listing")
    st.markdown("### Cek Mahal/Murah Saham yang Udah Ada di Bursa")
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        ticker_list = st.text_input("Kode Saham (Contoh: BBRI)", "BBRI").upper()
        harga_sekarang = st.number_input("Harga Sekarang (Rp)", min_value=1, value=3700)
    with col2:
        eps = st.number_input("EPS (Laba per Lembar)", min_value=1, value=300, help="Cek di Key Stats > EPS Annualized")
        bvps_list = st.number_input("BVPS (Modal per Lembar)", min_value=1, value=1800, help="Cek di Key Stats > Book Value Per Share")

    st.divider()

    if st.button("🔍 BEDAH SEKARANG!", type="primary", use_container_width=True):
        # Rumus Saham Listing
        per = harga_sekarang / eps if eps > 0 else 0
        pbv_list = harga_sekarang / bvps_list if bvps_list > 0 else 0

        st.subheader(f"📊 Diagnosa Dokter Saham: {ticker_list}")
        
        c1, c2 = st.columns(2)
        c1.metric("PER (Balik Modal)", f"{per:.1f} x")
        c2.metric("PBV (Harga vs Modal)", f"{pbv_list:.2f} x")

        st.write("---")
        
        # Vonis PER
        if per < 10:
            st.success("✅ **PER MURAH (<10x)**: Balik modal cepet. Sikat!")
        elif per < 20:
            st.info("⚖️ **PER WAJAR (10-20x)**: Standar perusahaan sehat.")
        else:
            st.error("⚠️ **PER MAHAL (>20x)**: Hati-hati, harga udah ketinggian.")

        # Vonis PBV
        if pbv_list < 1:
            st.success("💎 **PBV DISKON (<1x)**: Lebih murah dari modalnya!")
        elif pbv_list < 3:
            st.info("⚖️ **PBV NORMAL (1-3x)**: Harga wajar.")
        else:
            st.warning("🔥 **PBV PREMIUM (>3x)**: Mahal, pastiin ini saham Bank/Tech bagus.")

# ==============================================================================
# FITUR 3: TUTORIAL IPO (Contekan)
# ==============================================================================
elif pilihan_menu == "📚 Tutorial: Cari Data IPO":
    st.title("📚 Cara Nyari Data IPO")
    st.markdown("Buka PDF **Prospektus Ringkas**, terus tekan `Ctrl+F` cari kata kunci ini:")
    
    # PERBAIKAN: Pake tanda kutip tiga (""") biar bisa multi-line
    st.info("""
    **1. HARGA PENAWARAN (Rp)**
    * 📍 Lokasi: Cover Depan.
    * 🔍 Keyword: "Harga Penawaran".
    
    **2. JUMLAH SAHAM PUBLIK (Lembar)**
    * 📍 Lokasi: Tabel Struktur Permodalan.
    * 🔍 Cari: Kolom *Setelah Penawaran* -> Baris *Masyarakat*.
    
    **3. TOTAL SAHAM BEREDAR (Lembar)**
    * 📍 Lokasi: Tabel Struktur Permodalan.
    * 🔍 Cari: Angka *Total/Jumlah* paling bawah di kolom *Setelah Penawaran*.
    
    **4. EKUITAS AWAL (Rupiah)**
    * 📍 Lokasi: Laporan Keuangan.
    * 🔍 Cari: Baris *Total Ekuitas* (Tahun Terakhir).
    * ⚠️ **Ingat:** Kalau satuannya "Jutaan", tambahin 6 nol!
    """)

# ==============================================================================
# FITUR 4: TUTORIAL SAHAM LISTING (Contekan Baru)
# ==============================================================================
elif pilihan_menu == "📖 Tutorial: Cari Data Saham Listing":
    st.title("📖 Cara Nyari Data Saham (BBRI/BUMI)")
    st.markdown("Gak perlu baca laporan keuangan, cukup buka **Stockbit / RTI Business**.")
    
    st.warning("""
    **1. EPS (Laba per Lembar)**
    * Buka menu **Key Stats**.
    * Cari tulisan: `EPS (Annualized)` atau `EPS (TTM)`.
    * *Ini buat ngitung PER.*
    
    **2. BVPS (Modal per Lembar)**
    * Buka menu **Key Stats**.
    * Cari tulisan: `Book Value Per Share`.
    * *Ini buat ngitung PBV.*
    """)
    
    st.caption("Tinggal input, biar Python yang ngitung!")