# 🔐 CTF Steganografi Challenge: PNG içinde gizli PNG

Bu challenge, steganografi kategorisinde PNG dosyası içerisine gizlenmiş ikinci bir PNG görüntüsünü bulmayı amaçlar.

## 📁 Dosyalar

- `flag1.png` - İlk görsel (sadece "hack" yazısı)
- `flag2.png` - Gizli görsel (sadece "hacksafe{0V3RTH1NK_V4KTI}" yazısı)
- `challenge.png` - **Challenge dosyası** (içinde gizli PNG var)
- `create_stego_challenge.py` - Challenge oluşturma scripti
- `verify_challenge.py` - Challenge doğrulama scripti

## 🎯 Challenge Açıklaması

`challenge.png` dosyasını normal bir görüntüleyici ile açtığınızda sadece "hack" yazısını göreceksiniz. Ancak dosyanın içinde ikinci bir PNG dosyası gizlenmiştir. Bu gizli PNG dosyası "hacksafe{0V3RTH1NK_V4KTI}" yazısını içerir.

## 🔍 Çözüm Yolu

### 1. Hex Editör ile Çözüm
1. `challenge.png` dosyasını hex editör ile açın (HxD, 010 Editor, Hex Fiend, vs.)
2. Dosyada ikinci PNG header'ını arayın: `89 50 4E 47 0D 0A 1A 0A`
3. İkinci PNG header'ının bulunduğu pozisyondan itibaren yeni bir dosya oluşturun
4. Bu dosyayı PNG olarak açın ve flag'i görün

### 2. Binwalk ile Çözüm
```bash
binwalk -e challenge.png
```

### 3. dd Komutu ile Çözüm
```bash
dd if=challenge.png of=extracted.png bs=1 skip=18153
```

### 4. Python ile Çözüm
```bash
python verify_challenge.py
```

### 5. Metadata Analizi ile İpucu
```bash
python check_metadata.py
# veya
exiftool challenge.png
```

## 🛠️ Teknik Detaylar

- **İlk PNG Header**: Offset 0 (0x00000000)
- **İkinci PNG Header**: Offset 18153 (0x000046E9)
- **Gizleme Yöntemi**: İkinci PNG dosyası ilk PNG dosyasının sonuna eklenmiştir
- **Flag Formatı**: `hacksafe{0V3RTH1NK_V4KTI}`

## 🚫 Çalışmayan Yöntemler

Bu challenge'da aşağıdaki yöntemler işe yaramayacaktır:
- `steghide` - LSB steganografi kullanılmamış
- `strings` - Düz metin arama yeterli değil
- `file` - Sadece ilk dosya formatını gösterir

**Not**: `exiftool` artık metadata'da ipucu gösterecektir!

## 📋 Challenge Gereksinimleri

✅ İki ayrı PNG dosyası oluşturuldu  
✅ İkinci PNG ilk PNG'nin içine gömüldü  
✅ Normal görüntüleyici sadece ilk görseli gösteriyor  
✅ Hex analiz ile ikinci PNG bulunabilir  
✅ Flag formatı doğru: `hacksafe{0V3RTH1NK_V4KTI}`  
✅ Tüm dosyalar sorunsuz açılıyor
✅ HD kalitede resimler (1920x1080)
✅ Güzel gradient arka planlar
✅ Metadata'da ipucu eklendi  

## 🎮 Challenge Kurulumu

Challenge'ı yeniden oluşturmak için:

```bash
python create_stego_challenge.py
```

Challenge'ı test etmek için:

```bash
python verify_challenge.py
```

Metadata'yı kontrol etmek için:

```bash
python check_metadata.py
```

## 🔧 Geliştirici Notları

Bu challenge, dosya formatları ve binary analiz konularını test eder. Katılımcılar:
- PNG dosya formatını anlamalı
- Hex editör kullanabilmeli
- Binary dosya analizi yapabilmeli
- Dosya birleştirme tekniklerini bilmeli

## 📊 Zorluk Seviyesi

- **Kategori**: Steganografi
- **Zorluk**: Orta
- **Gerekli Araçlar**: Hex Editör, Binwalk (opsiyonel)
- **Tahmini Süre**: 10-30 dakika
- **Çözünürlük**: HD (1920x1080) 