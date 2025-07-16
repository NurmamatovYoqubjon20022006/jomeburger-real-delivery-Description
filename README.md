# 🍔 Jomeburger - Professional Food Delivery Ecosystem

[![Deploy Status](https://github.com/NurmamatovYoqubjon20022006/jomeburger-real-delivery-Description/workflows/🍔%20Deploy%20Jomeburger%20to%20GitHub%20Pages/badge.svg)](https://github.com/NurmamatovYoqubjon20022006/jomeburger-real-delivery-Description/actions)
[![Production](https://img.shields.io/badge/Production-Ready-brightgreen.svg)](https://nurmamatovyoqubjon20022006.github.io/jomeburger-real-delivery-Description/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://t.me/JomeBurgerbot_bot)

## 🌟 Professional Food Delivery Platform

**Jomeburger** - Real-world production-ready food delivery ecosystem built for millions of users with enterprise-grade architecture and 50-year maintainability.

### 🚀 Live Demo
- **🌐 Web App (HTTPS)**: https://nurmamatovyoqubjon20022006.github.io/jomeburger-real-delivery-Description/app.html
- **📱 Telegram Bot**: https://t.me/JomeBurgerbot_bot
- **📲 Mobile App**: Coming Soon (Flutter)

## 🚀 XUSUSIYATLAR

### 🌐 Telegram Web App Integration
- ✅ **Professional Web Interface** - Bringo kabi zamonaviy dizayn
- ✅ **Mobile-First Design** - Telefonda mukammal ishlaydi
- ✅ **Real-time Integration** - Telegram bilan to'liq integratsiya
- ✅ **Native Feel** - Telegram ichida native app sifatida ishlaydi

### 🍔 Buyurtma Tizimlari
- ✅ **Kategoriyalar** - 8 xil mahsulot kategoriyasi
- ✅ **Mahsulot Katalogi** - Professional mahsulot ko'rsatish
- ✅ **Savatcha** - Real-time savatcha boshqaruvi
- ✅ **Qidiruv** - Tez va aqlli qidiruv tizimi
- ✅ **Filter** - Kategoriya bo'yicha filterlash

### 🎨 UI/UX Features
- ✅ **Modern Design** - 2025-yil standartlari
- ✅ **Smooth Animations** - Professional animatsiyalar
- ✅ **Responsive** - Barcha ekran o'lchamlari uchun
- ✅ **Dark/Light Theme** - Telegram theme-ga moslashadi
- ✅ **Fast Loading** - Optimallashtirilgan yuklash

### 💳 To'lov Integratsiyasi
- ✅ **Telegram Payments** - Ichki to'lov tizimi
- ✅ **UzCard/Humo** - Mahalliy kartalar
- ✅ **Payme/Click** - O'zbekiston e-wallet
- ✅ **Naqd to'lov** - Yetkazib berishda to'lov

## 📁 FAYL STRUKTURASI

```
jomeburger-telegram-bot/
├── 📁 app/                     # Asosiy dastur kodlari
│   ├── 📁 handlers/            # Xabar handler-lari
│   │   ├── __init__.py         # Handler-lar import
│   │   ├── webapp.py           # Web App handler-lari
│   │   ├── start.py            # Start buyrug'i
│   │   └── menu.py             # Menyu handler-lari
│   ├── 📁 keyboards/           # Klaviatura layoutlari
│   ├── 📁 services/            # Business logic
│   ├── 📁 models/              # Ma'lumot modellari
│   └── 📁 utils/               # Yordamchi funksiyalar
├── 📁 config/                  # Konfiguratsiya fayllari
│   └── settings.py             # Asosiy sozlamalar
├── 📁 jomeburger-web/         # Web App fayllari
│   └── index.html              # Asosiy web interface
├── main.py                     # Bot entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables namunasi
├── .gitignore                 # Git ignore fayli
└── README.md                  # Ushbu fayl
```

## 🛠️ O'RNATISH VA ISHGA TUSHIRISH

### 1. Telegram Bot Yaratish

```bash
# 1. @BotFather-ga /newbot yuboring
# 2. Bot nomini kiriting: Jomeburger Bot
# 3. Username kiriting: jomeburger_bot
# 4. Olingan tokenni saqlang
```

### 2. Loyihani Klonlash

```bash
git clone https://github.com/jomeburger/telegram-bot.git
cd jomeburger-telegram-bot
```

### 3. Virtual Environment Yaratish

```bash
# Python virtual environment yaratish
python -m venv venv

# Windows-da aktivlashtirish
venv\Scripts\activate

# Linux/Mac-da aktivlashtirish
source venv/bin/activate
```

### 4. Dependencies O'rnatish

```bash
# Barcha kerakli kutubxonalarni o'rnatish
pip install -r requirements.txt
```

### 5. Environment Variables Sozlash

```bash
# .env faylini yaratish
cp .env.example .env

# .env faylini tahrirlash va quyidagi qiymatlarni kiriting:
JOMEBURGER_BOT_TOKEN=your_bot_token_here
JOMEBURGER_DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/jomeburger_bot
JOMEBURGER_REDIS_URL=redis://localhost:6379/0
JOMEBURGER_API_BASE_URL=http://localhost:8001/api/v1
```

### 6. Ma'lumotlar Bazasini Sozlash

```bash
# PostgreSQL va Redis-ni o'rnatish va ishga tushirish
# Database migratsiyalarini ishga tushirish
python -m alembic upgrade head
```

### 7. Botni Ishga Tushirish

```bash
# Development rejimida
python main.py

# Production rejimida
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

## 🌐 WEB APP SOZLASH

### 1. Web Server Sozlash

```bash
# Web fayllarni serve qilish uchun
cd jomeburger-web

# Simple HTTP server (development)
python -m http.server 3000

# Yoki nginx/apache bilan (production)
```

### 2. Domain va SSL

```bash
# Production uchun domain sozlash
# SSL sertifikat o'rnatish
# Telegram Web App URL-ni yangilash
```

### 3. Telegram Web App Ro'yxatdan O'tkazish

```bash
# @BotFather-ga quyidagi buyruqlarni yuboring:
/setmenubutton
# Bot-ni tanlang
# Button text: 🍔 Buyurtma berish
# Web App URL: https://your-domain.com
```

## 🎯 ASOSIY FUNKSIYALAR

### 🚀 Bot Buyruqlari

```
/start          - Botni ishga tushirish
/help           - Yordam ma'lumotlari
/menu           - Mahsulotlar katalogi
/orders         - Buyurtmalar tarixi
/profile        - Foydalanuvchi profili
/contact        - Bog'lanish ma'lumotlari
```

### 🌐 Web App Pages

- **🏠 Bosh sahifa** - Kategoriyalar va popular mahsulotlar
- **🔍 Qidiruv** - Mahsulot qidiruv va filter
- **🛒 Savatcha** - Buyurtma boshqaruvi
- **📋 Buyurtmalar** - Buyurtmalar tarixi
- **👤 Profil** - Foydalanuvchi sozlamalari

### 💬 Callback Handler-lar

```python
# Kategoriyalar
"category_pizza"     -> Pitsa mahsulotlari
"category_burger"    -> Burger mahsulotlari
"category_shawarma"  -> Shaurma mahsulotlari

# Buyurtma jarayoni
"add_to_cart_{id}"   -> Savatga qo'shish
"remove_from_cart"   -> Savatdan o'chirish
"place_order"        -> Buyurtma berish

# Navigatsiya
"back_to_main"       -> Asosiy menyuga qaytish
"contact"            -> Bog'lanish ma'lumotlari
"info"               -> Kompaniya haqida
```

## 🔧 KONFIGURATSIYA

### Bot Sozlamalari

```python
# config/settings.py da sozlash mumkin:

BOT_TOKEN = "your_telegram_bot_token"
WEB_APP_URL = "https://your-domain.com"
WEBHOOK_URL = "https://your-api.com/webhook"  # Production uchun
API_BASE_URL = "https://api.jomeburger.uz"
```

### Web App Sozlamalari

```html
<!-- jomeburger-web/index.html da -->
<script>
const WEB_APP_URL = "https://jomeburger.uz";  // Production URL
const DEV_WEB_APP_URL = "http://localhost:3000";  // Development URL
</script>
```

## 📊 MONITORING VA ANALYTICS

### Logging Tizimi

```python
# Barcha harakatlar log qilinadi:
✅ Foydalanuvchi start bosganda
✅ Web App ochilganda  
✅ Mahsulot savatga qo'shilganda
✅ Buyurtma berilganda
✅ Xatoliklar va istisnolar
```

### Performance Metrics

```python
# Redis orqali kuzatiladi:
- Aktiv foydalanuvchilar
- Buyurtmalar soni
- Popular mahsulotlar
- API response vaqtlari
```

## 🚨 XAVFSIZLIK

### Rate Limiting
```python
# Spam himoyasi
- 1 daqiqada maksimum 60 so'rov
- IP address blacklisting
- Suspicious activity detection
```

### Data Protection
```python
# Xavfsiz ma'lumot saqlash
- JWT tokenlar
- Parollar hash qilinadi
- Sensitive data encryption
- GDPR compliance
```

## 🧪 TESTING

### Unit Tests

```bash
# Testlarni ishga tushirish
python -m pytest tests/

# Coverage report
python -m pytest --cov=app tests/
```

### Integration Tests

```bash
# Telegram Bot API testlari
python -m pytest tests/integration/

# Web App testlari
# Browser automation bilan
```

## 🚀 DEPLOYMENT

### Development

```bash
# Local development
python main.py

# Web server
python -m http.server 3000
```

### Staging

```bash
# Staging server-da
docker-compose -f docker-compose.staging.yml up
```

### Production

```bash
# Production deployment
docker-compose -f docker-compose.prod.yml up -d

# Yoki Kubernetes
kubectl apply -f k8s/
```

## 📈 MASSHTABLASH

### Horizontal Scaling

```yaml
# docker-compose.yml
services:
  bot:
    replicas: 3  # Multiple bot instances
  web:
    replicas: 2  # Multiple web servers
  redis:
    cluster: true  # Redis cluster
```

### Load Balancing

```nginx
# nginx.conf
upstream telegram_bot {
    server bot1:8000;
    server bot2:8000;
    server bot3:8000;
}
```

## 📞 QOLLAB-QUVVATLASH

### Development Team
- **Telegram Bot Developer**: @jomeburger_dev
- **Frontend Developer**: React/HTML/CSS expert
- **Backend Developer**: Python/FastAPI expert
- **DevOps Engineer**: Docker/Kubernetes expert

### Support Channels
- 📧 **Email**: support@jomeburger.uz
- 💬 **Telegram**: @jomeburger_support
- 📖 **Documentation**: /docs/telegram-bot/
- 🐛 **Bug Reports**: GitHub Issues

## 📋 ROADMAP

### v1.1 (Keyingi oy)
- [ ] Push notifications
- [ ] Voice ordering
- [ ] Group ordering
- [ ] Loyalty program

### v1.2 (2 oy)
- [ ] AI chatbot integration
- [ ] Multi-language support
- [ ] Advanced analytics
- [ ] Restaurant management

### v2.0 (3 oy)
- [ ] Mini-app games
- [ ] Social features
- [ ] Advanced personalization
- [ ] AR menu viewing

---

> **Eslatma**: Bu professional production loyiha uchun yaratilgan Telegram bot. Bringo kabi zamonaviy interface bilan, lekin yanada ko'proq funksiyalar bilan! Sizning rasmlaringizdan ilhomlanib yaratildi va 50 yil keyin ham tushunarli bo'lishi uchun batafsil hujjatlashtirilgan! 🤖✨

## 🎯 LOYIHANI ISHGA TUSHIRISH

1. **Telegram bot yarating** - @BotFather orqali
2. **Konfiguratsiyani sozlang** - .env faylida
3. **Ma'lumotlar bazasini sozlang** - PostgreSQL va Redis
4. **Web App-ni deploy qiling** - Domain va SSL bilan
5. **Botni ishga tushiring** - `python main.py`
6. **Testlang va enjoy qiling!** 🎉
