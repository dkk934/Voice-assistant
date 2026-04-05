# 💬 AI Assistant: Voice-Controlled Automation using Python  

Welcome to your **AI Assistant project**, powered by `speech recognition`, `pyttsx3`, `pywhatkit`, and more! This assistant listens to your voice commands, performs actions like sending WhatsApp messages, Wikipedia searches, launching web pages, and even automates your system tasks.

---

## 🛠️ Features  
- **WhatsApp Messaging**  
  Send scheduled WhatsApp messages via voice input.
  
- **Wikipedia Search**  
  Retrieve brief summaries from Wikipedia on the go.

- **Web Navigation**  
  Open Google, Udemy, or Instagram through voice commands.

- **System Commands**  
  Perform actions like opening Paint, shutting down the system, or killing tasks.

---

## 🚀 How to Run  

### 1. Install Dependencies  
Make sure you have Python installed. Use the following command to install the required packages:  
```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia-python python-dotenv
```

### 2. Setup Environment Variables
Create a .env file:
```makefile
Number=<YOUR_WHATSAPP_NUMBER>
Daksh=<DAKSH'S_INSTAGRAM_URL>
Deepahshu=<DEEPAHSHU'S_INSTAGRAM_URL>
path=<PATH_TO_SHORTCUTS_OR_FILES>
```

### 3. Run the Assistant
```bash
python assistant.py
```

---

## 🗣️ Available Commands  
Below is a list of sample commands you can try with the assistant:

| Command Example                  | Action Performed                                      |
|----------------------------------|-------------------------------------------------------|
| "Friday WhatsApp"                | Sends a WhatsApp message to the number in `.env`.    |
| "Friday Wikipedia [query]"       | Fetches a 2-sentence summary from Wikipedia.          |
| "Friday Google Udemy"            | Opens Udemy and lets you choose a course.             |
| "Friday Instagram Daksh"         | Opens Daksh’s Instagram.                              |
| "Friday paint"                   | Launches Microsoft Paint.                            |
| "Friday shutdown"                | Shuts down the system.                                |
| "Friday rest"                    | Ends the assistant session.                          |

---

## ⚙️ Code Walkthrough  
The code consists of several modular functions:

- **`text_to_speech(text)`**: Converts text input to spoken output using `pyttsx3`.  
- **`get_speech_input(prompt)`**: Captures audio input and converts it into text using `SpeechRecognition`.  
- **`execute_command(cmd)`**: Executes different commands based on user input—like WhatsApp messaging, Wikipedia search, etc.  
- **Main Loop**: Continuously listens for commands until the user says "rest" or "shutdown".  

---

## 🖥️ Demo Preview  
Here’s a basic workflow:

1. **User Input:** "Friday Wikipedia Python"  
   **Response:** Fetches a brief summary about Python from Wikipedia.  
2. **User Input:** "Friday shutdown"  
   **Response:** Shuts down the system.  

---

## ⚠️ Known Issues  
- **SpeechRecognition:** May sometimes raise network errors if there's no internet connection.  
- **Task Automation:** Ensure paths and URLs are correctly set in the `.env` file to avoid errors.  

---

## 🤖 Future Improvements  
- Add support for **voice authentication**.  
- Integrate with **Google Assistant** or **Alexa API**.  
- Enable **SMS** or **email alerts**.  

---

## 📜 License  
This project is open-source under the **MIT License**. Feel free to modify and improve it!  

---

## 👏 Contribute  
Found a bug? Have a suggestion? Open an issue or submit a pull request!  
