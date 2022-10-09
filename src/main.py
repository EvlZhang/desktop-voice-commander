import speech_recognition as sr

def main():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening")

        audio = r.listen(source)
        
        try:
            dest = r.recognize_google(audio)
            print("You said " + dest)

        except Exception as e:
            print("Error: " + str(e))    
if __name__ == main():
    main()