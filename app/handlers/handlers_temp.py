# 🤖 JOMEBURGER TELEGRAM BOT - HANDLER-LAR ASOSIY FAYLI
# ====================================================
# Bu fayl barcha handler-larni import qilib, bitta router-da birlashtiradi
# Handler - bu foydalanuvchi xabariga javob beradigan funksiya
# 50 yil keyin ham tushunarli bo'lishi uchun har bir qator izohlanган! 🚀

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
    }
