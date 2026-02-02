# formatters.py

import json
import base64

def _format_dict(data: dict, title: str) -> str:
    """Helper to format a dictionary into a readable string."""
    output = [f"--- {title} ---"]
    for key, value in data.items():
        if isinstance(value, dict):
            output.append(f"{key.replace('_', ' ').title()}:")
            for sub_key, sub_value in value.items():
                output.append(f"  {sub_key.replace('_', ' ').title()}: {sub_value}")
        else:
            output.append(f"{key.replace('_', ' ').title()}: {value}")
    output.append("-" * (len(title) + 8)) # Adjust line length for title
    return "\n".join(output)

def _format_list_of_dicts(data: list, title: str, fields: list) -> str:
    """Helper to format a list of dictionaries into a readable string."""
    output = [f"--- {title} ---"]
    if not data:
        output.append("Tidak ada data ditemukan.")
        return "\n".join(output)
    
    for i, item in enumerate(data):
        item_details = []
        for field in fields:
            item_details.append(f"{field.replace('_', ' ').title()}: {item.get(field, 'N/A')}")
        output.append(f"{i+1}. {', '.join(item_details)}")
    output.append("-" * (len(title) + 8))
    return "\n".join(output)

# --- Perguruan Tinggi Formatters ---
def format_pt_details(data: dict) -> str:
    """Formats the detailed information of a university."""
    if not data:
        return "Detail Perguruan Tinggi tidak ditemukan."
    
    title = "Detail Perguruan Tinggi"
    output = [f"--- {title} ---"]
    output.append(f"Nama PT      : {data.get('nama_pt', 'N/A')}")
    output.append(f"Singkatan PT : {data.get('nm_singkat', 'N/A')}")
    output.append(f"Kode PT      : {data.get('kode_pt', 'N/A')}")
    output.append(f"Alamat       : {data.get('alamat', 'N/A')}")
    output.append(f"Kota/Kab     : {data.get('kab_kota_pt', 'N/A')}")
    output.append(f"Provinsi     : {data.get('provinsi_pt', 'N/A')}")
    output.append(f"Website      : {data.get('website', 'N/A')}")
    output.append(f"Email        : {data.get('email', 'N/A')}")
    output.append(f"Telepon      : {data.get('no_tel', 'N/A')}")
    output.append(f"Status       : {data.get('status_pt', 'N/A')}")
    output.append(f"Akreditasi   : {data.get('akreditasi_pt', 'N/A')}")
    output.append("-" * (len(title) + 8))
    return "\n".join(output)

def format_prodi_pt_list(data: list) -> str:
    """Formats a list of study programs from a university."""
    if not data:
        return "Program Studi tidak ditemukan untuk PT ini."
    
    fields = ['nama_prodi', 'jenjang_prodi', 'akreditasi', 'jumlah_mahasiswa', 'jumlah_dosen']
    return _format_list_of_dicts(data, "Daftar Program Studi di PT", fields)

def format_logo_pt(data: str) -> str:
    """Formats the base64 logo data."""
    if not data:
        return "Logo tidak ditemukan."
    return f"Data Logo (base64) diterima. Panjang: {len(data)} karakter. Cuplikan: {data[:100]}..."

def format_rasio_pt(data: dict) -> str:
    """Formats the student-lecturer ratio of a university."""
    if not data:
        return "Rasio Mahasiswa & Dosen tidak ditemukan."
    return _format_dict(data, "Rasio Mahasiswa & Dosen")

def format_mahasiswa_pt_stats(data: dict) -> str:
    """Formats the student statistics of a university."""
    if not data:
        return "Statistik Mahasiswa tidak ditemukan."
    return _format_dict(data, "Statistik Mahasiswa")

def format_waktu_studi_pt(data: list) -> str:
    """Formats the average study time data for a university."""
    if not data:
        return "Data Waktu Studi tidak ditemukan."
    fields = ['jenjang', 'mean_masa_studi']
    return _format_list_of_dicts(data, "Rata-rata Waktu Studi PT", fields)

def format_name_histories_pt(data: list) -> str:
    """Formats the name history of a university."""
    if not data:
        return "Sejarah Nama PT tidak ditemukan."
    fields = ['nama_lama', 'tanggal_perubahan'] # Assuming these fields based on common patterns
    return _format_list_of_dicts(data, "Sejarah Nama Perguruan Tinggi", fields)

def format_cost_range_pt(data: dict) -> str:
    """Formats the cost range data for a university."""
    if not data:
        return "Kisaran Biaya Kuliah PT tidak ditemukan."
    return _format_dict(data, "Kisaran Biaya Kuliah PT")

def format_graduation_rate_pt(data: dict) -> str:
    """Formats the graduation rate of a university."""
    if not data:
        return "Tingkat Kelulusan PT tidak ditemukan."
    return _format_dict(data, "Tingkat Kelulusan PT")

def format_jumlah_prodi_pt(data: dict) -> str:
    """Formats the count of study programs in a university."""
    if not data:
        return "Jumlah Program Studi PT tidak ditemukan."
    return _format_dict(data, "Jumlah Program Studi PT")

def format_jumlah_mahasiswa_pt(data: dict) -> str:
    """Formats the count of students in a university."""
    if not data:
        return "Jumlah Mahasiswa PT tidak ditemukan."
    return _format_dict(data, "Jumlah Mahasiswa PT")

def format_jumlah_dosen_pt(data: dict) -> str:
    """Formats the count of lecturers in a university."""
    if not data:
        return "Jumlah Dosen PT tidak ditemukan."
    return _format_dict(data, "Jumlah Dosen PT")

def format_sarpras_file_name_pt(data: list) -> str:
    """Formats the sarpras file names for a university."""
    if not data:
        return "Nama File Sarpras tidak ditemukan."
    fields = ['id_blob', 'file_name']
    return _format_list_of_dicts(data, "Nama File Sarpras PT", fields)

def format_sarpras_blob_pt(data: str) -> str:
    """Formats the sarpras blob data."""
    if not data:
        return "Blob Sarpras tidak ditemukan."
    return f"Data Blob Sarpras (base64) diterima. Panjang: {len(data)} karakter. Cuplikan: {data[:100]}..."

# --- Dosen Formatters ---
def format_dosen_profile(data: dict) -> str:
    """Formats the detailed profile of a lecturer."""
    if not data:
        return "Profil Dosen tidak ditemukan."
    
    title = "Profil Dosen"
    output = [f"--- {title} ---"]
    output.append(f"Nama Dosen        : {data.get('nama_dosen', 'N/A')}")
    output.append(f"NIDN              : {data.get('nidn', 'N/A')}")
    output.append(f"Jenis Kelamin     : {data.get('jenis_kelamin', 'N/A')}")
    output.append(f"Jabatan Akademik  : {data.get('jabatan_akademik', 'N/A')}")
    output.append(f"Pendidikan Tertinggi: {data.get('pendidikan_tertinggi', 'N/A')}")
    output.append(f"Status Ikatan Kerja: {data.get('status_ikatan_kerja', 'N/A')}")
    output.append(f"Status Aktivitas  : {data.get('status_aktivitas', 'N/A')}")
    output.append(f"Nama PT           : {data.get('nama_pt', 'N/A')}")
    output.append(f"Nama Prodi        : {data.get('nama_prodi', 'N/A')}")
    output.append("-" * (len(title) + 8))
    return "\n".join(output)

def format_dosen_penelitian(data: list) -> str:
    """Formats a list of research activities for a lecturer."""
    if not data:
        return "Penelitian Dosen tidak ditemukan."
    fields = ['judul_kegiatan', 'tahun_kegiatan', 'jenis_kegiatan']
    return _format_list_of_dicts(data, "Penelitian Dosen", fields)

def format_dosen_pengabdian(data: list) -> str:
    """Formats a list of community service activities for a lecturer."""
    if not data:
        return "Pengabdian Dosen tidak ditemukan."
    fields = ['judul_kegiatan', 'tahun_kegiatan', 'jenis_kegiatan']
    return _format_list_of_dicts(data, "Pengabdian Dosen", fields)

def format_dosen_karya(data: list) -> str:
    """Formats a list of academic works for a lecturer."""
    if not data:
        return "Karya Ilmiah Dosen tidak ditemukan."
    fields = ['judul_kegiatan', 'tahun_kegiatan', 'jenis_kegiatan']
    return _format_list_of_dicts(data, "Karya Ilmiah Dosen", fields)

def format_dosen_paten(data: list) -> str:
    """Formats a list of patents for a lecturer."""
    if not data:
        return "Paten Dosen tidak ditemukan."
    fields = ['judul_kegiatan', 'tahun_kegiatan', 'jenis_kegiatan']
    return _format_list_of_dicts(data, "Paten Dosen", fields)

def format_dosen_study_history(data: list) -> str:
    """Formats the study history of a lecturer."""
    if not data:
        return "Riwayat Studi Dosen tidak ditemukan."
    fields = ['jenjang', 'bidang_studi', 'nama_pt', 'tahun_lulus']
    return _format_list_of_dicts(data, "Riwayat Studi Dosen", fields)

def format_dosen_teaching_history(data: list) -> str:
    """Formats the teaching history of a lecturer."""
    if not data:
        return "Riwayat Mengajar Dosen tidak ditemukan."
    fields = ['nama_semester', 'nama_matkul', 'nama_kelas', 'nama_pt']
    return _format_list_of_dicts(data, "Riwayat Mengajar Dosen", fields)

# --- Mahasiswa Formatters ---
def format_mahasiswa_details(data: dict) -> str:
    """Formats the detailed information of a student."""
    if not data:
        return "Detail Mahasiswa tidak ditemukan."
    
    title = "Detail Mahasiswa"
    output = [f"--- {title} ---"]
    output.append(f"Nama         : {data.get('nama', 'N/A')}")
    output.append(f"NIM          : {data.get('nim', 'N/A')}")
    output.append(f"Jenis Kelamin: {data.get('jenis_kelamin', 'N/A')}")
    output.append(f"Tempat Lahir : {data.get('tempat_lahir', 'N/A')}")
    output.append(f"Tgl. Lahir   : {data.get('tanggal_lahir', 'N/A')}")
    output.append(f"Universitas  : {data.get('nama_pt', 'N/A')}")
    output.append(f"Program Studi: {data.get('prodi', 'N/A')}")
    output.append(f"Jenjang      : {data.get('jenjang', 'N/A')}")
    output.append(f"Tgl. Masuk   : {data.get('tanggal_masuk', 'N/A')}")
    output.append(f"Status       : {data.get('status_saat_ini', 'N/A')}")
    output.append(f"Nama Ibu     : {data.get('nama_ibu', 'N/A')}")
    output.append("-" * (len(title) + 8))
    return "\n".join(output)

# --- Program Studi Formatters ---
def format_prodi_details(data: dict) -> str:
    """Formats the detailed information of a study program."""
    if not data:
        return "Detail Program Studi tidak ditemukan."
    
    title = "Detail Program Studi"
    output = [f"--- {title} ---"]
    output.append(f"Nama Prodi      : {data.get('nama_prodi', 'N/A')}")
    output.append(f"Jenjang         : {data.get('jenj_didik', 'N/A')}")
    output.append(f"Kode Prodi      : {data.get('kode_prodi', 'N/A')}")
    output.append(f"Akreditasi      : {data.get('akreditasi', 'N/A')}")
    output.append(f"Nama PT         : {data.get('nama_pt', 'N/A')}")
    output.append(f"Tanggal Berdiri : {data.get('tgl_berdiri', 'N/A')}")
    output.append(f"Status          : {data.get('status', 'N/A')}")
    output.append(f"Email           : {data.get('email', 'N/A')}")
    output.append(f"Website         : {data.get('website', 'N/A')}")
    output.append("-" * (len(title) + 8))
    return "\n".join(output)

def format_prodi_description(data: dict) -> str:
    """Formats the description of a study program."""
    if not data:
        return "Deskripsi Program Studi tidak ditemukan."
    
    title = "Deskripsi Program Studi"
    output = [f"--- {title} ---"]
    output.append(f"Deskripsi Singkat  : {data.get('deskripsi_singkat', 'N/A')}")
    output.append(f"Visi               : {data.get('visi', 'N/A')}")
    output.append(f"Misi               : {data.get('misi', 'N/A')}")
    output.append(f"Kompetensi         : {data.get('kompetensi', 'N/A')}")
    output.append(f"Capaian Belajar    : {data.get('capaian_belajar', 'N/A')}")
    output.append("-" * (len(title) + 8))
    return "\n".join(output)

def format_prodi_name_histories(data: list) -> str:
    """Formats the name history of a study program."""
    if not data:
        return "Sejarah Nama Program Studi tidak ditemukan."
    fields = ['nama_lama', 'tanggal_perubahan'] # Assuming common fields
    return _format_list_of_dicts(data, "Sejarah Nama Program Studi", fields)

def format_prodi_num_students_lecturers(data: dict) -> str:
    """Formats the number of students and lecturers in a study program."""
    if not data:
        return "Jumlah Mahasiswa & Dosen Prodi tidak ditemukan."
    return _format_dict(data, "Jumlah Mahasiswa & Dosen Prodi")

def format_prodi_cost_range(data: dict) -> str:
    """Formats the cost range of a study program."""
    if not data:
        return "Kisaran Biaya Kuliah Prodi tidak ditemukan."
    return _format_dict(data, "Kisaran Biaya Kuliah Prodi")

def format_prodi_daya_tampung(data: dict) -> str:
    """Formats the capacity of a study program."""
    if not data:
        return "Daya Tampung Prodi tidak ditemukan."
    return _format_dict(data, "Daya Tampung Prodi")

def format_prodi_rasio_dosen_mahasiswa(data: dict) -> str:
    """Formats the student-lecturer ratio of a study program."""
    if not data:
        return "Rasio Dosen Mahasiswa Prodi tidak ditemukan."
    return _format_dict(data, "Rasio Dosen Mahasiswa Prodi")

def format_prodi_graduation_rate(data: dict) -> str:
    """Formats the graduation rate of a study program."""
    if not data:
        return "Tingkat Kelulusan Prodi tidak ditemukan."
    return _format_dict(data, "Tingkat Kelulusan Prodi")

def format_logo_prodi(data: str) -> str:
    """Formats the base64 logo data for a study program."""
    if not data:
        return "Logo Prodi tidak ditemukan."
    return f"Data Logo Prodi (base64) diterima. Panjang: {len(data)} karakter. Cuplikan: {data[:100]}..."

def format_homebase_prodi(data: dict) -> str:
    """Formats the homebase ratio of a study program."""
    if not data:
        return "Homebase Prodi tidak ditemukan."
    return _format_dict(data, "Homebase Prodi")

def format_penghitung_ratio_prodi(data) -> str:
    """Formats the ratio counter of a study program."""
    if not data:
        return "Penghitung Rasio Prodi tidak ditemukan."

    if isinstance(data, list):
        title = "Penghitung Rasio Prodi"
        output = [f"--- {title} ---"]
        if not data:
            output.append("Tidak ada data ditemukan.")
        else:
            for i, item in enumerate(data):
                output.append(f"{i+1}. Data:")
                if isinstance(item, dict):
                    for key, value in item.items():
                        output.append(f"   {key.replace('_', ' ').title()}: {value}")
                else:
                    output.append(f"   {item}")
        output.append("-" * (len(title) + 8))
        return "\n".join(output)

    return _format_dict(data, "Penghitung Rasio Prodi")

# --- Statistik & Visualisasi Formatters ---
def format_dosen_count_active(data: dict) -> str:
    """Formats the active lecturer count."""
    if not data:
        return "Jumlah Dosen Aktif tidak ditemukan."
    return _format_dict(data, "Jumlah Dosen Aktif")

def format_mahasiswa_count_active(data: dict) -> str:
    """Formats the active student count."""
    if not data:
        return "Jumlah Mahasiswa Aktif tidak ditemukan."
    return _format_dict(data, "Jumlah Mahasiswa Aktif")

def format_prodi_count(data: dict) -> str:
    """Formats the study program count."""
    if not data:
        return "Jumlah Program Studi tidak ditemukan."
    return _format_dict(data, "Jumlah Program Studi")

def format_pt_count(data: dict) -> str:
    """Formats the university count."""
    if not data:
        return "Jumlah Perguruan Tinggi tidak ditemukan."
    return _format_dict(data, "Jumlah Perguruan Tinggi")

def format_data_dosen_keaktifan(data: list) -> str:
    """Formats the lecturer activeness visualization data."""
    if not data:
        return "Data Keaktifan Dosen tidak ditemukan."
    fields = ['status_keaktifan', 'jumlah_dosen']
    return _format_list_of_dicts(data, "Visualisasi Keaktifan Dosen", fields)

def format_data_dosen_bidang(data: list) -> str:
    """Formats the lecturer field of study visualization data."""
    if not data:
        return "Data Dosen Berdasarkan Bidang tidak ditemukan."
    fields = ['bidang', 'jumlah_dosen']
    return _format_list_of_dicts(data, "Visualisasi Dosen Berdasarkan Bidang", fields)

def format_data_dosen_jenis_kelamin(data: list) -> str:
    """Formats the lecturer gender visualization data."""
    if not data:
        return "Data Dosen Berdasarkan Jenis Kelamin tidak ditemukan."
    fields = ['jenis_kelamin', 'jumlah']
    return _format_list_of_dicts(data, "Visualisasi Dosen Berdasarkan Jenis Kelamin", fields)

def format_data_dosen_jenjang(data: list) -> str:
    """Formats the lecturer education level visualization data."""
    if not data:
        return "Data Dosen Berdasarkan Jenjang tidak ditemukan."
    fields = ['jenjang_dosen', 'jumlah_dosen']
    return _format_list_of_dicts(data, "Visualisasi Dosen Berdasarkan Jenjang", fields)

def format_data_dosen_ikatan(data: list) -> str:
    """Formats the lecturer employment bond visualization data."""
    if not data:
        return "Data Dosen Berdasarkan Ikatan tidak ditemukan."
    fields = ['ikatan_dosen', 'jumlah']
    return _format_list_of_dicts(data, "Visualisasi Dosen Berdasarkan Ikatan", fields)

def format_data_mahasiswa_bidang(data: list) -> str:
    """Formats the student field of study visualization data."""
    if not data:
        return "Data Mahasiswa Berdasarkan Bidang tidak ditemukan."
    fields = ['bidang', 'jumlah_mhs']
    return _format_list_of_dicts(data, "Visualisasi Mahasiswa Berdasarkan Bidang", fields)

def format_data_mahasiswa_jenis_kelamin(data: list) -> str:
    """Formats the student gender visualization data."""
    if not data:
        return "Data Mahasiswa Berdasarkan Jenis Kelamin tidak ditemukan."
    fields = ['jenis_kelamin', 'jumlah_mhs']
    return _format_list_of_dicts(data, "Visualisasi Mahasiswa Berdasarkan Jenis Kelamin", fields)

def format_data_mahasiswa_jenjang(data: list) -> str:
    """Formats the student education level visualization data."""
    if not data:
        return "Data Mahasiswa Berdasarkan Jenjang tidak ditemukan."
    fields = ['nama_jenjang', 'jumlah_mhs']
    return _format_list_of_dicts(data, "Visualisasi Mahasiswa Berdasarkan Jenjang", fields)

def format_data_mahasiswa_kelompok_lembaga(data: list) -> str:
    """Formats the student institutional group visualization data."""
    if not data:
        return "Data Mahasiswa Berdasarkan Kelompok Lembaga tidak ditemukan."
    fields = ['kelompok_lembaga', 'jumlah_mhs']
    return _format_list_of_dicts(data, "Visualisasi Mahasiswa Berdasarkan Kelompok Lembaga", fields)

def format_data_mahasiswa_status(data: list) -> str:
    """Formats the student status visualization data."""
    if not data:
        return "Data Mahasiswa Berdasarkan Status tidak ditemukan."
    fields = ['status_mahasiswa', 'jumlah']
    return _format_list_of_dicts(data, "Visualisasi Mahasiswa Berdasarkan Status", fields)

def format_data_pt_bentuk(data: list) -> str:
    """Formats the university type visualization data."""
    if not data:
        return "Data Perguruan Tinggi Berdasarkan Bentuk tidak ditemukan."
    fields = ['bentuk_pt', 'jumlah_pt']
    return _format_list_of_dicts(data, "Visualisasi Perguruan Tinggi Berdasarkan Bentuk", fields)

def format_data_pt_akreditasi(data: list) -> str:
    """Formats the university accreditation visualization data."""
    if not data:
        return "Data Perguruan Tinggi Berdasarkan Akreditasi tidak ditemukan."
    fields = ['akreditasi', 'jumlah_pt']
    return _format_list_of_dicts(data, "Visualisasi Perguruan Tinggi Berdasarkan Akreditasi", fields)

def format_data_pt_kelompok_pembina(data: list) -> str:
    """Formats the university administrative overseer group visualization data."""
    if not data:
        return "Data Perguruan Tinggi Berdasarkan Kelompok Pembina tidak ditemukan."
    fields = ['kelompok_pembina', 'jumlah_pt']
    return _format_list_of_dicts(data, "Visualisasi Perguruan Tinggi Berdasarkan Kelompok Pembina", fields)

def format_data_pt_provinsi(data: list) -> str:
    """Formats the university province visualization data."""
    if not data:
        return "Data Perguruan Tinggi Berdasarkan Provinsi tidak ditemukan."
    fields = ['provinsi', 'jumlah_pt']
    return _format_list_of_dicts(data, "Visualisasi Perguruan Tinggi Berdasarkan Provinsi", fields)

def format_data_prodi_jenjang(data: list) -> str:
    """Formats the study program education level visualization data."""
    if not data:
        return "Data Program Studi Berdasarkan Jenjang tidak ditemukan."
    fields = ['jenjang_prodi', 'jumlah_prodi']
    return _format_list_of_dicts(data, "Visualisasi Program Studi Berdasarkan Jenjang", fields)

def format_data_prodi_akreditasi(data: list) -> str:
    """Formats the study program accreditation visualization data."""
    if not data:
        return "Data Program Studi Berdasarkan Akreditasi tidak ditemukan."
    fields = ['akreditasi_prodi', 'jumlah_prodi']
    return _format_list_of_dicts(data, "Visualisasi Program Studi Berdasarkan Akreditasi", fields)

def format_data_prodi_bidang_ilmu(data: list) -> str:
    """Formats the study program field of study visualization data."""
    if not data:
        return "Data Program Studi Berdasarkan Bidang Ilmu tidak ditemukan."
    fields = ['bidang_ilmu', 'jumlah_prodi']
    return _format_list_of_dicts(data, "Visualisasi Program Studi Berdasarkan Bidang Ilmu", fields)

def format_data_prodi_kelompok_pembina(data: list) -> str:
    """Formats the study program administrative overseer group visualization data."""
    if not data:
        return "Data Program Studi Berdasarkan Kelompok Pembina tidak ditemukan."
    fields = ['kelompok_pembina', 'jumlah_prodi']
    return _format_list_of_dicts(data, "Visualisasi Program Studi Berdasarkan Kelompok Pembina", fields)

# --- Search Results Formatters (for initial search lists) ---
def format_search_results(data: list, title: str, fields: list) -> str:
    """Formats a generic list of search results."""
    if not data:
        return f"Tidak ada {title} yang ditemukan."
    
    output = [f"--- Hasil Pencarian {title} ---"]
    for i, item in enumerate(data):
        output.append(f"{i + 1}. ")
        for field in fields:
            output.append(f"  {field.replace('_', ' ').title()}: {item.get(field, 'N/A')}")
    output.append("-" * (len(title) + 20))
    return "\n".join(output)

def format_search_dosen(data: list) -> str:
    """Formats the search results for lecturers."""
    fields = ['nama', 'nidn', 'nama_pt', 'nama_prodi']
    return _format_list_of_dicts(data, "Dosen", fields)

def format_search_mahasiswa(data: list) -> str:
    """Formats the search results for students."""
    fields = ['nama', 'nim', 'nama_pt', 'nama_prodi']
    return _format_list_of_dicts(data, "Mahasiswa", fields)

def format_search_pt(data: list) -> str:
    """Formats the search results for universities."""
    fields = ['nama', 'kode', 'nama_singkat']
    return _format_list_of_dicts(data, "Perguruan Tinggi", fields)

def format_search_prodi(data: list) -> str:
    """Formats the search results for study programs."""
    fields = ['nama', 'jenjang', 'pt']
    return _format_list_of_dicts(data, "Program Studi", fields)

# --- Data Umum Formatters ---
def format_contributor_list(data: list) -> str:
    """Formats the list of contributors."""
    if not data:
        return "Daftar Kontributor tidak ditemukan."
    fields = ['name', 'role', 'universitas', 'linkedin']
    return _format_list_of_dicts(data, "Daftar Kontributor", fields)

def format_news_list(data: list) -> str:
    """Formats the list of news articles."""
    if not data:
        return "Daftar Berita tidak ditemukan."
    fields = ['title', 'date', 'url'] # Assuming 'url' field based on common news API responses
    return _format_list_of_dicts(data, "Daftar Berita", fields)

def format_bidang_ilmu_prodi(data: list) -> str:
    """Formats the list of study program fields of science."""
    if not data:
        return "Daftar Bidang Ilmu Prodi tidak ditemukan."
    fields = ['nama'] # Assuming field is 'nama' for the name of the field
    return _format_list_of_dicts(data, "Daftar Bidang Ilmu Program Studi", fields)

