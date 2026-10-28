# YT Music Playlist Downloader

Script Python simpel buat download seluruh lagu dari playlist YouTube atau YouTube Music langsung jadi file `.mp3` dengan kualitas 320kbps. Jadi lo gak perlu download satu-satu lagi.

## Fitur

- **Download satu playlist langsung** - Bisa download semua lagu dalam 1x run
- **Otomatis jadi MP3** - Langsung dikonversi dari audio terbaik ke format MP3 320kbps
- **Penamaan rapi** - File akan otomatis dinamain jadi `01 - Judul Lagu.mp3`, `02 - Judul Lagu.mp3`, dst.
- **Skip otomatis kalo error** - Kalo ada lagu yang dihapus/private/unavailable, script bakal lewatin aja tanpa berhenti
- **Otomatis simpan ke folder terpisah** - Hasil download bakal masuk ke folder `Unduhan_Musik/`

## Kebutuhan

Sebelum make script ini, pastiin lo udah install beberapa tools ini:

| Tools | Keterangan | Link |
| --- | --- | --- |
| **Python 3.9+** | Buat jalanin scriptnya | [python.org](https://www.python.org/downloads/) |
| **FFmpeg** | Wajib. Dipake buat konversi audio ke MP3 | [ffmpeg.org](https://ffmpeg.org/download.html) |
| **Node.js (LTS)** | Disaranin. Kadang dibutuhin `yt-dlp` biar lebih stabil, terutama buat beberapa playlist YouTube Music | [nodejs.org](https://nodejs.org/) |
| **yt-dlp** | Library utama buat downloadnya | [github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) |

## Instalasi

### 1. Download project ini
Bisa lo clone repo ini, atau tinggal copy file `yt.py` aja ke folder kosong.

### 2. Buat Virtual Environment (Opsional tapi disaranin)

Biar dependency-nya nggak bercampur sama project lain.

**Linux / macOS**

```bash
python -m venv venv
source venv/bin/activate
```

**Windows (CMD)**

```cmd
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell)**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

> Catatan: Kalo lo liat ada folder `yt/` disitu, itu kemungkinan udah venv lo. Jadi bisa lo pakai yang itu aja, atau bisa lo hapus kalo pengen bikin yang baru. Nggak wajib diupload ke repo juga sih, bisa masukin ke `.gitignore` aja.

### 3. Install dependency

Cukup install `yt-dlp` aja.

```bash
pip install yt-dlp
```

Bisa juga lo bikin file `requirements.txt` isinya:

```txt
yt-dlp
```

Terus install pake:

```bash
pip install -r requirements.txt
```

### 4. Cek FFmpeg & Node.js

Pastiin udah kebaca di `PATH`. Bisa dicek pake perintah ini di terminal lo:

```bash
ffmpeg -version
node -v
```

Kalo keluar versinya, berarti aman.

## Cara Pakai

1. Aktifin virtual environment lo
2. Jalanin scriptnya

```bash
python yt.py
```

3. Salin link playlist YouTube/YouTube Music lo terus tempel ke terminal. Contoh:

```
https://music.youtube.com/playlist?list=PLxxxxxxxxxxxxxxxxxxxx
```

4. Tunggu prosesnya sampe muncul `Selesai!`. Hasilnya bakal langsung ada di folder `Unduhan_Musik/`.

## Catatan

- **Hanya untuk penggunaan pribadi**. Perhatiin [Terms of Service YouTube](https://www.youtube.com/static?template=terms) ya.
- **Butuh koneksi internet** selama proses download.
- **Playlist publik lebih aman**. Kalo playlist private, script ini nggak bakal bisa akses.
- Kalo lo pengen ubah nama folder output, bisa langsung edit aja baris `output_folder` di `yt.py`.

## Dibuat Dengan

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Download engine
- [FFmpeg](https://ffmpeg.org/) - Konversi & processing audio
