import tkinter as tk
from tkinter import Toplevel, messagebox
import customtkinter as ctk


# Inisialisasi CustomTkinter
ctk.set_appearance_mode("light")  # Default: light mode
ctk.set_default_color_theme("blue")

# Variabel Global
total_harga = [0]
pesanan = []

# Konfigurasi jendela utama
lebar, tinggi = 600, 500
window = ctk.CTk()
window.title("Rumah Makan Cinto Bundo!")
window.geometry(f"{lebar}x{tinggi}")
screenwidth, screenheight = window.winfo_screenwidth(), window.winfo_screenheight()
newx, newy = (screenwidth - lebar) // 2, (screenheight - tinggi) // 2
window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")
window.resizable(False, False)

# Header
opening = ctk.CTkLabel(window, text="Selamat Datang di Rumah Makan Cinto Bundo!", font=("Courier New", 20))
opening.pack(pady=10)

label_total_harga = ctk.CTkLabel(window, text=f"Total Harga: Rp{total_harga[0]}", font=("Times New Roman", 16), text_color="#FF6633")
label_total_harga.pack(pady=10)

# Fungsi untuk memperbarui total harga
def update_total_harga():
    label_total_harga.configure(text=f"Total Harga: Rp{total_harga[0]}")

# Fungsi untuk toggle dark mode
def toggle_mode():
    current_mode = ctk.get_appearance_mode()
    new_mode = "dark" if current_mode == "light" else "light"
    ctk.set_appearance_mode(new_mode)
    window.update() 

# Fungsi pembuatan tombol menu
def create_menu_button(parent, text, command):
    return ctk.CTkButton(
        parent,
        text=text,
        font=("Times New Roman", 14),
        corner_radius=10,
        fg_color="#3E5F8A",
        hover_color="#28527A",
        command=command
    )

# Fungsi untuk menangani menu makanan
def window_Menu_Makanan():
    Menu_Makanan = {
        "Ayam Goreng": 8000, "Ayam Bakar": 8000, "Ayam Gulai": 12000,
        "Ayam Pop": 15000, "Dendeng Balado": 20000, "Gulai Ikan": 12000,
        "Rendang": 25000, "Ikan Bakar": 20000, "Pindang": 15000, "Sup Ayam": 10000
    }
    window_makanan = ctk.CTkToplevel(window)
    window_makanan.title("Menu Makanan")
    window_makanan.geometry("300x400")

    # Frame Scrollable
    scrollable_frame = ctk.CTkScrollableFrame(window_makanan, width=400, height=300)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    ctk.CTkLabel(
        scrollable_frame,
        text="Daftar Menu Makanan",
        font=("Courier New", 16)
    ).pack(pady=10)

    # Fungsi untuk menambah pesanan
    def tambah_pesanan_makanan(menu, harga):
        total_harga[0] += harga
        pesanan.append(f"{menu} - Rp{harga}")
        update_total_harga()

    # Tambahkan menu makanan ke dalam scrollable frame
    for makanan, harga in Menu_Makanan.items():
        ctk.CTkButton(
            scrollable_frame,
            text=f"{makanan} - Rp{harga}",
            command=lambda m=makanan, h=harga: tambah_pesanan_makanan(m, h),
            font=("Times New Roman", 14),
            corner_radius=10,
            fg_color="#3E5F8A",
            hover_color="#28527A"
        ).pack(pady=5, padx=10)

# Fungsi untuk menangani menu minuman
def window_Menu_Minuman():
    Menu_Minuman = {
        "Es Teh Manis": 2500, "Es Teh Tawar": 2500, "Kopi Hitam": 3000, "Kopi Susu": 5000,
        "Es Jeruk": 8000, "Es Tebu": 10000, "Jus Alpukat": 12000, "Jus Jeruk": 10000,
        "Jus Mangga": 12000, "Jus Nanas": 12000, "Es Kelapa": 10000, "Air Mineral": 5000
    }
    window_minuman = ctk.CTkToplevel(window)
    window_minuman.title("Menu Minuman")
    window_minuman.geometry("300x400")

    # Frame Scrollable
    scrollable_frame = ctk.CTkScrollableFrame(window_minuman, width=400, height=300)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    ctk.CTkLabel(
        scrollable_frame,
        text="Daftar Menu Minuman",
        font=("Courier New", 16)
    ).pack(pady=10)

    # Fungsi untuk menambah pesanan
    def tambah_pesanan_minuman(menu, harga):
        total_harga[0] += harga
        pesanan.append(f"{menu} - Rp{harga}")
        update_total_harga()

    # Tambahkan menu minuman ke dalam scrollable frame
    for minuman, harga in Menu_Minuman.items():
        ctk.CTkButton(
            scrollable_frame,
            text=f"{minuman} - Rp{harga}",
            command=lambda m=minuman, h=harga: tambah_pesanan_minuman(m, h),
            font=("Times New Roman", 14),
            corner_radius=10,
            fg_color="#3E5F8A",
            hover_color="#28527A"
        ).pack(pady=5, padx=10)

# Function to handle Menu Tambahan
def Window_Menu_Tambahan():
    Menu_Tambahan = {
        "Daun Singkong": 1500, "Sambal Merah": 1500, "Sambal Hijau": 2000,
        "Serundeng": 2000, "Kuah Rendang": 2500, "Kerupuk": 1000,
        "Perkedel Kentang": 3000, "Telur Dadar": 5000, "Tempe Goreng": 2000,
        "Tahu Goreng": 2000, "Sayur Asem": 4000, "Lalapan": 1500
    }
    window_tambahan = ctk.CTkToplevel(window)
    window_tambahan.title("Menu Tambahan")
    window_tambahan.geometry("300x400")

    # Mengatur dark mode untuk jendela tambahan
    ctk.set_appearance_mode(ctk.get_appearance_mode())

    def tambah_pesanan_tambahan(menu, harga):
        total_harga[0] += harga
        pesanan.append(f"{menu} - Rp{harga}")
        update_total_harga()

    # Scrollable frame untuk daftar menu tambahan
    scrollable_frame = ctk.CTkScrollableFrame(window_tambahan, width=400, height=300)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Label judul
    ctk.CTkLabel(
        scrollable_frame,
        text="Daftar Menu Tambahan",
        font=("Courier New", 16)
    ).pack(pady=10)

    # Tambahkan setiap item ke dalam scrollable frame
    for tambahan, harga in Menu_Tambahan.items():
        ctk.CTkButton(
            scrollable_frame,
            text=f"{tambahan} - Rp{harga}",
            command=lambda m=tambahan, h=harga: tambah_pesanan_tambahan(m, h),
            font=("Times New Roman", 14),
            corner_radius=10,
            fg_color="#3E5F8A",
            hover_color="#28527A"
        ).pack(pady=5, padx=10)


# Fungsi untuk rincian pemesanan
def window_Rincian_Pemesanan():
    window_rincian = ctk.CTkToplevel(window)
    window_rincian.title("Rincian Pemesanan")
    window_rincian.geometry("300x400")

    ctk.CTkLabel(
        window_rincian,
        text="Rincian Pemesanan",
        font=("Courier New", 16),
    ).pack(pady=10)

    # Frame Scrollable
    scrollable_frame = ctk.CTkScrollableFrame(window_rincian, width=400, height=300)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Tampilkan daftar pesanan
    if pesanan:
        for item in pesanan:
            ctk.CTkLabel(
                scrollable_frame,
                text=item,
                font=("Times New Roman", 14),
            ).pack(anchor="w", pady=2, padx=10)
    else:
        ctk.CTkLabel(
            scrollable_frame,
            text="Belum ada pesanan",
            font=("Times New Roman", 14),
            text_color="gray"
        ).pack(pady=10)


def nama_pelanggan():
    teks = Nama.get()
    if teks.strip():  # Pastikan tidak kosong
        label_hasil.configure(text=f"Nama disimpan: {teks}", text_color="#3E5F8A")
    else:
        messagebox.showwarning(title="Peringatan", message="Mohon maaf, silahkan isi Nama Anda terlebih dahulu")

# Fungsi untuk reset pesanan
def reset_pesanan():
    total_harga[0] = 0
    pesanan.clear()
    update_total_harga()
    messagebox.showinfo("Reset", "Semua pesanan dan total harga telah dihapus!")

def window_Pembayaran():
    window_pembayaran = ctk.CTkToplevel(window)
    window_pembayaran.title("Pembayaran")
    window_pembayaran.geometry("400x400")

    # Scrollable frame untuk semua elemen pembayaran
    scrollable_frame = ctk.CTkScrollableFrame(window_pembayaran, width=400, height=400)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Label untuk judul pembayaran
    ctk.CTkLabel(
        scrollable_frame,
        text="Pembayaran",
        font=("Courier New", 16),
    ).pack(pady=10)

    # Tampilkan total harga
    ctk.CTkLabel(
        scrollable_frame,
        text=f"Total Harga: Rp{total_harga[0]}",
        font=("Times New Roman", 14),
        text_color="#FF6633"
    ).pack(pady=5)

    # Pilihan metode pembayaran
    ctk.CTkLabel(
        scrollable_frame,
        text="Pilih Metode Pembayaran:",
        font=("Times New Roman", 14),
        text_color="#3E5F8A"
    ).pack(pady=10)

    # Variabel untuk menyimpan pilihan metode pembayaran
    metode_pembayaran = tk.StringVar(value="")

    # Variabel untuk menyimpan bank yang dipilih
    bank_pilihan = tk.StringVar(value="Pilih Bank")

    # Dictionary untuk nomor rekening berdasarkan bank
    nomor_rekening = {
        "BCA": "6274439156",
        "Mandiri": "008-8044510590",
        "BNI": "2220790486",
        "BRI": "002-123456789012",
        "CIMB": "022-123456789012"
    }

    # Frame untuk input tunai
    frame_tunai = ctk.CTkFrame(scrollable_frame)

    ctk.CTkLabel(
        frame_tunai,
        text="Masukkan jumlah uang:",
        font=("Times New Roman", 14)
    ).pack(anchor="w", padx=10, pady=5)

    entry_uang = ctk.CTkEntry(frame_tunai, placeholder_text="Masukkan uang tunai")
    entry_uang.pack(pady=5, padx=10)

    # Frame untuk dropdown bank
    frame_bank = ctk.CTkFrame(scrollable_frame)
    ctk.CTkLabel(
        frame_bank,
        text="Pilih Bank:",
        font=("Times New Roman", 14)
    ).pack(anchor="w", padx=10, pady=5)

    # Dropdown untuk memilih bank
    dropdown_bank = ctk.CTkOptionMenu(
        frame_bank,
        variable=bank_pilihan,
        values=list(nomor_rekening.keys()),
        command=lambda _: label_rekening.configure(
            text=f"Nomor Rekening: {nomor_rekening.get(bank_pilihan.get(), 'Pilih bank')}"
        )
    )
    dropdown_bank.pack(pady=5)

    # Label untuk menampilkan nomor rekening
    label_rekening = ctk.CTkLabel(
        frame_bank,
        text="Pilih bank untuk melihat nomor rekening",
        font=("Times New Roman", 14)
    )
    label_rekening.pack(pady=5)

    # Fungsi untuk memperbarui tampilan metode pembayaran
    def update_metode_pembayaran():
        if metode_pembayaran.get() == "Transfer Bank":
            frame_bank.pack(pady=10, padx=10, before=tombol_bayar)
            frame_tunai.pack_forget()
        elif metode_pembayaran.get() == "Tunai":
            frame_tunai.pack(pady=10, padx=10, before=tombol_bayar)
            frame_bank.pack_forget()
        else:
            frame_bank.pack_forget()
            frame_tunai.pack_forget()

    # Tombol Radio untuk metode pembayaran
    metode_list = [("Tunai", "Tunai"), ("Kartu Kredit", "Kartu Kredit"),
                   ("Transfer Bank", "Transfer Bank"), ("E-Wallet", "E-Wallet")]

    for text, value in metode_list:
        ctk.CTkRadioButton(
            scrollable_frame,
            text=text,
            value=value,
            variable=metode_pembayaran,
            font=("Times New Roman", 14),
            command=update_metode_pembayaran
        ).pack(anchor="w", padx=20, pady=5)

    # Tombol proses pembayaran
    tombol_bayar = ctk.CTkButton(
        scrollable_frame,
        text="Proses Pembayaran",
        font=("Times New Roman", 14),
        fg_color="#3E5F8A",
        hover_color="#28527A",
        command=lambda: proses_pembayaran(metode_pembayaran.get(), bank_pilihan.get(), entry_uang.get())
    )
    tombol_bayar.pack(pady=20)

    # Fungsi untuk memproses pembayaran
    def proses_pembayaran(metode, bank, jumlah_uang):
        if not metode:
            messagebox.showerror("Metode Pembayaran", "Silakan pilih metode pembayaran!")
            return

        if metode == "Transfer Bank":
            if bank == "Pilih Bank":
                messagebox.showerror("Pilih Bank", "Silakan pilih bank untuk transfer!")
                return
            nomor = nomor_rekening.get(bank, "Tidak ada nomor rekening")
            messagebox.showinfo("Pembayaran Berhasil", f"Silakan transfer ke rekening:\n{nomor}\nAtas Nama RM Cinto Bundo.")
            window_pembayaran.destroy()
            window_Penilaian()
        elif metode == "Tunai":
            try:
                uang = int(jumlah_uang)
                if uang >= total_harga[0]:
                    kembalian = uang - total_harga[0]
                    messagebox.showinfo("Pembayaran Berhasil", f"Pembayaran Tunai berhasil!\nKembalian: Rp{kembalian}")
                    window_pembayaran.destroy()
                    window_Penilaian()
                else:
                    messagebox.showerror("Uang Tidak Cukup", "Jumlah uang yang dimasukkan tidak mencukupi!")
            except ValueError:
                messagebox.showerror("Input Tidak Valid", "Masukkan jumlah uang dalam angka!")
        elif metode == "Kartu Kredit":
            messagebox.showinfo("Pembayaran Berhasil", "Pembayaran menggunakan Kartu Kredit berhasil!")
            window_pembayaran.destroy()
            window_Penilaian()
        elif metode == "E-Wallet":
            messagebox.showinfo("Pembayaran Berhasil", "Silakan lanjutkan pembayaran melalui aplikasi E-Wallet.")
            window_pembayaran.destroy()
            window_Penilaian()
        else:
            messagebox.showerror("Metode Pembayaran", "Metode pembayaran tidak valid.")

def window_Penilaian():
    # Membuka jendela penilaian setelah pembayaran
    window_penilaian = ctk.CTkToplevel(window)
    window_penilaian.title("Penilaian dan Kritik")
    window_penilaian.geometry("300x400")

    ctk.CTkLabel(
        window_penilaian,
        text="Berikan Penilaian Anda",
        font=("Courier New", 16)
    ).pack(pady=10)

    # Frame Scrollable
    scrollable_frame = ctk.CTkScrollableFrame(window_penilaian, width=400, height=300)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    rating = tk.IntVar(value=1)  # Default rating adalah 1

    # Menambahkan label dan tombol radio untuk rating dengan scroll
    ctk.CTkLabel(
        scrollable_frame,
        text="Berikan Rating:",
        font=("Times New Roman", 14)
    ).pack(pady=5)

    for i in range(1, 6):  # Menambahkan 5 pilihan rating
        ctk.CTkRadioButton(
            scrollable_frame,
            text=str(i),
            value=i,
            variable=rating,
            font=("Times New Roman", 14)
        ).pack(side="top", pady=5)

    # Menambahkan ruang kosong untuk memisahkan bagian rating dan kritik/saran
    ctk.CTkLabel(scrollable_frame, text=" ").pack(pady=5)

    # Kritik dan Saran
    ctk.CTkLabel(
        scrollable_frame,
        text="Kritik dan Saran:",
        font=("Times New Roman", 14)
    ).pack(pady=5)

    kritik_saran = ctk.CTkTextbox(
        scrollable_frame,
        font=("Times New Roman", 14),
        width=350,
        height=100
    )
    kritik_saran.pack(pady=10, padx=20)  # Menambahkan padding horizontal untuk memusatkan kotak input

    # Menambahkan ruang kosong untuk memisahkan kotak input dan tombol kirim
    ctk.CTkLabel(scrollable_frame, text=" ").pack(pady=5)

    # Tombol Kirim Penilaian
    def kirim_penilaian():
        rating_value = rating.get()
        kritik_value = kritik_saran.get("1.0", tk.END).strip() # mengambil teks dari awal sampai akhir

        if kritik_value == "":
            messagebox.showwarning("Kritik dan Saran", "Mohon isi kritik dan saran Anda!")
            return

        messagebox.showinfo("Terima Kasih", f"Terima kasih atas penilaian Anda!\nRating: {rating_value}\nKritik: {kritik_value}")
        window_penilaian.destroy()

    tombol_kirim = ctk.CTkButton(
        scrollable_frame,
        text="Kirim Penilaian",
        font=("Times New Roman", 14),
        command=kirim_penilaian,
        width=150
    )
    tombol_kirim.pack(pady=20)  # Menambahkan padding horizontal untuk memusatkan tombol

# Nama Pelanggan
Nama = tk.StringVar()
entry_nama = ctk.CTkEntry(window, textvariable=Nama, placeholder_text="Masukkan Nama Anda", font=("Times New Roman", 14))
entry_nama.pack(pady=10)

# button simpan nama
btn_simpan_nama = ctk.CTkButton(
    window,
    text="Simpan Nama",
    font=("Times New Roman", 14),
    fg_color="#3E5F8A",
    hover_color="#28527A",
    command=nama_pelanggan
)
btn_simpan_nama.pack(pady=5)

# Label hasil nama disimpan
label_hasil = ctk.CTkLabel(window, text="Nama disimpan: ", font=("Times New Roman", 14), text_color="#3E5F8A")
label_hasil.pack(pady=5)

# Tombol Menu
frame_buttons = ctk.CTkFrame(window)
frame_buttons.pack(pady=20)

create_menu_button(frame_buttons, "Menu Makanan", window_Menu_Makanan).grid(row=0, column=0, padx=10, pady=10)
create_menu_button(frame_buttons, "Menu Minuman", window_Menu_Minuman).grid(row=0, column=1, padx=10, pady=10)
create_menu_button(frame_buttons, "Menu Tambahan", Window_Menu_Tambahan).grid(row=1, column=0, padx=10, pady=10)
create_menu_button(frame_buttons, "Rincian Pemesanan", window_Rincian_Pemesanan).grid(row=1, column=1, padx=10, pady=10)
create_menu_button(frame_buttons, "Pembayaran", window_Pembayaran).grid(row=2, column=0, padx=10, pady=10)
create_menu_button(frame_buttons, "Reset Pesanan", reset_pesanan).grid(row=2, column=1, padx=10, pady=10)

# Fungsi untuk toggle dark mode dengan switch
def toggle_mode_switch():
    if switch_mode.get() == 1:  # Jika switch aktif (1), gunakan dark mode
        ctk.set_appearance_mode("dark")
    else:  # Jika switch mati (0), gunakan light mode
        ctk.set_appearance_mode("light")

# Tambahkan CTkSwitch untuk toggle mode
switch_mode = ctk.CTkSwitch(
    window,
    text="Dark Mode",
    font=("Times New Roman", 14),
    command=toggle_mode_switch
)
switch_mode.pack(pady=15)


# Exit confirmation
def on_closing():
    if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

# Jalankan GUI
window.mainloop()
