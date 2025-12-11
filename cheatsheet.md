# 📈 MODULE: BASIC FUNDAMENTAL ANALYSIS CHEATSHEET
# LEVEL: BEGINNER / INTERMEDIATE
# PURPOSE: Quick reference for Stock Valuation, Business Quality, & Data Reading.

================================================================================
PART 1: KEY METRICS (DEFINISI & LOGIKA)
================================================================================

1. EPS (Earnings Per Share)
   - Analogi IT: Bandwidth / Throughput.
   - Arti: Laba bersih yang dihasilkan per 1 lembar saham.
   - Target: HARUS POSITIF (+) dan NAIK terus tiap tahun (Growth).
   - Indikasi: Mesin pencetak duit berjalan lancar.

2. PER (Price to Earnings Ratio)
   - Analogi IT: ROI Time (Estimasi waktu balik modal).
   - Rumus: Harga Saham / EPS.
   - Arti: Butuh berapa tahun modal balik dari profit perusahaan?
   - Target: 
     * < 10x  : MURAH (Undervalued) -> Target Beli.
     * 10x-15x: WAJAR (Fair Price).
     * > 20x  : MAHAL (Overvalued) -> Kecuali perusahaan Tech/Growth tinggi.

3. PBV (Price to Book Value)
   - Analogi IT: Hardware Cost vs Selling Price.
   - Rumus: Harga Saham / Nilai Aset Bersih per Lembar (BVPS).
   - Arti: Kita beli barang di harga diskon atau harga premium?
   - Target:
     * < 1x   : DISKON (Murah banget, cek ada masalah gak?).
     * 1x - 2x: WAJAR (Untuk perusahaan bagus/Bluechip).
     * > 3x   : MAHAL (Premium).

4. ROE (Return on Equity)
   - Analogi IT: System Efficiency / Performance.
   - Rumus: (EPS / BVPS) * 100.
   - Arti: Seberapa jago manajemen muterin duit pemegang saham?
   - Target:
     * > 15%  : BAGUS (Manajemen Efisien/High Performance).
     * < 8%   : JELEK (Lemot, mending Deposito).

5. MARKET CAP (Kapitalisasi Pasar)
   - Analogi IT: Server Size / Scale.
   - Rumus: Harga Saham x Total Lembar Saham.
   - Arti: Ukuran perusahaan (Gajah vs Semut).
   - Note:
     * Big Cap (> 100 Triliun): Stabil, gerak lambat, aman (BBRI, BBCA).
     * Small Cap (< 1-5 Triliun): Volatil, gerak liar, rawan digoreng.

================================================================================
PART 2: CARA CARI DATA (FETCHING)
================================================================================

TOOLS: RTI Business / Stockbit / Yahoo Finance / Google Finance.

STEP-BY-STEP (STOCKBIT):
1. Search kode saham (Ticker), misal: "BBRI".
2. Buka Tab "Key Stats".
3. Cek Section "Valuation" untuk PER & PBV.
4. Cek Section "Profitability" untuk ROE.
5. Cek Section "Share Issued" untuk Jumlah Lembar Saham.

================================================================================
PART 3: ALGORITMA KEPUTUSAN (PSEUDO-CODE)
================================================================================

def investment_decision(per, pbv, roe):
    
    # 1. CEK KUALITAS (Quality Check)
    if roe < 10:
        return "SKIP: Perusahaan Kurang Efisien (Bad Performance)."
    
    # 2. CEK HARGA (Valuation Check)
    else:
        # Skenario Murah
        if per < 10 and pbv < 1.5:
            return "STRONG BUY: Barang Bagus, Harga Diskon (Undervalued)."
        
        # Skenario Wajar
        elif (per >= 10 and per <= 20) or (pbv >= 1.5 and pbv <= 3.0):
            return "BUY/HOLD: Harga Wajar (Fair Value). Cicil pelan-pelan."
        
        # Skenario Mahal
        else:
            return "WAIT: Harga Kemahalan (Overvalued). Tunggu koreksi."

================================================================================
PART 4: CARA BACA ANGKA (US FORMAT VS INDO) ⚠️ PENTING!
================================================================================

Banyak aplikasi (Stockbit/Yahoo Finance) pake standar US/Inggris.
Jangan salah baca Titik (.) dan Koma (,)!

1. ATURAN TANDA BACA
   - 🇺🇸 US (Stockbit): Koma (,) = Ribuan | Titik (.) = Desimal/Pecahan.
   - 🇮🇩 INDO (Kita): Titik (.) = Ribuan | Koma (,) = Desimal/Pecahan.

2. ATURAN HURUF "B" (BILLION)
   Di aplikasi, "B" artinya Miliar ($10^9$). TAPI liat angka depannya!

   | Tampilan di Layar | Cara Baca (Indo) | Nilai Asli (Rupiah/Lembar) |
   | :--- | :--- | :--- |
   | **151.56 B** | 151 Koma 56 Miliar | **151 MILIAR** (Ratusan Miliar) |
   | **331,191 B** | 331 Ribu Miliar | **331 TRILIUN** (Ratusan Triliun) |
   | **1,000 B** | 1 Ribu Miliar | **1 TRILIUN** |

   > **RULE OF THUMB:**
   > Kalau angka di depan "B" udah Ribuan (ada komanya), itu artinya udah **TRILIUN**.

3. INPUT KE PYTHON/CALCULATOR
   Jangan masukin huruf "B" atau "T". Masukin Nol-nya lengkap!
   - 151 Miliar -> `151000000000` (9 Nol)
   - 331 Triliun -> `331000000000000` (12 Nol)