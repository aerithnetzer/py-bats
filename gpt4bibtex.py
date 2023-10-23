# This file will use the GPT-4 API to generate a bibtex file from a plain text file

import os
import openai

openai.api_type = "azure"
openai.api_base = "https://nul-staff-openai.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")
# Set the API key
    
# Set the temperature
temperature = 0.7
# Set the max tokens
max_tokens = 500
# Set the top p
top_p = 1
# Set the frequency penalty
frequency_penalty = 0.5
# Set the presence penalty
presence_penalty = 0.0
# get content of file

def get_input_content():
    input_path = input('Enter the path to the file containing the plaintext citations: ')
    with open(input_path, 'r') as f:
        content = f.read()
    chunks = content.split('\n')
    return chunks, input_path

def call_gpt(content_chunks):
    responses = []
    for chunk in content_chunks:
    
        completion = openai.ChatCompletion.create(
            engine="nul-general-gpt35",
            messages=[{"role": "user", "content": chunk},
                      {"role": "system", "content": "You are an AI that converts plaintext citations to biblatex. Only respond with code in plain text."}],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=["\n\n"],
        )
        response = completion.choices[0].message.content
        print(response)
        responses.append(response)
        print("")
        print(responses)

    return responses

# Save responses to a bib file
def write_bib_file(responses, input_file_path):
    output_file_path = os.path.splitext(input_file_path)[0] + '.bib'
    with open(output_file_path, 'w') as f:
        for response in responses:
            f.write(response)
            f.write('\n')
    print(f"Responses saved to {output_file_path}")

def gpt4bibtex():
    content_chunks, input_file_path = get_input_content()
    responses = call_gpt(content_chunks)
    write_bib_file(responses, input_file_path)

gpt4bibtex()