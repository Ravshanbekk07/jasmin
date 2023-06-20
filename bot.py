import os
from telegram.ext import (
    CommandHandler,
   Dispatcher,CallbackQueryHandler

  
)
from telegram import Bot,Update
from callback_functions import (
    start, buyurtma, kontaktlar,sozlamalar,my_booking,aksiyalar,savtchammy

)
from flask import Flask,request

app = Flask(__name__)


TOKEN = os.environ.get('TOKEN')
bot = Bot(TOKEN)




@app.route('/webhook/',methods = ['POST'])
def main():
   
    

   
    disp = Dispatcher(bot,None,workrs = 0)

    data = request.get_json(force=True)
    update = Update.de_json(data=data,bot=bot)

    disp.add_handler(handler=CommandHandler('start', start))
   
    disp.add_handler(handler=CallbackQueryHandler(buyurtma, pattern="buyurtma booking rjhdfjgj"))
    disp.add_handler(handler=CallbackQueryHandler(kontaktlar, pattern="jasmin kontaktlari"))
    disp.add_handler(handler=CallbackQueryHandler(sozlamalar, pattern="sozlamalar"))
    disp.add_handler(handler=CallbackQueryHandler(my_booking, pattern="mybooking"))
    disp.add_handler(handler=CallbackQueryHandler(aksiyalar, pattern="aksiyalar"))
    disp.add_handler(handler=CallbackQueryHandler(savtchammy, pattern="savatcham"))
    

    disp.process_update(update)
    return 'cool'
@app.route('/')
def home():
    return 'runing well'

@app.route('/set-webhook/')
def set_hook():

    r=bot.set_webhook('https://stanger.pythonanywhere.com/webhook/')
    return f'info:{r}'