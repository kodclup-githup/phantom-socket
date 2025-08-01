# 🔍 Phantom Socket Premium v2.0

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-Educational-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Termux-lightgrey.svg)
![Version](https://img.shields.io/badge/Version-2.0%20Premium-red.svg)

**Gelişmiş Port Tarama ve Güvenlik Analiz Aracı**

*Eğitim amaçlı geliştirilmiş profesyonel ağ güvenliği aracı*

</div>

---

## 📋 İçindekiler

- [🎯 Genel Bakış](#-genel-bakış)
- [✨ Özellikler](#-özellikler)
- [🔧 Kurulum](#-kurulum)
  - [🐧 Linux Kurulumu](#-linux-kurulumu)
  - [🪟 Windows Kurulumu](#-windows-kurulumu)
  - [📱 Termux Kurulumu](#-termux-kurulumu)
- [🚀 Kullanım](#-kullanım)
- [📊 Tarama Tipleri](#-tarama-tipleri)
- [🛡️ Güvenlik Özellikleri](#️-güvenlik-özellikleri)
- [📈 Raporlama](#-raporlama)
- [⚖️ Etik Kullanım](#️-etik-kullanım)
- [🤝 Katkıda Bulunma](#-katkıda-bulunma)
- [📞 İletişim](#-i̇letişim)

---

## 🎯 Genel Bakış

**Phantom Socket Premium**, ağ güvenliği uzmanları ve siber güvenlik öğrencileri için geliştirilmiş kapsamlı bir port tarama ve güvenlik analiz aracıdır. Bu araç, hedef sistemlerdeki açık portları tespit ederek detaylı güvenlik analizleri sunar ve kapsamlı raporlar oluşturur.

### 🎓 Eğitim Amaçlı Geliştirme

Bu araç tamamen **eğitim amaçlı** olarak geliştirilmiştir ve aşağıdaki konularda öğrenme sağlar:
- Ağ protokolleri ve port yapıları
- Güvenlik açığı tespiti
- Sistem güvenliği analizi
- Penetrasyon testi metodolojileri

---

## ✨ Özellikler

### 🔍 **Gelişmiş Tarama Yetenekleri**
- **Çoklu Thread Desteği**: 2.000'e kadar eşzamanlı bağlantı
- **Banner Grabbing**: Servis bilgilerini otomatik tespit
- **Akıllı Port Tanıma**: 50+ yaygın servis için detaylı bilgi
- **Hızlı Tarama**: Optimize edilmiş algoritma ile yüksek performans

### 📊 **Kapsamlı Analiz**
- **Risk Değerlendirmesi**: 4 seviyeli risk analizi (Düşük, Orta, Yüksek, Çok Yüksek)
- **Servis Kategorileri**: Web, Veritabanı, E-posta, Uzak Erişim vb.
- **Güvenlik Önerileri**: Her port için özel güvenlik tavsiyeleri
- **Detaylı Raporlama**: JSON formatında export desteği

### 🎨 **Kullanıcı Dostu Arayüz**
- **Renkli Terminal Çıktısı**: Kolay okunabilir sonuçlar
- **İlerleme Çubuğu**: Gerçek zamanlı tarama durumu
- **Kategorik Sonuçlar**: Organize edilmiş port listesi
- **Interaktif Menü**: Kolay kullanım için menü sistemi

### 🛡️ **Güvenlik Odaklı**
- **Etik Kullanım Kontrolü**: Kullanıcı onay sistemi
- **Güvenlik Uyarıları**: Risk seviyelerine göre uyarılar
- **Detaylı Öneriler**: Güvenlik açıklarını kapatma rehberi
- **Yasal Uyarılar**: Etik kullanım hatırlatmaları

---

## 🔧 Kurulum

### 📋 Sistem Gereksinimleri

- **Python**: 3.6 veya üzeri
- **İşletim Sistemi**: Windows 10+, Linux (Ubuntu 18.04+), Android (Termux)
- **RAM**: Minimum 512MB
- **Ağ**: İnternet bağlantısı

---

### 🐧 Linux Kurulumu

#### Adım 1: Sistem Güncellemesi
```bash
# Ubuntu/Debian tabanlı sistemler için
sudo apt update && sudo apt upgrade -y

# CentOS/RHEL tabanlı sistemler için
sudo yum update -y
# veya
sudo dnf update -y

# Arch Linux için
sudo pacman -Syu
```

#### Adım 2: Python ve Pip Kurulumu
```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip git -y

# CentOS/RHEL
sudo yum install python3 python3-pip git -y
# veya
sudo dnf install python3 python3-pip git -y

# Arch Linux
sudo pacman -S python python-pip git
```

#### Adım 3: Python Sürümü Kontrolü
```bash
python3 --version
pip3 --version
```

#### Adım 4: Proje İndirme
```bash
# GitHub'dan klonlama (eğer repository varsa)
git clone https://github.com/kodclup-githup/phantom-socket.git
cd phantom-socket

# Veya manuel indirme
mkdir phantom-socket
cd phantom-socket
wget https://raw.githubusercontent.com/kodclup-githup/phantom-socket/main/phantom_socket.py
wget https://raw.githubusercontent.com/kodclup-githup/phantom-socket/main/requirements.txt
```

#### Adım 5: Bağımlılıkları Kurma
```bash
pip3 install -r requirements.txt
```

#### Adım 6: Çalıştırma İzni Verme
```bash
chmod +x phantom_socket.py
```

#### Adım 7: Çalıştırma
```bash
python3 phantom_socket.py
```

---

### 🪟 Windows Kurulumu

#### Adım 1: Python İndirme ve Kurma
1. [Python.org](https://www.python.org/downloads/) adresinden Python 3.6+ indirin
2. Kurulum sırasında **"Add Python to PATH"** seçeneğini işaretleyin
3. **"Install for all users"** seçeneğini tercih edin

#### Adım 2: Kurulum Doğrulama
```cmd
# Command Prompt'u yönetici olarak açın
python --version
pip --version
```

#### Adım 3: Git Kurulumu (Opsiyonel)
1. [Git for Windows](https://git-scm.com/download/win) indirin ve kurun
2. Kurulum sırasında varsayılan ayarları kullanın

#### Adım 4: Proje İndirme
```cmd
# Git ile (eğer kuruluysa)
git clone https://github.com/kodclup-githup/phantom-socket.git
cd phantom-socket

# Manuel indirme alternatifi
# 1. Proje dosyalarını indirin
# 2. Bir klasöre çıkarın
# 3. Command Prompt ile o klasöre gidin
```

#### Adım 5: Bağımlılıkları Kurma
```cmd
pip install -r requirements.txt
```

#### Adım 6: Çalıştırma
```cmd
python phantom_socket.py
```

#### Windows Güvenlik Duvarı Ayarları
```cmd
# Windows Defender Firewall'da Python'a izin verme
# 1. Windows Güvenlik Duvarı'nı açın
# 2. "Bir uygulamaya veya özelliğe izin ver" seçin
# 3. Python.exe'yi bulun ve işaretleyin
# 4. Hem özel hem de genel ağlar için izin verin
```

---

### 📱 Termux Kurulumu

#### Adım 1: Termux Kurulumu
1. Google Play Store'dan **Termux** uygulamasını indirin
2. Uygulamayı açın ve kurulumun tamamlanmasını bekleyin

#### Adım 2: Sistem Güncellemesi
```bash
pkg update && pkg upgrade -y
```

#### Adım 3: Gerekli Paketleri Kurma
```bash
# Python ve gerekli araçları kurma
pkg install python git wget curl -y

# Ek geliştirme araçları
pkg install build-essential -y
```

#### Adım 4: Pip Kurulumu
```bash
# Pip kurulumu
pkg install python-pip -y

# Pip güncellemesi
pip install --upgrade pip
```

#### Adım 5: Depolama İzni
```bash
# Termux'a depolama erişimi verme
termux-setup-storage
```

#### Adım 6: Proje İndirme
```bash
# Ana dizine gitme
cd ~

# Proje klasörü oluşturma
mkdir phantom-socket
cd phantom-socket

# Dosyaları indirme
wget https://raw.githubusercontent.com/kodclup-githup/phantom-socket/main/phantom_socket.py
wget https://raw.githubusercontent.com/kodclup-githup/phantom-socket/main/requirements.txt
```

#### Adım 7: Bağımlılıkları Kurma
```bash
pip install -r requirements.txt
```

#### Adım 8: Çalıştırma
```bash
python phantom_socket.py
```

#### Termux İpuçları
```bash
# Klavye kısayolları
# Ctrl + C = Volume Down + C
# Ctrl + Z = Volume Down + Z
# Tab = Volume Down + T

# Ekstra tuş çubuğu gösterme
echo "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]" >> ~/.termux/termux.properties
```

---

## 🚀 Kullanım

### 🎯 Temel Kullanım

```bash
python3 phantom_socket.py
```

### 📝 Kullanım Adımları

1. **Aracı Başlatma**: Yukarıdaki komutu çalıştırın
2. **Hedef Girme**: Domain adı veya IP adresi girin
   ```
   Örnekler:
   - example.com
   - www.example.com
   - https://example.com
   - 192.168.1.1
   ```
3. **Tarama Tipi Seçme**: 1-6 arası seçenek seçin
4. **Export Seçeneği**: JSON export isteyip istemediğinizi belirtin
5. **Etik Onay**: Etik kullanım onayını verin
6. **Sonuçları İnceleme**: Detaylı raporu inceleyin

### 🎮 Interaktif Menü

```
🎯 Hedef domain veya IP adresini girin: example.com

📋 Tarama tipini seçin:
1. Hızlı Tarama (Yaygın portlar)
2. Standart Tarama (1-1000 + önemli portlar)
3. Tam Tarama (1-65535)
4. Web Servisleri
5. Veritabanı Servisleri
6. Uzak Erişim Servisleri

Seçiminiz (1-6, varsayılan 1): 1

Sonuçları JSON dosyasına export etmek istiyor musunuz? (e/h): e

Bu aracı sadece kendi sistemlerinizde kullandığınızı onaylıyor musunuz? (e/h): e
```

---

## 📊 Tarama Tipleri

### 1. 🚀 Hızlı Tarama (Quick Scan)
- **Port Sayısı**: 21 kritik port
- **Süre**: 10-30 saniye
- **Kullanım**: Hızlı güvenlik kontrolü
- **Portlar**: 21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 1433, 3306, 3389, 5432, 5900, 6379, 8080, 27017

### 2. 📈 Standart Tarama (Common Scan)
- **Port Sayısı**: ~1010 port
- **Süre**: 2-5 dakika
- **Kullanım**: Kapsamlı güvenlik analizi
- **Portlar**: 1-1000 + kritik yüksek portlar

### 3. 🔍 Tam Tarama (Full Scan)
- **Port Sayısı**: 65535 port
- **Süre**: 10-30 dakika
- **Kullanım**: Detaylı penetrasyon testi
- **Portlar**: 1-65535 (tüm portlar)

### 4. 🌐 Web Servisleri
- **Port Sayısı**: 8 port
- **Süre**: 5-10 saniye
- **Kullanım**: Web sunucu analizi
- **Portlar**: 80, 443, 8000, 8080, 8443, 8888, 9000, 9090

### 5. 🗄️ Veritabanı Servisleri
- **Port Sayısı**: 7 port
- **Süre**: 5-10 saniye
- **Kullanım**: Veritabanı güvenlik kontrolü
- **Portlar**: 1433, 1521, 3306, 5432, 6379, 27017, 50000

### 6. 🖥️ Uzak Erişim Servisleri
- **Port Sayısı**: 6 port
- **Süre**: 5-10 saniye
- **Kullanım**: Uzak erişim güvenlik kontrolü
- **Portlar**: 22, 23, 3389, 5900, 5901, 5902

---

## 🛡️ Güvenlik Özellikleri

### 🔍 Port Analizi

#### Desteklenen Servisler
- **Web Servisleri**: HTTP, HTTPS, Alternative HTTP/HTTPS
- **Dosya Transfer**: FTP, SFTP, FTPS, TFTP, NFS
- **E-posta**: SMTP, POP3, IMAP, SMTPS, IMAPS, POP3S
- **Veritabanları**: MySQL, PostgreSQL, MSSQL, Oracle, MongoDB, Redis
- **Uzak Erişim**: SSH, Telnet, RDP, VNC
- **Windows Servisleri**: SMB, NetBIOS, RPC
- **Ağ Servisleri**: DNS, DHCP, SNMP, LDAP

#### Risk Seviyeleri
- 🟢 **DÜŞÜK**: Güvenli yapılandırılmış servisler
- 🟡 **ORTA**: Dikkat gerektiren servisler
- 🟠 **YÜKSEK**: Risk taşıyan servisler
- 🔴 **ÇOK YÜKSEK**: Kritik güvenlik riski

### 🔒 Banner Grabbing

Araç, açık portlardan servis bilgilerini otomatik olarak toplar:
```
[+] HTTP Web Server (HTTP) - Port 80
    📝 Açıklama: Hypertext Transfer Protocol
    ⚠️  Risk Seviyesi: ORTA
    🏷️  Banner: Apache/2.4.41 (Ubuntu)
    💡 Güvenlik Önerisi: HTTPS'e yönlendirme yapın
```

### 📊 Risk Analizi

```
📈 RİSK ANALİZİ
• DÜŞÜK Risk: 2 port
• ORTA Risk: 1 port
• YÜKSEK Risk: 0 port
• ÇOK YÜKSEK Risk: 1 port

📊 Toplam Risk Skoru: 8/100
⚠️  UYARI: Orta seviye risk tespit edildi.
```

---

## 📈 Raporlama

### 📄 Terminal Raporu

Araç, tarama sonuçlarını kategorilere ayırarak sunar:
- **Açık Portlar ve Servisler**
- **Risk Analizi**
- **Detaylı Güvenlik Önerileri**
- **Tarama İstatistikleri**

### 📁 JSON Export

```json
{
  "scan_info": {
    "target": "example.com",
    "scan_time": "2024-01-15T14:30:00",
    "duration": 45.2,
    "total_ports_scanned": 1000
  },
  "results": {
    "open_ports": 3,
    "closed_ports": 995,
    "filtered_ports": 2
  },
  "detailed_results": {
    "80": {
      "name": "HTTP",
      "service": "Web Server",
      "risk": "ORTA",
      "banner": "Apache/2.4.41",
      "advice": "HTTPS'e yönlendirme yapın"
    }
  }
}
```

### 📊 Rapor İçeriği

1. **Tarama Bilgileri**
   - Hedef sistem
   - Tarama süresi
   - Tarih ve saat

2. **Port Durumları**
   - Açık portlar
   - Kapalı portlar
   - Filtrelenmiş portlar

3. **Servis Detayları**
   - Servis adı ve açıklaması
   - Banner bilgileri
   - Risk seviyesi

4. **Güvenlik Önerileri**
   - Port bazlı öneriler
   - Genel güvenlik tavsiyeleri
   - Acil eylem gerektiren durumlar

---

## ⚖️ Etik Kullanım

### 🎓 Eğitim Amaçlı Kullanım

Bu araç **sadece eğitim amaçlı** geliştirilmiştir ve aşağıdaki durumlarda kullanılmalıdır:

✅ **İzin Verilen Kullanımlar:**
- Kendi sistemlerinizde güvenlik testi
- Laboratuvar ortamında öğrenme
- Siber güvenlik eğitimi
- Penetrasyon testi eğitimi
- Ağ güvenliği araştırması

❌ **Yasak Kullanımlar:**
- Yetkisiz sistemlerde tarama
- Kötü niyetli saldırılar
- Yasal olmayan penetrasyon testleri
- İzinsiz güvenlik testleri
- Ticari amaçlı kötüye kullanım

### ⚖️ Yasal Sorumluluk

- Bu aracın kullanımından doğan tüm yasal sorumluluk **kullanıcıya** aittir
- Araç geliştiricileri hiçbir yasal sorumluluk kabul etmez
- Kullanım öncesi mutlaka yasal izinleri alın
- Yerel yasalara ve düzenlemelere uygun hareket edin

### 🛡️ Güvenlik Uyarıları

1. **İzin Kontrolü**: Sadece sahip olduğunuz veya izin aldığınız sistemlerde kullanın
2. **Yasal Çerçeve**: Bulunduğunuz ülkenin siber güvenlik yasalarına uyun
3. **Etik Sınırlar**: Araçları sadece savunma amaçlı kullanın
4. **Gizlilik**: Elde ettiğiniz bilgileri üçüncü şahıslarla paylaşmayın

### 📋 Kullanım Sözleşmesi

Bu aracı kullanarak aşağıdakileri kabul etmiş sayılırsınız:

1. Aracı sadece eğitim amaçlı kullanacağınız
2. Yetkisiz sistemlerde kullanmayacağınız
3. Yasal sorumluluğun size ait olduğu
4. Etik kurallara uyacağınız

---

## 🔧 Teknik Detaylar

### 🏗️ Mimari

```
Phantom Socket Premium v2.0
├── Ana Sınıf (PhantomSocketPremium)
├── Port Veritabanı (50+ servis)
├── Tarama Motoru (Multi-threading)
├── Banner Grabbing Sistemi
├── Risk Analiz Motoru
├── Raporlama Sistemi
└── Export Modülü
```

### ⚡ Performans

- **Maksimum Thread**: 20.000 eşzamanlı bağlantı
- **Timeout**: 2 saniye (ayarlanabilir)
- **Hız**: 1000+ port/dakika
- **Bellek Kullanımı**: ~50MB

### 🔌 Ağ Protokolleri

- **TCP Connect Scan**: Tam bağlantı taraması
- **Banner Grabbing**: HTTP, FTP, SSH, SMTP protokolleri
- **DNS Resolution**: Otomatik domain çözümleme
- **IPv4 Desteği**: Tam IPv4 uyumluluğu

---

## 🤝 Katkıda Bulunma

### 🐛 Hata Bildirimi

Hata bulduğunuzda lütfen aşağıdaki bilgileri paylaşın:
- İşletim sistemi ve versiyonu
- Python versiyonu
- Hata mesajı
- Yeniden üretme adımları

### 💡 Özellik Önerileri

Yeni özellik önerilerinizi şu kategorilerde değerlendiriyoruz:
- Tarama teknikleri
- Raporlama geliştirmeleri
- Performans optimizasyonları
- Kullanıcı deneyimi

### 📝 Kod Katkısı

1. Repository'yi fork edin
2. Yeni bir branch oluşturun
3. Değişikliklerinizi yapın
4. Test edin
5. Pull request gönderin

---

## 📞 İletişim

### 👨‍💻 Geliştirici

**KodClup**
- 🐙 GitHub: [@kodclup](https://github.com/kodclup)

### 🆘 Destek

- 📖 Dokümantasyon: Bu README dosyası
- 🐛 Hata Bildirimi: GitHub Issues
- 💬 Topluluk: Discord/Telegram grupları
- 📚 Eğitim: YouTube kanalı

### 🔗 Bağlantılar

- 📦 Repository: [GitHub](https://github.com/kodclup-githup/phantom-socket)
- 📄 Lisans: MİT License
---

## 📜 Lisans

Bu proje **MİT Lisansı** altında lisanslanmıştır. Detaylar için `LICENSE` dosyasını inceleyiniz.

### 📋 Lisans Özeti

- ✅ Eğitim amaçlı kullanım
- ✅ Kişisel öğrenme
- ✅ Araştırma projeleri
- ❌ Ticari kullanım
- ❌ Yeniden dağıtım
- ❌ Kötüye kullanım

---

## 🙏 Teşekkürler

Bu projenin geliştirilmesinde katkıda bulunan herkese teşekkür ederiz:

- Siber güvenlik topluluğu
- Beta test kullanıcıları
- Geri bildirim sağlayan eğitmenler
- Açık kaynak kütüphane geliştiricileri

---

<div align="center">

**⚠️ Bu araç sadece eğitim amaçlıdır. Etik kullanım zorunludur! ⚠️**

*Geliştirici: KodClup | Versiyon: 2.0 Premium*

</div>