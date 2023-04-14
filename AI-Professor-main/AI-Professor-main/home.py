import streamlit as st
import requests
from streamlit_lottie import st_lottie 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

#--- Load Assets ---
lottie_professor = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_Fy9W8c.json")
lottie_SnipRead = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_4D9n2fWE2B.json")
lottie_QueryPal = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_au4zdsr8.json")
lottie_QuizMaster = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_rI27TX7MBp.json")


def homeWork():
    with st.container():
        left_column,right_column = st.columns(2)
        with left_column:
            st.write('##')
            st.write('##')
            st.write('##')
            st.write('##')
            st.title("Hey Fellas!")
            st.subheader("Meet the AI Professor")
            ##fill the below function with some suitable short description
            st.write("""
            Your personal academic assistant! Summarizes long articles, creates questions, and auto-grades your responses, 
            making learning simpler and efficient. Get instant feedback and save valuable time with this innovative tool for higher education. 
            Say goodbye to tedious note-taking and grading, and embrace the future of education with AI Professor.
            """)
        with right_column:
            st.write('##')
            st_lottie(lottie_professor,height=500)

    st.write("---")

    with st.container():
        st.markdown("""
        <style>
        .stCentered {
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

        st.write("<h2 class='stCentered'>Tools</h2>", unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")


        col1, col2 = st.columns(2)

        with col1:
            st.write("##")
            st.write("<h4>SnipRead</h4>",unsafe_allow_html=True)
            st.write("""
            SnipRead is a powerful tool for higher education that can automatically summarize lengthy academic texts and generate dynamic questions
            and answers based on the material. It saves time and effort for students and educators by condensing information into easy-to-digest
            summaries and providing quick evaluation through auto-generated questions.
            """)
        with col2:
            st.write("##")
            st_lottie(lottie_SnipRead, height=275)
    
    #st.write('---')
    
    with st.container():
        col3,col4 = st.columns(2)

        with col3:
            st.write("##")
            st.write("<h4>QueryPal</h4>",unsafe_allow_html=True)
            st.write("""QueryPal is a professional grade tool for higher education that streamlines the learning process and also enables users to search for relevant
              questions and receive suitable solutions while also generating auto-questions that allow for active engagement and assessment of the material""")
        with col4:
            st.write('##')
            st_lottie(lottie_QueryPal, height=200)

    #st.write('---')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')

    with st.container():
        col5,col6 = st.columns(2)

        with col5:
            st.write("##")
            st.write("<h4>QuizMaster</h4>",unsafe_allow_html=True)
            st.write("""
            QuizMaster is an auto mcq generator tool for higher education that streamlines that provides instant feedback to students. 
            It can be used by the students for the preparation of exams.
            """)
        with col6:
            
            st_lottie(lottie_QuizMaster, height=230)