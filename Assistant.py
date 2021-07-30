'''
#################   AI ASSISTENT ALEX TEST PROJECT 1   ################

'''




import sys
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os, subprocess
# import smtplib  -------> I am commenting it out, because i don't need this library, I have tested the email sending through the assistant.
                           

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alex Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"

    return query


# def open_file(filename):
#     if sys.platform == "win32":
#         os.startfile(filename)
#     else:
#         opener ="open" if sys.platform == "darwin" else "xdg-open"
#         subprocess.call([opener, filename])

''' This Function also didn't worked
    in the place of os.startfile
    Due to which the Assistant cound not open any file on my system(which is MAC OS)
 '''

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'yourpassword')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

'''
The above function is used for sending email using the smtp.
Above I have imported the smtp library.
No need to install smtp lib, it is present in the python (default).
'''


if __name__ == "__main__":
    wishMe()

    # while True:  ''' IT WILL RUN THE ASSISTANT IN A NEVER STOPING LOOP'''

    if 1:     # IT WILL RUN THE ASSISTANT ONLY ONCE
        query = takeCommand().lower()

        # Logic for executing tasks based query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")




            ''' IT WORKS ONLY FOR WINDOWS,
            ISSUE IN RUNNING THIS MODULE IN MAC
             '''

        # elif 'play music' in query:
        #     audio_file = '/Users/vishal/Desktop//Music'
        #     Music = os.listdir(audio_file)
        #     print(Music)
        #     Random = os.startfile(os.path.join(audio_file , Music[1]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, The Time is{strTime}")


        # elif 'open my visual studio' in query:
        #     codePath = '/Applications/Visual/Studio/Code.app'
        #     subprocess.call(open, codePath)


        # elif 'email to vishal' in query:
        #     try:
        #         speak("What should I say ?")
        #         content = takeCommand()
        #         to = "youremail@gmail.com"  ----> Here you have to provide your email through which you are sending the email.
        #         sendEmail(to, content)
        #         speak("Email has been sent !")

        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend vishal bhai. I am not able to send this above provided email")

        '''  This above module is used to send email

             visit this website https://support.google.com/a/answer/6260879?hl=en 
             to remove the access to less secure app in your google administrator account
        '''