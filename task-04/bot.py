import os
import telebot
import requests
import json
import csv

os.environ['api_key']='6911a8d2'
os.environ['bot_id']='5969831787:AAFu_lAEvuQQeWUb7b0paeLU2IPRmFlgVw4'

# TODO: 1.1 Get your environment variables 
yourkey = os.getenv('api_key')
bot_id = os.getenv('bot_id')

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')

# TODO: 1.2 Get movie information from the API

@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    name=message.text[7:] #Getting the movie title
    key='http://www.omdbapi.com/?t='+name+'&apikey=6911a8d2'
    apimov= requests.get(key).json()
    movie=apimov['Title']
    Poster=apimov["Poster"]
    year=apimov["Year"]
    released=apimov['Released']
    direc=apimov['Director']
    imd=apimov["imdbRating"]
    act=apimov['Actors']
    genre=apimov["Genre"]
    filename="movie.csv"
    field=['Movie','Poster','Year','Released','Director','Imdb_Ratings',"Actors",'Genre']
    
    # TODO: 2.1 Create a CSV file and dump the movie information in it
    with open (filename,'w')as mov:
        csvwrite=csv.writer(mov)
        csvwrite.writerow(field)
        csvwrite.writerow([movie,Poster,year,released,direc,imd,act,genre])
        
        
    # TODO: 1.3 Show the movie information in the chat window
    #Sending info in chat window with the help strings 
    text=("Movie: "+movie+'\n'+Poster+'\n'+"Year: "+year+'\n'+"Released: "+released+'\n'+"Director: "+direc+'\n'+"Imdb Ratings: "+imd+'\n'+"Actor: "+act+'\n'+"Genre: "+genre)
    bot.reply_to(message,text)

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    bot.reply_to(message, 'Generating file...')
    file = open('movie.csv', 'r')
    bot.send_document(message.chat.id, file )

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()

