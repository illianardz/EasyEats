import streamlit as st
import pandas as pd
import os

def custom_css():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;700&display=swap');
            .stApp {
                font-family: 'League Spartan', sans-serif;
            }
            h1, h2, h3, h4, h5, h6 {
                font-family: 'League Spartan', sans-serif;

            }
            div, span, p, label {
                font-family: 'League Spartan', sans-serif;

            }
            .stTextInput input, .stTextArea textarea {
                color: #DFE0E2 !important;
            }
           
            hr {
                border-top: solid #6F686D;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

custom_css()

# Define CSV file
CSV_FILE = 'users.csv'

# Function to create users CSV file if it doesn't exist
def create_user_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w') as f:
            f.write('username,password\n')

# Function to register a new user
def register_user(username, password):
    # Read existing users
    df = pd.read_csv(CSV_FILE)
    
    # Check if username already exists
    if username in df['username'].values:
        st.error("Username already exists. Please choose another.")
    else:
        # Create new DataFrame for new user
        new_user = pd.DataFrame({'username': [username], 'password': [password]})
        
        # Concatenate new user DataFrame with existing one
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)  # Save to CSV
        st.success("Account created successfully!")

# Function to verify user credentials
def verify_user(username, password):
    df = pd.read_csv(CSV_FILE)
    if username in df['username'].values:
        if df[df['username'] == username]['password'].values[0] == password:
            return True
    return False

# Main application
def main():
    create_user_file()
    
    st.title("EasyEats Log-In Page")
    st.markdown('---')

    # Login form
    st.subheader("Login")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if verify_user(login_username, login_password):
            st.success("Logged in successfully!")
            st.session_state.page = "other_page"
            return
        else:
            st.error("Invalid username or password.")

    # Registration form
    st.markdown('---')
    st.subheader("Create Account")
    register_username = st.text_input("Registration Username")
    register_password = st.text_input("Registration Password", type="password")
    
    if st.button("Sign Up"):
        register_user(register_username, register_password)

if __name__ == "__main__":
    main()