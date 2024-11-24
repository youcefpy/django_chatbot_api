from transformers import pipeline
# from transformers import LlamaForCausalLM, LlamaTokenizer
import torch
import re
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# model = GPT2LMHeadModel.from_pretrained("gpt2")
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


model_id = "gpt2"
# tokenizer = GPT2Tokenizer.from_pretrained(model_id)
# model = GPT2LMHeadModel.from_pretrained(model_id)
chatbot_model = pipeline("text-generation", model=model_id,torch_dtype=torch.bfloat16, device_map="auto")

# print("chatbot model ======> :: ",chatbot_model)
# conversation_history = ""


def remove_repeated_sentences(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    unique_sentences = []
    for sentence in sentences:
        if sentence not in unique_sentences:
            unique_sentences.append(sentence)
        else:
            break  # Stop adding sentences after the first repetition
    return ' '.join(unique_sentences)

def clean_response(response_text, prompt):
    # Remove the prompt from the response
    stripped_response = response_text.replace(prompt, '').strip()

    # Split the stripped response text into lines
    lines = stripped_response.split('\n')

    combined_lines = " ".join(line.strip() for line in lines if line.strip())
    return remove_repeated_sentences(combined_lines)


def get_response(user_message):

    #conversation history for the context
    # Create a conversational format
    # conversation_prompt = f"User: {user_message}\nBot:"
    # print("chatbot model ======> :: ",chatbot_model)

    # global conversation_history
    # conversation_history += f"User: {user_message}\nBot:"

    responses = chatbot_model(
        user_message,
        truncation=True,
        max_length=70,  # Maximum response length
        temperature=0.4,  # Adjust creativity
        top_p=0.9,       # Top-p sampling for better coherence
        top_k=50,        # Top-k sampling to control randomness
        do_sample=True,  # Enable sampling
    )
    print('User Message ================> :: =',user_message)
    

    response = responses[0]['generated_text']

    cleaned_response = clean_response(response, user_message)


    # if "Bot:" in bot_response:
    #     bot_response = bot_response.split("Bot:")[1].strip()
    # Add the bot's response to the conversation history
    # conversation_history += f" {bot_response}\n"

    return cleaned_response 


