#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CTF Steganografi Challenge - PNG içinde gizli PNG
Bu script iki PNG dosyası oluşturur ve ikincisini birincisinin içine gömer.
"""

from PIL import Image, ImageDraw, ImageFont
import os
from PIL.PngImagePlugin import PngInfo

def create_png_with_text(text, filename, size=(1920, 1080), bg_color='white', text_color='black'):
    """Belirtilen metni içeren HD PNG dosyası oluşturur"""
    # Yeni HD görsel oluştur
    img = Image.new('RGB', size, (255, 255, 255))  # Başlangıçta beyaz
    draw = ImageDraw.Draw(img)
    
    # Gradient arka plan oluştur
    if bg_color == 'white':
        # Beyazdan griye gradient
        for y in range(size[1]):
            r = int(255 - (y / size[1]) * 30)
            g = int(255 - (y / size[1]) * 30)
            b = int(255 - (y / size[1]) * 30)
            for x in range(size[0]):
                img.putpixel((x, y), (r, g, b))
    else:
        # Koyu arka plan için gradient
        for y in range(size[1]):
            r = int(20 + (y / size[1]) * 40)
            g = int(20 + (y / size[1]) * 40)
            b = int(40 + (y / size[1]) * 60)
            for x in range(size[0]):
                img.putpixel((x, y), (r, g, b))
    
    # Font ayarları - daha büyük ve kaliteli font
    try:
        # Windows'ta büyük font
        font_size = min(size[0] // 15, size[1] // 8)
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback font
        font = ImageFont.load_default()
    
    # Metni ortala
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Gölge efekti ekle
    shadow_offset = 3
    draw.text((x + shadow_offset, y + shadow_offset), text, fill='gray', font=font)
    
    # Ana metni çiz
    draw.text((x, y), text, fill=text_color, font=font)
    
    # PNG olarak yüksek kalitede kaydet
    img.save(filename, 'PNG', optimize=True, quality=95)
    print(f"✓ {filename} oluşturuldu (HD: {size[0]}x{size[1]})")

def create_png_with_metadata(text, filename, size=(1920, 1080), bg_color='white', text_color='black', metadata_hint=""):
    """Belirtilen metni içeren HD PNG dosyası oluşturur ve metadata'ya ipucu ekler"""
    # Yeni HD görsel oluştur
    img = Image.new('RGB', size, (255, 255, 255))  # Başlangıçta beyaz
    draw = ImageDraw.Draw(img)
    
    # Gradient arka plan oluştur
    if bg_color == 'white':
        # Beyazdan griye gradient
        for y in range(size[1]):
            r = int(255 - (y / size[1]) * 30)
            g = int(255 - (y / size[1]) * 30)
            b = int(255 - (y / size[1]) * 30)
            for x in range(size[0]):
                img.putpixel((x, y), (r, g, b))
    else:
        # Koyu arka plan için gradient
        for y in range(size[1]):
            r = int(20 + (y / size[1]) * 40)
            g = int(20 + (y / size[1]) * 40)
            b = int(40 + (y / size[1]) * 60)
            for x in range(size[0]):
                img.putpixel((x, y), (r, g, b))
    
    # Font ayarları - daha büyük ve kaliteli font
    try:
        # Windows'ta büyük font
        font_size = min(size[0] // 15, size[1] // 8)
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback font
        font = ImageFont.load_default()
    
    # Metni ortala
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Gölge efekti ekle
    shadow_offset = 3
    draw.text((x + shadow_offset, y + shadow_offset), text, fill='gray', font=font)
    
    # Ana metni çiz
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Metadata'ya ipucu ekle
    metadata = PngInfo()
    metadata.add_text("Author", "Hacksafe Overthink Ekibi")
    metadata.add_text("Description", "Dosya yapısının derinliklerine bakın...")
    metadata.add_text("Hint", metadata_hint)
    metadata.add_text("Keywords", "steganografi, gizli, png, binary")
    
    # PNG olarak yüksek kalitede kaydet (metadata ile)
    img.save(filename, 'PNG', pnginfo=metadata, optimize=True, quality=95)
    print(f"✓ {filename} oluşturuldu (HD: {size[0]}x{size[1]}) - Metadata ipucu eklendi")

def embed_png_in_png(host_file, secret_file, output_file):
    """İkinci PNG dosyasını ilk PNG dosyasının sonuna ekler"""
    
    # Dosyaları oku
    with open(host_file, 'rb') as f:
        host_data = f.read()
    
    with open(secret_file, 'rb') as f:
        secret_data = f.read()
    
    # İkinci PNG'yi ilk PNG'nin sonuna ekle
    combined_data = host_data + secret_data
    
    # Birleştirilmiş dosyayı kaydet
    with open(output_file, 'wb') as f:
        f.write(combined_data)
    
    print(f"✓ {output_file} oluşturuldu (içinde gizli PNG var)")

def main():
    print("🔐 CTF Steganografi Challenge - PNG içinde gizli PNG")
    print("=" * 50)
    
    # İlk PNG: "hack" yazısı (açık arka plan) - metadata ipucu ile
    create_png_with_metadata("hack", "flag1.png", size=(1920, 1080), bg_color='white', text_color='black', 
                            metadata_hint="Gördüğünüzden daha fazlası var. Birden fazla dosya imzası arayın!")
    
    # İkinci PNG: "hacksafe{0V3RTH1NK_V4KTI}" yazısı (koyu arka plan)
    create_png_with_text("hacksafe{0V3RTH1NK_V4KTI}", "flag2.png", size=(1920, 1080), bg_color='dark', text_color='white')
    
    # İkinci PNG'yi ilk PNG'nin içine gömer
    embed_png_in_png("flag1.png", "flag2.png", "challenge.png")
    
    print("\n📁 Oluşturulan dosyalar:")
    print("- flag1.png: İlk görsel (hack)")
    print("- flag2.png: Gizli görsel (hacksafe{0V3RTH1NK_V4KTI})")
    print("- challenge.png: Challenge dosyası")
    
    print("\n🔍 Challenge Çözüm Yolu:")
    print("1. challenge.png dosyasını normal görüntüleyici ile aç")
    print("2. Sadece 'hack' yazısını göreceksin")
    print("3. Dosyayı hex editör ile aç (HxD, 010 Editor, vs.)")
    print("4. Dosyanın sonunda ikinci PNG header'ını ara: 89 50 4E 47 0D 0A 1A 0A")
    print("5. İkinci PNG header'ından itibaren yeni bir dosya oluştur")
    print("6. Bu dosyayı PNG olarak aç ve flag'i gör")
    
    print("\n💡 Alternatif çözüm yöntemleri:")
    print("- binwalk -e challenge.png")
    print("- dd if=challenge.png of=extracted.png bs=1 skip=<offset>")
    print("- Python ile dosyayı okuyup PNG header'larını bul")

if __name__ == "__main__":
    main() 