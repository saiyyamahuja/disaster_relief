import json
import os
import speech_recognition as sr
import spacy
from gtts import gTTS
import pygame

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def load_disaster_data(filename="disaster_data.json"):
    """Load the disaster relief instructions from JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

def speak(text, slow=False, lang='en'):
    """Convert text to speech and play it with enhanced audio quality."""
    try:
        # Create TTS with better settings
        tts = gTTS(text=text, lang=lang, slow=slow)
        filename = "response.mp3"
        tts.save(filename)
        
        # Initialize pygame mixer with better audio settings
        pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
        pygame.mixer.init()
        
        # Load and play the audio
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(0.8)  # Set volume to 80%
        pygame.mixer.music.play()
        
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)
        
        # Clean up
        pygame.mixer.music.unload()
        os.remove(filename)
    except Exception as e:
        print(f"TTS Error: {e}")
        print(text)

def speak_emergency_numbers():
    """Speak emergency numbers clearly for Indian users."""
    emergency_info = """
    Emergency numbers for India:
    Police: 100
    Fire: 101  
    Ambulance: 102
    Disaster Response: 108
    """
    print(emergency_info)
    speak(emergency_info, slow=True)

def listen_to_user():
    """Capture audio from mic and convert to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 2
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn’t understand that.")
        return None
    except sr.RequestError:
        print("Speech service unavailable.")
        return None

def process_command(text, data):
    """Match user input with disaster relief keywords."""
    doc = nlp(text.lower())
    for keyword, entry in data["scenarios"].items():
        terms = [keyword] + entry.get("synonyms", [])
        for token in doc:
            if token.lemma_ in terms:
                return keyword
    return None

def give_instructions(keyword, data):
    """Provide disaster relief instructions step by step."""
    entry = data["scenarios"].get(keyword)
    if not entry:
        speak(f"Sorry, I don't have disaster relief instructions for {keyword}.")
        return

    # Critical check
    if entry.get("critical", False):
        warning = f"URGENT: {keyword} is a critical emergency. Call emergency services immediately at 100 for police, 101 for fire, 102 for ambulance, or 108 for disaster response. Here are immediate safety steps:"
        print(warning)
        speak(warning, slow=True)  # Use slower speech for critical messages
    else:
        intro_warning = f"Disaster relief guidance for {keyword}. Follow these steps carefully:"
        print(intro_warning)
        speak(intro_warning)

    # Start instructions
    instructions = entry.get("instructions", [])
    if not instructions:
        speak(f"No detailed disaster relief steps found for {keyword}.")
        return

    intro = f"Here are the disaster relief steps for {keyword}:"
    print(f"\n--- Disaster Relief Instructions: {keyword.capitalize()} ---")
    speak(intro)

    for i, step in enumerate(instructions):
        msg = f"Step {i+1}: {step}"
        print(msg)
        speak(msg)

        if i < len(instructions) - 1:
            speak("Say 'next' to continue or 'stop' to exit.")
            while True:
                response = listen_to_user()
                if response:
                    if "next" in response:
                        break
                    elif "stop" in response:
                        speak("Stopping disaster relief instructions. Stay safe and follow emergency protocols.")
                        return

    final_msg = f"Those were the disaster relief steps for {keyword}. Remember to call emergency services at 100, 101, 102, or 108 if the situation becomes life-threatening."
    print(final_msg)
    speak(final_msg)

if __name__ == "__main__":
    disaster_data = load_disaster_data()

    disclaimer = """
    Welcome to the Disaster Relief Emergency Assistant.
    I can help you with guidance for various natural disasters and emergency situations.
    For life-threatening emergencies, call 100 for police, 101 for fire, 102 for ambulance, or 108 for disaster response.
    """
    print(disclaimer)
    speak(disclaimer)

    while True:
        user_command = listen_to_user()
        if user_command:
            if any(exit_word in user_command for exit_word in ["exit", "quit", "goodbye", "bye"]):
                speak("Goodbye! Stay safe and be prepared for emergencies.")
                break
            elif any(emergency_word in user_command for emergency_word in ["emergency numbers", "emergency contacts", "help numbers", "100", "101", "102", "108"]):
                speak_emergency_numbers()
            else:
                keyword = process_command(user_command, disaster_data)
                if keyword:
                    give_instructions(keyword, disaster_data)
                else:
                    speak("I can help with disaster relief situations like earthquakes, floods, hurricanes, wildfires, tornadoes, and other emergencies. Say 'emergency numbers' for help contacts. Please describe the disaster or emergency clearly.")
