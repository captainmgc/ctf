#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PNG Metadata Kontrol Scripti
Bu script PNG dosyalarının metadata'sını kontrol eder ve ipuçlarını gösterir.
"""

from PIL import Image
from PIL.PngImagePlugin import PngImageFile
import os

def check_png_metadata(filename):
    """PNG dosyasının metadata'sını kontrol eder"""
    try:
        with Image.open(filename) as img:
            print(f"\n📋 {filename} Metadata Bilgileri:")
            print("=" * 50)
            
            # PNG metadata'sını kontrol et
            if hasattr(img, 'info') and img.info:
                print("✅ Metadata bulundu:")
                for key, value in img.info.items():
                    print(f"  {key}: {value}")
            else:
                print("❌ Metadata bulunamadı")
            
            # Dosya boyutu
            file_size = os.path.getsize(filename)
            print(f"\n📊 Dosya Boyutu: {file_size} bytes")
            
            # Çözünürlük
            print(f"🖼️  Çözünürlük: {img.size[0]}x{img.size[1]}")
            
    except Exception as e:
        print(f"❌ Hata: {e}")

def main():
    print("🔍 PNG Metadata Kontrol Aracı")
    print("=" * 40)
    
    # Tüm PNG dosyalarını kontrol et
    png_files = ["flag1.png", "flag2.png", "challenge.png"]
    
    for filename in png_files:
        if os.path.exists(filename):
            check_png_metadata(filename)
        else:
            print(f"\n❌ {filename} dosyası bulunamadı")
    
    print("\n💡 Metadata İpucu Analizi:")
    print("1. exiftool ile metadata kontrol edilebilir")
    print("2. PNG dosyalarında gizli metin alanları olabilir")
    print("3. Metadata'da ipuçları aranmalı")
    print("4. Binary analiz ile dosya yapısı incelenmeli")

if __name__ == "__main__":
    main()
