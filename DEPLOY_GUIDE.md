# 🚀 JOMEBURGER GITHUB PAGES DEPLOY GUIDE

## Step 1: GitHub Repository yaratish

1. **GitHub.com ga kiring**: https://github.com
2. **New Repository tugmasini bosing**
3. **Repository nomi**: `jomeburger-telegram-bot`
4. **Public** qilib qo'ying (GitHub Pages uchun kerak)
5. **Initialize this repository with README** - BELGILAMANG (bizda bor)
6. **Create repository** tugmasini bosing

## Step 2: Local repositoryni GitHub ga push qilish

Terminal/PowerShell da quyidagi komandalarni ishlating:

```powershell
# GitHub repository URL ni qo'shish (USERNAME ni o'zingiznikiga almashtiring)
git remote add origin https://github.com/USERNAME/jomeburger-telegram-bot.git

# Kodni GitHub ga yuklash
git push -u origin main
```

## Step 3: GitHub Pages ni yoqish

1. **GitHub repository-ga kiring**
2. **Settings** tab ni bosing
3. **Pages** bo'limini toping (chap menuda)
4. **Source** da: **Deploy from a branch** ni tanlang
5. **Branch** da: **main** ni tanlang
6. **Folder** da: **/ (root)** ni tanlang
7. **Save** tugmasini bosing

## Step 4: HTTPS URL olish

GitHub Pages deploy qilgandan keyin sizga URL beriladi:
```
https://USERNAME.github.io/jomeburger-telegram-bot/
```

## Step 5: Bot ni yangilash

.env faylingizda WEB_APP_URL ni yangilang:
```
WEB_APP_URL=https://USERNAME.github.io/jomeburger-telegram-bot/app.html
```

## Step 6: Bot ni qayta ishga tushirish

```powershell
python main_simple.py
```

## ✅ NATIJA

- 🌐 **Web App**: https://USERNAME.github.io/jomeburger-telegram-bot/
- 🤖 **Telegram Bot**: Professional WebApp tugmasi bilan
- 🔒 **HTTPS**: GitHub Pages avtomatik ta'minlaydi
- 📱 **Mobile Ready**: Responsive design
- 🚀 **Production Ready**: Real foydalanuvchilar uchun tayyor

---
**Muhim**: USERNAME ni o'z GitHub username ingiz bilan almashtiring!
