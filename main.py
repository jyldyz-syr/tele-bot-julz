from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes 

TOKEN: Final ='6617048356:AAFsMXDH1oSFS4VXryQ73UWz7dPdXqtijN8'
BOT_USERNAME: Final = '@ulzyyy_bot'




# Commands
async def start_command(update: Update, cotext: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello thanks for chatting with me, I am Julz and I love chatting!")


async def help_command(update: Update, cotext: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey, type something so I can respond")


async def custom_command(update: Update, cotext: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")



# Responses

def handle_response(text: str)-> str:
     processed: str = text.lower()
     if 'hello' in processed:
         return 'hey there'
     if 'how are you' in processed:
         return 'good thanks!'
     if 'can we talk' in processed :
         return 'Absolutely!'
     return 'I do not understand, please try agian!'
     


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text:  str = update.message.text

    print(f'User({update.message.id}) in {message_type}: "{text}")')
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


# Logging Errors
 
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':

    print('Starting Bot')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)
    print('Polling') 
    app.run_polling(poll_interval=3)

