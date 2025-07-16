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
        logging.FileHandler('jomeburger_react.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Bot configuration
BOT_TOKEN = "7342883964:AAHsjK7_pNDAPNVe0sjVS48D2S8sMKGe7D8"
WEBAPP_URL = "https://nurmamatovyoqubjon20022006.github.io/jomeburger-real-delivery-Description/react_app.html"

# Real database simulation
class JomeburgerDatabase:
    def __init__(self):
        self.users = {}
        self.orders = {}
        self.restaurants = {
            1: {"name": "Jomeburger Premium", "status": "open", "rating": 4.8},
            2: {"name": "Pizza Palace", "status": "open", "rating": 4.9},
            3: {"name": "O'zbek Oshxonasi", "status": "open", "rating": 4.7}
        }
        
    def add_user(self, user_id: int, user_data: Dict):
        """Add or update user in database"""
        self.users[user_id] = {
            **user_data,
            'registration_date': datetime.now().isoformat(),
            'orders_count': 0,
            'total_spent': 0
        }
        logger.info(f"✅ User {user_id} added to React database")
        
    def get_user(self, user_id: int) -> Optional[Dict]:
        """Get user from database"""
        return self.users.get(user_id)
        
    def create_order(self, user_id: int, order_data: Dict) -> str:
        """Create new order"""
        order_id = f"REACT{datetime.now().strftime('%Y%m%d%H%M%S')}{user_id}"
        self.orders[order_id] = {
            'user_id': user_id,
            'items': order_data.get('items', []),
            'total': order_data.get('total', 0),
            'status': 'pending',
            'created_at': datetime.now().isoformat(),
            'delivery_address': order_data.get('address', ''),
            'payment_method': order_data.get('payment', 'cash')
        }
        
        if user_id in self.users:
            self.users[user_id]['orders_count'] += 1
            self.users[user_id]['total_spent'] += order_data.get('total', 0)
            
        logger.info(f"🆕 React Order {order_id} created for user {user_id}")
        return order_id

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
dp.include_router(router)

@router.message(CommandStart())
async def start_command(message: types.Message):
    """Handle /start command with React interface"""
    user = message.from_user
    user_id = user.id
    
    logger.info(f"⚛️ User {user_id} (@{user.username}) started React Bot")
    
    # Add user to database
    db.add_user(user_id, {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'language_code': user.language_code
    })
    
    # Create React webapp keyboard
    webapp_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⚛️ React Super App",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ],
            [
                InlineKeyboardButton(
                    text="📋 Buyurtmalar",
                    callback_data="my_orders"
                ),
                InlineKeyboardButton(
                    text="ℹ️ React Info",
                    callback_data="info"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🛠️ React Features",
                    callback_data="features"
                ),
                InlineKeyboardButton(
                    text="⚙️ Sozlamalar",
                    callback_data="settings"
                )
            ]
        ]
    )
    
    welcome_text = f"""⚛️ <b>Jomeburger React Super App ga xush kelibsiz!</b>

👋 Salom, <b>{user.first_name}</b>!

🌟 <b>React JSX Interface:</b>
⚛️ Modern React Components
🎨 Professional UI/UX Design  
🚀 Super Fast Performance
💎 Premium User Experience
🔄 Real-time State Management

🎁 <b>React loyihasi uchun maxsus chegirma!</b>
Promokod: <code>REACT50</code>

👆 <b>React App ni ochish uchun pastdagi tugmani bosing!</b>"""
    
    await message.answer(
        welcome_text,
        reply_markup=webapp_keyboard,
        disable_web_page_preview=True
    )

@router.callback_query(lambda c: c.data == "my_orders")
async def show_my_orders(callback: types.CallbackQuery):
    """Show user orders"""
    user_id = callback.from_user.id
    orders = [order for order in db.orders.values() if order['user_id'] == user_id]
    
    if not orders:
        await callback.answer("❌ Sizda hali React buyurtmalar yo'q!")
        return
        
    orders_text = "📋 <b>React Buyurtmalaringiz:</b>\n\n"
    for i, order in enumerate(orders[-5:], 1):
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
    """Show React app information"""
    info_text = """ℹ️ <b>Jomeburger React App haqida</b>

⚛️ <b>React Technology Stack:</b>
• React 18 - Latest version
• JSX Components - Modern syntax
• Hooks - State management
• Real-time updates

🎯 <b>Features:</b>
• Component-based architecture
• Virtual DOM for performance
• Responsive design
• Modern ES6+ JavaScript

📊 <b>Statistics:</b>
👥 1,000+ React users
🏪 50+ React components
⚡ 99.9% uptime
⭐ 5.0/5 developer rating

🕐 <b>Support:</b> 24/7
📱 <b>Version:</b> React 18.0"""

    await callback.message.edit_text(
        info_text,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🔙 Ortga", callback_data="back_to_main")]
            ]
        )
    )

@router.callback_query(lambda c: c.data == "features")
async def show_features(callback: types.CallbackQuery):
    """Show React features"""
    features_text = """🛠️ <b>React Super Features</b>

⚛️ <b>Core Features:</b>
• JSX Syntax - HTML in JavaScript
• Components - Reusable UI blocks
• Props - Data passing
• State - Dynamic updates
• Hooks - useState, useEffect, useCallback

🎨 <b>UI Components:</b>
• Header - Animated gradient
• SearchBar - Real-time filtering
• Categories - Interactive grid
• RestaurantCard - Hover effects
• BottomNav - Modern navigation

🚀 <b>Performance:</b>
• Virtual DOM diffing
• Optimized re-renders
• Lazy loading
• Memory efficiency

💎 <b>User Experience:</b>
• Smooth animations
• Responsive design
• Touch-friendly interface
• Progressive Web App ready"""

    await callback.message.edit_text(
        features_text,
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
    
    settings_text = f"""⚙️ <b>React App Sozlamalari</b>

👤 <b>Profil:</b>
Ism: {callback.from_user.first_name}
Username: @{callback.from_user.username or 'Noaniq'}
React User: {user_data.get('registration_date', 'Noaniq')[:10] if user_data else 'Noaniq'}

📊 <b>React Statistics:</b>
Buyurtmalar: {user_data.get('orders_count', 0) if user_data else 0}
Sarflangan: {user_data.get('total_spent', 0):,} so'm

⚛️ <b>React Settings:</b>
• Hot Reload: ✅ Enabled
• Dev Tools: ✅ Active  
• JSX Validation: ✅ On
• Performance Mode: 🚀 High"""

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
                    text="⚛️ React Super App",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ],
            [
                InlineKeyboardButton(
                    text="📋 Buyurtmalar",
                    callback_data="my_orders"
                ),
                InlineKeyboardButton(
                    text="ℹ️ React Info",
                    callback_data="info"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🛠️ React Features",
                    callback_data="features"
                ),
                InlineKeyboardButton(
                    text="⚙️ Sozlamalar",
                    callback_data="settings"
                )
            ]
        ]
    )
    
    welcome_text = f"""⚛️ <b>Jomeburger React Super App ga xush kelibsiz!</b>

👋 Salom, <b>{user.first_name}</b>!

🌟 <b>React JSX Interface:</b>
⚛️ Modern React Components
🎨 Professional UI/UX Design  
🚀 Super Fast Performance
💎 Premium User Experience
🔄 Real-time State Management

🎁 <b>React loyihasi uchun maxsus chegirma!</b>
Promokod: <code>REACT50</code>

👆 <b>React App ni ochish uchun pastdagi tugmani bosing!</b>"""
    
    await callback.message.edit_text(
        welcome_text,
        reply_markup=webapp_keyboard
    )

@router.message()
async def handle_webapp_data(message: types.Message):
    """Handle React WebApp data and user messages"""
    user_id = message.from_user.id
    
    # Check if message contains WebApp data
    if message.web_app_data:
        try:
            data = json.loads(message.web_app_data.data)
            logger.info(f"⚛️ React WebApp data received from {user_id}: {data}")
            
            # Process order data
            if data.get('type') == 'order':
                order_id = db.create_order(user_id, data)
                
                await message.answer(
                    f"✅ <b>React buyurtma qabul qilindi!</b>\n\n"
                    f"📋 Buyurtma raqami: <code>{order_id}</code>\n"
                    f"💰 Jami summa: {data.get('total', 0):,} so'm\n"
                    f"⚛️ React Interface orqali\n"
                    f"🕐 Yetkazib berish: 20-30 daqiqa\n\n"
                    f"🤖 React bot operatori tez orada bog'lanadi!"
                )
            else:
                await message.answer("✅ React ma'lumot muvaffaqiyatli yuborildi!")
                
        except json.JSONDecodeError:
            logger.error(f"❌ Invalid JSON data from React user {user_id}")
            await message.answer("❌ React xatolik. Qaytadan urinib ko'ring.")
    else:
        # Handle regular text messages
        text = message.text.lower()
        
        if any(word in text for word in ['react', 'jsx']):
            await message.answer("⚛️ React Super App ishlamoqda! Tugmani bosing!")
        elif any(word in text for word in ['salom', 'hello']):
            await message.answer("👋 Salom! React App ga xush kelibsiz!")
        else:
            await message.answer(
                "⚛️ <b>Jomeburger React Bot</b>\n\n"
                "React buyurtma berish uchun pastdagi tugmani bosing!\n\n"
                "🛠️ <b>React Commands:</b>\n"
                "• /start - React Interface\n"
                "• /menu - React Menu\n"
                "• /features - React Features",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="⚛️ React App",
                                web_app=WebAppInfo(url=WEBAPP_URL)
                            )
                        ]
                    ]
                )
            )

@router.message(Command("menu"))
async def show_menu(message: types.Message):
    """Show React menu"""
    menu_text = """🍽️ <b>React Super Menu</b>

⚛️ <b>React Components Menu:</b>

🍔 <b>FASTFUD COMPONENTS:</b>
• HeaderComponent - 35,000 so'm
• SearchBarComponent - 32,000 so'm
• ButtonComponent - 30,000 so'm

🍕 <b>UI COMPONENTS:</b>
• CardComponent - 45,000 so'm
• GridComponent - 55,000 so'm
• ModalComponent - 60,000 so'm

🍛 <b>HOOK COMPONENTS:</b>
• useState Hook - 28,000 so'm
• useEffect Hook - 32,000 so'm
• useCallback Hook - 25,000 so'm

🎨 <b>STYLING:</b>
• CSS-in-JS - 18,000 so'm
• Styled Components - 22,000 so'm
• Tailwind CSS - 8,000 so'm"""

    await message.answer(
        menu_text,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="⚛️ React App",
                        web_app=WebAppInfo(url=WEBAPP_URL)
                    )
                ]
            ]
        )
    )

async def set_bot_commands():
    """Set bot commands for menu"""
    commands = [
        BotCommand(command="start", description="⚛️ React Interface"),
        BotCommand(command="menu", description="🍽️ React Menu"),
        BotCommand(command="features", description="🛠️ React Features"),
        BotCommand(command="orders", description="📋 React Orders")
    ]
    
    await bot.set_my_commands(commands)
    logger.info("✅ React bot commands set successfully")

async def main():
    """Main function to run the React bot"""
    try:
        logger.info("⚛️ Starting Jomeburger React Bot...")
        
        # Set bot commands
        await set_bot_commands()
        
        # Delete webhook and start polling
        await bot.delete_webhook(drop_pending_updates=True)
        
        logger.info("✅ React Bot started successfully!")
        logger.info(f"🌐 React WebApp URL: {WEBAPP_URL}")
        
        # Start polling
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"❌ Error starting React bot: {e}")
        raise
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 React Bot stopped by user")
    except Exception as e:
        logger.error(f"💥 React Critical error: {e}")
