# XSS Vulnerable Web Application

Bu proje, Stored XSS (Cross-Site Scripting) güvenlik açığını test ortamında exploit etmek amacıyla oluşturulmuş basit bir web uygulamasıdır.

## Gereksinimler

- [Podman](https://podman.io/getting-started/installation)

## Stored XSS Zafiyetli Web Uygulaması Kurulum ve Çalıştırma

1. **Container imajını oluşturun:**

   ```bash
   podman build -t xss-app .

2. **Container'ı başlatın:**

   ```bash
   podman run -d -p 9090:80 --name xss-vuln xss-app

3. **Tarayıcıdan uygulamaya erişin:**

   ```bash

   http://localhost:9090

Amaç

Bu uygulama, geliştiricilere ve güvenlik uzmanlarına XSS açıklarını test etme ve anlama imkanı sağlar. Eğitim ve araştırma amaçlıdır.


![resim](https://github.com/user-attachments/assets/b67869fb-84c4-49ac-a646-233d427c113c)


![resim](https://github.com/user-attachments/assets/b2bdf1e3-1867-438e-b98e-d105b8ba3da8)


![resim](https://github.com/user-attachments/assets/95d22b30-36a6-4eaf-a3bd-d173e19a970f)






## "Trigger of Admin Account" Kurulum ve Çalıştırma


1. **HTTP Sunucu Başlatın:**

   ```bash
   python3 -m http.server 4455
   
![resim](https://github.com/user-attachments/assets/48cf8088-f243-4d95-92d1-d187704198ca)



![resim](https://github.com/user-attachments/assets/4c3d98b9-0f6a-4b3b-b8d2-09f05ed90894)



















