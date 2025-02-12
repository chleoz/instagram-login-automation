# Instagram Login Automation with Proxy Support

## 📌 Proje Açıklaması
Bu Python projesi, **Selenium** kullanarak Instagram'a giriş yapmayı otomatikleştirir. **SOCKS5 veya HTTP proxy desteği** ile çalışabilir ve **başarılı girişleri ve 2FA (İki Faktörlü Kimlik Doğrulama) aktif hesapları** kaydeder.

---

## 📦 Gerekli Bağımlılıklar
Bu projenin çalışabilmesi için aşağıdaki kütüphanelerin yüklenmiş olması gerekir:

| Kütüphane | Açıklama |
|-----------|---------|
| `selenium` | Web otomasyonu için gerekli (Instagram'a giriş ve işlemler için) |
| `colorama` | Terminalde renkli çıktı almak için |
| `webdriver-manager` | ChromeDriver'ı otomatik olarak yönetmek için (isteğe bağlı) |

### 🔹 **Bağımlılıkları Yüklemek İçin**
Tüm bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:
```sh
pip install selenium colorama webdriver-manager
```

Alternatif olarak, aşağıdaki komutla **`requirements.txt`** dosyasındaki bağımlılıkları yükleyebilirsiniz:
```sh
pip install -r requirements.txt
```

---

## 🔧 **Ekstra Gereksinimler**
### 1️⃣ **Google Chrome veya Chromium Yüklenmeli**
- Chrome veya Chromium’un kurulu olup olmadığını kontrol etmek için:
  ```sh
  google-chrome --version
  ```
  veya
  ```sh
  chromium --version
  ```
- Eğer yüklü değilse, Linux için yükleme:
  ```sh
  sudo apt update && sudo apt install google-chrome-stable
  ```
  veya
  ```sh
  sudo apt install chromium-browser
  ```

### 2️⃣ **ChromeDriver'ın Uygun Sürümde Olması Gerekiyor**
- ChromeDriver'ın uygun olup olmadığını kontrol etmek için:
  ```sh
  chromedriver --version
  ```
- Eğer güncellenmesi gerekiyorsa:
  ```sh
  wget https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.91/linux64/chromedriver-linux64.zip
  unzip chromedriver-linux64.zip
  sudo mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver
  sudo chmod +x /usr/local/bin/chromedriver
  ```

---

## 📂 **Gerekli Dosyalar**
Bu proje için aşağıdaki dosyalar oluşturulmalıdır:

- **`socks5.txt`** → SOCKS5 Proxy listesi.
- **`http.txt`** → HTTP Proxy listesi.
- **`chleoz.txt`** → Instagram hesap bilgileri (format: `username:password`).
- **`passed.txt`** → Başarılı giriş yapılan hesaplar buraya kaydedilir.
- **`2fa.txt`** → 2FA (İki Faktörlü Kimlik Doğrulama) açık hesaplar buraya kaydedilir.

📌 **Örnek Dosya İçerikleri**
#### `chleoz.txt`
```
user1:password1
user2:password2
```

#### `socks5.txt`
```
192.168.1.100:1080
192.168.1.101:1080
```

#### `http.txt`
```
192.168.1.100:8080
192.168.1.101:8080
```

---

## 🚀 **Nasıl Kullanılır?**

1️⃣ **Python dosyanızı çalıştırın:**
```sh
python3 chleoz.py
```

2️⃣ **Proxy türünü seçin:**
```
Proxy türünü seçin (socks5 / http / proxysiz): socks5
```
- **SOCKS5 veya HTTP seçerseniz**, ilgili dosyadan proxyler otomatik olarak alınır.
- **"proxysiz" seçerseniz**, proxy kullanmadan Instagram'a bağlanır.

3️⃣ **Program, `chleoz.txt` dosyasındaki hesapları sırayla dener.**
- Başarılı girişler **`passed.txt`** dosyasına kaydedilir.
- 2FA aktif hesaplar **`2fa.txt`** dosyasına kaydedilir.
- Tüm denemeler terminal ekranında takip edilebilir.

---

## 📌 **Özellikler**
⚡︎ **Proxy desteği:** SOCKS5 veya HTTP Proxy kullanılabilir.  
⚡︎ **Proxy'siz çalışma seçeneği:** Kullanıcı, proxy kullanıp kullanmayacağını seçebilir.
⚡︎ **2FA (İki Faktörlü Kimlik Doğrulama) tespiti:** Eğer hesapta 2FA açıksa, program bunu algılar ve **`2fa.txt`** dosyasına kaydeder.  
⚡︎ **Renkli terminal çıktısı:** İşlemler **renk kodlarıyla** gösterilir.

---

## ⚠ **Önemli Uyarılar**
- **Bu araç yalnızca eğitim ve test amaçlı kullanılmalıdır!** Instagram'ın kullanım koşullarına aykırı eylemler **hesap engellemesi veya IP yasağı ile sonuçlanabilir.**
- **Instagram çok fazla başarısız giriş denemesinde hesabı kilitleyebilir.** Denemeleri çok sık yapmaktan kaçının.
- **VPN veya proxy kullanarak güvenliği artırabilirsiniz.**

---