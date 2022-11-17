import requests
import telebot
import io

def finder(req):
    req = req.replace(' ','+').lower()

    user_headers = {
        'User-Agent': 'PostmanRuntime/7.29.2',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin'
    }

    url_req = 'https://musicstax.com/search?q=' + req
    
    session = requests.session()

    response = session.get(url_req).text.splitlines() 

    i = 0
    while i < len(response):
        if response[i].startswith('<a data-cy="song-image" class="song-image search-image" href="/') is True:
            song_url = str(response[i])
            break
        else:
            i += 1
            
    song_url = song_url[62:]
    song_url = song_url[:(len(song_url)-2)]
    song_url = 'https://musicstax.com' + song_url

    song_response = session.get(song_url).text.splitlines()

    j = 0
    while j < len(song_response):
        if song_response[j].startswith('<div class="song-meta-title">'):
            info = song_response[j+3]
            break
        else:
            j += 1
    
    def trimmer(dump, phrase, starter, stopper):
        dump = dump[(dump.find(phrase))+len(phrase):]
        if starter is None:
            dump = dump[:dump.find(stopper)]
        else:
            dump = dump[(dump.find(starter))+len(starter):dump.find(stopper)]
        return dump

    key = trimmer(info,'data-cy="meta-Key-value">',None,'</div>')
    tempo = trimmer(info,'data-cy="meta-Tempo-value">',None,'</div>')
    song_name = trimmer(info,'data-cy="meta-Name-value">',None,'</div>')
    artist_name = trimmer(info,'data-cy="meta-Artist(s)-value"><','<u>','</u>')
    album_name = trimmer(info,'data-cy="meta-Album-value"><','<u>','</u>')
    release_date = trimmer(info,'data-cy="meta-Release+Date-value">',None,'</div>')

    answer = f'I guess you mean "{song_name}"\n'\
            f'by {artist_name}\n'\
            f'from the album "{album_name}" released on {release_date}\n\n'\
            f'-- -- -- -- -- -- -- -- --\n\n'\
            f'The song is probably in \n {key} \n\nTempo:\n {tempo} BPM'
    return answer

tokenTG = io.open('token.txt', mode="r", encoding='utf-8').read()
bot = telebot.TeleBot(tokenTG)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot_resopnse_on_start = f'<b>Hello, {message.from_user.first_name}</b>\n\n' \
                            f' This bot will show you the Key and the Tempo of almost any song \n' \
                            f" Just send me the name of the song and (preferably) it's perfomer \n\n\n\n" \
                            f'<b>Привет, {message.from_user.first_name}</b>\n\n' \
                            f' Я умею искать тональность и темп почти любой (зарубежной) песни \n' \
                            f' Просто отправь мне её название и (очень желательно) исполнителя '
    bot.send_message(message.chat.id, bot_resopnse_on_start, parse_mode='html')

@bot.message_handler()
def main(message):
    three_hundred_list = ['триста', '300', '150+150']
    if message.text == 'testme':
        bot.reply_to(message, f'<b>Your Technical Data:</b>\n\n{message}', parse_mode='html')
    elif message.text.lower() in three_hundred_list:
        bot.reply_to(message, f'<b>ОТСОСИ У ТРАКТОРИСТА АХАХХААХХАХА))))))</b>')
    else:
        find_this = message.text
        bot.reply_to(message, finder(find_this))

bot.polling(none_stop=True)