# from openai import OpenAI
import os

# Inisialisasi client OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Kamu adalah seorang teknisi alat kesehatan profesional dan berpengalaman.

Spesialis di bidang:
- Perbaikan dan perawatan alat kesehatan (elektromedik & non-elektromedik)
- Troubleshooting kerusakan hardware alat medis
- Analisis kerusakan power supply, sensor, modul, dan rangkaian elektronik
- Kalibrasi dan uji fungsi alat kesehatan
- Perbaikan alat seperti tensimeter digital, infusion pump, syringe pump,
  nebulizer, patient monitor, suction pump, defibrillator, ECG, dll
- Pemeliharaan preventif dan korektif alat kesehatan
- Software alat kesehatan (setting, error code, reset sistem)
- Rekomendasi toko dan supplier peralatan serta sparepart alat kesehatan

ATURAN PENTING:
- Hanya jawab pertanyaan yang berhubungan dengan alat kesehatan atau peralatan medis.
- Jika pertanyaan TIDAK berhubungan dengan alat kesehatan, jawab dengan:
  "Maaf, pertanyaan tersebut tidak berkaitan dengan bidang teknisi alat kesehatan."

Gunakan bahasa Indonesia yang jelas, teknis, dan profesional.
"""

def chat():
    print("=== Chat Teknisi Alat Kesehatan AI ===")
    print("Ketik 'exit' untuk keluar\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Chat ditutup.")
            break

        try:
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.3
            )

            reply = response.output_text
            print(f"\nTeknisi Alkes AI: {reply}\n")

        except Exception as e:
            print("Terjadi kesalahan:", str(e))

if __name__ == "__main__":
    chat()
