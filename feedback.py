import streamlit as st

def show_feedback_page():
    user_id = st.session_state.get('user_id')
    # Display content for feedback
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        st.markdown("<div class='form-style'>", unsafe_allow_html=True)
        order_id = st.text_input("Order ID", key="order_id")
        rating = st.slider("Rating", 1, 5, 3)
        comments = st.text_area("Comments", key="comments")
        if st.button('Submit Feedback'):
            # Feedback processing logic goes here
            st.write("Feedback submitted for Order ID:", order_id)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Initialize session state for feedback page
if 'page' not in st.session_state:
    st.session_state['page'] = 'feedback'

if st.session_state['page'] == 'feedback':
    show_feedback_page()
