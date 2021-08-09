from telegram import ReplyKeyboardMarkup

from telegram.ext import Updater, CommandHandler

bottons = ReplyKeyboardMarkup(['OmadLotto'],['SharqonaLotto'] repley_keyboard = True)

def start(update, context):
    update.message.reply_text(
    	'Salom{} '. format(update.massage.from_user.first_name), repley_markup = buttons)


updater = Updater('1610242538:AAHxrI8yYjCMftKI-FS-E4hKzdf6NOKPK88', use_context = True)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
