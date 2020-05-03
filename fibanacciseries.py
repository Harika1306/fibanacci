
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio_data = r.listen(source)
    print("Recgnozing ....")
    text=r.recognize_google(audio_data)
    print(text)

    