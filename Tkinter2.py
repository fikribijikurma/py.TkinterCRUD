import sqlite3 # modul untuk mengelola database SQLite
import tkinter as tk
from tkinter import messagebox # membuat atau membuka database SQLite

# Membuat tabel nilai_siswa
def initialize_db():
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE nilai_siswa ( -- membuat tabel bernama 'nilai_siswa' hanya jika belum ada 
            id INTEGER PRIMARY KEY AUTOINCREMENT, -- membuat atribut ID sebagai primary key, auto increment
            nama_siswa TEXT, -- membuat atribut untuk menyimpan nama siswa
            biologi INTEGER, -- membuat atribut untuk menyimpan nilai Biologi
            fisika INTEGER, -- membuat atribut untuk menyimpan nilai Fisika
            inggris INTEGER, -- membuat atribut untuk menyimpan nilai Inggris
            prediksi_fakultas TEXT, -- membuat atribut untuk menyimpan prediksi fakultas
        )
    """)
    conn.commit() # menyimpan perubahan ke database
    conn.close()

# Fungsi untuk menyimpan data ke database
def submit_data():
    nama = entry_nama.get() # mengambil data nama siswa dari input
    try:
        biologi = int(entry_biologi.get()) # mengambil nilai biologi dari input
        fisika = int(entry_fisika.get()) # mengambil nilai fisika dari input
        inggris = int(entry_inggris.get()) # mengambil nilai inggris dari input
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai berupa angka.") # menampilkan pesan error jika input salah
        return

    # Menentukan prediksi fakultas berdasarkan nilai tertinggi
    if biologi > fisika and biologi > inggris: # jika nilai biologi paling tinggi
        prediksi = "Kedokteran"
    elif fisika > biologi and fisika > inggris: # jika nilai fisika paling tinggi
        prediksi = "Teknik"
    elif inggris > biologi and inggris > fisika: # jika nilai inggris paling tinggi
        prediksi = "Bahasa"
    else:
        prediksi = "Tidak dapat ditentukan"

    # Menyimpan data ke database
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    """, (nama, biologi, fisika, inggris, prediksi)) # masukan data ke tabel
    conn.commit() # menyimpan perubahan ke database
    conn.close()

    # tampilkan pesan sukses
    messagebox.showinfo("Sukses", f"Data telah disimpan.\nPrediksi Fakultas: {prediksi}")

    # Mengosongkan field input
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

# Inisialisasi database
initialize_db()

# Membuat GUI menggunakan Tkinter
root = tk.Tk() # membuat jendela utama aplikasi
root.title("Prediksi Fakultas Berdasarkan Nilai") # judul aplikasi

# Label dan Entry untuk nama siswa
tk.Label(root, text="Nama Siswa:").grid(row=0, column=0, padx=10, pady=5) # label untuk nama siswa
entry_nama = tk.Entry(root) # variabel untuk menyimpan input nama siswa
entry_nama.grid(row=0, column=1, padx=10, pady=5)

# Label dan Entry untuk nilai Biologi
tk.Label(root, text="Nilai Biologi:").grid(row=1, column=0, padx=10, pady=5) # label untuk nilai Biologi
entry_biologi = tk.Entry(root) # variabel untuk menyimpan input nilai Biologi
entry_biologi.grid(row=1, column=1, padx=10, pady=5) # input field untuk nilai Biologi

# Label dan Entry untuk nilai Fisika
tk.Label(root, text="Nilai Fisika:").grid(row=2, column=0, padx=10, pady=5) # label untuk nilai Fisika
entry_fisika = tk.Entry(root) # variabel untuk menyimpan input nilai Fisika
entry_fisika.grid(row=2, column=1, padx=10, pady=5) # input field untuk nilai Fisika

# Label dan Entry untuk nilai Inggris
tk.Label(root, text="Nilai Inggris:").grid(row=3, column=0, padx=10, pady=5) # label untuk nilai Inggris
entry_inggris = tk.Entry(root) # variabel untuk menyimpan input nilai Inggris
entry_inggris.grid(row=3, column=1, padx=10, pady=5) # input field untuk nilai Inggris

# Button untuk submit data
btn_submit = tk.Button(root, text="Submit Nilai", command=submit_data)
btn_submit.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan GUI
root.mainloop()
