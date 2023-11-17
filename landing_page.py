import streamlit as st
import booking as bk
import past_orders as po
import feedback as fp
import mysql.connector

db_host = 'localhost'
db_user = 'root'
db_password = 'sqlroot321#'  
db_name = 'centralised_canteen_system'

conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name
)
cursor = conn.cursor()

def show_home_page():
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
    st.markdown('<div class="welcome-message">Welcome to Our Café!</div>', unsafe_allow_html=True)
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
            st.rerun()
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
# Registration logic goes here
# For example, you can check if the username exists and if not, insert the new user into the database.   
        if st.button('Register'):
            query = "SELECT * FROM User WHERE username = %s OR email = %s"
            cursor.execute(query, (username, email))
            result = cursor.fetchone()
            #if result:
                #print("Username or email already exists.")
            if not result:
                insert_query = "INSERT INTO User (first_name, last_name, email, username, password) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (first_name, last_name, email, username, password))
                conn.commit()
                st.session_state['user_signed_in'] = True
            st.rerun()
        
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
    selected_page = st.sidebar.radio("Go to", list(pages_dict.keys()))
    pages_dict[selected_page]()


if __name__ == "__main__":
    main()

