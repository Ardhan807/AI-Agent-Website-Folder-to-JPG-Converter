# 🧠 AI Agent — Website Folder to JPG Converter
## 📘 Deskripsi Proyek
AI Agent berbasis OpenRouter yang mampu membaca satu folder berisi file HTML, CSS, dan JS lalu mengonversinya menjadi gambar JPG secara otomatis. Agent juga bisa menjawab pertanyaan pengguna secara interaktif (chat-style) bila tidak ada perintah konversi.
## 🚀 Cara Menjalankan Proyek
- Clone repo
  ```
  git clone https://github.com/Ardhan807/AI-Agent-Website-Folder-to-JPG-Converter.git
  cd AI-Agent-Website-Folder-to-JPG-Converter
  ```
- Istall dependencies
  ```
  pip install -r requirements.txt
  ```
- Tambahkan API KEY, Buat file .env dengan isi:
  ```
  OPENROUTER_API_KEY=masukkan_api_key_kamu_disini
  ```
- Tambahkan folder website ke folder input dengan format sebagai berikut:
  ```
  input/
  └── folder-website/
    ├── index.html
    ├── style.css
    ├── halaman1.html
    └── ...
  ```
- Jalankan program
  ```
  python main.py
  ```
## 🧩 Struktur Proyek
```
📁 ai-agent-Website-Folder-to-JPG-Converter
│
├─ 📁 input/                    → folder untuk memasukkan folder website
│   └─ (tempat folder website kamu)
│
├─ 📁 output/                   → penyimpanan file JPG hasil konversi
│
├─ .env                         → berisi OPENROUTER_API_KEY
├─ main.py                      → program utama dengan terminal interactive
├─ agent.py                     → fungsi ask_ai (menghubungkan ke OpenRouter)           
├─ tools.py                     → fungsi konversi HTML ke JPG
├─ requirements.txt
├─ README.md.
```
## ⚠ Catatan Penting
- Scraping Tokopedia bisa berubah karena perubahan struktur HTML.
- File hasil konversi JPG akan tersimpan otomatis di folder output/.
- Wajib mengisi file .env sebelum menjalankan program.
- Koneksi internet diperlukan.
