import streamlit as st

def apply_theme():
    # Add a toggle button for theme selection with a unique key
    theme_option = st.sidebar.radio("Select Theme", ("Light", "Dark"), key="theme_selector")

    # Apply dynamic theme changes based on the selected option
    if theme_option == "Dark":
        # Dark theme CSS
        dark_theme = """
        <style>
        .main {
            background-color: #0E1117;  /* Main background */
            color: #FAFAFA;  /* Text color */
        }
        .sidebar .sidebar-content {
            background-color: #262730;  /* Sidebar background */
            color: #FAFAFA;  /* Sidebar text color */
        }
        .stButton>button {
            background-color: #FF4B4B;  /* Button background color */
            color: #FAFAFA;  /* Button text color */
        }
        .stTextInput>div>input {
            background-color: #262730;  /* Input field background */
            color: #FAFAFA;  /* Input field text color */
        }
        </style>
        """
        st.markdown(dark_theme, unsafe_allow_html=True)
    else:
        # Light theme CSS
        light_theme = """
        <style>
        .main {
            background-color: #FFFFFF;  /* Main background */
            color: #000000;  /* Text color */
        }
        .sidebar .sidebar-content {
            background-color: #F0F2F6;  /* Sidebar background */
            color: #000000;  /* Sidebar text color */
        }
        .stButton>button {
            background-color: #FF4B4B;  /* Button background color */
            color: #FFFFFF;  /* Button text color */
        }
        .stTextInput>div>input {
            background-color: #FFFFFF;  /* Input field background */
            color: #000000;  /* Input field text color */
        }
        </style>
        """
        st.markdown(light_theme, unsafe_allow_html=True)

    return theme_option
