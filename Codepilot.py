from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage,SystemMessage
from io import StringIO
import streamlit as st
from dotenv import load_dotenv
import base64
import time

load_dotenv()

def text_downloader(text):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    b64 = base64.b64encode(text.encode()).decode()
    new_filename = f"code_review_{timestr}.txt"
    st.markdown(f"### Download File")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Download File</a>'
    st.markdown(href, unsafe_allow_html=True)


st.title("Let's Review Your Code")
st.write("I am an AI Code Reviewer. I can help you review your code. Just paste your code below and I will give you feedback on it.")

code = st.file_uploader("Upload your code file", type=[".py"])


if code:
    string = StringIO(code.getvalue().decode("utf-8"))
    fetched_code = string.read()
    st.write(fetched_code)

    chat = ChatOpenAI(model_name="gpt-4",temperature=0.9)
    system_message = SystemMessage(content="You are a experience code reviewer and performance manager. You are reviewing a python code. Your task is to provide suggestions and feedback on the given code also provide performance metrics.")
    human_message = HumanMessage(content=fetched_code)

    final_response = chat([system_message,human_message])

    st.markdown(f"### AI Response: \n {final_response.content}")

    text_downloader(final_response.content)

    st.markdown("### Also don't forget to check out the [AI Code Reviewer](/Repo_reviewer/)")