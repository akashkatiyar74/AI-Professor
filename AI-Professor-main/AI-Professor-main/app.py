import streamlit as st
from streamlit_option_menu import option_menu
import SnipRead.Summary_page as sp
import QuizMaster.quiz as qm
from home import homeWork as hW
import openai
from question import generate_random_questions
from QueryPal.Question_page import Query

st.set_page_config(layout="wide",page_title="AI Professor",page_icon="balloon")

#if you want a sidebar
with st.sidebar:
    selected = option_menu(
        
        menu_title="SpeedBar",
        options = ["Home",
                   "SnipRead",
                   "QueryPal",
                   "QuizMaster"],
        menu_icon=["lightning"],
        icons= ["house","scissors","robot"],
        default_index= 0,
    )

# If you want it in middle of the page, uncomment down!
    
# selected = option_menu(
#         # menu_title="SpeedBar",
#         menu_title=None,
#         options = ["Home",
#                    "SnipRead",
#                    "QueryPal"],
#         # menu_icon=["lightning"],
#         icons= ["house","scissors","robot"],
#         default_index= 0,
#         orientation= "horizontal"
#     )

if selected == "Home":
    hW()
if selected == "SnipRead":
    sp.Snip()

    if "summary" in st.session_state:
        summarized_text = st.session_state["summary"]
    else:
        summarized_text = None

    openai.api_key = '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'
    generate_questions_button = st.button('Generate Questions and Answers')
    if generate_questions_button:
        if summarized_text is not None:
            questions, answers = generate_random_questions(summarized_text)

            for i in range(len(questions)):
                st.write(f"Question {i + 1}: {questions[i]}")
                st.write(f"Answer {i + 1}: {answers[i]}")
if selected == "QueryPal":
    st.title('Ask a Question')
    question = st.text_input('Enter your question:', '')
    answer = st.empty()  # Placeholder for displaying the answer
    if st.button('Get Answer'):
        if not question:
            st.warning('Please enter a question.')
        else:
            # Call the get_openai_answer() function with the user-inputted question
            try:
                answer_text = Query(question)
                answer.success('Answer:')
                answer.write(answer_text)
            except Exception as e:
                st.error(f'Error: {e}')

if selected == "QuizMaster":
    qm.Quiz()
