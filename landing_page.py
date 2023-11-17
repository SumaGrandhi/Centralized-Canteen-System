import streamlit as st
import booking as bk
import past_orders as po
import feedback as fp

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

def show_signin_page():
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        st.markdown("<div class='form-style'>", unsafe_allow_html=True)
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        if st.button('Sign In'):
            # Authentication logic goes here
            st.write("Sign In logic not implemented.")
            st.session_state['user_signed_in'] = True
            st.experimental_rerun()
            #show_home_page()
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
            st.session_state['user_signed_in'] = True
            st.experimental_rerun()
            #show_home_page()
            # If registration is successful, you might want to show the profile page
            # show_profile_page()
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

if 'user_signed_in' not in st.session_state:
    st.session_state['user_signed_in'] = False

# Navigation
def main():
    st.sidebar.title("Navigation")
    if st.session_state['user_signed_in']:
        # Show extended navigation after sign in or register
        pages_dict = {"Home": show_home_page,
                      "Booking": bk.show_booking_page,
                      "Past Orders": po.show_past_orders_page,
                      "Feedback" : fp.show_feedback_page}
    else:
        pages_dict = {"Home": show_home_page,
                        "Sign In": show_signin_page,
                        "Register": show_register_page}
        #pages_dict["Booking"] = bk.show_booking_page
        #pages_dict["Past Orders"] = po.show_past_orders_page
    selected_page = st.sidebar.radio("Go to", list(pages_dict.keys()))
    pages_dict[selected_page]()


if __name__ == "__main__":
    main()

