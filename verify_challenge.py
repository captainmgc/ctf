#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Challenge Doğrulama ve Test Scripti
Bu script challenge'ın doğru çalıştığını test eder ve çözüm yolunu gösterir.
"""

def find_png_headers(filename):
    """Dosyada PNG header'larını bulur"""
    png_signature = b'\x89PNG\r\n\x1a\n'
    headers = []
    
    with open(filename, 'rb') as f:
        data = f.read()
    
    offset = 0
    while True:
        pos = data.find(png_signature, offset)
        if pos == -1:
            break
        headers.append(pos)
        offset = pos + 1
    
    return headers

def extract_second_png(filename, output_filename):
    """İkinci PNG'yi çıkarır"""
    headers = find_png_headers(filename)
    
    if len(headers) < 2:
        print("❌ İkinci PNG header'ı bulunamadı!")
        return False
    
    # İkinci PNG header'ının pozisyonu
    second_png_start = headers[1]
    
    with open(filename, 'rb') as f:
        f.seek(second_png_start)
        second_png_data = f.read()
    
    with open(output_filename, 'wb') as f:
        f.write(second_png_data)
    
    print(f"✓ İkinci PNG {output_filename} olarak çıkarıldı")
    return True

def main():
    print("🔍 CTF Challenge Doğrulama")
    print("=" * 40)
    
    # PNG header'larını bul
    headers = find_png_headers("challenge.png")
    
    print(f"📊 challenge.png dosyasında {len(headers)} PNG header'ı bulundu:")
    for i, pos in enumerate(headers):
        print(f"  Header {i+1}: Offset {pos} (0x{pos:08X})")
    
    if len(headers) >= 2:
        print("\n✅ Challenge başarılı! İkinci PNG gizlenmiş.")
        
        # İkinci PNG'yi çıkar
        if extract_second_png("challenge.png", "extracted_flag.png"):
            print("\n🎯 Çözüm başarılı! Flag dosyası çıkarıldı.")
    else:
        print("\n❌ Challenge başarısız! İkinci PNG bulunamadı.")
    
    print("\n📋 Challenge Özeti:")
    print("- İlk görsel: 'hack' yazısı")
    print("- Gizli görsel: 'hacksafe{0V3RTH1NK_V4KTI}' yazısı")
    print("- Çözüm: Hex analiz ile ikinci PNG'yi çıkar")
    
    print("\n🛠️  Çözüm Komutları:")
    print("1. Hex Editör ile:")
    print("   - challenge.png dosyasını hex editörde aç")
    print("   - İkinci PNG header'ını bul: 89 50 4E 47 0D 0A 1A 0A")
    print("   - O pozisyondan itibaren yeni dosya oluştur")
    
    print("\n2. Binwalk ile:")
    print("   binwalk -e challenge.png")
    
    print("\n3. dd komutu ile:")
    print("   dd if=challenge.png of=extracted.png bs=1 skip=<offset>")
    
    print("\n4. Python ile:")
    print("   python verify_challenge.py")

if __name__ == "__main__":
    main() 