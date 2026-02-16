import argparse
import os
import sys
import warnings

# Filter warning agar output lebih bersih
warnings.filterwarnings("ignore")

try:
    import whisper
except ImportError:
    print("Error: Pustaka 'openai-whisper' belum terinstall.")
    print("Silakan install dengan menjalankan: pip install openai-whisper")
    sys.exit(1)

def transcribe_video(video_path, model_size="small", language=None):
    """
    Mentranskrip video ke teks menggunakan OpenAI Whisper.
    """
    if not os.path.exists(video_path):
        print(f"Error: File '{video_path}' tidak ditemukan.")
        return

    print(f"--- Memulai Transkripsi ---")
    print(f"File: {video_path}")
    print(f"Model: {model_size}")
    
    if language:
        print(f"Bahasa dipaksa ke: {language}")
    else:
        print("Bahasa: Auto-detect (Akan mendeteksi bahasa dominan)")

    print("Sedang memuat model (ini mungkin memakan waktu)...")
    
    try:
        # Load model
        model = whisper.load_model(model_size)
        
        print("Sedang memproses transkripsi...")
        
        # Opsi transkripsi
        # fp16=False digunakan agar kompatibel dengan CPU jika tidak ada GPU
        options = {"fp16": False} 
        if language:
            options["language"] = language

        result = model.transcribe(video_path, **options)
        
        transcribed_text = result["text"]
        
        # Simpan hasil ke file .txt
        base_name = os.path.splitext(video_path)[0]
        output_file = f"{base_name}_transcript.txt"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcribed_text)
            
        print("\n--- Transkripsi Selesai ---")
        print(f"Hasil disimpan di: {output_file}")
        
        # Tampilkan sedikit preview
        print("\nPreview (100 karakter pertama):")
        print(transcribed_text[:100] + "...")

    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script Transkripsi Video (MP4) ke Teks")
    parser.add_argument("video_path", help="Path ke file video mp4")
    parser.add_argument("--model", default="small", choices=["tiny", "base", "small", "medium", "large"], 
                        help="Ukuran model. 'small' cepat, 'large' paling akurat (bagus untuk logat daerah).")
    parser.add_argument("--lang", help="Kode bahasa (contoh: 'id' untuk Indonesia). Kosongkan untuk auto-detect.")

    args = parser.parse_args()
    
    transcribe_video(args.video_path, args.model, args.lang)
