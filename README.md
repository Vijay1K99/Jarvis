
# Jarvis AI Bot

## Overview

Jarvis AI Bot is a voice-activated assistant developed in Python that helps users manage their day-to-day tasks through voice commands. Using various Python libraries, Jarvis AI Bot can perform tasks such as opening Google, YouTube, VSCode, playing music, and more.

(https://github.com/Vijay1K99/Jarvis/assets/139844971/95b4932a-4249-42bf-9dcb-8eee494ade3d)



## Features

- **Voice Recognition**: Uses `speech_recognition` to understand and interpret voice commands.
- **Text-to-Speech**: Utilizes `pyttsx3` to provide audio feedback.
- **Web Browsing**: Opens websites like Google and YouTube through voice commands.
- **Application Control**: Launches applications like VSCode.
- **Music Playback**: Plays music from the user's library.
- **Wikipedia Integration**: Fetches summaries from Wikipedia.
- **Email Sending**: Sends emails using `smtplib`.

## Libraries Used

- `pyttsx3`: Text-to-speech conversion library in Python.
- `speech_recognition`: Recognizes speech input from the microphone.
- `datetime`: Provides date and time functionalities.
- `wikipedia`: Fetches information from Wikipedia.
- `webbrowser`: Provides a high-level interface to allow displaying Web-based documents to users.
- `smtplib`: Defines an SMTP client session object that can be used to send mail.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/Jarvis-AI-Bot.git
    cd Jarvis-AI-Bot
    ```

2. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main script to start the Jarvis AI Bot:
```sh
python jarvis.py
```

## Voice Commands

Here are some example voice commands you can use with Jarvis AI Bot:

- **Open Websites**: 
    - "Open Google"
    - "Open YouTube"
- **Launch Applications**:
    - "Open VSCode"
- **Play Music**:
    - "Play Music"
- **Wikipedia Search**:
    - "Tell me about [topic]"
- **Date and Time**:
    - "What is the time?"
    - "What is the date?"
- **Send Email**:
    - "Send email to [contact]"

## Project Structure

```plaintext
Jarvis-AI-Bot/
├── README.md
├── requirements.txt
├── jarvis.py
└── ...
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to update the documentation if you make any changes to the code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to open an issue or contact me at [kumarvj448@gmail.com].
