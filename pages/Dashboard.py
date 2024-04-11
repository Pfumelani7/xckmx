import streamlit as st
from streamlit_option_menu import option_menu

from st_pages import hide_pages
import Un as Un

Un.Nevigate()

#if st.button("logout"):
    #st.session_state.loggedin = ""


              
                
def dash():
    
  
    selected = option_menu("My Dashboard", ["Rental History", "My Cart"], 
    menu_icon="cast", default_index=1)
    selected
    
    
    
dash()

    