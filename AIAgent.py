import google.generativeai as genai


API_KEY = "AIzaSyD1weJf-5aApL2J1EJ9y9wcAnYf5xqG11Q"

genai.configure (
    api_key=API_KEY
)

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


while (True):
    question = input("You: ")

    if (question.strip() == 'exit'):
        break

    response = chat.send_message(question)
    print("\n")
    print(f"Bot (Exit To Quit): {response.text}")
    print('\n')