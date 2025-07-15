# 🔧 JOMEBURGER TELEGRAM BOT KONFIGURATSIYA
# Bu fayl botning barcha sozlamalarini o'z ichiga oladi
# Environment variables orqali production/development sozlamalari boshqariladi
# 50 yil keyin ham tushunarli bo'lishi uchun har bir parametr izohlanган! 🚀

import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field, validator


class Settings(BaseSettings):
    """
    Telegram bot uchun barcha sozlamalar sinfi
    Bu sinf environment variables-dan sozlamalarni o'qiydi
    Va ularga type validation qo'llaydi
    """
    
    # ================================
    # TELEGRAM BOT SOZLAMALARI
    # ================================
    
    # Telegram bot token - BotFather-dan olinadi
    # Misol: 1234567890:ABCDEFGHijklmnopqrstuvwxyz1234567890
    BOT_TOKEN: str = Field(
        ...,  # majburiy parametr
        description="Telegram bot token BotFather-dan olingan",
        min_length=45,  # telegram token minimum uzunligi
        max_length=50   # telegram token maksimum uzunligi
    )
    
    # Bot nomi - loglar va identifikatsiya uchun
    BOT_NAME: str = Field(
        default="JomeBurger Bot",
        description="Bot rasmiy nomi"
    )
    
    # Bot username - @jomeburger_bot kabi
    BOT_USERNAME: str = Field(
        default="jomeburger_bot",
        description="Bot username @ belgisisiz"
    )
    
    # Webhook URL - production uchun webhook mode
    # Development-da None qilib webhook o'chiriladi
    WEBHOOK_URL: Optional[str] = Field(
        default=None,
        description="Production uchun webhook URL"
    )
    
    # Webhook path - webhook endpoint
    WEBHOOK_PATH: str = Field(
        default="/webhook",
        description="Webhook endpoint path"
    )
    
    # Web app URL - web server porti
    WEBAPP_HOST: str = Field(
        default="0.0.0.0",
        description="Web app host IP manzili"
    )
    
    WEBAPP_PORT: int = Field(
        default=8000,
        description="Web app port raqami",
        ge=1000,  # minimum 1000
        le=65535  # maksimum 65535
    )
    
    # ================================
    # MA'LUMOTLAR BAZASI SOZLAMALARI
    # ================================
    
    # PostgreSQL ma'lumotlar bazasi URL
    # Format: postgresql+asyncpg://user:password@host:port/database
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://jomeburger:secret123@localhost:5432/jomeburger_bot",
        description="PostgreSQL ma'lumotlar bazasi URL"
    )
    
    # Ma'lumotlar bazasi connection pool sozlamalari
    DB_POOL_SIZE: int = Field(
        default=20,
        description="Ma'lumotlar bazasi connection pool o'lchami",
        ge=1,
        le=100
    )
    
    DB_MAX_OVERFLOW: int = Field(
        default=30,
        description="Ma'lumotlar bazasi connection pool maksimum overflow",
        ge=0,
        le=100
    )
    
    # ================================
    # REDIS CACHE SOZLAMALARI
    # ================================
    
    # Redis server sozlamalari
    REDIS_HOST: str = Field(
        default="localhost",
        description="Redis server host"
    )
    
    REDIS_PORT: int = Field(
        default=6379,
        description="Redis server port",
        ge=1,
        le=65535
    )
    
    # Redis ma'lumotlar bazasi raqami (0-15)
    REDIS_DB: int = Field(
        default=0,
        description="Redis database raqami",
        ge=0,
        le=15
    )
    
    # Redis parol (production uchun majburiy)
    REDIS_PASSWORD: Optional[str] = Field(
        default=None,
        description="Redis server paroli"
    )
    
    # Redis URL (to'liq format)
    @property
    def REDIS_URL(self) -> str:
        """Redis URL ni qaytaradi"""
        if self.REDIS_PASSWORD:
            return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
    
    # ================================
    # BACKEND API SOZLAMALARI
    # ================================
    
    # Backend API base URL
    API_BASE_URL: str = Field(
        default="http://localhost:8001/api/v1",
        description="Backend API asosiy URL"
    )
    
    # API timeout (soniyalarda)
    API_TIMEOUT: int = Field(
        default=30,
        description="API so'rovlar uchun timeout",
        ge=5,
        le=300
    )
    
    # API retry count - xato bo'lganda necha marta takrorlash
    API_RETRY_COUNT: int = Field(
        default=3,
        description="API xatolik bo'lganda takrorlash soni",
        ge=0,
        le=10
    )
    
    # ================================
    # XAVFSIZLIK SOZLAMALARI
    # ================================
    
    # JWT secret key - token yaratish uchun
    JWT_SECRET_KEY: str = Field(
        default="your-super-secret-jwt-key-change-in-production",
        description="JWT token uchun secret key",
        min_length=32
    )
    
    # JWT token muddati (minutlarda)
    JWT_EXPIRE_MINUTES: int = Field(
        default=1440,  # 24 soat
        description="JWT token amal qilish muddati (minutlarda)",
        ge=30,
        le=10080  # 1 hafta
    )
    
    # Admin foydalanuvchilar ro'yxati (Telegram ID)
    ADMIN_USER_IDS: list[int] = Field(
        default=[],
        description="Admin foydalanuvchilar Telegram ID ro'yxati"
    )
    
    # ================================
    # TO'LOV TIZIMLARI SOZLAMALARI
    # ================================
    
    # Stripe to'lov tizimi
    STRIPE_SECRET_KEY: Optional[str] = Field(
        default=None,
        description="Stripe secret key"
    )
    
    STRIPE_PUBLISHABLE_KEY: Optional[str] = Field(
        default=None,
        description="Stripe publishable key"
    )
    
    # Payme to'lov tizimi (O'zbekiston)
    PAYME_MERCHANT_ID: Optional[str] = Field(
        default=None,
        description="Payme merchant ID"
    )
    
    PAYME_SECRET_KEY: Optional[str] = Field(
        default=None,
        description="Payme secret key"
    )
    
    # Click to'lov tizimi (O'zbekiston)
    CLICK_MERCHANT_ID: Optional[str] = Field(
        default=None,
        description="Click merchant ID"
    )
    
    CLICK_SECRET_KEY: Optional[str] = Field(
        default=None,
        description="Click secret key"
    )
    
    # ================================
    # FAYL VA MEDIA SOZLAMALARI
    # ================================
    
    # Media fayllar uchun maksimum o'lcham (baytlarda)
    MAX_FILE_SIZE: int = Field(
        default=50 * 1024 * 1024,  # 50 MB
        description="Maksimum fayl o'lchami (baytlarda)",
        ge=1024,  # minimum 1 KB
        le=100 * 1024 * 1024  # maksimum 100 MB
    )
    
    # Qo'llab-quvvatlanadigan fayl turlari
    ALLOWED_FILE_TYPES: list[str] = Field(
        default=["jpg", "jpeg", "png", "gif", "webp", "pdf"],
        description="Qo'llab-quvvatlanadigan fayl turlari"
    )
    
    # Media fayllar saqlanadigan papka
    MEDIA_ROOT: str = Field(
        default="./media",
        description="Media fayllar saqlanadigan papka"
    )
    
    # ================================
    # LOGGING SOZLAMALARI
    # ================================
    
    # Log darajasi (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    LOG_LEVEL: str = Field(
        default="INFO",
        description="Logging darajasi"
    )
    
    # Log fayl nomi
    LOG_FILE: str = Field(
        default="jomeburger_bot.log",
        description="Log fayl nomi"
    )
    
    # Log faylning maksimum o'lchami (MB)
    LOG_MAX_SIZE: int = Field(
        default=100,
        description="Log fayl maksimum o'lchami (MB)",
        ge=1,
        le=1000
    )
    
    # Saqlanadigan log fayllar soni
    LOG_BACKUP_COUNT: int = Field(
        default=5,
        description="Saqlanadigan log fayllar soni",
        ge=1,
        le=20
    )
    
    # ================================
    # PERFORMANCE VA OPTIMIZATSIYA
    # ================================
    
    # Foydalanuvchi so'rovlari uchun rate limiting
    RATE_LIMIT_PER_MINUTE: int = Field(
        default=60,
        description="Daqiqada maksimum so'rovlar soni (foydalanuvchi uchun)",
        ge=1,
        le=1000
    )
    
    # Cache muddati (soniyalarda)
    CACHE_TTL: int = Field(
        default=3600,  # 1 soat
        description="Cache ma'lumotlar muddati (soniyalarda)",
        ge=60,
        le=86400  # 24 soat
    )
    
    # ================================
    # XALQARO SOZLAMALAR
    # ================================
    
    # Default til
    DEFAULT_LANGUAGE: str = Field(
        default="uz",
        description="Default til kodi (uz, ru, en)"
    )
    
    # Qo'llab-quvvatlanadigan tillar
    SUPPORTED_LANGUAGES: list[str] = Field(
        default=["uz", "ru", "en"],
        description="Qo'llab-quvvatlanadigan tillar ro'yxati"
    )
    
    # Vaqt zonasi
    TIMEZONE: str = Field(
        default="Asia/Tashkent",
        description="Vaqt zonasi"
    )
    
    # ================================
    # DEVELOPMENT SOZLAMALARI
    # ================================
    
    # Development mode (test rejimi)
    DEBUG: bool = Field(
        default=False,
        description="Development/Debug rejimi"
    )
    
    # Test rejimida ishlatish uchun
    TESTING: bool = Field(
        default=False,
        description="Test rejimi"
    )
    
    # ================================
    # VALIDATORLAR
    # ================================
    
    @validator('BOT_TOKEN')
    def validate_bot_token(cls, v):
        """Bot token formatini tekshirish"""
        if not v or ':' not in v:
            raise ValueError('Bot token noto\'g\'ri formatda. BotFather-dan to\'g\'ri token oling.')
        return v
    
    @validator('ADMIN_USER_IDS', pre=True)
    def validate_admin_ids(cls, v):
        """Admin ID larni tekshirish"""
        if isinstance(v, str):
            # String formatda bo'lsa, vergul bilan ajratib ro'yxatga aylantirish
            return [int(x.strip()) for x in v.split(',') if x.strip()]
        return v
    
    @validator('LOG_LEVEL')
    def validate_log_level(cls, v):
        """Log darajasini tekshirish"""
        allowed_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if v.upper() not in allowed_levels:
            raise ValueError(f'Log darajasi {allowed_levels} dan biri bo\'lishi kerak')
        return v.upper()
    
    # ================================
    # CLASS META SOZLAMALAR
    # ================================
    
    class Config:
        """Pydantic konfiguratsiya"""
        # .env fayldan o'qish
        env_file = ".env"
        env_file_encoding = "utf-8"
        # Environment variable prefixi
        env_prefix = "JOMEBURGER_"
        # Case sensitive emas
        case_sensitive = False
        # Extra fieldlarga ruxsat bermaslik
        extra = "forbid"
        # Validation batafsil
        validate_assignment = True


# Global sozlamalar obyekti
# Bu obyekt loyiha bo'ylab ishlatiladi
settings = Settings()


# ================================
# HELPER FUNKSIYALAR
# ================================

def is_admin(user_id: int) -> bool:
    """
    Foydalanuvchi admin ekanligini tekshirish
    
    Args:
        user_id: Telegram foydalanuvchi ID si
        
    Returns:
        bool: Admin bo'lsa True, aks holda False
    """
    return user_id in settings.ADMIN_USER_IDS


def get_database_url() -> str:
    """
    Ma'lumotlar bazasi URL ni qaytarish
    
    Returns:
        str: Database URL
    """
    return settings.DATABASE_URL


def get_api_url(endpoint: str) -> str:
    """
    API endpoint uchun to'liq URL yaratish
    
    Args:
        endpoint: API endpoint (masalan: /users/me)
        
    Returns:
        str: To'liq API URL
    """
    return f"{settings.API_BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}"


# ================================
# ESLATMA: Bu konfiguratsiya fayli professional production loyiha uchun yaratilgan
# Barcha parametrlar batafsil izohlanган va type validation qo'shilgan
# Environment variables orqali har xil muhitlarda ishlaydi
# 50 yil keyin ham tushunarli bo'lishi uchun har bir qator izohlanган! 🎯
# ================================
