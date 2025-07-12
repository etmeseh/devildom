# 🧠 Raqpelz Otomatik Tuş Botu - v1.2



Bu Python scripti, Raqpelz oyun penceresi aktifken:

\- Belirli aralıklarla 1, 2, 3, 4 tuşlarına basar (kullanıcı tanımlı)

\- Rastgele zamanlarda W, A, S, D yön tuşlarına basarak hareket simülasyonu yapar

\- F8 tuşu ile başlatılır/durdurulur

\- Tüm ayarlar GUI (grafik arayüz) üzerinden yapılandırılır




Oyun içinde farmlama, görev veya bot testi için kullanılabilir.  



> ⚠️ Yalnızca eğitim ve kişisel otomasyon içindir. Online oyunların kullanım şartlarını ihlal etmediğinizden emin olun.



---



## 🚀 Kurulum Adımları



### 1. Python 3.13.5 kurulumu (Windows) — winget ile



PowerShell veya CMD’yi \*\*Yönetici olarak çalıştır\*\* ve aşağıdaki komutu kullan:



```powershell

winget install --id=Python.Python.3.13 -e
```
Kurulum tamamlandıktan sonra terminali kapatıp tekrar aç.
Python sürümünü kontrol etmek için:
```
python3 --version

```

### 2. Gerekli Paketleri Kur
Terminalde (PowerShell, CMD veya Git Bash):

```
# Proje klasörüne git
cd devildom

# (İsteğe bağlı) Sanal ortam oluştur ve aktif et
python -m venv venv
.\venv\Scripts\activate  # Windows için

# Gerekli paketleri yükle
pip install -r requirements.txt

```

### Botu Başlatmak

```
bot_launcher.bat    (Yönetici olarak çalıştırılmalıdır.)

```

## Başlangıçta seni aşağıdaki ekran karşılar:
```
[1] Ayarları Aç (GUI)
[2] Botu Başlat (farm.py)
[Q] Çıkış

```

Ekranda beliren seçenekleri tercih etmek için [] içindeki değerleri tuşlayıp Enter'e basın:

### [1] Ayarları Aç (GUI) 

W, A, S, D yön tuşlarından hangilerine ne sıklıkla basılacağını belirleyebilirsiniz.

1, 2, 3, 4 skill tuşlarına ne sıklıkla basılacağını belirleyebilirsiniz.

Bu ayarlamalar bilgisayarınızda kayıtlı olup tekrar değiştirmek için bu sectionu tekrarlamanız yeterlidir.

### [2] Botu Başlat (farm.py)

Bu seçenek  botu hazır hale getirir. Oyun penceresinin aktif olduğu durumda f8 tuşuyla etkinleştirilmeyi bekler. 

Ctrl + C ile terminal ekranından sonlandırılabilir.

### [Q] Çıkış

Botu başlatmadan hızlı çıkış kullanılabilir. Alt+f4 alternatifi olarak görebilirsiniz.



## 🔐 Notlar
Script, bazı işlemleri gerçekleştirmek için Yönetici olarak çalıştırılmalıdır. (ön ayarların kayıtlanması, tuş basım teklitlerinin yapılması vb.)

Oyun penceresi tam olarak "Rappelz" ismine sahip olmalıdır.

Girişler yalnızca aktif pencere "Rappelz" olduğunda yapılır.

## Dosyalar
```
config_gui.py         → Ayarları belirlemek için GUI
farm.py               → Botun çalıştığı ana script
bot_launcher.bat      → GUI ve farm.py’yi yöneten menülü başlatıcı (sağ click yönetici olarak çalıştır)
config.json           → GUI ile oluşturulan yapılandırma dosyası
requirements.txt      → Gerekli modüller (keyboard, pygetwindow)

```
## 📌 v1.1 Yenilikleri
F8 tuşu botu başlatıp durdurma.

Admin olarak başlatma kolaylığı için iki farklı .bat dosyası ekleme.

## 📌 v1.2 Yenilikleri
Tuş aralıkları GUI ile ayarlanabilir

WASD yönleri kullanıcı tarafından seçilebilir

Hareket süresi ve gecikme aralığı belirlenebilir

Tek bir farm_launcher.bat dosyası üzerinden Python/Python3 uyumlu başlatma