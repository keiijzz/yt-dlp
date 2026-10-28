import os
from yt_dlp import YoutubeDL


def download_yt_music_playlist(playlist_url, output_folder="Unduhan_Musik"):
    # Membuat folder tujuan jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Konfigurasi yt-dlp untuk download audio kualitas terbaik & konversi ke MP3
    ydl_opts = {
        "format": "bestaudio/best",  # Ambil kualitas audio terbaik
        "outtmpl": os.path.join(
            output_folder, "%(playlist_index)s - %(title)s.%(ext)s"
        ),  # Format nama file: No urut - Judul Lagu
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",  # Konversi otomatis ke MP3
                "preferredquality": "320",  # Kualitas audio tertinggi (320kbps)
            },
            {
                "key": "FFmpegEmbedSubtitle",  # Opsional: Jika ada lirik/sub
            },
        ],
        "ignoreerrors": True,  # Lewati jika ada satu lagu yang error/dihapus agar playlist tetap jalan
        "yesplaylist": True,  # Memastikan seluruh playlist terunduh
    }

    print("🎵 Memulai proses analisis playlist... Mohon tunggu.")

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    print(
        f"\n✅ Selesai! Semua lagu berhasil disimpan di folder: '{output_folder}'"
    )


if __name__ == "__main__":
    # Masukkan link playlist YouTube Music Anda di bawah ini
    # Contoh: 'https://youtube.com'
    LINK_PLAYLIST = input("Masukkan URL Playlist YouTube Music: ")

    # Jalankan fungsi download
    download_yt_music_playlist(LINK_PLAYLIST)
