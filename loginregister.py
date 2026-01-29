import streamlit as st
import pymysql

conc = pymysql.connect(
    host="localhost", user="root", password="Sql@3117", database="student_db"
)
cursor = conc.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Auths (username VARCHAR(255) PRIMARY KEY, email VARCHAR(255), password VARCHAR(255))"
)


def login_user(username, password):
    query = "select * from Auths where username=%s and password=%s"
    cursor.execute(query, (username, password))
    data = cursor.fetchone()
    return data


def register_user(username,email, password):
    us = cursor.execute("select * from Auths where username=%s", (username,))
    if us:
        return False
    else:
        query = "insert into Auths(username,email,password) values(%s,%s,%s)"
        cursor.execute(query, (username, email, password))
        conc.commit()
        return True


st.sidebar.title("Login & Registration")
menu = st.sidebar.radio("Menu", ["Login", "Register"])
# registration
if menu == "Register":
    st.header("Registration Form")
    with st.form("register_form"):
        new_username = st.text_input("New Username")
        new_email = st.text_input("Email")
        new_password = st.text_input("New Password", type="password")
        register_submitted = st.form_submit_button("Register")
    if register_submitted:
        if register_user(new_username, new_email, new_password):
            st.success(f"User {new_username} registered successfully!")
        else:
            st.error("Username already exists. Please choose a different username.")
# login
if menu == "Login":
    st.header("Login Form")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_submitted = st.form_submit_button("Login")
        if login_submitted:
            user = login_user(username, password)
            if user:
                st.success(f"Welcome back, {username}!")
            else:
                st.error("Invalid username or password")
