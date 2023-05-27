# VoiceVerse

VoiceVerse is a cutting-edge web application that leverages the power of OpenAI's GPT-4 to provide an interactive, speech-to-text and text-to-speech enabled 
AI chatbot. It uses Python Flask for the backend and Brython for client-side Python code.

## Features

- Voice-enabled AI chatbot: The chatbot utilizes the state-of-the-art GPT-4 model for generating human-like text.
- Speech-to-text: Conversations with the bot can be held verbally, thanks to the integration of the Web Speech API.
- Text-to-speech: The bot's responses are vocalized, providing an immersive and interactive experience.
- Modern, sleek UI: The user interface is designed with dark earth tones and a sophisticated, modern aesthetic.

## Getting Started

### Prerequisites

To run VoiceVerse locally, you will need Python 3.8 or above and a working installation of Flask. Also, you need to have access to GPT-4 through OpenAI's 
API.

### Setup

Clone the repository:

```
git clone https://github.com/jo-tm/VoiceVerse-ai.git
```

Install the required packages:

```
pip install -r requirements.txt
```

### Running the Application

Set the FLASK_APP environment variable:

```
export FLASK_APP=app.py
```

Run the Flask server:

```
flask run
```

The application will be accessible at `localhost:5000` in your web browser.

## Usage

Interact with the chatbot by speaking into your microphone. The bot's responses will be displayed in the chat box and vocalized using text-to-speech.

## Contributing

Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Acknowledgments

- Flask for the web framework
- Brython for providing Python support on the client-side

