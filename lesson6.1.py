import wikipediaapi

import telebot

bot = telebot.TeleBot("6608715523:AAF9rMJd4RPqsLgFxaVTiu9-O0L9sfGLhHE")
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '''Привет рад видеть тебя! Напиши что ищешь в википедии''')




@bot.message_handler(content_types=['text'])
def get_response(message):

    search = message.text.strip().lower()
    wiki_wiki = wikipediaapi.Wikipedia(f'MyProjectName (merlin@example.com)', 'ru')
    page_py = wiki_wiki.page(f'{search}')
    if page_py.exists() == True:
        bot.reply_to(message, f'''{page_py.summary[0:250]} 
{page_py.fullurl}''')
        bot.send_message(message.chat.id, 'Напиши что ищешь в википедии')


    else: bot.reply_to(message, f'Такой страницы не существует')




bot.polling(none_stop=True)