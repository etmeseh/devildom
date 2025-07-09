\# 🧠 Raqpelz Otomatik Tuş Botu



Bu Python scripti, Raqpelz oyun penceresi aktifken:

\- Belirli aralıklarla 1, 2, 3, 4 tuşlarına basar (kullanıcı tanımlı)

\- Rastgele zamanlarda W, A, S, D yön tuşlarına basarak hareket simülasyonu yapar



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
cd proje-klasoru

# (İsteğe bağlı) Sanal ortam oluştur ve aktif et
python -m venv venv
.\venv\Scripts\activate  # Windows için

# Gerekli paketleri yükle
pip install -r requirements.txt

```

### Scripti Çalıştır

```
python3 ./farm.py

```

## Başlangıçta senden aşağıdaki gibi tuş aralıkları istenir:
```
Enter interval for key '1' (in seconds): 0.5
Enter interval for key '2' (in seconds): 1
Enter interval for key '3' (in seconds): 1.5
Enter interval for key '4' (in seconds): 2
```

Script çalışırken:

1-4 tuşlarına verdiğin sürelerle basılır

W, A, S, D rastgele zamanlarla basılır

F8 Tuşu scripti başlatıp durdurur.

## 🔐 Notlar
Script, bazı işlemleri gerçekleştirmek için Yönetici olarak çalıştırılmalıdır.

Oyun penceresi tam olarak "Rappelz" ismine sahip olmalıdır.

Girişler yalnızca aktif pencere "Rappelz" olduğunda yapılır.

## Dosyalar
```
farm.py             → Ana Python scripti
requirements.txt    → Gerekli bağımlılıklar
start.bat           → Sağ tık Yönetici olarak çalıştırılmasını sağlar (python)
start3.bat          → Sağ tık Yönetici olarak çalıştırılmasını sağlar (python3)
README.md           → Bu dökümantasyon
```