import streamlit as st
# Function to set the background image

def set_bg_image_and_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1512389098783-66b81f86e199?q=80&w=1828");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        .header {
            text-align: center;
            font-size: 5.5em;
            margin-top: 200px; 
            color : Black;
        }
        /* Additional styles for buttons if needed */
        </style>
        """,
        unsafe_allow_html=True
    )

# Functions to display different pages
def show_signup_page():
    st.session_state['page'] = 'signup'

def show_register_page():
    st.session_state['page'] = 'register'

def show_home_page():
    st.session_state['page'] = 'home'

def show_profile_page():
    st.session_state['page'] = 'profile'

# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Set background
set_bg_image_and_styles()

# Create a top bar for the header and buttons
top_bar = st.container()
st.markdown('<div class="header">CANTEEN ORDERS</div>', unsafe_allow_html=True)
with top_bar:
    col1, col2, col3 = st.columns([1, 0.2, 0.2])
    with col2:
        if st.button('Sign Up'):
            show_signup_page()
    with col3:
        if st.button('Register'):
            show_register_page()

# Display content based on the current page
if st.session_state['page'] == 'signup':
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        st.markdown("<div class='form-style'>", unsafe_allow_html=True)
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        if st.button('Sign In'):
            # Authentication logic goes here
            st.write("Sign In logic not implemented.")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    if st.button('Back to Home'):
        show_home_page()
elif st.session_state['page'] == 'register':
    # Sign In form in the center
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        st.markdown("<div class='form-style'>", unsafe_allow_html=True)
        email = st.text_input("email", key="email")
        first_name = st.text_input("first_name",key="first_name")
        last_name = st.text_input("last_name", key="last_name")
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        if st.button(' Register'):
            # Authentication logic goes here
            show_profile_page()
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    #if st.session_state['page'] == 'sign_in':
        #st.write("Register page content here")
    if st.button('Back to Home'):
        show_home_page()
