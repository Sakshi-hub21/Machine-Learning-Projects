#Import Required Library
import openai

#Import API Key:-
openai.api_key= 'OpenAI.API-Key'

#Creating function to get the response from ChatGPT
# Using gpt-3.5-turbo version for reliable output as it is fastest verwsion of GPT
def get_completion(query):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user", "content": query}])
    print(completion.choices[0].message.content)


# Write Query (Question to the Chat GPT) in a variable i.e to get the best proposal to secure
# Any project
query = " write the best proposal to secure AI-Powered Chatbot project"

#To store the response from Chat GPT use variable
response = get_completion(query)

# Display the response
print(response)
