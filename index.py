from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PreCheckoutQueryHandler
from telegram import Update, Chat, Bot, User, LabeledPrice, Invoice, CallbackQuery, PreCheckoutQuery
from tokenconfig import TOKEN
import urllib3
import logging

Token = TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token=Token)
dispatcher = updater.dispatcher

#start function
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Use: \n /list - to check out the list of available products!')
#start command
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#list function
def list(bot, update):
    # using urllib3 to send multiple photos to user
    http = urllib3.PoolManager()
    urls = ['https://burst.shopifycdn.com/photos/choker-with-triangle_925x.jpg', 'https://burst.shopifycdn.com/photos/blue-gemstone-pendant_925x.jpg']
    itemInUrls = int(len(urls))
    captions = ['product1', 'product2']
    iterations = 0
    while iterations < itemInUrls:
        bot.send_photo(chat_id=update.message.chat_id, photo=urls[iterations], caption=captions[iterations])
        iterations += 1
    # sending additional info
    bot.send_message(chat_id=update.message.chat_id, text='Use: \n /product1 - for more information on product 1 \n /product2 - for more informaitno on product 2')
#list handler
list_handler = CommandHandler('list', list)
dispatcher.add_handler(list_handler)

#product1 function
def product1(bot, update):
    bot.send_invoice(chat_id=update.message.chat_id,
    title='Choker',
    description='This is a choker',
    payload='payload',
    start_parameter='start_parameter',
    currency='SGD',
    prices=[LabeledPrice('Product1', 1200), LabeledPrice('Product1 tax', (100))],
    photo_url='https://burst.shopifycdn.com/photos/choker-with-triangle_925x.jpg',
    photo_width = 100,
    photo_height = 100,
    # need_name=True,
    # need_email=True,
    # send_email_to_provider=True,
    # need_shipping_address=True,
    provider_token='284685063:TEST:NThjMDMyNmE3MDRj')
#product1 handler
product1_handler = CommandHandler('product1', product1)
dispatcher.add_handler(product1_handler)

#answerQuery
def answerQuery(bot, update):
    bot.answer_pre_checkout_query(pre_checkout_query_id=update.pre_checkout_query.id, ok=True)

#PreCheckoutQueryHandler
precheckout_handler = PreCheckoutQueryHandler(answerQuery)
dispatcher.add_handler(precheckout_handler)

updater.start_polling()
