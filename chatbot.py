import os
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = genai.GenerativeModel(model_name="gemini-1.0-pro")
genai.configure(api_key = GOOGLE_API_KEY)

context = [
    {
        "role" : "user",
        "parts" : [
            {
                "text" : "You are a doctor and your name is Dr. Will. The user is the patient and you will suggest medications and treatments to treat their issues. Don't respond in more than 50 words."
            }
        ],
    },
    {
        "role" : "model",
        "parts" : [
            {
                "text" : "understood"
            }
        ]
    }
]

chat = model.start_chat(history = context)