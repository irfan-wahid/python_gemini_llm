# Importing the necessary modules from the Streamlit and LangChain packages
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Setting the title of Streamlit Application
st.title('Simple LLM App')
# Creating a sidebar input widget for the OpenAI API key, input type is password for security
google_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Defining a function to generate a response using the GeminiAI language model
def generate_response(input_text):
    # Initializing the GeminiAI language model with a specified temperature and API key
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)
    # Displaying the generated response as an informational message in the Streamlit app
    response = llm.invoke(input_text)
    st.info(response.content)

# Creating a form in the Streamlit app for user input
with st.form('my_form'):
    # Adding a text area for user input
    text = st.text_area('Enter text:', '')
    # Adding submit button for the form
    submitted = st.form_submit_button('Submit')
    # Displaying a warning if the entered API key does not start with 'sk-'
    if not google_api_key:
        st.warning('Please enter your Google API key!', icon='⚠')
    # If the form is submitted and the API key is valid, generate a response
    if submitted and google_api_key:
        generate_response(text)