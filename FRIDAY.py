from dotenv import load_dotenv
import pythoncom
pythoncom.CoInitialize()

import os
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia as wiki
import webbrowser as web
import sounddevice as sd
import numpy as np
import time
from faster_whisper import WhisperModel

# Load environment variables
load_dotenv()

# ---------------- TEXT TO SPEECH ---------------- #

def text_to_speech(text):
    try:
        engine = pyttsx3.init()   # re-init every time
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("TTS Error:", e)

    print(text)


# ---------------- SPEECH INPUT ---------------- #

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

def get_speech_input(prompt):
    text_to_speech(prompt)

    try:
        # ✅ Load model once (FASTEST)
        if not hasattr(get_speech_input, "model"):
            get_speech_input.model = WhisperModel(
                "base",
                compute_type="int8"   # 🔥 critical for CPU speed
            )

        samplerate = 16000
        SILENCE_TIMEOUT = 3
        MAX_DURATION = 8

        audio_buffer = []
        last_speech_time = time.time()
        start_time = time.time()

        def callback(indata, frames, time_info, status):
            nonlocal last_speech_time

            volume = np.linalg.norm(indata)

            if volume > 0.01:
                audio_buffer.append(indata.copy())
                last_speech_time = time.time()

        with sd.InputStream(
            samplerate=samplerate,
            channels=1,
            dtype="float32",
            callback=callback
        ):
            while True:
                if time.time() - last_speech_time > SILENCE_TIMEOUT:
                    break

                if time.time() - start_time > MAX_DURATION:
                    print("Max recording limit reached")
                    break

        if not audio_buffer:
            print("No speech detected")
            return None

        audio = np.concatenate(audio_buffer, axis=0).flatten()

        text_to_speech("Recognizing....")

        # ✅ CORRECT faster-whisper usage
        segments, _ = get_speech_input.model.transcribe(audio)
        text = " ".join([seg.text for seg in segments]).strip()

        if text == "":
            print("Silence detected. Resetting...\n")
            return None

        print("user:", text,"\n")
        return text.lower()

    except Exception as e:
        print("Error:", e)
        text_to_speech("SIR.... ERROR CAPTURING AUDIO...\n")

# ---------------- COMMAND EXECUTION ---------------- #

def execute_command(cmd):

    if "wikipedia" in cmd:
        text_to_speech("searching pedia..")
        query = cmd.replace("Wikipedia", "")
        results = wiki.summary(query, sentences=2)
        text_to_speech("According to pedia..")
        print(results)
        text_to_speech(results)

    elif "google" in cmd:
        text_to_speech("searching..")
        query = cmd.replace("google", "").replace(" ", "")
        web.open(f"https://www.{query}.com")

        if "udemy" in query:
            u_cmd = get_speech_input(f"What you like to study on {query}..")
            study = {
                "web development": "https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture",
                "python": "https://www.udemy.com/course/100-days-of-code/learn/lecture"
            }
            try:
                web.open(study[u_cmd])
            except Exception as e:
                print(f"Failed to open course: {e}\n")

    elif "instagram" in cmd:
        web.open("https://www.instagram.com/dkking5143/")
        text_to_speech("SIR.... HERE WHAT YOU..ASKED...")
        in_cmd = get_speech_input("Whom do you want to message....")

        contacts = {}

        try:
            web.open(contacts[in_cmd])
        except Exception as e:
            print(f"Failed to open contact: {e}\n")

    elif "paint" in cmd:
        os.system(f"start {os.getenv('path')}Paint.lnk")
        text_to_speech("SIR.... HERE WHAT YOU..ASKED...")

    elif "shutdown" in cmd:
        os.system("shutdown /s")
        text_to_speech("SIR SYSTEM GOING TO SHUTDOWN IN LESS THAN MINUTE ....")
        return False

    elif "rest" in cmd:
        text_to_speech("GOOD DAY SIR....")
        return False

    else:
        try:
            os.system(cmd)
        except Exception as e:
            print(f"Failed: {e}\n")

    return True


# ---------------- MAIN LOOP ---------------- #

agin = True
retry_count = 0
MAX_RETRY = 3

while agin:
    text = get_speech_input("Listening...")

    if not text or text.strip() == "":
        retry_count += 1

        if retry_count == 1:
            text_to_speech("SIR... I didn't catch that\n.")
        elif retry_count == 2:
            text_to_speech("SIR... please say that again.\n")
        elif retry_count >= MAX_RETRY:
            text_to_speech("SIR... I am waiting for your command.\n")
            retry_count = 0

        continue

    # Reset retry counter on valid input
    retry_count = 0

    text = text.lower()

    # 🔥 Wake word detection
    if "friday" in text:
        cmd = text.replace("friday", "").strip()

        if cmd == "":
            text_to_speech("Yes Sir...")
            continue

        agin = execute_command(cmd)

    elif "kill" in text:
        text_to_speech("GOOD DAY SIR....\n")
        os.system('taskkill /IM "code.exe" /F')