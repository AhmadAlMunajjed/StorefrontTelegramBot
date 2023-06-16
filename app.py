from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, Dispatcher, CallbackQueryHandler

app = Flask(__name__)

# Replace 'TOKEN' with your Bot's API token
bot = Bot("6000617212:AAFr1D4GbJa95wvKGOCCaYAephdnkxYfpZk")

dispatcher = Dispatcher(bot, None, use_context=True)

def start_handler(update, context):
    keyboard = [[
        InlineKeyboardButton("Tell me a joke", callback_data='joke'),
        InlineKeyboardButton("Say Hi", callback_data='hi')
    ]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Choose an option:", reply_markup=reply_markup)

def button_handler(update, context):
    query = update.callback_query

    query.answer()

    if query.data == 'joke':
        query.edit_message_text(text="Why don't scientists trust atoms? Because they make up everything!")
    elif query.data == 'hi':
        query.edit_message_text(text="Hi there! How can I assist you today?")

def text_handler(update, context):
    text = update.effective_message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"You said: {text}")

start_command_handler = CommandHandler('start', start_handler)
button_handler = CallbackQueryHandler(button_handler)
text_message_handler = MessageHandler(Filters.text & (~Filters.command), text_handler)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(text_message_handler)

@app.route('/' + "6000617212:AAFr1D4GbJa95wvKGOCCaYAephdnkxYfpZk", methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        update = Update.de_json(request.get_json(), bot)
        dispatcher.process_update(update)
    return 'ok'

@app.route('/')
def index():
    return 'Hello!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
