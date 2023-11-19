import streamlit as st
import mysql.connector

def get_database_connection():
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
    return conn

def show_feedback_page():
    # Ensure the user is signed in
    if 'user_id' not in st.session_state or st.session_state['user_id'] is None:
        st.error("Please sign in to submit feedback.")
        return

    st.title('Submit Feedback')

    # User input for Rating and Comments
    rating = st.slider("Rating", 1, 5, 3)
    comments = st.text_area("Comments")

    if st.button('Submit Feedback'):
        # Insert the feedback into the database
        conn = get_database_connection()
        cursor = conn.cursor()
        user_id = st.session_state['user_id']  # Retrieve the user_id from the session state
        insert_query = "INSERT INTO Feedback (CustomerID, Rating, Comments) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (user_id, rating, comments))
        conn.commit()
        cursor.close()
        conn.close()

        st.success("Thank you for your feedback!")

# Call the function to display the feedback page
show_feedback_page()
