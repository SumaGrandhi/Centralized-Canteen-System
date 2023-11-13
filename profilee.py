import streamlit as st

# Function to set the background image and styles
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
            color: Black;
        }
        /* Additional styles for buttons if needed */
        </style>
        """,
        unsafe_allow_html=True
    )

# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'profile'

# Set background
set_bg_image_and_styles()
def show_profile_page():
    st.session_state['page'] = 'profile'

# Page display functions
def show_booking_page():
    st.session_state['page'] = 'booking'

def show_past_orders():
    st.session_state['page'] = 'past_orders'

# Create a top bar for the header and buttons
top_bar = st.container()
st.markdown('<div class="header">CANTEEN ORDERS</div>', unsafe_allow_html=True)
with top_bar:
    col1, col2, col3 = st.columns([1, 0.2, 0.4])
    with col2:
        if st.button('Book'):
            show_booking_page()
    with col3:
        if st.button('Past Orders'):
            show_past_orders()

# Display content based on the current page
if st.session_state['page'] == 'profile':
    st.write("Profile page content here")
elif st.session_state['page'] == 'booking':
    st.write("Booking page content here")
elif st.session_state['page'] == 'past_orders':
    st.write("Past orders page content here")
# Add other page conditions as needed
