from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import Final

TOKEN: Final = '6062355033:AAH3p94pc6sDyFjScmsgV2qL5NHd7Yf9Jh0'
BOT_USERNAME: Final = '@justafakebotfortestingheheboibot'
#https://api.telegram.org/bot6062355033:AAH3p94pc6sDyFjScmsgV2qL5NHd7Yf9Jh0/setWebhook?url=https://abc123.ngrok.io/
#https://api.telegram.org/bot6062355033:AAH3p94pc6sDyFjScmsgV2qL5NHd7Yf9Jh0/setWebhook?url=https://524a-60-51-51-146.ngrok-free.app/6062355033:AAH3p94pc6sDyFjScmsgV2qL5NHd7Yf9Jh0
#LTZYL6IMKQU5XPTXR3BWIIZDSHW7RXIH
app = Flask(__name__)
bot = Bot(TOKEN)
application = Application.builder().token(TOKEN).build()

@app.route('/' + TOKEN, methods=['POST'])
async def webhook():
    update = Update.de_json(request.get_json(), bot)
    await application.process_update(update)
    return 'ok'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Try typing anything and I will do my best to respond!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I\'m good!'

    if 'i love python' in processed:
        return 'Remember to subscribe!'

    return 'I don\'t understand'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == "__main__":
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('custom', custom_command))
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    application.add_error_handler(error)

    app.run(debug=True)
