import streamlit as st
import pymysql

def get_database_connection():
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'vid18par10@'  
    db_name = 'centralised_canteen_system'

    # Establishing a connection to the database
    conn = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name
    )
    return conn

def show_past_orders_page():
    # Check if the user is signed in and the user_id is stored in session state
    if 'user_id' not in st.session_state or st.session_state['user_id'] is None:
        st.error("Please sign in to view past orders.")
        return  # Exit the function if user_id is not set

    user_id = st.session_state['user_id']  # Retrieve the user_id from the session state

    # Establishing a new connection to the database
    conn = get_database_connection()
    cursor = conn.cursor()

    def get_past_orders(cursor, customer_id):
        """ Fetch past orders for the given customer ID """
        sql = """
        SELECT o.OrderID, o.Price, i.Name
        FROM Orders o
        JOIN Items i ON o.ItemID = i.ItemID
        WHERE o.CustomerID = %s
        """
        cursor.execute(sql, (customer_id,))
        result = cursor.fetchall()
        return result

    st.title("Past Orders")

    # Use the signed-in user's ID to fetch past orders
    past_orders = get_past_orders(cursor, user_id)
    if past_orders:
        for order in past_orders:
            st.write(f"Order ID: {order[0]}, Item: {order[2]}, Price: ${order[1]}")
    else:
        st.error("No past orders found for your account.")

    # Close the cursor and the connection
    cursor.close()
    conn.close()

# If this is part of a larger Streamlit app, you may call this function from a navigation menu or similar.
