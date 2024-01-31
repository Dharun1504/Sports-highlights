import os
from transformers import pipeline, Conversation 

os.environ['HF_HOME']='F:\Software-Project\Sport-Highlights\CACHE'

model_name = "umm-maybe/SportsFanGhost"

converse = pipeline('conversational',model=model_name, device='cuda')

conversation = Conversation()

while True:
    user_input = input("You : ")
    if user_input.lower() == 'quit':
        break
    conversation.add_user_input(user_input)
    response = converse([conversation])
    print(f"Bot : {response.generated_responses[-1]}")