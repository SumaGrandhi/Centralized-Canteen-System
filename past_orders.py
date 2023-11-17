import streamlit as st
import mysql.connector

def show_past_orders_page():
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'sqlroot321#'  # Replace with your actual password
    db_name = 'centralised_canteen_system'

    # Establishing a connection to the database
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name
    )

    def get_past_orders(cursor, customer_id):
        """ Fetch past orders for the given customer ID """
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

    st.title("Past Orders")

    # User input for Customer ID
    customer_id = st.number_input("Enter Your Customer ID", min_value=1, step=1)

    if st.button("Show Past Orders"):
        with conn.cursor() as cursor:
            past_orders = get_past_orders(cursor, customer_id)
            if past_orders:
                st.write("Past Orders:")
                for order in past_orders:
                    st.write(f"Order ID: {order[0]}, Item: {order[3]}, Price: ${order[2]}, Cooking Time: {order[1]} mins, Handled by: {order[4]}")
            else:
                st.error("No past orders found for this Customer ID.")

    conn.close()
