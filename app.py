from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = Flask(__name__)
CORS(app)

tokenizer = T5Tokenizer.from_pretrained("./telugu_romanized_translator")
model = T5ForConditionalGeneration.from_pretrained("./telugu_romanized_translator")

@app.route("/")
def home():
    return "English Translator API is running"

def translate(tweet):
    text = "translate romanized telugu to english: " + tweet
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs)
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translation

@app.route("/translate", methods=["POST"])
def translate_api():
    data = request.json
    tweet = data["tweet"]
    result = translate(tweet)
    return jsonify({"translation": result})

if __name__ == "__main__":
    app.run(debug=True)