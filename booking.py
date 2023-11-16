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

def show_booking_page():
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'vid18par10@'  # Replace with your actual password
    db_name = 'centralised_canteen_system'

    # Establishing a connection to the database
    conn = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name
    )

    def get_all_items(cursor):
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

    if selected_item_ids:
        st.write("Selected Items, Quantities, and Total Price:")
        total_bill = 0
        for item_id in selected_item_ids:
            max_qty = item_dict[item_id][2]  # Maximum available quantity
            qty = st.number_input(f"Quantity of {item_dict[item_id][0]}", min_value=1, max_value=max_qty, step=1, key=item_id)
            total_price_for_item = item_dict[item_id][1] * qty
            total_bill += total_price_for_item
            st.write(f"{item_dict[item_id][0]}: ${item_dict[item_id][1]} x {qty} = ${total_price_for_item:.2f}")

        st.write(f"Total Bill Amount: ${total_bill:.2f}")

    conn.close()

# The main function would now be redundant if you are using navigation
# So you can remove the main function or adjust it to your app's navigation logic
# if __name__ == "__main__":
#     main()
