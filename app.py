from flask import Flask, render_template, request
import chatbot
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        if request.form.get("prompt"):
            response = chatbot.chat.send_message(request.form.get("prompt")).text
            response.replace("*", "")
            # sound = gTTS(text=response, lang="en", slow=False)
            # sound.save("response.mp3")
            # playsound("response.mp3")
            # os.remove("response.mp3")

            return render_template("index.html", message=response)
        
        return render_template("index.html")

if __name__ == '__main__':
    app.run(port=8000)