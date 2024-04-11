import streamlit as st
#import pandas as pd
from st_pages import hide_pages
from streamlit_extras.switch_page_button import switch_page

def Nevigate():
    if "loggedin" not in st.session_state :
        st.session_state["loggedin"]= ""
   

    hide_pages("Addbook")
    hide_pages("DisplayBooks")
    hide_pages("Dashboard")
    hide_pages("Settings")
    hide_pages("ReturnBooks")
    hide_pages("SearchBook")
    hide_pages("About")
    hide_pages("testing")
    hide_pages("testing2")
    hide_pages("Login")




    if st.session_state.loggedin == "ok":

        col1, col2, col3, col4, col5,col6,col7, col8= st.columns(8)
        with col1:
            st.page_link("pages/DisplayBooks.py", label="Display")
        with col2:
            st.page_link("pages/SearchBook.py", label="Search")
        with col3:
            st.page_link("pages/Addbook.py", label="Add Book")
        with col4:
            st.page_link("pages/Settings.py", label="Settings")
        with col5:
            st.page_link("pages/ReturnBooks.py", label="Return") 
        with col6:
            st.page_link("pages/Dashboard.py", label="Dasboard") 
        with col7:
            st.page_link("pages/About.py", label="About")  
        with col8:
            if st.button("logout"):
                st.session_state["loggedin"]= "" 
                switch_page("Login")            
                
                