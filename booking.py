import streamlit as st
import mysql.connector

def show_booking_page():
    if 'user_id' not in st.session_state or st.session_state['user_id'] is None:
        st.error("Please sign in to make a booking.")
        return

    user_id = st.session_state['user_id']
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='vid18par10@',
        database='centralised_canteen_system'
    )
    
    # Fetch and display personalized recommendations
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ItemID, COUNT(*) as order_count
        FROM Orders
        WHERE CustomerID = %s
        GROUP BY ItemID
        ORDER BY order_count DESC
        LIMIT 3;
    """, (user_id,))
    frequent_items = cursor.fetchall()
    cursor.close()

    if frequent_items:
        st.write("Based on your past orders, you might like:")
        for item_id, _ in frequent_items:
            cursor = conn.cursor()
            cursor.execute("SELECT Name FROM Items WHERE ItemID = %s", (item_id,))
            item_name = cursor.fetchone()[0]
            cursor.close()
            st.write(f"- {item_name}")

    # Fetch all items available for booking
    cursor = conn.cursor()
    cursor.execute("SELECT ItemID, Name, Price, Quantity FROM Items")
    all_items = cursor.fetchall()
    cursor.close()

    item_dict = {item[0]: (item[1], item[2], item[3]) for item in all_items}

    selected_item_ids = st.multiselect(
        "Select Items", 
        options=list(item_dict.keys()), 
        format_func=lambda x: f"{item_dict[x][0]} - ${item_dict[x][1]} - Available: {item_dict[x][2]}"
    )

    item_quantities = {}
    for item_id in selected_item_ids:
        max_qty = item_dict[item_id][2]  # Maximum available quantity
        qty = st.number_input(f"Quantity of {item_dict[item_id][0]}", min_value=1, max_value=max_qty, step=1, key=item_id)
        item_quantities[item_id] = qty

    if st.button('Calculate Bill'):
        if selected_item_ids:
            st.write("Selected Items, Quantities, and Total Price:")
            total_bill = 0
            for item_id in selected_item_ids:
                qty = item_quantities[item_id]
                total_price_for_item = item_dict[item_id][1] * qty
                total_bill += total_price_for_item
                st.write(f"{item_dict[item_id][0]}: ${item_dict[item_id][1]} x {qty} = ${total_price_for_item:.2f}")
                
            cursor = conn.cursor()
            for item_id in selected_item_ids:
                qty = item_quantities[item_id]
                query = "INSERT INTO Orders (CustomerID, ItemID, Quantity, Price) VALUES (%s, %s, %s, %s);"
                cursor.execute(query, (user_id, item_id, qty, item_dict[item_id][1]))
            conn.commit()
            cursor.close()
            st.write(f"Total Bill Amount: ${total_bill:.2f}")

    conn.close()

show_booking_page()
