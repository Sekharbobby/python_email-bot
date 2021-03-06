import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sender@gmail.com', 'PASS')
    email = EmailMessage()
    email['From'] = 'sender@gmail.com'
    email ['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

# If u want to send just email to destination without accesing email list , remove # tag  
  #server.sendmail('abc@gmail.com',
                #'efgh@gmail.com',
                #'Hi Dude make sure you join the party on cristmas otherwise i will move out from the house')

email_list = {
    'balayya': 'balayya@gmail.com',
    'chiru': 'chiru@gmail.com',
    'pink': 'diamond@bts.com',
    'lisa': 'lisa@blackpink.com',
    'irene': 'irene@redvelvet.com'
}

def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey lazy as.. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()
