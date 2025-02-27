from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def translate_text(text, source_lang='en', target_lang='ja'):
    url = f"https://findmyip.net/api/translate.php?text={text}&source_lang={source_lang}&target_lang={target_lang}"
    response = requests.get(url)
    try:
        data = response.json()
        if response.status_code == 200 and data['code'] == 200:
            return data['data']['translate_result']
        else:
            return "Translation error"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/api/translate', methods=['GET'])
def translate():
    text = request.args.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    translated = translate_text(text)
    return jsonify({"translated": translated})

if __name__ == '__main__':
    app.run()
