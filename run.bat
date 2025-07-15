@echo off
echo 🚀 Jomeburger Bot ishga tushmoqda...
echo.

REM Virtual environment yaratish va faollashtirish
if not exist venv (
    echo 📦 Virtual environment yaratilmoqda...
    python -m venv venv
)

call venv\Scripts\activate

echo 📥 Dependencies o'rnatilmoqda...
pip install -r requirements.txt

echo.
echo 🤖 Bot ishga tushmoqda...
echo 📱 Web App: http://localhost:8000/webapp
echo ⏹️  To'xtatish uchun Ctrl+C bosing
echo.

python main.py

pause
