# 🤖 JOMEBURGER TELEGRAM BOT - HANDLER-LAR ASOSIY FAYLI
# ====================================================
# Bu fayl barcha handler-larni import qilib, bitta router-da birlashtiradi.
# Handler - bu foydalanuvchi xabariga javob beradigan funksiya.
# 50 yil keyin ham tushunarli bo'lishi uchun har bir qator izohlanған! 🚀

from aiogram import Router

# ================================
# ASOSIY ROUTER YARATISH
# ================================

# Router - bu handler-larni guruhlash va tartibga solish uchun ishlatiladi
router = Router(name="main_router")

# ================================
# HOZIRCHA BO'SH - STEP BY STEP QO'SHAMIZ
# ================================

# Handler-larni import qilish - step by step qo'shamiz
# from .start import start_router
# from .webapp import webapp_router
# from .menu import menu_router

# Router-larni ulash
# router.include_router(start_router)
# router.include_router(webapp_router)
# router.include_router(menu_router)

def get_router_info() -> dict:
    """Router haqida ma'lumot qaytarish"""
    return {
        "main_router": "main_router",
        "description": "Jomeburger bot uchun asosiy router"
    }ER TELEGRAM BOT - HANDLER-LAR ASOSIY FAYLI
====================================================

Bu fayl barcha handler-larni import qilib, bitta router-da birlashtiradi.
Handler - bu foydalanuvchi xabariga javob beradigan funksiya.

50 yil keyin ham tushunarli bo'lishi uchun har bir qator izohlanган! 🚀
"""

from aiogram import Router

# Hozircha oddiy import - step by step qo'shamiz
# from .start import start_router
# from .menu import menu_router
# from .webapp import webapp_routerELEGRAM BOT - HANDLER-LAR ASOSIY FAYLI
====================================================

Bu fayl barcha handler-larni import qilib, bitta router-da birlashtiradi.
Handler - bu foydalanuvchi xabariga javob beradigan funksiya.

50 yil keyin ham tushunarli bo'lishi uchun har bir qator izohlanған! 🚀
"""

from aiogram import Router

# Local handler imports - mahalliy handler modullarini import qilish
from .start import start_router
from .menu import menu_router
from .order import order_router
from .profile import profile_router
from .admin import admin_router
from .payment import payment_router
from .help import help_router

# ================================
# ASOSIY ROUTER YARATISH
# ================================

# Router - bu handler-larni guruhlash va tartibga solish uchun ishlatiladi
# Barcha handler-lar bitta router-da yig'iladi va main.py-da ishlatiladi
router = Router(name="main_router")

# ================================
# SUB-ROUTER-LARNI ULASH
# ================================

# Handler-larni muhimlik tartibida ulash kerak
# Eng muhim va tez-tez ishlatiluvchi handler-lar birinchi bo'lishi kerak

# 1. Start handler - /start buyrug'i, botga birinchi marta kirish
router.include_router(start_router)

# 2. Menu handler - mahsulotlar katalogi, kategoriyalar
router.include_router(menu_router)

# 3. Order handler - buyurtma berish, savatcha boshqaruvi
router.include_router(order_router)

# 4. Profile handler - foydalanuvchi profili, sozlamalar
router.include_router(profile_router)

# 5. Payment handler - to'lov tizimlari, to'lov jarayoni
router.include_router(payment_router)

# 6. Help handler - yordam, FAQ, qo'llab-quvvatlash
router.include_router(help_router)

# 7. Admin handler - admin funksiyalari (eng oxirida)
router.include_router(admin_router)

# ================================
# ROUTER STATISTIKASI
# ================================

def get_router_info() -> dict:
    """
    Router haqida ma'lumot qaytarish
    
    Returns:
        dict: Router statistikasi
    """
    return {
        "main_router": "main_router",
        "total_sub_routers": 7,
        "sub_routers": [
            "start_router",
            "menu_router", 
            "order_router",
            "profile_router",
            "payment_router",
            "help_router",
            "admin_router"
        ],
        "description": "Jomeburger bot uchun barcha handler-lar"
    }

# ================================
# ESLATMALAR:
# 
# 1. Handler-lar muhimlik tartibida joylashtirilgan
# 2. Har bir handler alohida fayl va router-da
# 3. Modular struktura - oson maintain qilish uchun
# 4. Professional kod tashkil etish
# 5. 50 yil keyin ham tushunarli bo'lishi uchun izohlanған
# ================================
