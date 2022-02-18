#Importando bibliotecas necessárias ao código: Python Telegram Bot, Requests e Regex.
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re

#Criação de função para pegar URL da imagem e de função para checar se o link é uma imagem
#DOG
def get_url():
    #cria variável dentro da função para receber o conteúdo do link em formato json
    contents = requests.get('https://random.dog/woof.json').json()
    # cria var para selecionar dentro do json o valor correspondente ao campo "URL"
    url = contents['url']
    #retorna o valor da função
    return url

def get_image_url():
    #cria var para receber lista de possíveis valores
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    # cria um loop para verificar o link. 
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

#CAT
def get_url_cat():
    contents_cat = requests.get('https://api.thecatapi.com/v1/images/search').json()
    #nesse caso o requests retorna uma tupla, portanto deve se acessar a tupla para por fim acessar o dicionário
    url_cat = contents_cat[0]['url']
    return url_cat
def get_image_url_cat():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url_cat = get_url_cat()
        file_extension = re.search("([^.]*)$", url_cat).group(1).lower()
    return url_cat

#PATO
def get_url_duck():
    contents_duck = requests.get('https://random-d.uk/api/random').json()
    url_duck = contents_duck['url']
    return url_duck
def get_image_url_duck():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url_duck = get_url_duck()
        file_extension = re.search("([^.]*)$", url_duck).group(1).lower()
    return url_duck

#ANIMAIS
def get_url_duck():
    contents_duck = requests.get('https://random-d.uk/api/random').json()
    url_duck = contents_duck['url']
    return url_duck
def get_image_url_duck():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url_duck = get_url_duck()
        file_extension = re.search("([^.]*)$", url_duck).group(1).lower()
    return url_duck

def get_url_zoo():
    #variavel para armazenar o json
    contents_zoo = requests.get('https://zoo-animal-api.herokuapp.com/animals/rand').json()
    #var para acessar o conteudo imagem dentro da var json
    image_zoo = contents_zoo['image_link']
    #var para acessar o conteudo nome dentro da var json
    name_zoo = contents_zoo['name']
    #retorna dois valores
    return image_zoo, name_zoo


#estava no codigo original, mas ainda não sei para que serve co-execução de tarefas
@run_async

#CRIAÇÃO DE FUNÇÕES QUE SERÃO EXECUTADAS PELO COMANDO DO TELEGRAM

def dog(update, context):
    #cria uma var que armazeno o retorno da função criada previamente
    url = get_image_url()
    #usa os recursos da lib PTB para apontar o chat destino
    chat_id = update.message.chat_id
    #cria a ação a ser excutada (usando PTB.ext), no caso envio de foto
    context.bot.send_photo(chat_id=chat_id, photo=url)

def cat(update, context):
    url_cat = get_image_url_cat()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url_cat)

def duck(update, context):
    url_duck = get_image_url_duck()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url_duck)

def zoo(update, context):
    contents_json_zoo = get_url_zoo()
    name_zoo = contents_json_zoo[1]
    image_zoo = contents_json_zoo[0]
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=image_zoo)
    #cria ação de envio de texto
    context.bot.send_message(chat_id=chat_id, text=name_zoo)

def main():
    #atualiza o BOT
    updater = Updater('TOKEN', use_context=True)
    dp = updater.dispatcher
    #associa as funções criadas no código com os comando no Telegram
    dp.add_handler(CommandHandler('dog', dog))
    dp.add_handler(CommandHandler('cat', cat))
    dp.add_handler(CommandHandler('duck', duck))
    dp.add_handler(CommandHandler('zoo', zoo))
    #inicia o BOT
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
