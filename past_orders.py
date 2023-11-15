import streamlit as st
# Function to set the background image

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
            color : Black;
        }
        /* Additional styles for buttons if needed */
        </style>
        """,
        unsafe_allow_html=True
    )
import streamlit as st
import pymysql  # or import psycopg2 for PostgreSQL

# Database connection details (update with your database information)
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

def get_past_orders(customer_id):
    """ Fetch past orders for the given customer ID """
    with conn.cursor() as cursor:
        sql = """
        SELECT o.OrderID, o.Cooking_Time, o.Price, i.Name, e.Name
        FROM Orders o
        JOIN Items i ON o.ItemID = i.ItemID
        JOIN Employee e ON o.EmployeeID = e.EmployeeID
        WHERE o.CustomerID = %s
        """
        cursor.execute(sql, (customer_id,))
        result = cursor.fetchall()
        return result

def main():
    """ Main function to run the Streamlit app """
    st.title("Past Orders")

    # User input for Customer ID
    customer_id = st.number_input("Enter Your Customer ID", min_value=1, step=1)

    if st.button("Show Past Orders"):
        past_orders = get_past_orders(customer_id)
        if past_orders:
            st.write("Past Orders:")
            for order in past_orders:
                st.write(f"Order ID: {order[0]}, Item: {order[3]}, Price: ${order[2]}, Cooking Time: {order[1]} mins, Handled by: {order[4]}")
        else:
            st.error("No past orders found for this Customer ID.")

if __name__ == "__main__":
    main()