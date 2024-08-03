import google.generativeai as genai


API_KEY = "YOUR_API_KEY"

genai.configure (
    api_key=API_KEY
)

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


while (True):
    question = input("You: ")

    if (question.strip() == 'exit'):
        print("Goodbye!")
        break

    response = chat.send_message(question)
    print("\n")
    print(f"Bot (exit to quit): {response.text}")
    print('\n')