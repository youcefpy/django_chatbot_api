from transformers import pipeline
import torch

# Chargement du model nlp
model_id = "gpt2"
chatbot_model = pipeline("text-generation", model=model_id,torch_dtype=torch.bfloat16)

def get_response(user_message):

    #Utilisation du model pour la generation du text
    responses = chatbot_model(user_message, max_length=50, num_return_sequences=1)
    return responses[0]['generated_text']
