#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install SpeechRecognition


# In[4]:


pip install pyttsx3


# In[ ]:


import speech_recognition as sr
import pyttsx3
from wit import Wit

WIT_AI_ACCESS_TOKEN = "YOUR_WIT_AI_ACCESS_TOKEN"


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def wit_ai_query(query):
    client = Wit(WIT_AI_ACCESS_TOKEN)
    try:
        response = client.message(query)
        intent = response['intents'][0]['name'] if response['intents'] else None
        entities = response['entities']
        return intent, entities
    except Exception as e:
        print(f"Wit.ai error: {e}")
        return None, None


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""


def main():
    speak("Hello! How can I help you today?")

    while True:
        query = listen()

        if "exit" in query:
            speak("Goodbye!")
            break

        if query:
            intent, entities = wit_ai_query(query)

            if intent == "greeting":
                speak("Hello! How can I assist you?")
            elif intent == "weather":
                # You can add code here to fetch and speak the weather information
                speak("I'm sorry, I don't have weather information right now.")
            elif intent == "your_custom_command":
                # Add your custom command logic here
                speak("Your custom response.")
            else:
                speak("I'm sorry, I didn't understand that. Can you please repeat?")


if __name__ == "__main__":
    main()


# In[ ]:




