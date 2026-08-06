import asyncio
from rubka import Robot

# توکن ربات روبیکا را اینجا قرار دهید
TOKEN = "BJAGFE0AVAZUFDXTFIYQRPKPOBEUTVMRTUNRPDLXXWNYUBEVEJZFEGQHTWPJFTHE"

bot = Robot(TOKEN)

@bot.on_message()
async def handle_message(message):
    # چک کردن وجود متن در پیام برای جلوگیری از خطا هنگام ارسال استیکر یا فایل
    if message.text:
        await message.reply("پیام دریافت شد")

async def main():
    print("ربات با موفقیت روشن شد و آماده دریافت پیام است...")
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
