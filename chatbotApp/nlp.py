from transformers import pipeline
import torch

# Charger le modèle NLP
model_id = "gpt2"
chatbot_model = pipeline("text-generation", model=model_id,torch_dtype=torch.bfloat16, device_map="auto")

def get_response(user_message):

    # Utiliser le modèle pour générer une réponse
    responses = chatbot_model(user_message, max_length=50, num_return_sequences=1)
    return responses[0]['generated_text']
