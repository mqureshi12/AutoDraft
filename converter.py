import speech_recognition as sr 

def converter(the_file):

    recog = sr.Recognizer()

    filename = input(the_file)
    with sr.AudioFile(filename) as source:
        audiofile = recog.listen(source)
        try:
            text = recog.recognize_google(audiofile)
            print(text)
        except:
            print("Error, check internet connection.")

