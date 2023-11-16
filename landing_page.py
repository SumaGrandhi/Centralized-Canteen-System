import streamlit as st
import profilee
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

# # Functions to display different pages
# def show_signup_page():
#     st.session_state['page'] = 'signup'

# def show_register_page():
#     st.session_state['page'] = 'register'

def show_home_page():
    # Custom styles
    st.markdown("""
        <style>
        .welcome-message {
            font-size: 2em;
            font-weight: bold;
            color: #4F8BF9;
            text-align: center;
            margin-top: 50px;
        }
        .streamlit-container {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            height: 100vh;
            background-color: #fafafa;
        }
        .streamlit-image {
            margin-top: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Welcome message
    st.markdown('<div class="welcome-message">Welcome to Our Café!</div>', unsafe_allow_html=True)
    
    # You can use an image as a background or decoration
    #st.image('', use_column_width=True, caption='Enjoy our cozy atmosphere.')

    # Add any other widgets or text you want on your homepage
    st.write("Explore our menu and make orders easily with our app.")

    

# def show_profile_page():
#     st.session_state['page'] = 'profilee'

# # Initialize session state
# if 'page' not in st.session_state:
#     st.session_state['page'] = 'home'

# # Set background
# set_bg_image_and_styles()

# # Create a top bar for the header and buttons
# top_bar = st.container()
# st.markdown('<div class="header">CANTEEN ORDERS</div>', unsafe_allow_html=True)
# with top_bar:
#     col1, col2, col3 = st.columns([1, 0.2, 0.2])
#     with col2:
#         if st.button('Sign Up'):
#             show_signup_page()
#     with col3:
#         if st.button('Register'):
#             show_register_page()

# # Display content based on the current page
# if st.session_state['page'] == 'signup':
#     with st.container():
#         st.markdown("<div class='form-container'>", unsafe_allow_html=True)
#         st.markdown("<div class='form-style'>", unsafe_allow_html=True)
#         username = st.text_input("Username", key="username")
#         password = st.text_input("Password", type="password", key="password")
#         if st.button('Sign In'):
#             # Authentication logic goes here
#             st.write("Sign In logic not implemented.")
#         st.markdown("</div>", unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)
#     if st.button('Back to Home'):
#         show_home_page()
# elif st.session_state['page'] == 'register':
#     # Sign In form in the center
#     with st.container():
#         st.markdown("<div class='form-container'>", unsafe_allow_html=True)
#         st.markdown("<div class='form-style'>", unsafe_allow_html=True)
#         email = st.text_input("email", key="email")
#         first_name = st.text_input("first_name",key="first_name")
#         last_name = st.text_input("last_name", key="last_name")
#         username = st.text_input("Username", key="username")
#         password = st.text_input("Password", type="password", key="password")
#         if st.button(' Register'):
#             # Authentication logic goes here
#             show_profile_page()
#         st.markdown("</div>", unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)
#     #if st.session_state['page'] == 'sign_in':
#         #st.write("Register page content here")
#     if st.button('Back to Home'):
#         show_home_page()

import streamlit as st
import pymysql
def show_signin_page():
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        st.markdown("<div class='form-style'>", unsafe_allow_html=True)
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        if st.button('Sign In'):
            # Authentication logic goes here
            st.write("Sign In logic not implemented.")
            import profilee
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    
def show_register_page():
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        st.markdown("<div class='form-style'>", unsafe_allow_html=True)
        
        email = st.text_input("Email", key="email")
        first_name = st.text_input("First Name", key="first_name")
        last_name = st.text_input("Last Name", key="last_name")
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        
        if st.button('Register'):
            # Registration logic goes here
            # For example, you can check if the username exists and if not, insert the new user into the database.
            import profilee
            # If registration is successful, you might want to show the profile page
            # show_profile_page()
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
# Navigation
def main():
    st.sidebar.title("Navigation")
    pages_dict = {
        "Home": show_home_page,
        "Sign In": show_signin_page,
        "Register": show_register_page
    }

    selected_page = st.sidebar.radio("Go to", list(pages_dict.keys()))
    pages_dict[selected_page]()

if __name__ == "__main__":
    main()

