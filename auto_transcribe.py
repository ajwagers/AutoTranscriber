import speech_recognition as sr

def live_audio_to_transcript():
    # Initialize recognizer class
    recognizer = sr.Recognizer()
    
    # Open the microphone stream
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening for audio...")
        
        try:
            while True:
                # Capture audio from the microphone
                audio = recognizer.listen(source)
                
                # Recognize speech using Google Web Speech API
                try:
                    transcript = recognizer.recognize_google(audio)
                    print(f"Transcript: {transcript}")
                except sr.UnknownValueError:
                    # Speech was unintelligible
                    print("Sorry, I did not understand that.")
                except sr.RequestError as e:
                    # API request failed
                    print(f"Sorry, there was an error with the request: {e}")
        
        except KeyboardInterrupt:
            print("Terminating...")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    live_audio_to_transcript()
