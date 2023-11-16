import streamlit as st

def set_bg_image_and_styles():
    # Define your desired font color and size for the input fields
    input_font_color = "#333333"  # Dark grey color; change as you like
    input_font_size = "16px"      # Change the font size as you like

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1512389098783-66b81f86e199?q=80&w=1828");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        .header {{
            text-align: center;
            font-size: 5.5em;
            color: Black;
        }}
        /* Style the input field */
        .stTextInput input {{
            color: {input_font_color} !important;
            font-size: {input_font_size} !important;
        }}
        /* Style the input label */
        .stTextInput label {{
            color: {input_font_color} !important;
            font-size: {input_font_size} !important;
        }}
        /* Style the placeholder text */
        .stTextInput input::placeholder {{
            color: {input_font_color} !important;
            font-size: {input_font_size} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )



# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'sign_in'

set_bg_image_and_styles()

# Create a top bar for the header
# top_bar = st.container()
# with top_bar:
#     st.markdown('<div class="header">CANTEEN ORDERS</div>', unsafe_allow_html=True)
#     _, col2, _ = st.columns([1, 0.2, 0.2])
#     with col2:
#         if st.button('Register'):
#             st.session_state['page'] = 'register'

# # Display content based on the current page
# if st.session_state['page'] == 'register':
#     st.write("Register page content here")
# elif st.session_state['page'] == 'sign_in':
#     # Sign In form in the center
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

import streamlit as st

# Assuming 'page' is part of the session state to track the current page
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

def show_signin_page():
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        st.markdown("<div class='form-style'>", unsafe_allow_html=True)
        username = st.text_input("Username", key="signin_username")
        password = st.text_input("Password", type="password", key="signin_password")
        if st.button('Sign In', key='signin_button'):
            # Authentication logic goes here
            # For now, let's just simulate successful sign-in
            st.session_state['page'] = 'profile'  # Redirect to the profile page
            st.write("Sign In logic not implemented.")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


    # Include your registration form and logic here

def main():
    top_bar = st.container()
    with top_bar:
        st.markdown('<div class="header">CANTEEN ORDERS</div>', unsafe_allow_html=True)
        _, col2, _ = st.columns([1, 0.2, 0.2])
        with col2:
            if st.button('Register'):
                st.session_state['page'] = 'register'

    # Display content based on the current page
    if st.session_state['page'] == 'register':
        show_register_page()
    elif st.session_state['page'] == 'sign_in':
        show_signin_page()
    # Add more conditions for other pages like profile, home, etc.

if __name__ == "__main__":
    main()
