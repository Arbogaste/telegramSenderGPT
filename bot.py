import telebot 
import openai
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'

bot = telebot.TeleBot(bot_token)
openai.api_key = "YOUR_OPENAI_API_KEY"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, I am a Telegram bot. Use /help to see what I can do.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "I support the following commands: \n /start \n /generate \n /info \n /help \n /status")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "I am a simple Telegram bot created using the python-telegram-bot library.")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "I am up and running.")

@bot.message_handler(commands=['generate'])
def generate(message):
        prompt = ("""Generate funny, creative and intelligent jokes, people enjoy black humour, politics jokes, controversial jokes, so generate the best joke for a good stand up comedy in a real world comedy. Be a real comedian, use the style of ricky gervais, louis ck, bill hicks, bill murray...""")
        #prompt = 'Generate funny, creative and intelligent jokes, people enjoy black humour, politics jokes, controversial jokes, so generate the best joke for a good stand up comedy in a real world comedy. Be a real comedian, use the style of ricky gervais, louis ck, bill hicks, bill murray...'
        
        response = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=prompt,
                        temperature=0.75,
                        max_tokens=90,
                        n=1,
                        stop=None,
                        frequency_penalty=0,
                        presence_penalty=0
                    )

        text = response.choices[0].text.strip()

        bot.reply_to(message, text)
    
print("Hey, I am up....")
bot.polling()
