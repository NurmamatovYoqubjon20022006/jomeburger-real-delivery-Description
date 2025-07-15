#!/bin/bash
# Jomeburger Bot Setup Script

echo "🍔 Jomeburger Telegram Bot Setup"
echo "================================"

# Python version check
python_version=$(python3 --version 2>&1)
if [[ $? -ne 0 ]]; then
    echo "❌ Python3 topilmadi. Iltimos Python 3.8+ ni o'rnating."
    exit 1
fi

echo "✅ Python: $python_version"

# Virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Virtual environment yaratilmoqda..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "📥 Dependencies o'rnatilmoqda..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Setup tugallandi!"
echo ""
echo "🔧 Keyingi qadamlar:"
echo "1. @BotFather dan bot token oling"
echo "2. config.py da BOT_TOKEN ni o'zgartiring"
echo "3. python main.py bilan botni ishga tushiring"
echo ""
echo "📱 Web App URL: http://localhost:8000/webapp"
