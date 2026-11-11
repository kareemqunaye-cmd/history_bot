import asyncio, os
from google import genai
from google.genai import types
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = os.getenv("TOKEN", "9157462280:AAFLMuaWk760I6n2iNc0HdY3ANI3fNTW80o")
KEY = os.getenv("GEMINI_KEY", "AQ.Ab8RN6IgTlxV343Xf4mxRonB4dGBrlclHj6x9UGX31fe2l0anw")
client = genai.Client(api_key=KEY)
async def start(u,c):
    await u.message.reply_text("شغال! بوت تاريخ أولى ثانوي 🇪🇬 اسألني")
async def answer(u,c):
    p = f"مدرس تاريخ أولى ثانوي، جاوب في سطرين بالعامية المصرية وبس: {u.message.text}"
    try:
        r = client.models.generate_content(model="gemini-2.0-flash-lite", contents=p, config=types.GenerateContentConfig(max_output_tokens=200, temperature=0.2))
        await u.message.reply_text(r.text)
    except:
        await u.message.reply_text("جرب تاني ثانية")
async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer))
    await app.run_polling()
asyncio.run(main())
