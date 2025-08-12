import openai

openai.api_key = "YOUR_API_KEY"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def main():
    print("GPT Chatbot. გასაგები კითხვების დასმა შეგიძლიათ.")
    while True:
        user_input = input("თქვენი კითხვა: ")
        if user_input.lower() in ["გამოსვლა", "exit", "quit"]:
            break
        answer = chat_with_gpt(user_input)
        print("ჩატბოტის პასუხი:", answer)

if __name__ == "__main__":
    main()
