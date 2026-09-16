import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Welcome to VIP Bonus!\n\n"
        "Access exclusive content, member perks, special offers, and community rewards.\n\n"
        "Commands:\n"
        "/menu - Main menu\n"
        "/benefits - View member benefits\n"
        "/help - Help"
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 VIP Bonus Menu\n\n"
        "🎁 Member Benefits\n"
        "⭐ Exclusive Content\n"
        "🔥 Special Offers\n"
        "🏆 Community Rewards"
    )

async def benefits(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Benefits include:\n"
        "• Exclusive content\n"
        "• Special offers\n"
        "• Community perks\n"
        "• Member rewards"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use /menu to explore VIP Bonus features."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("benefits", benefits))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
