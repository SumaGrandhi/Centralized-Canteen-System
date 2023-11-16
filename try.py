import streamlit as st
from profilee import show_profile_page
from past_orders import show_past_orders_page
from booking import show_booking_page
from sign_in import show_signin_page
from register import show_register_page

# Define session states for user authentication and page navigation
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'

def show_home_page():
    st.write("Welcome to Our Café!")
    st.write("Please sign in or register to make a booking or view past orders.")

def main():
    # If the user is authenticated, show booking and past orders in the sidebar
    if st.session_state['authenticated']:
        page = st.sidebar.radio("Navigation", ['Home', 'Booking', 'Past Orders', 'Profile'])
    else:
        page = st.sidebar.radio("Navigation", ['Home', 'Sign In', 'Register'])

    if page == 'Home':
        show_home_page()
    elif page == 'Sign In':
        show_signin_page()
    elif page == 'Register':
        show_register_page()
    elif page == 'Booking':
        show_booking_page()
    elif page == 'Past Orders':
        show_past_orders_page()
    elif page == 'Profile':
        show_profile_page()

    # Redirects to the profile page after sign in or registration
    if st.session_state['current_page'] == 'sign_in':
        st.session_state['authenticated'] = True  # Update based on real authentication logic
        show_profile_page()
    elif st.session_state['current_page'] == 'register':
        st.session_state['authenticated'] = True  # Update based on real registration logic
        show_profile_page()

if __name__ == "__main__":
    main()
