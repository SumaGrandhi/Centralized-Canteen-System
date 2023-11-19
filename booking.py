import streamlit as st
import mysql.connector

def show_booking_page():
    user_id = st.session_state.get('user_id')
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'vid18par10@'  # Replace with your actual password
    db_name = 'centralised_canteen_system'

    # Establishing a connection to the database
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name
    )
    cursor = conn.cursor()

    def get_all_items(cursor):
        user_id = st.session_state.get('user_id')
        """ Fetch all item IDs, Names, Prices, and Available Quantities from the database """
        sql = "SELECT ItemID, Name, Price, Quantity FROM Items"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    with conn.cursor() as cursor:
        all_items = get_all_items(cursor)
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
            #print("SSS",item_dict)
            for item_id in selected_item_ids:
                qty = item_quantities[item_id]
                total_price_for_item = item_dict[item_id][1] * qty
                total_bill += total_price_for_item
                st.write(f"{item_dict[item_id][0]}: ${item_dict[item_id][1]} x {qty} = ${total_price_for_item:.2f}")
                user_id = st.session_state.get('user_id')
                db_host = 'localhost'
                db_user = 'root'
                db_password = 'vid18par10@'  # Replace with your actual password
                db_name = 'centralised_canteen_system'

                # Establishing a connection to the database
                conn = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_password,
                    db=db_name
                )
                cursor = conn.cursor()
                query = "INSERT INTO Orders (CustomerID,ItemID,Quantity,Price) VALUES (%s,%s,%s,%s);"
                cursor.execute(query,(user_id,item_id,qty,item_dict[item_id][1]))
                conn.commit()
            st.write(f"Total Bill Amount: ${total_bill:.2f}")
            

    conn.close()
