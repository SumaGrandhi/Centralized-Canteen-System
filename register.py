import streamlit as st

def set_bg_image_and_styles():
    # Define your desired font color and size for the input fields
    input_font_color = "red"  # Dark grey color; change as you like
    input_font_size = "20px"      # Change the font size as you like

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
    st.session_state['page'] = 'register'

set_bg_image_and_styles()

# Create a top bar for the header
top_bar = st.container()
with top_bar:
    st.markdown('<div class="header">CANTEEN ORDERS</div>', unsafe_allow_html=True)
    _, col2, _ = st.columns([1, 0.2, 0.2])
    with col2:
        if st.button('Sign in'):
            st.session_state['page'] = 'sign_in'

# Display content based on the current page
def show_register_page():
    st.write("Register page content here")
    if st.session_state['page'] == 'sign_in':
        st.write("Register page content here")
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
                if st.button('Register'):
                    # Authentication logic goes here
                    st.write("Sign In logic not implemented.")
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)