import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to generate multiple-choice questions using OpenAI
def generate_mcq(topic):
    prompt = f"Generate a multiple-choice question related to {topic}"
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        max_tokens=1024,
        temperature=0.5
    )
    question = completions.choices[0].text.strip()
    return question

# Function to check if the answer is correct and provide a grade
def check_answer(question, answer):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"What is the correct answer for the following question?\n\n{question}",
        n=1,
        max_tokens=1024,
        temperature=0.5
    )
    correct_answer = completions.choices[0].text.strip().lower()
    if answer.lower() == correct_answer:
        return "Correct! Great job!"
    else:
        return f"Incorrect. The correct answer is: {correct_answer}"

# Streamlit app
def Quiz():
    st.title("QuizMaster")

    # Get user input for topic
    topic = st.text_input("Enter a topic for the QuizMaster:")
    if topic:
        # Generate MCQ question
        question = generate_mcq(topic)
        st.write("Question:")
        st.write(question)

        # Get user input for answer
        answer = st.text_input("Enter your answer:")
        submit_button=st.button("Submit")
        if submit_button:
            if answer:
                # Check answer and provide grade
                grade = check_answer(question, answer)
                if grade.startswith("Correct"):
                    st.write("")  # Add empty line
                    st.write(grade)
                    st.text_input("Enter your answer:", value="", key="answer")  # Add this line to clear the input box
                else:
                    st.warning(grade)
                    if grade.startswith("Correct"):
                        st.write("")  # Add empty line
                        st.write(grade)
                # else:
                #     st.warning(grade)
# import openai
# import streamlit as st

# # Function to generate MCQs using GPT-3
# openai.api_key = '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' # Replace with your OpenAI API key
# model_engine = 'text-davinci-003' # Specify the GPT-3 model to use

# def generate_mcq_questions(topic):
#     # Generate MCQs using GPT-3
#     prompt = f"Generate multiple-choice questions related to the topic: {topic}"
#     completions = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         n=5,  # Number of completions to generate
#         max_tokens=1024,
#         temperature=0.7
#     )

#     # Extract questions from API response
#     questions = []
#     for choice in completions.choices:
#         text = choice.text.strip()
#         if text:
#             questions.append(text)
#     return questions

# # Function to administer MCQ quiz and calculate grade
# def administer_mcq_quiz(topic, questions, user_choices):
#     # Display MCQs to the user
#     st.write(f"Topic: {topic}")
#     grade = 0
#     for i, question in enumerate(questions):
#         st.write(f"\nQuestion {i+1}: {question}")
#         st.write("Options:")
#         # Replace with logic to generate options for each question
#         options = ['Option A', 'Option B', 'Option C', 'Option D']
#         user_choice = st.selectbox(f"Your answer for Question {i+1}", options=options, key=f"q{i}", index=user_choices[i])
#         user_choices[i] = options.index(user_choice)
#         # Replace with logic to check user's answer against correct answer
#         # and update grade
#         correct_answer = '' # Placeholder for correct answer from GPT-3
#         # Replace with logic to get correct answer from GPT-3 based on the question
#         if options[user_choices[i]] == correct_answer:
#             grade += 1
#         st.write(f"\nQuiz Complete! Your grade: {grade} out of {len(questions)}")
#     return grade
    

# # Streamlit app
# def Quiz():
#     # Get topic input from user
#     topic = st.text_input("Enter a topic for the quiz:")
#     if st.button("Start Quiz"):
#         if topic:
#             # Generate MCQs related to the topic using OpenAI's GPT-3
#             questions = generate_mcq_questions(topic)
#             user_choices = [0] * len(questions)
#             with st.form(key='quiz_form'):
#                 # Administer the quiz and store user's choices
#                 grade = administer_mcq_quiz(topic, questions, user_choices)
#                 submit_button = st.form_submit_button(label='Submit Quiz')
#                 if submit_button:
#                     # Display the final grade after form submission
#                     st.write(f"\nQuiz Complete! Your grade: {grade}/{len(questions)}")

# import streamlit as st
# import openai

# # Set your OpenAI API key
# openai.api_key = "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"

# # Function to generate multiple-choice questions using OpenAI
# def generate_mcq(topic):
#     prompt = f"Generate a multiple-choice question related to {topic}"
#     completions = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         n=1,
#         max_tokens=1024,
#         temperature=0.5
#     )
#     question = completions.choices[0].text.strip()
#     return question

# # Function to check if the answer is correct and provide a grade
# def check_answer(question, answer):
#     completions = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=f"What is the correct answer for the following question?\n\n{question}",
#         n=1,
#         max_tokens=1024,
#         temperature=0.5
#     )
#     correct_answer = completions.choices[0].text.strip().lower()
#     if answer.lower() == correct_answer:
#         return "Correct! Great job!"
#     else:
#         return "Incorrect. Please try again."

# # Streamlit app
# def Quiz():
#     st.title("QuizMaster")

#     # Get user input for topic
#     topic = st.text_input("Enter a topic for the MCQ question:")
#     if topic:
#         # Generate MCQ question
#         question = generate_mcq(topic)
#         st.write("Question:")
#         st.write(question)

#         # Get user input for answer
#         answer = st.text_input("Enter your answer:")
#         if answer:
#             # Check answer and provide grade
#             grade = check_answer(question, answer)
#             st.write(grade)