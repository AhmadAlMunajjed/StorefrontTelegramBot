from flask import Flask, request
from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Dispatcher, CommandHandler, CallbackContext, CallbackQueryHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = '6062355033:AAH3p94pc6sDyFjScmsgV2qL5NHd7Yf9Jh0'
bot = Bot(TOKEN)

app = Flask(__name__)

dispatcher = Dispatcher(bot, None, use_context=True)

def start_command(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query

    query.answer()

    query.edit_message_text(text=f"Selected option: {query.data}")

start_handler = CommandHandler('start', start_command)
button_handler = CallbackQueryHandler(button)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_handler)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

if __name__ == '__main__':
    #should set 5000 on ngrok too
    app.run(port=5000)
