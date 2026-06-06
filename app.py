import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Pengenalan Alat Laboratorium Kimia",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# DATA ALAT
# =========================
alat_data = [
    {
        "id": 1,
        "nama": "Gelas Beaker",
        "emoji": "🥛",
        "kategori": "Wadah",
        "foto": "gelas ukur.jpg",
        "fungsi": "Wadah serbaguna untuk mencampur, memanaskan, dan menyimpan larutan kimia.",
        "penjelasan_awam": (
            "Gelas beaker adalah wadah silindris dengan dasar datar"
            "dan bibir tuang yang umum digunakan di laboratorium untuk menampung, mencampur, mengaduk, dan memanaskan cairan/larutan."
        ),
        "cara_guna": "Tuang larutan ke dalamnya, aduk dengan batang pengaduk, bisa dipanaskan di atas kompor bunsen.",
        "bahaya": "⚠️ Jangan dipakai untuk minum! Kaca tipis, bisa pecah jika kena benturan.",
        "ukuran": "50 mL – 2000 mL",
        "warna_hex": "#3b82f6",
    },
    {
        "id": 2,
        "nama": "Erlenmeyer",
        "emoji": "⚗️",
        "kategori": "Wadah",
        "foto": "erlenmeyer labu.jpg",
        "fungsi": "Wadah berbentuk kerucut dengan leher sempit, digunakan untuk titrasi dan melarutkan zat.",
        "penjelasan_awam": (
            "Bentuknya seperti botol dengan badan lebar di bawah dan leher sempit di atas. "
            "Leher sempitnya berguna agar larutan tidak mudah tumpah saat digoyangkan."
        ),
        "cara_guna": "Isi larutan, goyangkan memutar saat titrasi berlangsung.",
        "bahaya": "⚠️ Jangan dipanaskan langsung tanpa alas kawat kasa.",
        "ukuran": "100 mL – 1000 mL",
        "warna_hex": "#8b5cf6",
    },
    {
        "id": 3,
        "nama": "Buret",
        "emoji": "🌡️",
        "kategori": "Pengukur Volume",
        "foto": "burett.jpg",
        "fungsi": "Tabung panjang bergraduasi untuk mengukur dan mengeluarkan volume larutan secara presisi.",
        "penjelasan_awam": (
            "Buret adalah alat laboratorium berbentuk silinder panjang dari kaca yang dilengkapi dengan skala ukur dan keran"
            "di bagian bawahnya. Alat ini berfungsi untuk meneteskan reagen cair atau titran dengan volume yang sangat presisi "
            "dan akurasi tinggi, terutama pada proses analisis titrasi."
        ),
        "cara_guna": "Isi dari atas, buka kran bawah perlahan-lahan, baca angka volume yang berkurang.",
        "bahaya": "⚠️ Rapuh, jangan terjatuh. Kran kaca bisa macet jika tidak dibersihkan.",
        "ukuran": "10 mL – 50 mL",
        "warna_hex": "#06b6d4",
    },
    {
        "id": 4,
        "nama": "Pipet Tetes",
        "emoji": "💧",
        "kategori": "Pemindah Cairan",
        "foto": "pipet tets.jpg",
        "fungsi": "Mengambil dan memindahkan cairan dalam jumlah kecil (tetes per tetes).",
        "penjelasan_awam": (
            "Pipet tetes berfungsi untuk memindahkan atau mengambil cairan dalam "
            "jumlah yang sangat sedikit (skala tetesan) dari suatu wadah ke wadah lain."
        ),
        "cara_guna": "Pencet karet atas → celupkan → lepaskan karet → cairan masuk → pindahkan → pencet untuk keluarkan.",
        "bahaya": "⚠️ Jangan dihisap dengan mulut! Bisa menelan bahan kimia berbahaya.",
        "ukuran": "±1–3 mL",
        "warna_hex": "#10b981",
    },
    {
        "id": 5,
        "nama": "Labu Ukur",
        "emoji": "🧫",
        "kategori": "Pengukur Volume",
        "foto": "labu ukur.jpg",
        "fungsi": "Membuat larutan dengan volume yang sangat tepat dan akurat.",
        "penjelasan_awam": (
            "Botol dengan leher panjang yang ada garis tanda batasnya. "
            "Dipakai saat kita butuh larutan dengan volume yang sudah diketahui."
        ),
        "cara_guna": "Masukkan zat, tambahkan air sedikit demi sedikit hingga tepat di garis tanda batas, kocok rata.",
        "bahaya": "⚠️ Tidak boleh dipanaskan, kaca presisi bisa retak dan ukuran jadi tidak akurat.",
        "ukuran": "50 mL – 2000 mL",
        "warna_hex": "#f59e0b",
    },
    {
        "id": 6,
        "nama": "Tabung Reaksi",
        "emoji": "🧫",
        "kategori": "Wadah Reaksi",
        "foto": "tabung reaksi.jpg",
        "fungsi": "Tempat melakukan reaksi kimia dalam skala kecil.",
        "penjelasan_awam": (
            "Tabung kecil berbentuk silinder panjang. "
            "Dipakai untuk mencampur bahan kimia dalam jumlah sedikit dan melihat perubahan yang terjadi."
        ),
        "cara_guna": "Isi maksimal ⅓ tabung, panaskan miring (arahkan ke ruang kosong), amati perubahan.",
        "bahaya": "⚠️ Arahkan mulut tabung menjauh dari wajah saat dipanaskan — bisa meletup!",
        "ukuran": "10 mL – 25 mL",
        "warna_hex": "#ef4444",
    },
    {
        "id": 7,
        "nama": "Corong",
        "emoji": "🔽",
        "kategori": "Penyaring",
        "foto": "corong.jpg",
        "fungsi": "Memindahkan cairan ke wadah bermulut sempit dan menyaring larutan dengan kertas saring.",
        "penjelasan_awam": (
            "Corong laboratorium adalah alat berbentuk kerucut dengan mulut lebar di bagian atas dan pipa sempit di bagian bawah. "
            "Di laboratorium, sering dipasang kertas saring di dalamnya untuk memisahkan padatan dari cairan "
        ),
        "cara_guna": "Letakkan di atas labu/gelas, pasang kertas saring jika perlu, tuangkan larutan perlahan.",
        "bahaya": "⚠️ Pastikan corong tidak mampet agar cairan mengalir lancar.",
        "ukuran": "diameter 50 mm - 150 mm",
        "warna_hex": "#84cc16",
    },
    {
        "id": 8,
        "nama": "Kaki Tiga",
        "emoji": "🔱",
        "kategori": "Penyangga",
        "foto": "kaki tiga.jpg",
        "fungsi": "Penyangga alat gelas saat proses pemanasan di atas pembakar spiritus.",
        "penjelasan_awam": (
            "Kaki tiga adalah alat penyangga berkaki tiga yang umumnya digunakan di laboratorium kimia atau "
            "biologi sebagai penopang wadah (seperti gelas beaker atau labu Erlenmeyer) saat proses pemanasan"
        ),
        "cara_guna": "Letakkan di atas pembakar spiritus, pasang kawat kasa di atasnya, baru letakkan gelas.",
        "bahaya": "⚠️ Besi akan panas! Jangan disentuh saat sedang atau baru selesai dipakai.",
        "ukuran": "Tinggi ±15 cm",
        "warna_hex": "#6b7280",
    },
    {
        "id": 9,
        "nama": "Pembakar Spiritus",
        "emoji": "🔥",
        "kategori": "Sumber Panas",
        "foto": "pembakar spirtus.jpg",
        "fungsi": "Sumber panas menggunakan bahan bakar spiritus (alkohol).",
        "penjelasan_awam": (
            "Pembakar spiritus adalah alat laboratorium yang berfungsi sebagai sumber panas atau api. Alat ini memanfaatkan cairan spiritus (alkohol yang "
            "didenaturasi) sebagai bahan bakar yang mengalir melalui sumbu untuk menghasilkan nyala"
        ),
        "cara_guna": "Nyalakan sumbu dengan korek api, letakkan tepat di bawah kaki tiga, matikan dengan tutupnya (jangan ditiup!).",
        "bahaya": "⚠️ JANGAN ditiup untuk mematikan — bisa memercikkan api! Gunakan tutupnya.",
        "ukuran": "Kapasitas ±150 mL spiritus",
        "warna_hex": "#f97316",
    },
    {
        "id": 10,
        "nama": "Kaca Arloji",
        "emoji": "🧫",
        "kategori": "Wadah",
        "foto": "kaca arloji.jpeg",
        "fungsi": "Untuk menimbang bahan kimia padat, menutup wadah saat pemanasan sampel, atau sebagai wadah untuk menguapkan sedikit larutan.",
        "penjelasan_awam": (
            "peralatan laboratorium berbentuk piringan bundar dan cekung yang terbuat dari kaca transparan. Alat ini "
            "dinamakan demikian karena bentuknya yang menyerupai kaca penutup jam tangan."
        ),
        "cara_guna": "Tuang larutan ke dalamnya, aduk dengan batang pengaduk, bisa dipanaskan di atas kompor bunsen.",
        "bahaya": "⚠️  Kaca tipis, bisa pecah jika kena benturan.",
        "ukuran": "diameter 50 mm - 180 mm",
        "warna_hex": "#3b82f6",
    },
    {
        "id": 11,
        "nama": "Cawan Porselen",
        "emoji": "🥛",
        "kategori": "Wadah",
        "foto": "porselen.jpeg",
        "fungsi": "Sebagai penyangga krus porselen saat dipanaskan langsung di atas nyala api Bunsen.",
        "penjelasan_awam": (
            "Cawan porselen adalah peralatan laboratorium khusus yang digunakan untuk memanaskan zat hingga suhu yang sangat tinggi. Cawan ini "
            "terbuat dari porselen, sejenis keramik yang sangat tahan terhadap panas dan reaksi kimia."
        ),
        "cara_guna": "Letakkan bahan di atas kaca arloji sebelum ditimbang, atau letakkan di atas gelas kimia sebagai penutup agar tidak terkontaminasi.",
        "bahaya": "⚠️ Mudah pecah/retak. Jika digunakan untuk menutup wadah panas, hati-hati saat membukanya karena uap panas akan keluar.",
        "ukuran": "5 mL – 500 mL",
        "warna_hex": "#3b82f6",
    },
    {
        "id": 12,
        "nama": "Segitiga Pembakar",
        "emoji": "🔥",
        "kategori": "Penyangga",
        "foto": "segitiga.jpeg",
        "fungsi": "Digunakan untuk memanaskan zat kimia pada suhu yang sangat tinggi (mengabukan sampel atau memijarkan padatan).",
        "penjelasan_awam": (
            "alat laboratorium yang berfungsi menopang wadah tahan panas, seperti cawan krus, saat proses pemanasan suhu tinggi "
            "menggunakan pembakar Bunsen. Alat ini memungkinkan kontak langsung dengan api dan distribusi panas yang merata."
        ),
        "cara_guna": "Letakkan sampel di dalam cawan, lalu letakkan di atas segitiga pembakar untuk dipanaskan.",
        "bahaya": "⚠️ Kaca tipis, bisa pecah jika kena benturaPermukaan porselen tetap panas dalam waktu lama setelah pemanasan. Risiko retak jika terkena perubahan suhu ekstrem secara mendadak (thermal shock).",
        "ukuran": "50 mm-75 mm setiap sisinya",
        "warna_hex": "#3b82f6",
    },
    {
        "id": 13,
        "nama": "Desikator",
        "emoji": "🥛",
        "kategori": "Wadah",
        "foto": "desikator.jpeg",
        "fungsi": "Menyimpan sampel agar tetap kering atau menghilangkan air dari bahan kimia (menjaga kelembapan rendah).",
        "penjelasan_awam": (
            "wadah tertutup kedap udara di laboratorium yang digunakan untuk menghilangkan kelembapan dari suatu zat atau mempertahankannya agar tetap kering. "
            "Alat ini sangat penting untuk mencegah bahan kimia atau sampel laboratorium menyerap uap air dari udara bebas. "
        ),
        "cara_guna": "Isi bagian bawah desikator dengan silika gel atau bahan pengering lainnya. Masukkan sampel, lalu tutup rapat (oleskan sedikit vaselin pada bibir penutup agar kedap udara).",
        "bahaya": "⚠️ Risiko implosi (pecah ke dalam) jika terjadi retakan pada kaca saat keadaan vakum. Selalu geser penutupnya sebelum diangkat, jangan ditarik paksa.",
        "ukuran": "50 mL – 2000 mL",
        "warna_hex": "#3b82f6",
    },
    {
        "id": 14,
        "nama": "Pipet Mohr",
        "emoji": "💧",
        "kategori": "Pemindah Cairan",
        "foto": "pipet mohr.jpeg",
        "fungsi": "Mengambil larutan dengan volume yang dapat divariasikan.",
        "penjelasan_awam": (
           " Pipet Mohr adalah jenis pipet yang memiliki garis-garis skala pengukuran di sepanjang tabungnya. Alat ini "
            "digunakan untuk mengambil dan memindahkan berbagai macam variasi volume cairan sesuai dengan kebutuhan."
        ),
        "cara_guna": "Gunakan filler (bola hisap) untuk menyedot larutan hingga volume yang diinginkan sesuai skala, lalu alirkan perlahan.",
        "bahaya": "⚠️ Jika digunakan untuk zat korosif, pastikan filler bekerja dengan baik agar cairan tidak terhisap masuk ke dalam filler.",
        "ukuran": "5 mL – 50 mL",
        "warna_hex": "#3b82f6",
    },
    {
        "id": 14,
        "nama": "Pipet Volumetri",
        "emoji": "💧",
        "kategori": "Pemindah Cairan",
        "foto": "pipet volumetri.jpeg",
        "fungsi": "Mengambil larutan dengan volume tunggal yang sangat akurat dan presisi (hanya satu ukuran/kapasitas).",
        "penjelasan_awam": (
            "Pipet volumetri adalah alat laboratorium yang didesain khusus untuk mengukur dan memindahkan cairan dengan "
            "satu volume tetap dan spesifik secara sangat akurat"
        ),
        "cara_guna": "Sedot cairan hingga melewati batas garis tanda, lalu lepaskan secara perlahan hingga meniskus cairan tepat berada pada garis. Alirkan dengan posisi tegak lurus.",
        "bahaya": "⚠️ Umumnya terbuat dari kaca tipis yang mudah patah. Hindari memaksakan pipet masuk ke dalam wadah yang sempit.",
        "ukuran": "5  mL – 100 mL",
        "warna_hex": "#3b82f6",
    },
]

# =========================
# DATA KUIS
# =========================
soal_kuis = [
    {
        "pertanyaan": "Alat berbentuk kerucut dengan leher sempit yang dipakai saat titrasi adalah...",
        "pilihan": ["Gelas Beker", "Erlenmeyer", "Labu Ukur", "Tabung Reaksi"],
        "jawaban": "Erlenmeyer",
    },
    {
        "pertanyaan": "Alat yang cara kerjanya mirip dengan pipet obat mata adalah...",
        "pilihan": ["Buret", "Pipet Tetes", "Corong", "Labu Ukur"],
        "jawaban": "Pipet Tetes",
    },
    {
        "pertanyaan": "Untuk mematikan pembakar spiritus, kita harus...",
        "pilihan": ["Meniupnya", "Menutup dengan tutupnya", "Menyiram air", "Menunggu habis sendiri"],
        "jawaban": "Menutup dengan tutupnya",
    },
    {
        "pertanyaan": "Alat yang dipakai untuk membuat larutan dengan volume SANGAT tepat adalah...",
        "pilihan": ["Gelas Beker", "Erlenmeyer", "Labu Ukur", "Tabung Reaksi"],
        "jawaban": "Labu Ukur",
    },
    {
        "pertanyaan": "Kaki tiga di laboratorium berfungsi sebagai...",
        "pilihan": ["Wadah reaksi", "Pengukur volume", "Penyangga saat pemanasan", "Pemindah cairan"],
        "jawaban": "Penyangga saat pemanasan",
    },
]

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.teks-kustom {
    color: #fcd34d !important; /* Warna kuning emas */
    font-weight: bold;
}
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0a0f1e 0%, #0f172a 50%, #0a1628 100%);
    color: #e2e8f0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.95) !important;
    border-right: 1px solid rgba(255,255,255,0.07);
    width: 200px;
}

section[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

/* Judul halaman */
h1 { font-family: 'Syne', sans-serif !important; font-weight: 800 !important; color: #f1f5f9 !important; }
h2 { font-family: 'Syne', sans-serif !important; font-weight: 700 !important; color: #f1f5f9 !important; }
h3 { font-family: 'Syne', sans-serif !important; font-weight: 700 !important; color: #f1f5f9 !important; }

/* Card alat */
.card-alat {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 16px;
    transition: all 0.3s;
    min-height: 210px;
}
.card-alat:hover {
    border-color: rgba(59,130,246,0.4);
    background: rgba(59,130,246,0.07);
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(59,130,246,0.15);
}

/* Info box */
.info-box {
    border-radius: 12px;
    padding: 14px 18px;
    margin-bottom: 12px;
}
.box-fungsi   { background: rgba(255,255,255,0.04); border-left: 3px solid #3b82f6; }
.box-awam     { background: rgba(16,185,129,0.08);  border-left: 3px solid #10b981; }
.box-cara     { background: rgba(59,130,246,0.08);  border-left: 3px solid #3b82f6; }
.box-bahaya   { background: rgba(239,68,68,0.08);   border-left: 3px solid #ef4444; }
.box-panduan  { background: rgba(255,255,255,0.03); border-left: 3px solid #f59e0b; }

.label-kecil {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

/* Badge kategori */
.badge {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.5px;
    background: rgba(59,130,246,0.15);
    color: #60a5fa;
    border: 1px solid rgba(59,130,246,0.3);
}

/* Metric */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 16px;
}

[data-testid="stMetricValue"] { color: #60a5fa !important; font-family: 'Syne', sans-serif !important; }
[data-testid="stMetricLabel"] { color: #64748b !important; }

/* Tombol utama */
.stButton > button {
    background: linear-gradient(135deg, #3b82f6, #8b5cf6) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    padding: 10px 24px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    opacity: 0.9 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(59,130,246,0.4) !important;
}

/* Radio */
.stRadio label { color: #e2e8f0 !important; }
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 15px;
    }

[data-testid="stSidebar"] label {
    font-size: 18px !important;      /* Perbesar font */
    padding: 15px 20px !important;   /* Perbesar area klik (padding) */
    background: rgba(255, 255, 255, 0.05); /* Latar belakang tombol */
    border-radius: 12px !important;  /* Sudut membulat */
    transition: all 0.3s ease;
    cursor: pointer;
}

[data-testid="stSidebar"] [role="radio"] {
    transform: scale(1.2); 
}

[data-testid="stSidebar"] label:hover {
    background: rgba(59, 130, 246, 0.2) !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: rgba(255,255,255,0.04) !important;
    border-radius: 12px !important;
    color: #f1f5f9 !important;
    font-weight: 700 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

/* Success / Warning */
.stSuccess { background: rgba(16,185,129,0.1) !important; border: 1px solid rgba(16,185,129,0.3) !important; color: #6ee7b7 !important; border-radius: 12px !important; }
.stWarning { background: rgba(245,158,11,0.1) !important; border: 1px solid rgba(245,158,11,0.3) !important; color: #fcd34d !important; border-radius: 12px !important; }
.stError   { background: rgba(239,68,68,0.1) !important;  border: 1px solid rgba(239,68,68,0.3) !important;  color: #fca5a5 !important; border-radius: 12px !important; }
.stInfo    { background: rgba(59,130,246,0.1) !important; border: 1px solid rgba(59,130,246,0.3) !important; color: #93c5fd !important; border-radius: 12px !important; }

/* Divider */
hr { border-color: rgba(255,255,255,0.07) !important; }

/* Footer */
.footer {
    text-align: center;
    padding: 24px;
    color: #334155;
    font-size: 13px;
    border-top: 1px solid rgba(255,255,255,0.06);
    margin-top: 40px;
}

/* Selectbox */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #e2e8f0 !important;
    border-radius: 20px !important;
}

#MENEBALKAN TOOGLE
[data-testid="stSidebarCollapseControl"] {
    font-weight: 900 !important; /* Membuat ikon lebih tebal */
    transform: scale(1.5);       /* Memperbesar ukuran ikon */
    color: #ffffff !important;   /* Memastikan warna kontras */
# Memperbesar ikon toggle sidebar saja
[data-testid="stSidebarCollapseControl"] button {
    transform: scale(100); 
    margin-left: 4px;      
}    

#MEMPERBESAR FONT SIDEBAR
[data-testid="stSidebarNav"] {
    font-size: 200px !important;
    }

[data-testid="stSidebarNav"] li {
    padding: 200px 0px
    }

[data-testid="stSidebarNav"] span {
    font-size: 30px !important;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.markdown("## ⚗️ PENGENALAN ALAT LABORATORIUM")
    
    # 1. INISIALISASI SESSION STATE
    if 'current_menu' not in st.session_state:
        st.session_state.current_menu = "🏠 Beranda"

    # 2. DEFINISIKAN MENU OPTIONS
    menu_options = ["🏠 Beranda", "🔬 Alat Laboratorium", "📖 Panduan Keselamatan", "📝 Kuis", "ℹ️ Tentang Kami"]

    # 3. GUNA FUNGSI INDEX DENGAN AMAN
    try:
        current_index = menu_options.index(st.session_state.current_menu)
    except ValueError:
        current_index = 0
        st.session_state.current_menu = menu_options[0]

    # 4. RADIO BUTTON
    menu = st.radio(
        "PETUNJUK",
        menu_options,
        index=current_index,
        label_visibility="collapsed"
    )

    # 5. UPDATE STATE
    st.session_state.current_menu = menu
    
# =========================
# ── BERANDA ──
# =========================
if menu == "🏠 Beranda":

    st.markdown("""
    <div style='text-align:center;padding:40px 0 20px'>
        <div style='display:inline-block;background:rgba(59,130,246,0.15);border:1px solid rgba(59,130,246,0.3);
             border-radius:999px;padding:6px 18px;font-size:12px;color:#60a5fa;
             letter-spacing:1px;text-transform:uppercase;font-weight:700;margin-bottom:20px'>
            🔬 Panduan Untuk Pemula
        </div>
        <h1 style='font-size:clamp(28px,5vw,52px);line-height:1.2;margin-bottom:16px'>
            Kenali Alat<br>
            <span style='background:linear-gradient(135deg,#3b82f6,#8b5cf6,#06b6d4);
                  -webkit-background-clip:text;-webkit-text-fill-color:transparent'>
                Laboratorium Kimia
            </span>
        </h1>
        <p style='color:#94a3b8;font-size:17px;max-width:500px;margin:0 auto 30px;line-height:1.7'>
            Pelajari alat - alat laboratorium kimia , penjelasan lengkap, mudah dipahami, disertai panduan keselamatan
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Statistik
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🧪 Total Alat", "15")
    c2.metric("📁 Kategori", "5")
    c3.metric("📝 Soal Kuis", "5")
    c4.metric("📸 Foto Alat", "15")

    st.markdown("---")

    # Gambar hero
    st.image(
        "https://images.unsplash.com/photo-1532187643603-ba119ca4109e?w=1200&q=80",
        use_container_width=True,
        caption='"Pertemuan dua kepribadian seperti kontak dua zat kimia: Jika ada reaksi, keduanya berubah - CG Jung"',
    )
    st.markdown("<p class='teks-kustom'>Tips: Klik menu Alat Laboratorium di sidebar untuk melihat foto dan penjelasan detail setiap alat atau langsung kuis untuk uji pemahamanmu</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ⚡ Preview Alat")

    # 3 alat pertama sebagai preview
    cols = st.columns(3)
    for i, alat in enumerate(alat_data[:3]):
        with cols[i]:
            st.markdown(f"""
            <div class='card-alat'>
                <h3 style='margin-bottom:6px;font-size:18px'>{alat['nama']}</h3>
                <span class='badge'>{alat['kategori']}</span>
                <p style='color:#94a3b8;font-size:13px;margin-top:10px;line-height:1.5'>{alat['fungsi']}</p>
            </div>
            """, unsafe_allow_html=True)
            
# =========================
# ── ALAT LABORATORIUM ──
# =========================
elif menu == "🔬 Alat Laboratorium":

    st.title("🔬 Alat Laboratorium Kimia")
    st.markdown("<p style='color:#64748b;margin-bottom:24px'>Klik ekspander setiap alat untuk melihat foto, fungsi, dan cara penggunaan lengkap.</p>", unsafe_allow_html=True)

    # Filter kategori
    semua_kategori = ["Semua"] + sorted(set(a["kategori"] for a in alat_data))
    filter_kat = st.selectbox("🗂️ Filter Kategori", semua_kategori)

    alat_tampil = alat_data if filter_kat == "Semua" else [a for a in alat_data if a["kategori"] == filter_kat]

    st.markdown(f"<p style='color:#64748b;font-size:13px;margin-bottom:16px'>Menampilkan {len(alat_tampil)} alat</p>", unsafe_allow_html=True)

    for alat in alat_tampil:
        with st.expander(f"{alat['emoji']}  **{alat['nama']}** — *{alat['kategori']}*"):

            col_foto, col_info = st.columns([1, 1.4])

            with col_foto:
                st.image(alat["foto"], use_container_width=True, caption=alat["nama"])
                st.markdown(f"""
                <div style='display:flex;gap:8px;flex-wrap:wrap;margin-top:10px'>
                    <span class='badge' style='background:rgba(255,255,255,0.06);color:#94a3b8;border-color:rgba(255,255,255,0.1)'>
                        📏 {alat['ukuran']}
                    </span>
                    <span class='badge'>{alat['kategori']}</span>
                </div>
                """, unsafe_allow_html=True)

            with col_info:
                st.markdown(f"""
                <div class='info-box box-fungsi'>
                    <div class='label-kecil' style='color:#3b82f6'>Fungsi Utama</div>
                    <div style='color:#e2e8f0;line-height:1.6'>{alat['fungsi']}</div>
                </div>

                <div class='info-box box-awam'>
                    <div class='label-kecil' style='color:#10b981'>💡 Penjelasan Sederhana</div>
                    <div style='color:#e2e8f0;line-height:1.6'>{alat['penjelasan_awam']}</div>
                </div>

                <div class='info-box box-cara'>
                    <div class='label-kecil' style='color:#3b82f6'>📋 Cara Penggunaan</div>
                    <div style='color:#e2e8f0;line-height:1.6'>{alat['cara_guna']}</div>
                </div>

                <div class='info-box box-bahaya'>
                    <div class='label-kecil' style='color:#ef4444'>Perhatian & Bahaya</div>
                    <div style='color:#fca5a5;line-height:1.6'>{alat['bahaya']}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")

    # Tabel ringkasan
    st.markdown("### 📊 Ringkasan Semua Alat")
    import pandas as pd
    df = pd.DataFrame([
        {
            "Alat": f"{a['emoji']} {a['nama']}",
            "Kategori": a["kategori"],
            "Fungsi": a["fungsi"],
            "Ukuran": a["ukuran"],
        }
        for a in alat_data
    ])
    st.dataframe(df, use_container_width=True, hide_index=True)

# =========================
# ── INSTRUMEN LABORATORIUM──
# =========================
if menu == "🏠 Beranda":

    st.markdown("""
    <div style='text-align:center;padding:40px 0 20px'>
        <div style='display:inline-block;background:rgba(59,130,246,0.15);border:1px solid rgba(59,130,246,0.3);
             border-radius:999px;padding:6px 18px;font-size:12px;color:#60a5fa;
             letter-spacing:1px;text-transform:uppercase;font-weight:700;margin-bottom:20px'>
            🔬 Panduan Untuk Pemula
        </div>
        <h1 style='font-size:clamp(28px,5vw,52px);line-height:1.2;margin-bottom:16px'>
            Kenali Alat<br>
            <span style='background:linear-gradient(135deg,#3b82f6,#8b5cf6,#06b6d4);
                  -webkit-background-clip:text;-webkit-text-fill-color:transparent'>
                Laboratorium Kimia
            </span>
        </h1>
        <p style='color:#94a3b8;font-size:17px;max-width:500px;margin:0 auto 30px;line-height:1.7'>
            Pelajari alat - alat laboratorium kimia , penjelasan lengkap, mudah dipahami, disertai panduan keselamatan
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Statistik
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🧪 Total Alat", "15")
    c2.metric("📁 Kategori", "5")
    c3.metric("📝 Soal Kuis", "5")
    c4.metric("📸 Foto Alat", "15")

    st.markdown("---")

    # Gambar hero
    st.image(
        "https://images.unsplash.com/photo-1532187643603-ba119ca4109e?w=1200&q=80",
        use_container_width=True,
        caption='"Pertemuan dua kepribadian seperti kontak dua zat kimia: Jika ada reaksi, keduanya berubah - CG Jung"',
    )
    st.markdown("<p class='teks-kustom'>Tips: Klik menu Alat Laboratorium di sidebar untuk melihat foto dan penjelasan detail setiap alat atau langsung kuis untuk uji pemahamanmu</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ⚡ Preview Alat")

    # 3 alat pertama sebagai preview
    cols = st.columns(3)
    for i, alat in enumerate(alat_data[:3]):
        with cols[i]:
            st.markdown(f"""
            <div class='card-alat'>
                <h3 style='margin-bottom:6px;font-size:18px'>{alat['nama']}</h3>
                <span class='badge'>{alat['kategori']}</span>
                <p style='color:#94a3b8;font-size:13px;margin-top:10px;line-height:1.5'>{alat['fungsi']}</p>
            </div>
            """, unsafe_allow_html=True)
            
# =========================
# ── PANDUAN KESELAMATAN ──
# =========================
elif menu == "📖 Panduan Keselamatan":

    st.title("📖 Panduan Keselamatan Laboratorium")
    st.markdown("<p style='color:#64748b;margin-bottom:28px'>Aturan penting yang wajib diketahui sebelum masuk laboratorium.</p>", unsafe_allow_html=True)

    aturan = [
        ("🥽", "Selalu Pakai APD", "Wajib mengenakan kacamata pelindung, sarung tangan, dan jas lab sebelum memulai eksperimen apapun.", "#3b82f6"),
        ("🚫", "Jangan Makan & Minum", "Dilarang keras makan, minum, atau mencicipi bahan kimia apapun di dalam laboratorium.", "#ef4444"),
        ("💨", "Jaga Ventilasi", "Bekerja dengan bahan kimia berbau atau beracun harus dilakukan di lemari asam (fume hood).", "#06b6d4"),
        ("🧹", "Bersihkan Setelah Selesai", "Cuci semua alat yang digunakan, buang limbah kimia dengan benar, bersihkan meja kerja.", "#10b981"),
        ("📋", "Baca Label Dahulu", "Selalu baca label botol bahan kimia sebelum menggunakannya. Pastikan kamu tahu sifat dan bahayanya.", "#f59e0b"),
        ("🔥", "Hati-hati Api", "Jauhkan bahan mudah terbakar dari api. Matikan pembakar spiritus dengan tutupnya, bukan ditiup!", "#f97316"),
    ]

    for icon, judul, deskripsi, warna in aturan:
        st.markdown(f"""
        <div style='display:flex;gap:16px;padding:18px 22px;background:rgba(255,255,255,0.03);
             border:1px solid rgba(255,255,255,0.07);border-radius:14px;margin-bottom:12px;
             border-left:3px solid {warna}'>
            <div style='font-size:32px;flex-shrink:0'>{icon}</div>
            <div>
                <div style='font-weight:700;font-size:16px;color:#f1f5f9;margin-bottom:5px'>{judul}</div>
                <div style='color:#94a3b8;line-height:1.6'>{deskripsi}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📞 Pertolongan Pertama Darurat")
    st.markdown("<p class='teks-kustom'>Segera hubungi guru/pengawas laboratorium jika terjadi kecelakaan!</p>", unsafe_allow_html=True)

    darurat = [
        ("👁️ Terkena cairan di mata", "Segera siram dengan air bersih mengalir selama 15 menit, jangan digosok."),
        ("💨 Terhirup gas berbahaya", "Segera keluar ke udara segar, duduk, hubungi pengawas segera."),
        ("🔥 Kebakaran kecil", "Padamkan dengan APAR atau pasir kering, jangan panik."),
        ("💧 Tumpahan bahan kimia", "Informasikan kepada pengawas, jangan dibersihkan sendiri tanpa arahan."),
        ("🩹 Luka terkena kaca", "Bilas dengan air bersih, berikan pertolongan pertama, hubungi pengawas."),
        ("🤢 Menelan bahan kimia", "JANGAN dimuntahkan paksa, segera cari bantuan medis."),
    ]

    c1, c2 = st.columns(2)
    for i, (kondisi, tindakan) in enumerate(darurat):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""
            <div style='background:rgba(245,158,11,0.07);border:1px solid rgba(245,158,11,0.2);
                 border-radius:12px;padding:14px;margin-bottom:10px'>
                <div style='color:#f59e0b;font-weight:700;font-size:13px;margin-bottom:6px'>{kondisi}</div>
                <div style='color:#94a3b8;font-size:13px;line-height:1.5'>{tindakan}</div>
            </div>
            """, unsafe_allow_html=True)

# =========================
# ── ABOUT US ──
# =========================
elif menu == "ℹ️ About Us":
    st.title("About Us")
    st.write("Aplikasi ini dibuat untuk membantu siswa memahami alat laboratorium kimia dengan cara yang interaktif.")

# =========================
# ── KUIS ──
# =========================
elif menu == "📝 Kuis":

    st.title("📝 Kuis Peralatan Laboratorium Kimia")
    st.markdown("<p style='color:#64748b;font-size:20px;margin-bottom:30px'>Uji pemahamanmu tentang alat-alat laboratorium kimia!</p>", unsafe_allow_html=True)

    # Inisialisasi session state
    if "kuis_jawaban" not in st.session_state:
        st.session_state.kuis_jawaban = {}
    if "kuis_submit" not in st.session_state:
        st.session_state.kuis_submit = False

    if not st.session_state.kuis_submit:
        with st.form("form_kuis"):
            for i, soal in enumerate(soal_kuis):
                st.markdown(f"""
                <div style='background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
                     border-radius:14px;padding:20px;margin-bottom:4px'>
                    <div style='font-weight:700;font-size:15px;color:#f1f5f9'>
                        <span style='color:#3b82f6;margin-right:8px'>#{i+1}</span>{soal['pertanyaan']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                jawaban = st.radio(
                    f"Pilihan soal {i+1}",
                    soal["pilihan"],
                    key=f"soal_{i}",
                    label_visibility="collapsed"
                )
                st.session_state.kuis_jawaban[i] = jawaban
                st.markdown("")

            submitted = st.form_submit_button("✅ Submit Jawaban", use_container_width=True)

            if submitted:
                st.session_state.kuis_submit = True
                st.rerun()

    else:
        # Hitung skor
        skor = 0
        for i, soal in enumerate(soal_kuis):
            if st.session_state.kuis_jawaban.get(i) == soal["jawaban"]:
                skor += 1

        persen = int((skor / len(soal_kuis)) * 100)

        # Header hasil
        if skor == len(soal_kuis):
            emoji_hasil = "🏆"
            pesan = "Sempurna! Kamu menguasai materi ini!"
        elif skor >= 3:
            emoji_hasil = "👍"
            pesan = "Bagus! Terus tingkatkan pemahamanmu."
        else:
            emoji_hasil = "📚"
            pesan = "Jangan menyerah, pelajari lagi ya!"

        st.markdown(f"""
        <div style='text-align:center;padding:32px;background:rgba(255,255,255,0.03);
             border:1px solid rgba(255,255,255,0.08);border-radius:20px;margin-bottom:28px'>
            <div style='font-size:64px;margin-bottom:12px'>{emoji_hasil}</div>
            <div style='font-size:52px;font-weight:800;font-family:"Syne",sans-serif;
                 background:linear-gradient(135deg,#3b82f6,#8b5cf6);
                 -webkit-background-clip:text;-webkit-text-fill-color:transparent'>
                {skor}/{len(soal_kuis)}
            </div>
            <div style='color:#94a3b8;font-size:17px;margin:10px 0 6px'>{pesan}</div>
            <div style='color:#64748b;font-size:14px'>Skor: {persen}%</div>
        </div>
        """, unsafe_allow_html=True)

        if skor == len(soal_kuis):
            st.balloons()

        # Review jawaban
        st.markdown("### 📋 Review Jawaban")
        for i, soal in enumerate(soal_kuis):
            jawaban_user = st.session_state.kuis_jawaban.get(i, "-")
            benar = jawaban_user == soal["jawaban"]

            if benar:
                st.success(f"✅ **Soal {i+1}:** {soal['pertanyaan']}\n\n**Jawaban kamu: {jawaban_user}** — Benar!")
            else:
                st.error(
                    f"❌ **Soal {i+1}:** {soal['pertanyaan']}\n\n"
                    f"Jawaban kamu: ~~{jawaban_user}~~\n\n"
                    f"✅ Jawaban benar: **{soal['jawaban']}**"
                )

        st.markdown("---")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🔄 Coba Lagi", use_container_width=True):
                st.session_state.kuis_jawaban = {}
                st.session_state.kuis_submit = False
                st.rerun()
        with col_b:
            if st.button("🔍 Pelajari Alat Laboratorium", use_container_width=True):
                st.session_state.current_menu = "🔬 Alat Laboratorium"
                st.popover("Klik menu 'Alat Laboratorium'")
                st.rerun()
            



# =========================
# FOOTER
# =========================
st.markdown("""
<div class='footer'>
    Dibuat untuk mengampu Project matkul Logika Pemrograman Komputer semester 2 Politeknik AKA Bogor
</div>
""", unsafe_allow_html=True)
