import streamlit as st
from data_management import check_user_password, check_user_role
if 'stage' not in st.session_state:
    st.session_state.stage = 'login'
if 'username' not in st.session_state:
    st.session_state.username = ''

if st.session_state.stage == 'login':
    st.title('Login page')


    with st.form(key='login_form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submitted = st.form_submit_button('Login')

    if submitted:
        if check_user_password(username, password):
            st.success('Login successful')
            st.session_state.stage = 'main'
            st.session_state.username = username
            st.experimental_rerun()
        else:
            st.error('Invalid username or password')

elif st.session_state.stage == 'main':
    if st.button('Log out'):
        st.session_state.stage = 'login'
