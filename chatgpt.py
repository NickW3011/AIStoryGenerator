import openai

class ChatGPT:
    def __init__(self, api_key, role) :
        openai.api_key = api_key
        #self.dialog = [{"role":"system", "content":role}]
        with open('initial_prompt.txt', 'r') as prompt:
            INITIAL_PROMPT = prompt.read()
        self.dialog = [{"role":"user", "content":INITIAL_PROMPT}]

    def choose_option(self, option):
        self.dialog.append({"role":"user", "content":"Remember that the options you give should only be direct actions from the main character"})
        self.dialog.append({"role":"user", "content":option})
        result = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages = self.dialog
        )
        answer = result.choices[0].message.content
        self.dialog.append({"role":"assistant", "content":answer})
        return answer

if __name__ == '__main__':
    with open('api_key.txt', 'r') as api_key:
        API_KEY = api_key.read()
    chat_gpt = ChatGPT(API_KEY, "Be the main character of a story!")
    
    print("Chose a keyword for your story...")
    keyword = input("> ")
    print()
    initial_result = chat_gpt.choose_option("The keyword is " + keyword + ".")
    print(initial_result)

    while(option := input('> ')) != 'X':
        print()
        result = chat_gpt.choose_option(option)
        print(result)