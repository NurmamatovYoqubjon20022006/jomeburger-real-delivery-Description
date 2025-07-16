import asyncio
import logging
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from aiogram.filters import Command, CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('jomeburger_super.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Bot configuration
BOT_TOKEN = "7342883964:AAHsjK7_pNDAPNVe0sjVS48D2S8sMKGe7D8"
WEBAPP_URL = "https://nurmamatovyoqubjon20022006.github.io/jomeburger-real-delivery-Description/super_app.html"

# Real database simulation
class JomeburgerDatabase:
    def __init__(self):
        self.users = {}
        self.orders = {}
        self.restaurants = {
            1: {"name": "Jomeburger Premium", "status": "open", "rating": 4.8},
            2: {"name": "Pizza Palace", "status": "open", "rating": 4.9},
            3: {"name": "O'zbek Oshxonasi", "status": "open", "rating": 4.7},
            4: {"name": "Fresh Zone", "status": "open", "rating": 4.6},
            5: {"name": "Sweet Dreams", "status": "open", "rating": 4.5},
            6: {"name": "Sushi Master", "status": "closed", "rating": 4.8}
        }
        
    def add_user(self, user_id: int, user_data: Dict):
        """Add or update user in database"""
        self.users[user_id] = {
            **user_data,
            'registration_date': datetime.now().isoformat(),
            'orders_count': 0,
            'total_spent': 0
        }
        logger.info(f"✅ User {user_id} added to database")
        
    def get_user(self, user_id: int) -> Optional[Dict]:
        """Get user from database"""
        return self.users.get(user_id)
        
    def create_order(self, user_id: int, order_data: Dict) -> str:
        """Create new order"""
        order_id = f"JMB{datetime.now().strftime('%Y%m%d%H%M%S')}{user_id}"
        self.orders[order_id] = {
            'user_id': user_id,
            'items': order_data.get('items', []),
            'total': order_data.get('total', 0),
            'status': 'pending',
            'created_at': datetime.now().isoformat(),
            'delivery_address': order_data.get('address', ''),
            'payment_method': order_data.get('payment', 'cash')
        }
        
        # Update user stats
        if user_id in self.users:
            self.users[user_id]['orders_count'] += 1
            self.users[user_id]['total_spent'] += order_data.get('total', 0)
            
        logger.info(f"🆕 Order {order_id} created for user {user_id}")
        return order_id
        
    def get_user_orders(self, user_id: int) -> List[Dict]:
        """Get all orders for user"""
        return [order for order in self.orders.values() if order['user_id'] == user_id]

# Initialize database
db = JomeburgerDatabase()

# Initialize bot
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

# Create dispatcher and router
dp = Dispatcher()
router = Router()

# Register router
dp.include_router(router)

@router.message(CommandStart())
async def start_command(message: types.Message):
    """Handle /start command with real functionality"""
    user = message.from_user
    user_id = user.id
    
    logger.info(f"🚀 User {user_id} (@{user.username}) started the bot")
    
    # Add user to database
    db.add_user(user_id, {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'language_code': user.language_code
    })
    
    # Create webapp keyboard
    webapp_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🍔 Jomeburger Super App",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ],
            [
                InlineKeyboardButton(
                    text="📋 Mening buyurtmalarim",
                    callback_data="my_orders"
                ),
                InlineKeyboardButton(
                    text="ℹ️ Ma'lumot",
                    callback_data="info"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📞 Qo'llab-quvvatlash",
                    callback_data="support"
                ),
                InlineKeyboardButton(
                    text="⚙️ Sozlamalar",
                    callback_data="settings"
                )
            ]
        ]
    )
    
    welcome_text = f"""🍔 <b>Jomeburger Super App ga xush kelibsiz!</b>

👋 Salom, <b>{user.first_name}</b>!

🌟 <b>Bizning imkoniyatlar:</b>
🍕 200+ restoran va kafe
🚀 20 daqiqada yetkazib berish
💳 Barcha to'lov usullari
⭐ Eng sifatli taomlar

🎁 <b>Birinchi buyurtma uchun 50% chegirma!</b>
Promokod: <code>JOME50</code>

👆 <b>Pastdagi tugmani bosing va buyurtma bering!</b>"""
    
    await message.answer(
        welcome_text,
        reply_markup=webapp_keyboard,
        disable_web_page_preview=True
    )

@router.callback_query(lambda c: c.data == "my_orders")
async def show_my_orders(callback: types.CallbackQuery):
    """Show user orders"""
    user_id = callback.from_user.id
    orders = db.get_user_orders(user_id)
    
    if not orders:
        await callback.answer("❌ Sizda hali buyurtmalar yo'q!")
        return
        
    orders_text = "📋 <b>Sizning buyurtmalaringiz:</b>\n\n"
    for i, order in enumerate(orders[-5:], 1):  # Show last 5 orders
        status_emoji = {
            'pending': '⏳',
            'confirmed': '✅',
            'preparing': '👨‍🍳',
            'delivering': '🚚',
            'completed': '✅',
            'cancelled': '❌'
        }
        
        orders_text += f"{i}. {status_emoji.get(order['status'], '⏳')} " \
                      f"#{order['created_at'][:10]} - {order['total']:,} so'm\n"
    
    await callback.message.edit_text(
        orders_text,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🔙 Ortga", callback_data="back_to_main")]
            ]
        )
    )

@router.callback_query(lambda c: c.data == "info")
async def show_info(callback: types.CallbackQuery):
    """Show app information"""
    info_text = """ℹ️ <b>Jomeburger Super App haqida</b>

🎯 <b>Bizning missiya:</b>
Eng tez va sifatli ovqat yetkazib berish xizmati

📊 <b>Statistika:</b>
👥 1,000,000+ foydalanuvchi
🏪 200+ restoran hamkori
🍕 10,000+ taom turi
⭐ 4.8/5 o'rtacha baho

🕐 <b>Ish vaqti:</b>
24/7 - doimo sizning xizmatingizda!

📱 <b>Versiya:</b> 2.0 Super Edition
🔄 <b>Oxirgi yangilanish:</b> 2025-01-16"""

    await callback.message.edit_text(
        info_text,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🔙 Ortga", callback_data="back_to_main")]
            ]
        )
    )

@router.callback_query(lambda c: c.data == "support")
async def show_support(callback: types.CallbackQuery):
    """Show support information"""
    support_text = """📞 <b>Qo'llab-quvvatlash xizmati</b>

🕐 <b>Ish vaqti:</b> 24/7

📞 <b>Telefon:</b> +998 90 123 45 67
💬 <b>Telegram:</b> @JomeburgerSupport
📧 <b>Email:</b> support@jomeburger.uz

❓ <b>Tez-tez so'raladigan savollar:</b>

<b>Q:</b> Yetkazib berish qancha vaqt oladi?
<b>A:</b> O'rtacha 20-30 daqiqa

<b>Q:</b> Minimum buyurtma summasi?
<b>A:</b> 50,000 so'm

<b>Q:</b> To'lov usullari?
<b>A:</b> Naqd, karta, Click, Payme"""

    await callback.message.edit_text(
        support_text,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🔙 Ortga", callback_data="back_to_main")]
            ]
        )
    )

@router.callback_query(lambda c: c.data == "settings")
async def show_settings(callback: types.CallbackQuery):
    """Show settings menu"""
    user_id = callback.from_user.id
    user_data = db.get_user(user_id)
    
    settings_text = f"""⚙️ <b>Sozlamalar</b>

👤 <b>Profil ma'lumotlari:</b>
Ism: {callback.from_user.first_name}
Username: @{callback.from_user.username or 'Noaniq'}
Ro'yxatdan o'tgan: {user_data.get('registration_date', 'Noaniq')[:10] if user_data else 'Noaniq'}

📊 <b>Statistika:</b>
Buyurtmalar soni: {user_data.get('orders_count', 0) if user_data else 0}
Jami sarflangan: {user_data.get('total_spent', 0):,} so'm

🔧 <b>Parametrlar:</b>
• Bildirishnomalar: ✅ Yoqilgan
• Til: 🇺🇿 O'zbek
• Lokatsiya: 📍 Toshkent"""

    await callback.message.edit_text(
        settings_text,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🔙 Ortga", callback_data="back_to_main")]
            ]
        )
    )

@router.callback_query(lambda c: c.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    """Return to main menu"""
    user = callback.from_user
    
    webapp_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🍔 Jomeburger Super App",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ],
            [
                InlineKeyboardButton(
                    text="📋 Mening buyurtmalarim",
                    callback_data="my_orders"
                ),
                InlineKeyboardButton(
                    text="ℹ️ Ma'lumot",
                    callback_data="info"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📞 Qo'llab-quvvatlash",
                    callback_data="support"
                ),
                InlineKeyboardButton(
                    text="⚙️ Sozlamalar",
                    callback_data="settings"
                )
            ]
        ]
    )
    
    welcome_text = f"""🍔 <b>Jomeburger Super App ga xush kelibsiz!</b>

👋 Salom, <b>{user.first_name}</b>!

🌟 <b>Bizning imkoniyatlar:</b>
🍕 200+ restoran va kafe
🚀 20 daqiqada yetkazib berish
💳 Barcha to'lov usullari
⭐ Eng sifatli taomlar

🎁 <b>Birinchi buyurtma uchun 50% chegirma!</b>
Promokod: <code>JOME50</code>

👆 <b>Pastdagi tugmani bosing va buyurtma bering!</b>"""
    
    await callback.message.edit_text(
        welcome_text,
        reply_markup=webapp_keyboard
    )

@router.message()
async def handle_webapp_data(message: types.Message):
    """Handle WebApp data and user messages"""
    user_id = message.from_user.id
    
    # Check if message contains WebApp data
    if message.web_app_data:
        try:
            data = json.loads(message.web_app_data.data)
            logger.info(f"📱 WebApp data received from {user_id}: {data}")
            
            # Process order data
            if data.get('type') == 'order':
                order_id = db.create_order(user_id, data)
                
                await message.answer(
                    f"✅ <b>Buyurtma qabul qilindi!</b>\n\n"
                    f"📋 Buyurtma raqami: <code>{order_id}</code>\n"
                    f"💰 Jami summa: {data.get('total', 0):,} so'm\n"
                    f"🕐 Yetkazib berish vaqti: 20-30 daqiqa\n\n"
                    f"📞 Bizning operator tez orada siz bilan bog'lanadi!"
                )
            else:
                await message.answer("✅ Ma'lumot muvaffaqiyatli yuborildi!")
                
        except json.JSONDecodeError:
            logger.error(f"❌ Invalid JSON data from {user_id}")
            await message.answer("❌ Xatolik yuz berdi. Qaytadan urinib ko'ring.")
    else:
        # Handle regular text messages
        text = message.text.lower()
        
        if any(word in text for word in ['salom', 'hello', 'hi']):
            await message.answer("👋 Salom! Buyurtma berish uchun pastdagi tugmani bosing!")
        elif any(word in text for word in ['rahmat', 'thanks']):
            await message.answer("🤗 Marhamat! Har doim xizmatdamiz!")
        elif any(word in text for word in ['yordam', 'help']):
            await message.answer(
                "❓ <b>Yordam kerakmi?</b>\n\n"
                "• Buyurtma berish uchun: 🍔 Jomeburger Super App tugmasini bosing\n"
                "• Qo'llab-quvvatlash: /support\n"
                "• Ma'lumot: /info"
            )
        else:
            # Default response
            await message.answer(
                "🤖 <b>Jomeburger Super Bot</b>\n\n"
                "Buyurtma berish uchun pastdagi tugmani bosing yoki quyidagi buyruqlardan foydalaning:\n\n"
                "• /start - Asosiy menyu\n"
                "• /menu - Taomlar ro'yxati\n"
                "• /orders - Buyurtmalarim\n"
                "• /support - Yordam",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="🍔 Buyurtma berish",
                                web_app=WebAppInfo(url=WEBAPP_URL)
                            )
                        ]
                    ]
                )
            )

@router.message(Command("menu"))
async def show_menu(message: types.Message):
    """Show restaurant menu"""
    menu_text = """🍽️ <b>Jomeburger Super Menu</b>

🍔 <b>FASTFUD:</b>
• Big Jome Burger - 35,000 so'm
• Cheese Deluxe - 32,000 so'm
• BBQ Chicken - 30,000 so'm

🍕 <b>PIZZA:</b>
• Margherita Classic - 45,000 so'm
• Pepperoni Supreme - 55,000 so'm
• Hawaiian Paradise - 60,000 so'm

🍛 <b>MILLIY TAOMLAR:</b>
• Toshkent Oshi - 28,000 so'm
• Manti - 32,000 so'm
• Lag'mon - 25,000 so'm

🥤 <b>ICHIMLIKLAR:</b>
• Orange Fresh - 18,000 so'm
• Berry Smoothie - 22,000 so'm
• Cola Classic - 8,000 so'm

🍰 <b>SHIRINLIKLAR:</b>
• Chocolate Cake - 35,000 so'm
• Tiramisu - 28,000 so'm
• Ice Cream - 15,000 so'm"""

    await message.answer(
        menu_text,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🛒 Buyurtma berish",
                        web_app=WebAppInfo(url=WEBAPP_URL)
                    )
                ]
            ]
        )
    )

async def set_bot_commands():
    """Set bot commands for menu"""
    commands = [
        BotCommand(command="start", description="🏠 Asosiy menyu"),
        BotCommand(command="menu", description="🍽️ Taomlar ro'yxati"),
        BotCommand(command="orders", description="📋 Mening buyurtmalarim"),
        BotCommand(command="support", description="📞 Qo'llab-quvvatlash"),
        BotCommand(command="info", description="ℹ️ Ma'lumot")
    ]
    
    await bot.set_my_commands(commands)
    logger.info("✅ Bot commands set successfully")

async def main():
    """Main function to run the bot"""
    try:
        logger.info("🚀 Starting Jomeburger Super Bot...")
        
        # Set bot commands
        await set_bot_commands()
        
        # Delete webhook and start polling
        await bot.delete_webhook(drop_pending_updates=True)
        
        logger.info("✅ Bot started successfully!")
        logger.info(f"🌐 WebApp URL: {WEBAPP_URL}")
        
        # Start polling
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"❌ Error starting bot: {e}")
        raise
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"💥 Critical error: {e}")
