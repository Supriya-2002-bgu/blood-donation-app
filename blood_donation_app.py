import streamlit as st
import pandas as pd

# Set the title of the app
st.title("Blood Donation Camp Form")

# Create a form using Streamlit's form container
with st.form(key='donation_form'):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=65, step=1)
    blood_group = st.selectbox(
        "Blood Group",
        options=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )
    gender = st.radio("Gender", options=["Male", "Female", "Other"])
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    
    submitted = st.form_submit_button("Submit")

if submitted:
    if not name or not email or not phone:
        st.error("Please fill in all the required fields.")
    else:
        # Save the data in a dataframe
        data = {
            "Name": [name],
            "Age": [age],
            "Blood Group": [blood_group],
            "Gender": [gender],
            "Email": [email],
            "Phone": [phone]
        }
        df = pd.DataFrame(data)
        
        # Append data to CSV file (creates the file if it doesn't exist)
        try:
            df.to_csv('donors.csv', mode='a', header=False, index=False)
        except FileNotFoundError:
            df.to_csv('donors.csv', mode='w', header=True, index=False)
        
        st.success(f"Thank you {name} for registering as a blood donor!")