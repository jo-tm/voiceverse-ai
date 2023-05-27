from browser import document, ajax, window
import json
from browser import html



SpeechRecognition = window.webkitSpeechRecognition
speech_synthesis = window.speechSynthesis
if SpeechRecognition == None :
    SpeechRecognition = window.SpeechRecognition

recognition = SpeechRecognition.new()
recognition.interimResults = False  # Set this to return interim results
recognition.continuous = True  # Add this to enable continuous recognition
recognition.lang = "es-AR"

def on_result(event):
    print('Speech result')
    interim_transcript = ''
    for result in event.results:
        print(str(result))
        if result.isFinal:
            interim_transcript += result[0].transcript
            add_user_message(interim_transcript)

    if interim_transcript:  # Only send the POST request if we have a final result
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": interim_transcript}
        ]

        req = ajax.ajax()
        req.bind('complete', lambda event: add_bot_response(json.loads(req.text)['response']))
        req.open('POST', '/api/generate', True)
        req.set_header('content-type', 'application/json')
        req.send(json.dumps(messages))

def add_bot_response(response):
    p = html.P()
    strong = html.STRONG("Bot: ", Class="bot")
    p <= strong + response
    document['conversation'] <= p
    utterance = window.SpeechSynthesisUtterance.new(response)
    utterance.lang = 'es-AR'
    utterance.rate = 0.65
    utterance.pitch = 0.95
    speech_synthesis.speak(utterance)

def add_user_message(message):
    p = html.P()
    strong = html.STRONG("User: ", Class="user")
    p <= strong + message
    document['conversation'] <= p

def on_speech_start(event):
    print('Speech started')

def on_speech_end(event):
    print('Speech ended')

#recognition.onspeechend = on_speech_end
#recognition.onresult = on_result

recognition.bind('result', on_result)
recognition.bind('start', on_speech_start)
recognition.bind('end', on_speech_end)

def start_recognition(event):
    recognition.start()

def stop_recognition(event):
    recognition.stop()

document['record'].bind('mousedown', start_recognition)
document['record'].bind('mouseup', stop_recognition)
