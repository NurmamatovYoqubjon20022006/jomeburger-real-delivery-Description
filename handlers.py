"""
Jomeburger Bot Handlers
"""

from aiogram import types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from main import dp, WEBAPP_HOST, WEBAPP_PORT

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    """Start command handler"""
    webapp_url = f"http://{WEBAPP_HOST}:{WEBAPP_PORT}/webapp"
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🍔 Jomeburger Ochish", 
            web_app=WebAppInfo(url=webapp_url)
        )],
        [InlineKeyboardButton(text="📞 Qo'llab-quvvatlash", callback_data="support")]
    ])
    
    await message.answer(
        "🍔 <b>Jomeburger-ga xush kelibsiz!</b>\n\n"
        "🚀 Eng mazali fast-food yetkazib berish xizmati\n"
        "⚡ 30-45 daqiqada yetkazib beramiz\n"
        "🆓 Toshkent bo'ylab bepul yetkazib berish\n\n"
        "👇 Buyurtma berish uchun tugmani bosing:",
        reply_markup=keyboard
    )

@dp.message(Command("menu"))
async def menu_handler(message: types.Message):
    """Menu command handler"""
    webapp_url = f"http://{WEBAPP_HOST}:{WEBAPP_PORT}/webapp"
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🍽️ Menyu ochish", 
            web_app=WebAppInfo(url=webapp_url)
        )]
    ])
    
    await message.answer(
        "🍽️ <b>Bizning menyu:</b>\n\n"
        "🍔 Burgerlar - 25,000 so'mdan\n"
        "🍕 Pizzalar - 40,000 so'mdan\n"
        "🥤 Ichimliklar - 8,000 so'mdan\n"
        "🍰 Desertlar - 12,000 so'mdan\n\n"
        "👇 To'liq menyuni ko'rish uchun:",
        reply_markup=keyboard
    )

@dp.callback_query(F.data == "support")
async def support_handler(callback: types.CallbackQuery):
    """Support callback handler"""
    await callback.message.answer(
        "📞 <b>Qo'llab-quvvatlash</b>\n\n"
        "☎️ Telefon: +998 90 123 45 67\n"
        "💬 Telegram: @jomeburger_support\n"
        "⏰ Ish vaqti: 24/7\n\n"
        "📋 Savol yoki muammo bo'lsa, biz bilan bog'laning!"
    )
    await callback.answer()

@dp.message(F.web_app_data)
async def web_app_handler(message: types.Message):
    """Web app data handler"""
    import json
    
    try:
        data = json.loads(message.web_app_data.data)
        action = data.get('action')
        
        if action == 'add_to_cart':
            food_id = data.get('food_id')
            await message.answer(f"✅ Mahsulot savatga qo'shildi: {food_id}")
        
        elif action == 'open_orders':
            await message.answer("📋 Buyurtmalar tarixi bo'sh")
        
        elif action == 'open_addresses':
            await message.answer("📍 Saqlangan manzillar yo'q")
        
        elif action == 'open_payments':
            await message.answer("💳 To'lov usullari: Naqd, Payme, Click")
        
        elif action == 'open_settings':
            await message.answer("⚙️ Sozlamalar: Til, Bildirishnomalar")
        
        elif action == 'open_support':
            await message.answer("📞 Qo'llab-quvvatlash bilan bog'lanish")
            
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi")
