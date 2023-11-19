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

def authenticate_user(username, password):
    # This function should only contain the logic to authenticate the user
    # and should not contain any Streamlit widgets like st.button
    query = "SELECT * FROM User WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    userid = result[0]
    #print("USER",userid,result)
    if result:
        conn.close()
        return True,userid
    else:
        return False

def show_signin_page():
    # Check if we need to reset the form and clear session state
    if 'reset_signin_form' in st.session_state and st.session_state['reset_signin_form']:
        for key in ['signin_username', 'signin_password']:
            st.session_state[key] = ''
        st.session_state['reset_signin_form'] = False  # Reset the flag


    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        st.markdown("<div class='form-style'>", unsafe_allow_html=True)
        username = st.text_input("Username", value="", key="signin_username")
        password = st.text_input("Password", type="password", value="", key="signin_password")
        if st.button('Sign In', key="signin_button"):
            val, userid = authenticate_user(username, password)
            if val:
                st.session_state['user_signed_in'] = True
                conn.close()
                st.rerun()
            else:
                st.error("Authentication failed. Please try again.")
                st.session_state['reset_signin_form'] = True
                st.session_state['user_id'] = userid
                #st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Initialize the reset flag in session state
    if 'reset_signin_form' not in st.session_state:
        st.session_state['reset_signin_form'] = False

# The rest of your code remains the same...


    
    
def show_register_page():
    if 'reset_form' in st.session_state and st.session_state['reset_form']:
        for key in ['email', 'first_name', 'last_name', 'username', 'password']:
            st.session_state[key] = ''
        st.session_state['reset_form'] = False
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
            if result:
                st.error("Username or email already exists.")
                st.session_state['reset_form'] = True  # Set the flag to reset the form on next run
                st.rerun()  # Rerun the app to reset the form
            else:
                insert_query = "INSERT INTO User (first_name, last_name, email, username, password) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (first_name, last_name, email, username, password))
                conn.commit()
                query = "select * from User where username = %s"
                cursor.execute(query,username)
                result = cursor.fetchone()
                userid = result[0]
                st.success("Registration successful!")
                st.session_state['user_signed_in'] = True
                st.session_state['user_id'] = userid
                #st.balloons()
                #st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

if 'user_signed_in' not in st.session_state:
    st.session_state['user_signed_in'] = False
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = None

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

