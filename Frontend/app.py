import streamlit as st
from streamlit_chat import message
import time

# Function to handle user login and signup
def authenticate_user():
    # Login or Signup toggle
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        show_login_signup()

    else:
        show_chat_interface()

# Show login and signup forms
def show_login_signup():
    # Toggling between login and signup
    st.markdown("<h2 style='text-align: center;'>Welcome to the Chatbot</h2>", unsafe_allow_html=True)
    action = st.radio("Choose an action", ('Login', 'Signup'))

    if action == 'Login':
        show_login_form()
    else:
        show_signup_form()

# Display login form
def show_login_form():
    with st.form(key='login_form'):
        st.text_input("Mobile Number", key="login_mobile")
        st.text_input("Password", type="password", key="login_password")
        submit_button = st.form_submit_button(label="Login")
        if submit_button:
            st.session_state.logged_in = True
            st.session_state.user_name = "User"  # Simulate user authentication
            st.session_state.user_mobile = st.session_state.login_mobile
            st.experimental_rerun()

# Display signup form
def show_signup_form():
    with st.form(key='signup_form'):
        st.text_input("Name", key="signup_name")
        st.text_input("Mobile Number", key="signup_mobile")
        st.text_input("Password", type="password", key="signup_password")
        submit_button = st.form_submit_button(label="Signup")
        if submit_button:
            st.session_state.logged_in = True
            st.session_state.user_name = st.session_state.signup_name
            st.session_state.user_mobile = st.session_state.signup_mobile
            st.experimental_rerun()

# Show chat interface once logged in
def show_chat_interface():
    st.markdown(f"<h2>Welcome {st.session_state.user_name}</h2>", unsafe_allow_html=True)

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Chat interaction section
    user_input = st.text_input("Type a message:", key="user_input")
    if st.button("Send"):
        if user_input:
            st.session_state.messages.append({"message": user_input, "is_user": True})
            st.session_state.messages.append({"message": "Processing your request...", "is_user": False})

        # Simulating chatbot response
        time.sleep(1)
        display_messages()

    # Display messages in chat format
    def display_messages():
        for msg in st.session_state.messages:
            if msg['is_user']:
                message(msg['message'], is_user=True, key=msg['message'])
            else:
                message(msg['message'], is_user=False, key=msg['message'])

    # Display logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.messages = []  # Clear chat history
        st.experimental_rerun()

# Run the application
authenticate_user()
