import requests
def send_msg(text):
   token = "5555491875:AAH-aKzegGa2ZGnKrnbvllac-tRueXQPzMI"
   chat_id = "688820140"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
   results = requests.get(url_req)
   print(results.json())
send_msg("Hello there!")

#token that can be generated talking with @BotFather on telegram
#my_token = '5555491875:AAH-aKzegGa2ZGnKrnbvllac-tRueXQPzMI'
#chat_id = '688820140'
#def send(msg, chat_id, token=my_token):

    #bot = telegram.Bot(token=token)
    #bot.sendMessage(chat_id=chat_id, text=msg)