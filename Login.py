
import streamlit as st
import hashlib
from st_pages import hide_pages
import Un as Un
st.set_page_config(layout='wide', page_title='Address Book', page_icon='📚', initial_sidebar_state="collapsed")

Un.Nevigate()
st.title("Welcome to Gaza Library")
st.write("---")
st.subheader("Please login")

if "loggedin" not in st.session_state :
    st.session_state["loggedin"]= ""
    
    
# DB Management
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="books",
    user="postgres"
)
c = conn.cursor()

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username VARCHAR,password VARCHAR)')

def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (%s,%s)', (username, password))
    conn.commit()

def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username =%s AND password = %s', (username, password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def main_func():
    """Gaza Library Login"""

    menu = ["Login", "SignUp"]
    choice = st.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        # if st.button("Login"):
        create_usertable()
        hashed_pswd = make_hashes(password)

        result = login_user(username, check_hashes(password, hashed_pswd))
        if result:
            st.session_state.loggedin = "ok"
            st.page_link("pages/DisplayBooks.py", label="Login")
            
        else:
            st.page_link("Login.py", label="Login")
            
            st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
            

if __name__ == '__main__':
    main_func()