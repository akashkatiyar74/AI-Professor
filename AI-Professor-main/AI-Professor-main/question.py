# import openai
# import streamlit as st
# def summarize(prompt):
#     augmented_prompt = f"summarize this text: {prompt}"
#     try:
#         st.session_state["summary"] = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=augmented_prompt,
#             temperature=.5,
#             max_tokens=1000,
#         )["choices"][0]["text"]
#     except:
#         st.write('There was an error')
# def generate_random_questions(summarize):
#     # Set up OpenAI API key and model
#     openai.api_key = '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' # Replace with your OpenAI API key
#     model_engine = 'text-davinci-003' # Specify the GPT-3 model to use

#     # Generate questions using GPT-3
#     prompt = f"Generate questions and answers from the following summary:\n\n{summarize}"
#     completions = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         n=5,  # Number of completions to generate
#         max_tokens=1024,
#         temperature=0.7
#     )

#     # Extract questions and answers from API response
#     questions = []
#     answers = []
#     for choice in completions.choices:
#         text = choice.text.strip()
#         if text:
#             if 'Q: ' in text and 'A: ' in text:
#                 question, answer = text.split('Q: ')[1], text.split('A: ')[1]
#                 questions.append(question)
#                 answers.append(answer)
#             else:
#                 # Handle cases where 'Q: ' or 'A: ' is not found in the text
#                 questions.append('')
#                 answers.append('')
#     return questions, answers  # Return questions and answers as a tuple

import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=1000,
        )["choices"][0]["text"]
    except:
        st.write('There was an error')

def generate_random_questions(summary):
    openai.api_key = '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' 
    model_engine = 'text-davinci-003'

    prompt = f"Generate questions and answers from the following summary:\n\n{summary}"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        n=5,  # Number of completions to generate
        max_tokens=1024,
        temperature=0.7
    )

    # Extract questions and answers from API response
    questions = []
    answers = []
    for choice in completions.choices:
        text = choice.text.strip()
        if text:
            if 'Q: ' in text and 'A: ' in text:
                question, answer = text.split('Q: ')[1], text.split('A: ')[1]
                questions.append(question)
                answers.append(answer)
            else:
                # Handle cases where 'Q: ' or 'A: ' is not found in the text
                questions.append('text')
                answers.append('')
    return questions, answers
