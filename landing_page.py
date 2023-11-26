import streamlit as st
import booking as bk
import past_orders as po
import feedback as fp
import mysql.connector

db_host = 'localhost'
db_user = 'root'
db_password = 'vid18par10@'  
db_name = 'centralised_canteen_system'

conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name
)
cursor = conn.cursor()

def set_bg_image_and_styles():
    # Replace the existing function content with the CSS provided above
    st.markdown(
        """
      
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?q=80&w=2956&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed; /* Makes the background fixed during scrolling */
}

/* Style for the main header */
.header {
    position: absolute;
    top: 1000%;  /* Center vertically */
    left: 1000%; /* Center horizontally */
    transform: translate(-50%, -50%); /* Ensure true centering */
    text-align: center; /* Align text inside the header */
    color: #000; /* White color for better visibility */
    font-size: 10.5em; /* Adjust the font size as needed */
}

/* Additional global styles */
body {
    color: white; /* Make all text white for better contrast */
    font-family: 'Arial', sans-serif; /* Use a common, clean font style */
    font-family: 'Roboto', sans-serif;
     /* Dark grey color for text for better visibility */
    color: #000;
}

/* Style for navigation and content */
.sidebar .sidebar-content {
    
    background-color: rgba(255, 255, 255, 0.5); /* Semi-transparent white */
    border-right: 2px solid rgba(255, 255, 255, 0.1); /* Slight white border */
    color: #000;
}

/* Style for buttons and interactive elements */
button {
    background-color: #FF4B4B; /* A warm color for your buttons */
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 12px; /* Rounded corners for buttons */
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* Subtle shadow for depth */
    font-family: 'Roboto', sans-serif;
}

/* Style adjustments for Streamlit components */
.stTextInput, .stSelectbox, .stMultiselect {
    background-color: #2C2C2C;
    color: white;
    border: 1px solid #4CAF50; /* A pleasant green */
}

.stTextInput:focus, .stSelectbox:focus, .stMultiselect:focus {
    border-color: #76FF03; /* Brighter green on focus */
}
.stTextInput, .stSelectbox, .stMultiselect, .stSlider, .stRadio, .stCheckbox {
    /* Your existing Streamlit component settings */
    font-family: 'Roboto', sans-serif; /* Roboto font for components */
}

/* Style for sliders */
.stSlider > div > div {
    background-color: #FF4B4B; /* Warm color for the slider thumb */
    background-color: black !important;
}

/* Style for markdown text */
.markdown-text-container {
    color: #ddd; /* Light grey for regular text */
    font-family: 'Roboto', sans-serif; 
}

.sidebar .sidebar-content {
    background-color: rgba(255, 255, 255, 0.5); /* Semi-transparent white */
    border-right: 2px solid rgba(255, 255, 255, 0.1); /* Slight white border */
    color: #000;
}
.css-1t42vg8-StyledSlider > div {
    background-color: black ;
}

/* Slider Thumb */
.css-jrd7h2-StyledThumb {
    background-color: black !important;
}

/* Style adjustments for sidebar widgets to make them stand out */
.sidebar .stRadio > label, .sidebar .stCheckbox > label, .sidebar .stSelectbox > label, .sidebar .stButton > button {
    background-color: rgba(255, 255, 255, 0.8); /* More opaque white for readability */
    border-radius: 15px; /* Rounded corners for the widgets */
    margin: 5px 0; /* Space out the widgets */
    padding: 5px; /* Padding inside the widgets */
    color: #000;
}
.sidebar .stRadio > label {
    color: #000; /* Black for radio items text */
}
</style>

       
        """,
        unsafe_allow_html=True
    )
set_bg_image_and_styles()

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
    # Establish a new database connection inside the function
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name
    )
    cursor = conn.cursor()
    
    query = "SELECT UserID FROM User WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()  # Close the cursor after you're done with it
    conn.close()  # Close the connection after you're done with it

    if result:
        userid = result[0]
        return True, userid
    else:
        return False, None


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
                st.session_state['user_id'] = userid  # Make sure userid is not None here
                st.experimental_rerun()
            else:
                st.error("Authentication failed. Please try again.")
                st.session_state['reset_signin_form'] = True


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
                cursor.execute(query,(username,))
                result = cursor.fetchone()
                userid = result[0]
                st.success("Registration successful!")
                st.session_state['user_signed_in'] = True
                st.session_state['user_id'] = userid
                st.balloons()
                st.rerun()
        
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

