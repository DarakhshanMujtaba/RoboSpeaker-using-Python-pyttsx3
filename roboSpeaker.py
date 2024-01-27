import pyttsx3

if __name__ =='__main__':
    print("Welcome to RoboSpeaker 2.0 Created By Darakhshan Mujtaba")
    engine = pyttsx3.init()
    while True:
        x= input("Enter what you want me to speak: ")

        if x== "n":
            engine.say(" 'Bye Bye nice to meet you' ")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
       