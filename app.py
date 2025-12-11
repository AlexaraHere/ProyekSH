import streamlit as st

# ==============================================================================
# 1. CONFIGURATION & STYLE
# ==============================================================================
st.set_page_config(
    page_title="Dukun Saham Pro 🔮",
    page_icon="🚀",
    layout="centered"
)

# Custom CSS biar agak ganteng dikit (Optional)
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. SIDEBAR MENU
# ==============================================================================
st.sidebar.title("🎛️ Menu Dukun")
st.sidebar.image("https://img.icons8.com/color/96/bullish.png", width=80) # Pemanis visual

pilihan_menu = st.sidebar.radio(
    "Mau ngapain hari ini?",
    ["🚀 Kalkulator IPO (Gorengan)", 
     "📈 Kalkulator Saham Listing (BBRI dkk)", 
     "📚 Tutorial: Cari Data IPO", 
     "📖 Tutorial: Cari Data Saham Listing"]
)

st.sidebar.divider()
st.sidebar.info("💡 **Tips Mentor:**\nJangan trading pake uang SPP/Dapur! \n\n_Code by: Junior Quant_")

# ==============================================================================
# FITUR 1: KALKULATOR IPO
# ==============================================================================
if pilihan_menu == "🚀 Kalkulator IPO (Gorengan)":
    st.title("🚀 Dukun IPO Calculator")
    st.markdown("### Alat Bantu Hitung Valuasi Saham Baru")
    st.info("Gunakan data dari **Prospektus Ringkas** halaman depan.")
    st.divider()

    st.header("📝 Input Data Prospektus")
    col1, col2 = st.columns(2)

    # Input Data
    with col1:
        ticker = st.text_input("Kode Saham (Contoh: GOTO)", "GOTO").upper()
        saham_publik = st.number_input("Jml Saham Publik (Lembar)", min_value=1, value=4000000000)
        ekuitas_awal = st.number_input("Total Ekuitas Awal (Rupiah)", min_value=1, value=4000000000000)
    with col2:
        harga_ipo = st.number_input("Harga Penawaran (Rp)", min_value=1, value=200)
        total_saham = st.number_input("Total Saham Beredar (Lembar)", min_value=1, value=30000000000)

    st.divider()
    
    if st.button("🔥 TERAWANG IPO!", type="primary", use_container_width=True):
        # --- LOGIKA MENTOR (Backend) ---
        dana_ipo = saham_publik * harga_ipo
        ekuitas_baru = ekuitas_awal + dana_ipo
        bvps = ekuitas_baru / total_saham
        market_cap = harga_ipo * total_saham
        pbv = harga_ipo / bvps if bvps > 0 else 0

        # --- TAMPILAN HASIL (Frontend) ---
        st.success(f"📊 Hasil Analisis IPO: {ticker}")
        
        # Row 1: Angka Penting
        c1, c2, c3 = st.columns(3)
        c1.metric("Target Dana IPO", f"Rp {dana_ipo/1_000_000_000:,.1f} M")
        c2.metric("Market Cap (Valuasi)", f"Rp {market_cap/1_000_000_000:,.1f} M")
        c3.metric("Harga Wajar (BVPS)", f"Rp {bvps:,.2f}")
        
        st.subheader("👨‍🏫 Vonis Mentor:")
        
        # 1. Analisis Market Cap (Berat/Enteng)
        if market_cap < 500_000_000_000:
            st.info(f"💰 **Size: MICIN / GORENGAN** (Rp {market_cap/1_000_000_000:,.1f} M).\nEnteng banget. Rawan digoreng bandar, tapi potensi ARA tinggi.")
        elif market_cap < 10_000_000_000_000:
            st.warning(f"💰 **Size: SEDANG** (Rp {market_cap/1_000_000_000:,.1f} M).\nCukup stabil, standar saham second liner.")
        else:
            st.error(f"💰 **Size: GAJAH** (Rp {market_cap/1_000_000_000_000:,.1f} T).\nBerat. Jangan ngarep ARA berjilid-jilid. Cocok buat invest jangka panjang.")

        # 2. Analisis PBV (Mahal/Murah)
        if pbv < 1:
            st.success(f"🏷️ **PBV: {pbv:.2f}x (SUPER MURAH)**.\nLebih murah dari modalnya. Sikat!")
        elif pbv <= 2:
            st.success(f"🏷️ **PBV: {pbv:.2f}x (WAJAR)**.\nHarga masuk akal.")
        elif pbv <= 4:
            st.warning(f"🏷️ **PBV: {pbv:.2f}x (MAHAL/PREMIUM)**.\nMahal, pastiin prospek bisnisnya bagus banget.")
        else:
            st.error(f"🏷️ **PBV: {pbv:.2f}x (GORENGAN MAHAL)**.\nHati-hati, harga udah di angkasa.")

# ==============================================================================
# FITUR 2: KALKULATOR SAHAM LISTING (UPDATED WITH ROE!)
# ==============================================================================
elif pilihan_menu == "📈 Kalkulator Saham Listing (BBRI dkk)":
    st.title("📈 Bedah Saham Listing")
    st.markdown("### Cek Valuasi & Kualitas Bisnis")
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        ticker_list = st.text_input("Kode Saham (Contoh: BBRI)", "BBRI").upper()
        harga_sekarang = st.number_input("Harga Sekarang (Rp)", min_value=1, value=3660)
    with col2:
        # User cukup input EPS & BVPS, ROE kita hitungin otomatis
        eps = st.number_input("EPS (Laba per Lembar)", min_value=1, value=370, help="Cek di RTI/Stockbit Key Stats")
        bvps_list = st.number_input("BVPS (Modal per Lembar)", min_value=1, value=2198, help="Cek di RTI/Stockbit Key Stats")

    st.divider()

    if st.button("🔍 BEDAH SEKARANG!", type="primary", use_container_width=True):
        # --- LOGIKA MENTOR (Backend) ---
        per = harga_sekarang / eps if eps > 0 else 0
        pbv_list = harga_sekarang / bvps_list if bvps_list > 0 else 0
        
        # HITUNG ROE OTOMATIS (New Feature!)
        # Rumus: ROE = (EPS / BVPS) * 100
        roe = (eps / bvps_list) * 100 if bvps_list > 0 else 0

        st.subheader(f"📊 Diagnosa Dokter Saham: {ticker_list}")
        
        # Tampilan 3 Kolom
        c1, c2, c3 = st.columns(3)
        c1.metric("PER (Balik Modal)", f"{per:.1f} x", help="Makin Kecil Makin Bagus (<15x)")
        c2.metric("PBV (Harga vs Modal)", f"{pbv_list:.2f} x", help="Makin Kecil Makin Bagus (<1x)")
        
        # Visualisasi ROE (Hijau kalau bagus, Merah kalau jelek)
        c3.metric("ROE (Profitability)", f"{roe:.1f} %", help="Makin Gede Makin Bagus (>15%)", 
                  delta=f"{roe:.1f}%" if roe > 15 else f"-{15-roe:.1f}% (Underperform)")

        st.write("---")
        st.subheader("👨‍🏫 Kesimpulan:")

        # 1. Analisis KUALITAS (ROE)
        if roe > 15:
            st.success(f"✅ **BISNIS BAGUS (ROE {roe:.1f}%)**: Manajemen pinter nyari duit. Mesin pencetak uang!")
        elif roe > 8:
            st.warning(f"⚠️ **BISNIS BIASA AJA (ROE {roe:.1f}%)**: Profit ada, tapi gak spesial.")
        else:
            st.error(f"❌ **BISNIS LEMOT (ROE {roe:.1f}%)**: Mending duitnya taruh Deposito aja.")

        # 2. Analisis HARGA (PER & PBV)
        # Logika Gabungan
        if per < 15 and pbv_list < 2:
            st.success("💎 **STATUS: UNDERVALUED (MURAH)**. Barang bagus lagi diskon. Serok!")
        elif per > 20 and pbv_list > 4:
            st.error("💣 **STATUS: OVERVALUED (MAHAL)**. Jangan FOMO, tunggu koreksi.")
        else:
            st.info("⚖️ **STATUS: FAIR VALUE (WAJAR)**. Boleh masuk buat jangka panjang.")

# ==============================================================================
# FITUR 3 & 4: TUTORIAL (Contekan)
# ==============================================================================
elif pilihan_menu == "📚 Tutorial: Cari Data IPO":
    st.title("📚 Cheat Sheet: Data IPO")
    st.markdown("Buka PDF **Prospektus Ringkas**, tekan `Ctrl+F`:")
    st.info("""
    1. **HARGA PENAWARAN**: Cari di Cover Depan.
    2. **JUMLAH SAHAM PUBLIK**: Tabel 'Struktur Permodalan' -> Kolom Masyarakat.
    3. **TOTAL SAHAM**: Tabel 'Struktur Permodalan' -> Baris Total Paling Bawah.
    4. **EKUITAS AWAL**: Laporan Keuangan -> Total Ekuitas.
    """)

elif pilihan_menu == "📖 Tutorial: Cari Data Saham Listing":
    st.title("📖 Cheat Sheet: Saham Listing")
    st.markdown("Buka **Stockbit** atau **RTI Business**:")
    st.success("""
    1. **EPS (Earning Per Share)**:
       - Menu: Key Stats -> Profitability.
       - *Fungsi: Buat ngitung PER.*
       
    2. **BVPS (Book Value Per Share)**:
       - Menu: Key Stats -> Valuation.
       - *Fungsi: Buat ngitung PBV & ROE.*
    """)