from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    """welcome function"""
    # chat = update.message.chat.id
    
    # create buttons
    btn1 = InlineKeyboardButton(
        text='buyurtmani boshlash', callback_data='buyurtma')
    btn2 = InlineKeyboardButton(
        text='mening savatcham', callback_data='savatcham')
    btn3 = InlineKeyboardButton(
        text='jasmin kontaktlari', callback_data='jasmin kontaktlari')
    btn4 = InlineKeyboardButton(text='sozlamalar', callback_data='sozlamalar')
    btn5 = InlineKeyboardButton(text='aksiyalar', callback_data='aksiyalar')
    btn6 = InlineKeyboardButton(
        text='buyurtmalarim', callback_data='mybooking')

    # create keyboard
    inline_keyboard = [[btn1], [btn2], [btn3], [btn4], [btn5, btn6]]

    # get first name
    first_name = update.message.chat.first_name

    # send message with two buttons
    update.message.reply_html(
        text=f"Hello, <b>{first_name}</b>. Xush Kelibsiz \n Sizni Evropa va Milliy restoranining etkazib berish xizmati kutib oladi Jasmin ☘️ \n Sahifani tanlang 👇🏼",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )


def buyurtma(update: Update, context: CallbackContext):

    
    btn1 = InlineKeyboardButton(
        text='sovuq gazaklar', callback_data='sovuq gazaklar ')
    btn2 = InlineKeyboardButton(
        text='issiq gazaklar', callback_data='issiq gazak')
    btn3 = InlineKeyboardButton(text='biznes lanch', callback_data='lanch')
    btn4 = InlineKeyboardButton(text='salatlar', callback_data='salatlar')
    btn5 = InlineKeyboardButton(text='sho\'rva', callback_data='sho\'rva')
    btn6 = InlineKeyboardButton(
        text='uygur taomlari', callback_data='uygur taomlari')
    btn7 = InlineKeyboardButton(text='milliy taomlar', callback_data='milliy')
    btn8 = InlineKeyboardButton(
        text='evropa taomlari', callback_data='evropa taomlari')
    btn9 = InlineKeyboardButton(text='pizza', callback_data='pizza')
    btn10 = InlineKeyboardButton(
        text='maxsus shefdan', callback_data='maxsus shefdan')
    btn11 = InlineKeyboardButton(text='six kabob', callback_data='six kabob')
    btn12 = InlineKeyboardButton(text='bezaklar', callback_data='bezaklar')
    btn13 = InlineKeyboardButton(text='non', callback_data='non')
    btn14 = InlineKeyboardButton(text='ichimlik', callback_data='ichimlik')
    btn15 = InlineKeyboardButton(text='samsa', callback_data='samsa')
    btn16 = InlineKeyboardButton(text='pivo', callback_data='pivo')
    btn17 = InlineKeyboardButton(text='fast food', callback_data='fast food')

    # create keyboard
    inline_keyboard = [[btn1, btn2], [btn3, btn4], [btn5, btn6], [btn7, btn8], [btn9, btn10], [btn11, btn12],
                       [btn13, btn14], [btn15, btn16], [btn17]]

    # send message with two buttons
    update.callback_query.message.reply_html(

        text=f"<b>Sahifani tanlang👇🏼</b>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )


def kontaktlar(update: Update, context: CallbackContext):
    btn1 = InlineKeyboardButton(text='instagram', url='https://instagram.com')
    btn2 = InlineKeyboardButton(text='kanal', url='https://t.me/Stranger070')
    btn3 = InlineKeyboardButton(
        text='boglanish', url='https://t.me/Stranger070')
    btn4 = InlineKeyboardButton(
        text='tavsiyalash', url='https://t.me/Stranger070')

    # create keyboard
    inline_keyboard = [[btn1, btn2], [btn3, btn4]]

    update.callback_query.message.reply_html(
        text=f"<b>Jasmin restaraunt</b>.\n+998934526621\n +998936252712 \n 🏠 Manzil:  Ул. Амира Темура 202, ориентир «SAMAUTO»\n⏳Ish vaqti:  10:00 - 22:00 (Yopiq) \n👨🏻‍🍳🍢🍲👨🏻‍🍳🍢🍲👨🏻‍🍳🍢🍲👨🏻‍🍳🍢🍲👨🏻‍🍳",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )


def sozlamalar(update: Update, context: CallbackContext):
    btn1 = InlineKeyboardButton(text='русский', callback_data='русский')
    btn2 = InlineKeyboardButton(text='ozbek', callback_data='ozbek')
    inline_keyboard = [[btn1], [btn2]]

    update.callback_query.message.reply_text(

        text=f"tilni tanlang",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )


def aksiyalar(update: Update, context: CallbackContext):
    update.callback_query.message.reply_photo(

        photo=open(file, 'rb'),
        caption=f"Har bir buyurtmangiz bilan birga Sizga raqamli kupon jo’natamiz🎫  \nUshbu kuponlarni to’plang va bir oyda bir marta o’ynaladigan o’yinda 3️⃣  ta mukofotning 🎁 biriga ega bo’ling! \n✔️Har bir ishtirokchi bizning @jasminsamarkand instagram kanalimizga obuna bo’lishi va xabarlarimizni kuzatishi lozim.❗️\nBuyurtma bering va nafaqat mazzali taom, balki qiziqarli mukofotga ega bo’ling ❗️Buyurtma 👇/start")


file = 'img..jpg'


def my_booking(update: Update, context: CallbackContext):

    update.callback_query.message.reply_text(

        text='siz hali buyurtma bermadingiz'
    )

    update.callback_query.message.reply_text(

        text=' 🙂'
    )


def savtchammy(update: Update, context: CallbackContext):
    update.callback_query.answer(

        text='savatchangiz bosh'
    )
