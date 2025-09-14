import streamlit as st
import requests

API_URL = "http://localhost:8000/customers/"

st.title("Customer Registration")

name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")

if st.button("Create Customer"):
    payload = {
        "name": name,
        "email": email,
        "phone": phone
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()
            st.success("Customer created successfully!")
            st.write("### Customer Details")
            st.json(data)
        else:
            st.error(f"Failed to create customer: {response.status_code}")
            st.json(response.json())
    except Exception as e:
        st.error(f"Error: {e}")
