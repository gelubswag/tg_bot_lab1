import telebot
import glob
TOKEN = "" #TOKEN
bot = telebot.TeleBot(TOKEN)

AUDIO_DIR = "audio"
AUDIO_SONGS = {i.replace(f"{AUDIO_DIR}\\","").replace("_"," ").replace(".mp3","") : i for i in glob.glob(f"{AUDIO_DIR}/*.mp3")}
START_MSG = "Лабораторная работа №1"

START_BTNS = [
    ("Работа с изображениями (выслать сгенерированное или готовое по запросу)", "image_button"),# image button
    ("Работа с аудиофайлами (выслать сгенерированный или готовый по запросу)", "audio_button"), # audio button
    ("Получить ссылку на публичный репозиторий с исходниками бота", "source_button") # source button
]

IMG_BTNS = [
    ("Сгенерировать сообщение по запросу", "generate_img"),
    ("Отправить изображение по ссылке", "link_img"),
            ]

AUDIO_BTNS = [
    ("Сгенерировать text-to-speech", "generate_audio"),
    ("Отправить аудио по ссылке", "link_sound")
]

