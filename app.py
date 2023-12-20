from flask import Flask, request, send_file
from gtts import gTTS
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Ubah settingan CORS jika diperlukan, secara default akan menerima request dari mana saja

@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text', '')
    language = data.get('language', 'en')

    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")

    return send_file("output.mp3", as_attachment=True)

if __name__ == '__main__':
    # Ubahlah pengaturan di bawah ini sesuai kebutuhan
    app.run(debug=True, port=8000, threaded=True, host='0.0.0.0')

