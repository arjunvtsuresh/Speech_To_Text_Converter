import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak to the microphone:')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said :{}'.format(text))
    except:
        print('Sorry cold not recognize your voice')

f = open('output.txt','w')

f.write(format(text))