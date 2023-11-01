import streamlit as st
from gtts import gTTS
import pygame

# Initialize pygame for audio playback
pygame.mixer.init()

# Voice announcement function
def speak(text):
    tts = gTTS(text, lang='en')
    tts.save("announcement.mp3")
    pygame.mixer.music.load("announcement.mp3")
    pygame.mixer.music.play()

# Streamlit app
st.title("Nike Run Club App")

# Sidebar options
lap_duration = st.sidebar.slider("Lap Duration (minutes)", 1, 60, 5)
selected_pace = st.sidebar.selectbox("Select Pace", ["10km", "5km", "Mile", "Best", "Warmup", "Recovery"])

# Pace dictionary
paces = {
    "10km": ("10 kilometer pace", 6.2),
    "5km": ("5 kilometer pace", 3.1),
    "Mile": ("Mile pace", 1.0),
    "Best": ("Your best pace", None),
    "Warmup": ("Warm-up pace", None),
    "Recovery": ("Recovery pace", None),
}

if st.button("Start Countdown"):
    if selected_pace in paces:
        pace, pace_length = paces[selected_pace]
        if pace_length:
            lap_length = lap_duration / pace_length
            st.write(f"Selected Pace: {pace}")
            st.write(f"Lap Length: {lap_length:.2f} kilometers")

        st.write("Start running and listen for the announcements:")

        for lap in range(1, 26):
            # Voice announcement 3 counts before each lap
            if lap == 1:
                speak("Get ready")
            elif lap == 2:
                speak("On your mark")
            elif lap == 3:
                speak("Get set")
            speak(f"Lap {lap}, {lap_duration} minutes at {pace} pace")

    else:
        st.write("Select a valid pace from the sidebar.")
