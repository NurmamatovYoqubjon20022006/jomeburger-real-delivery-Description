"""
🚀 JOMEBURGER TELEGRAM BOT - START HANDLER
==========================================

Bu fayl botga /start buyrug'i bilan kirganda ishlaydigan handler-larni o'z ichiga oladi.
Start handler - bu bot bilan tanishishning eng muhim qismi!

50 yil keyin ham tushunarli bo'lishi uchun har bir qator izohlanган! 🎯
"""

import logging
from typing import Union

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

# Local imports
from app.keyboards.main_menu import get_main_menu_keyboard
from app.keyboards.inline import get_welcome_keyboard, get_language_keyboard
from app.services.user import UserService
from app.utils.texts import get_text
from app.states.user import UserRegistrationState

# ================================
# ROUTER YARATISH
# ================================

# Start handler uchun alohida router
start_router = Router(name="start_router")
logger = logging.getLogger(__name__)

# ================================
# START BUYRUG'I HANDLER-I
# ================================

@start_router.message(CommandStart())
async def start_command_handler(message: Message, state: FSMContext) -> None:
    """
    /start buyrug'ini handle qilish
    
    Bu handler quyidagi vazifalarni bajaradi:
    1. Foydalanuvchini ma'lumotlar bazasida tekshiradi
    2. Yangi foydalanuvchi bo'lsa - ro'yxatdan o'tkazadi
    3. Xush kelibsiz xabarini yuboradi
    4. Asosiy menyuni ko'rsatadi
    
    Args:
        message: Telegram xabar obyekti
        state: FSM holati (ro'yxatdan o'tish uchun)
    """
    
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    
    logger.info(f"👤 Start buyrug'i: {user_id} (@{username})")
    
    try:
        # UserService orqali foydalanuvchini tekshirish
        user_service = UserService()
        user = await user_service.get_user_by_telegram_id(user_id)
        
        if user:
            # Mavjud foydalanuvchi - xush kelibsiz xabari
            await handle_existing_user(message, user)
        else:
            # Yangi foydalanuvchi - ro'yxatdan o'tkazish
            await handle_new_user(message, state, {
                'telegram_id': user_id,
                'username': username,
                'first_name': first_name,
                'last_name': last_name
            })
            
    except Exception as e:
        logger.error(f"❌ Start handler-da xatolik: {e}")
        
        # Xatolik bo'lganda oddiy xush kelibsiz xabari
        await message.answer(
            "🤖 <b>Jomeburger-ga xush kelibsiz!</b>\n\n"
            "❗ Hozircha texnik muammolar bor, biroz kuting...",
            reply_markup=get_main_menu_keyboard()
        )


async def handle_existing_user(message: Message, user: dict) -> None:
    """
    Mavjud foydalanuvchi uchun xush kelibsiz xabari
    
    Args:
        message: Telegram xabar obyekti
        user: Foydalanuvchi ma'lumotlari
    """
    
    # Foydalanuvchi ma'lumotlarini olish
    name = user.get('first_name', 'Foydalanuvchi')
    last_order_count = user.get('total_orders', 0)
    
    # Personallashtirilgan xush kelibsiz xabari
    welcome_text = (
        f"🎉 <b>Qaytib kelganingiz bilan, {name}!</b>\n\n"
        f"🍔 <b>Jomeburger</b> - eng mazali fast-food!\n\n"
    )
    
    # Agar oldin buyurtma bergan bo'lsa
    if last_order_count > 0:
        welcome_text += (
            f"📊 Siz bizdan <b>{last_order_count}</b> marta buyurtma bergansingiz.\n"
            f"🎁 Mukofotlar va chegirmalar sizni kutmoqda!\n\n"
        )
    
    welcome_text += (
        "🚀 <b>Nima qilishni xohlaysiz?</b>\n"
        "👇 Pastdagi tugmalardan birini tanlang:"
    )
    
    await message.answer(
        text=welcome_text,
        reply_markup=get_welcome_keyboard(is_registered=True)
    )
    
    logger.info(f"✅ Mavjud foydalanuvchi qarshilanди: {user['telegram_id']}")


async def handle_new_user(message: Message, state: FSMContext, user_data: dict) -> None:
    """
    Yangi foydalanuvchi uchun ro'yxatdan o'tkazish jarayoni
    
    Args:
        message: Telegram xabar obyekti
        state: FSM holati
        user_data: Foydalanuvchi ma'lumotlari
    """
    
    # Xush kelibsiz xabari yangi foydalanuvchi uchun
    welcome_text = (
        f"🎉 <b>Jomeburger-ga xush kelibsiz!</b>\n\n"
        f"👋 Salom, {user_data['first_name']}!\n\n"
        f"🍔 Biz O'zbekistondagi eng yaxshi fast-food yetkazib berish xizmatimiz!\n\n"
        f"✨ <b>Bizda siz quyidagilarni topasiz:</b>\n"
        f"🍟 Eng mazali burgerlar va kartoshka\n"
        f"🥤 Sovuq ichimliklar\n"
        f"🍰 Shirin desertlar\n"
        f"🚚 Tez va bepul yetkazib berish\n\n"
        f"📋 <b>Davom etish uchun ro'yxatdan o'ting:</b>"
    )
    
    # FSM holatini o'rnatish
    await state.set_state(UserRegistrationState.choosing_language)
    await state.update_data(user_data=user_data)
    
    await message.answer(
        text=welcome_text,
        reply_markup=get_language_keyboard()
    )
    
    logger.info(f"👤 Yangi foydalanuvchi ro'yxatdan o'tmoqda: {user_data['telegram_id']}")


# ================================
# TIL TANLASH HANDLER-I
# ================================

@start_router.callback_query(F.data.startswith("lang_"), UserRegistrationState.choosing_language)
async def language_selection_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Til tanlash callback handler-i
    
    Args:
        callback: Callback query obyekti
        state: FSM holati
    """
    
    # Callback data-dan tilni olish
    language_code = callback.data.split("_")[1]  # lang_uz -> uz
    
    logger.info(f"🌐 Til tanlandi: {language_code} - {callback.from_user.id}")
    
    try:
        # Foydalanuvchi ma'lumotlarini state-dan olish
        state_data = await state.get_data()
        user_data = state_data.get('user_data', {})
        user_data['language'] = language_code
        
        # Telefon raqam so'rash holatiga o'tish
        await state.set_state(UserRegistrationState.entering_phone)
        await state.update_data(user_data=user_data)
        
        # Til bo'yicha xabar matnini olish
        phone_text = get_text("request_phone", language_code)
        
        # Telefon raqam so'rash
        from app.keyboards.contact import get_contact_keyboard
        
        await callback.message.edit_text(
            text=phone_text,
            reply_markup=get_contact_keyboard(language_code)
        )
        
        await callback.answer("✅ Til tanlandi!")
        
    except Exception as e:
        logger.error(f"❌ Til tanlashda xatolik: {e}")
        await callback.answer("❌ Xatolik yuz berdi, qaytadan urinib ko'ring")


# ================================
# TELEFON RAQAM HANDLER-I
# ================================

@start_router.message(F.contact, UserRegistrationState.entering_phone)
async def contact_handler(message: Message, state: FSMContext) -> None:
    """
    Telefon raqam handle qilish
    
    Args:
        message: Contact o'z ichiga olgan xabar
        state: FSM holati
    """
    
    contact = message.contact
    phone_number = contact.phone_number
    
    logger.info(f"📞 Telefon raqam qabul qilindi: {phone_number}")
    
    try:
        # State-dan ma'lumotlarni olish
        state_data = await state.get_data()
        user_data = state_data.get('user_data', {})
        user_data['phone_number'] = phone_number
        
        # Foydalanuvchini ma'lumotlar bazasiga saqlash
        user_service = UserService()
        new_user = await user_service.create_user(user_data)
        
        if new_user:
            # Muvaffaqiyatli ro'yxatdan o'tdi
            success_text = get_text("registration_success", user_data.get('language', 'uz'))
            
            await message.answer(
                text=success_text,
                reply_markup=get_main_menu_keyboard(user_data.get('language', 'uz'))
            )
            
            # FSM holatini tozalash
            await state.clear()
            
            logger.info(f"✅ Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi: {user_data['telegram_id']}")
            
        else:
            # Xatolik bo'ldi
            error_text = get_text("registration_error", user_data.get('language', 'uz'))
            await message.answer(error_text)
            
    except Exception as e:
        logger.error(f"❌ Telefon raqam qabul qilishda xatolik: {e}")
        
        # Xatolik xabari
        await message.answer(
            "❌ Ro'yxatdan o'tishda xatolik yuz berdi.\n"
            "Iltimos, qaytadan urinib ko'ring yoki qo'llab-quvvatlash bilan bog'laning."
        )


# ================================
# HELP BUYRUG'I HANDLER-I
# ================================

@start_router.message(Command("help"))
async def help_command_handler(message: Message) -> None:
    """
    /help buyrug'i handler-i
    
    Args:
        message: Telegram xabar obyekti
    """
    
    help_text = (
        "🆘 <b>YORDAM - Jomeburger Bot</b>\n\n"
        
        "📋 <b>Asosiy buyruqlar:</b>\n"
        "/start - Botni qayta ishga tushirish\n"
        "/help - Bu yordam xabari\n"
        "/menu - Mahsulotlar katalogi\n"
        "/orders - Buyurtmalar tarixi\n"
        "/profile - Profil sozlamalari\n\n"
        
        "🍔 <b>Buyurtma berish:</b>\n"
        "1. 'Menyu' tugmasini bosing\n"
        "2. Kategoriyani tanlang\n"
        "3. Mahsulotni tanlang\n"
        "4. Savatga qo'shing\n"
        "5. Buyurtmani tasdiqlang\n\n"
        
        "💳 <b>To'lov usullari:</b>\n"
        "💰 Naqd pul\n"
        "💳 Payme\n"
        "💳 Click\n"
        "💳 Xalqaro kartalar\n\n"
        
        "🚚 <b>Yetkazib berish:</b>\n"
        "📍 Toshkent bo'ylab - BEPUL\n"
        "⏱ Yetkazib berish vaqti: 30-45 daqiqa\n"
        "📞 Kuryerimiz siz bilan bog'lanadi\n\n"
        
        "📞 <b>Qo'llab-quvvatlash:</b>\n"
        "☎️ +998 90 123 45 67\n"
        "🕘 24/7 ishlaymiz\n"
        "💬 @jomeburger_support\n\n"
        
        "❓ Agar savollaringiz bo'lsa, biz bilan bog'laning!"
    )
    
    await message.answer(help_text)
    logger.info(f"ℹ️ Help xabari yuborildi: {message.from_user.id}")


# ================================
# NOMA'LUM XABAR HANDLER-I
# ================================

@start_router.message()
async def unknown_message_handler(message: Message) -> None:
    """
    Noma'lum xabarlarni handle qilish
    
    Bu handler oxirgi handler sifatida ishlatiladi.
    Agar hech qaysi handler xabarni handle qilmasa, bu ishga tushadi.
    
    Args:
        message: Telegram xabar obyekti
    """
    
    logger.info(f"❓ Noma'lum xabar: {message.text} - {message.from_user.id}")
    
    # Dostona javob berish
    response_text = (
        "🤔 <b>Kechirasiz, sizning xabaringizni tushunmadim.</b>\n\n"
        "💡 <b>Quyidagilarni sinab ko'ring:</b>\n"
        "🔸 /help - Yordam olish\n"
        "🔸 /menu - Mahsulotlarni ko'rish\n"
        "🔸 Pastdagi tugmalardan foydalaning\n\n"
        "📞 Yordam kerakmi? @jomeburger_support-ga murojaat qiling!"
    )
    
    await message.answer(
        text=response_text,
        reply_markup=get_main_menu_keyboard()
    )


# ================================
# ESLATMALAR:
# 
# 1. Start handler - botning eng muhim qismi
# 2. Yangi va mavjud foydalanuvchilar uchun alohida flow
# 3. FSM (State Machine) orqali ro'yxatdan o'tish
# 4. Professional error handling
# 5. Batafsil logging barcha harakatlar uchun
# 6. User-friendly xabarlar va interface
# 7. 50 yil keyin ham tushunarli bo'lishi uchun izohlanган
# ================================
