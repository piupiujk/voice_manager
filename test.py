# pip install google
# pip install SpeechRecognition
# pip install pyttsx3
# pip install wikipedia-api
# pip install googletrans
# pip install python-dotenv
# pip install pyowm
import speech_recognition

main = speech_recognition.Recognizer()
with speech_recognition.Microphone(0) as micro:
    main.adjust_for_ambient_noise(micro, 0.5)
    audio = main.listen(source=micro)
    question = main.recognize_google(audio, language='ru-RU').lower()

print(question)
if question == "привет":
    print("Добрый день!")
else:
    print("Я тебя не понял")
