import streamlit as st
from streamlit_option_menu import option_menu
from st_pages import hide_pages
import Un as Un

Un.Nevigate()

#if st.button("logout"):
    #st.session_state.loggedin = ""
    
             
        
        
def update_personal_info():
    st.header("Update Personal Information")
    # Add input fields for updating personal information
    name = st.text_input("Name")
    email = st.text_input("Email")
    contact_number= st.text_input("Contact Number")
    address= st.text_input("address")
    
    # Add "Submit" button
    if st.button("Submit"):
        st.success("Personal information successfully updated!")
    
def update_payment_details():
    st.header("Update Payment Details")
    # Add input fields for updating payment details
    card_holders_name= st.text_input("Card Holder's Name")
    card_number = st.text_input("Card Number")
    expiry_date = st.date_input("Expiry Date")
    
    # Add "Submit" button
    if st.button("Submit"):
        st.success("Payment details successfully updated!")
    
def change_password():
    st.header("Change Password")
    # Add input fields for changing password
    current_password = st.text_input("Current Password", type="password")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    # Add "Submit" button
    if st.button("Submit"):
        st.success("Password successfully changed!")
    
def main():
    
    selected_option = option_menu("Setting", ["Update Personal Information", 
                                                  "Update Payment Details", 
                                                  "Change Password"], 
                                       menu_icon="cast", default_index=0)
    
    if selected_option == "Update Personal Information":
        update_personal_info()
    elif selected_option == "Update Payment Details":
        update_payment_details()
    elif selected_option == "Change Password":
        change_password()

if __name__ == "__main__":
    main()

        
