import openai

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
# openai.api_key = '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'
openai.api_key = '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'


def chat_with_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT-3.5 engine
            prompt=prompt,
            max_tokens=150  # Adjust the response length as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    print("Mini ChatGPT: Type 'exit' to end the conversation.")
    user_input = ""

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting the conversation.")
            break

        # Use the user input as a prompt for GPT-3.5
        response = chat_with_gpt(user_input)
        print("ChatGPT: " + response)
