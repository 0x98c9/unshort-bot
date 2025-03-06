# URL Unshortener Bot

A Telegram bot that unshortens URLs, revealing the original links behind shortened URLs like `bit.ly`, `tinyurl`, etc.

## 🚀 Features
- Unshortens URLs automatically
- Handles rate limiting (5 requests per minute per user)
- Provides error messages for invalid URLs
- Logs all activities for monitoring

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/0x98c9/url-unshort-bot.git
cd url-unshort-bot
```

### 2️⃣ Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add your bot token:
```ini
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
```
Or set it manually:
```bash
export TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here  # macOS/Linux
set TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here  # Windows
```

### 5️⃣ Run the Bot
```bash
python bot.py
```

## 🖥️ Deploying the Bot

### **Option 1: Railway.app (Recommended)**
1. Connect your GitHub repository to [Railway](https://railway.app/).
2. Add `TELEGRAM_BOT_TOKEN` as an environment variable.
3. Deploy and start the bot!

### **Option 2: Render.com**
1. Connect your GitHub repository to [Render](https://render.com/).
2. Add `TELEGRAM_BOT_TOKEN` as an environment variable.
3. Deploy and start the bot!

### **Option 3: VPS Deployment**
```bash
git clone https://github.com/0x98c9/url-unshort-bot.git
cd url-unshort-bot
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
python bot.py
```
Use `nohup` or `screen` to keep the bot running in the background.

## 📜 License
This project is open-source under the MIT License.

## 💬 Contact
For questions or support, open an issue on GitHub or contact me on Telegram!
