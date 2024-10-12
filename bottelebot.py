import telebot
from cfg import *
import MukeshAPI
import gtts
import glob

""""IMAGE START"""
def gen_img(msg):
        
    try:
        img = MukeshAPI.api.ai_image(msg.text)
        bot.send_photo(msg.chat.id, img, msg.text)
        return
    except:
        bot.send_message(msg.chat.id,"Не удалось отправить изображение")
        bot.register_next_step_handler(msg, gen_img)
        
def send_img(msg):
    
    try:
        bot.send_photo(msg.chat.id, msg.text)
        return
    except Exception as ex:
        bot.send_message(msg.chat.id,f"Не удалось отправить изображение: {ex}")
        bot.register_next_step_handler(msg, send_img)
        
@bot.callback_query_handler(func=lambda call: call.data == IMG_BTNS[1][1])
def link(call:telebot.types.CallbackQuery):
    msg = call.message
    bot.edit_message_text("Отправьте ссылку", msg.chat.id,msg.id)
    bot.register_next_step_handler(msg, send_img)

@bot.callback_query_handler(func=lambda call: call.data == IMG_BTNS[0][1])
def link(call:telebot.types.CallbackQuery):
    msg = call.message
    bot.edit_message_text("Отправьте запрос", msg.chat.id,msg.id)
    bot.register_next_step_handler(msg, gen_img)
# image
@bot.callback_query_handler(func=lambda call: call.data == START_BTNS[0][1])
def image_btn(call:telebot.types.CallbackQuery):
    msg = call.message
    keyboard = telebot.types.InlineKeyboardMarkup()
    buttons = [telebot.types.InlineKeyboardButton(text=text, callback_data=callback_data) for text, callback_data in IMG_BTNS]
    keyboard.add(*buttons)
    bot.edit_message_text("Работа с изображением", msg.chat.id,msg.id,reply_markup=keyboard)
"""IMAGE END"""


"""AUDIO START"""
def send_audio(msg:telebot.types.Message):
    try:
        bot.send_audio(chat_id=msg.chat.id,audio=msg.text)
    except Exception as ex:
        bot.send_message(msg.chat.id,f"Не удалось отправить аудио: {ex}")
        bot.register_next_step_handler(msg, send_audio)

@bot.callback_query_handler(func=lambda call: call.data == AUDIO_BTNS[1][1])
def audios(call:telebot.types.CallbackQuery):
    msg = call.message

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(*[telebot.types.InlineKeyboardButton(i,callback_data=i) for i in AUDIO_SONGS.keys()])
    bot.edit_message_text("Выберите аудио", msg.chat.id,msg.id,reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in AUDIO_SONGS.keys())
def send_audio(call):
    msg = call.message
    bot.delete_message(msg.chat.id,msg.id)
    with open(f"{AUDIO_SONGS[call.data]}", "rb") as f: bot.send_audio(msg.chat.id,f.read())

def gen_audio(msg:telebot.types.Message):
    try:
        tts = gtts.gTTS(text=msg.text, lang='en')
        tts.save("req.mp3")
        with open("req.mp3","rb") as f: bot.send_audio(chat_id=msg.chat.id,audio=f)
    except Exception as ex:
        bot.send_message(msg.chat.id,f"Не удалось отправить аудио: {ex}")
        bot.register_next_step_handler(msg, gen_audio)

@bot.callback_query_handler(func=lambda call: call.data == AUDIO_BTNS[0][1])
def tts_audio(call:telebot.types.CallbackQuery):
    msg = call.message
    bot.edit_message_text("Отправьте text-to-speech", msg.chat.id,msg.id)
    bot.register_next_step_handler(msg, gen_audio)

@bot.callback_query_handler(func=lambda call: call.data == START_BTNS[1][1])
def audio_btn(call:telebot.types.CallbackQuery):
    msg = call.message
    keyboard = telebot.types.InlineKeyboardMarkup()
    buttons = [telebot.types.InlineKeyboardButton(text=text, callback_data=callback_data) for text, callback_data in AUDIO_BTNS]
    keyboard.add(*buttons)
    bot.edit_message_text("Работа с изображением", msg.chat.id,msg.id,reply_markup=keyboard)
"""AUDIO END"""
@bot.callback_query_handler(func=lambda call: call.data == START_BTNS[2][1])
def scource_btn(call:telebot.types.CallbackQuery):
    msg = call.message
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text=f"Перейти в репозиторий", url=REP_URL)
    keyboard.add(button)
    bot.edit_message_text(REP_URL, msg.chat.id,msg.id,reply_markup=keyboard)
"""REP START"""
"""REP END"""
@bot.message_handler(commands=["start"])
def start(msg:telebot.types.Message):
    chat_id = msg.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    buttons = [telebot.types.InlineKeyboardButton(text=text, callback_data=callback_data) for text, callback_data in START_BTNS]
    keyboard.add(*buttons)
    return bot.send_message(chat_id,
                            START_MSG,
                            reply_markup= keyboard)

# @bot.message_handler(content_types=START_BTNS)
# def
bot.polling()