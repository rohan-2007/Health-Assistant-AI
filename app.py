from flask import Flask, render_template, request
import chatbot
import os
from google.api_core.exceptions import ResourceExhausted, GoogleAPIError

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        if request.form.get("prompt"):
            try:
                response = chatbot.chat.send_message(request.form.get("prompt")).text
                response.replace("*", "")
                # sound = gTTS(text=response, lang="en", slow=False)
                # sound.save("response.mp3")
                # playsound("response.mp3")
                # os.remove("response.mp3")

                return render_template("index.html", message=response)
            
            except ResourceExhausted:
                return render_template("index.html", message="You have hit the usage limit of the Gemini API. Please wait and try again later.")
            
            except GoogleAPIError as e:
                return render_template("index.html", message=f"Gemini API error: {str(e)}")
            
            except Exception:
                return render_template("index.html", message="Something went wrong. Please try again later.")
        
        return render_template("index.html")

if __name__ == '__main__':
    app.run(port=8000)