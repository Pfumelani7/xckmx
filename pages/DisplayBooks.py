# import pandas as pd
# import streamlit as st
# st.set_page_config(layout='wide', page_title='Address Book', page_icon='📚', initial_sidebar_state="collapsed")


# from st_pages import hide_pages

# hide_pages(["display"])
# hide_pages(["testing"])

# data = pd.read_csv("/Users/da-m1-40/Downloads/lib.csv")

# if st.button('details'):
#     st.page_link("pages/testing.py", label="Details")

# def book_description_section(title, description, ratings, genres, price):
#     st.write(f"Book Title: {title}")
#     st.write(f"Description: {description}")
#     st.write(f"Rating: {ratings}")
#     st.write(f"Genres: {genres}")
#     st.write(f"Price: {price}")

# def main():
#     st.markdown("<h1 style='text-align: center; color: blue;'>📚</h1>", unsafe_allow_html=True)
#     st.title("Book Store App")
    
#     if 'x' not in st.session_state:
#         st.session_state.x = 0

    
#     x = 100 
#     while x > 0:  # Adjusted the loop condition to stop at 0
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col1:
#             st.image(data["coverImg"][x], width=200) 
#             print("What is x:  ", x)
            
#             st.session_state[f'data["coverImg"][x]'] = x                       
#             st.page_link("pages/testing.py", label="Details")
#             x -= 1
#             print("Updated session state x:  ",  x)
#         with col2:   
#             st.image(data["coverImg"][x], width=200) 
#             if st.page_link("pages/testing.py", label="Details"):
#                 st.session_state.x = x  
#             x -= 1
#         with col3:
#             st.image(data["coverImg"][x], width=200) 
#             st.session_state[f'data["coverImg"][x]'] = x                           
#             st.page_link("pages/testing.py", label="Details")
#             x -= 1
#         with col4:
#             st.image(data["coverImg"][x], width=200) 
#             st.session_state[f'data["coverImg"][x]'] = x                           
#             st.page_link("pages/testing.py", label="Details")
#             x -= 1
#         with col5:
#             st.image(data["coverImg"][x], width=200)
#             st.session_state[f'data["coverImg"][x]'] = x                            
#             st.page_link("pages/testing.py", label="Details")
#             x -= 1

# if __name__ == "__main__":
#     main()



# import pandas as pd
# import streamlit as st
# from st_pages import hide_pages

# st.set_page_config(layout='wide', page_title='Address Book', page_icon='📚', initial_sidebar_state="collapsed")

# hide_pages(["display"])
# hide_pages(["testing"])

# data = pd.read_csv("/Users/da-m1-40/Downloads/lib.csv")

# def book_description_section(title, description, rating, genres, price):
#     st.write(f"Book Title: {title}")
#     st.write(f"Description: {description}")
#     st.write(f"Rating: {rating}")
#     st.write(f"Genres: {genres}")
#     st.write(f"Price: {price}")

# def main():
#     st.markdown("<h1 style='text-align: center; color: blue;'>📚</h1>", unsafe_allow_html=True)
#     st.title("Book Store App")
    
#     x = 1000
#     while x > 0:  # Adjusted the loop condition to stop at 0
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col1:
#             st.image(data["coverImg"][x], width=200) 
#             with st.expander(f"Details {x}", expanded=False):  # Adding a unique key
#                 st.markdown(f"[Details](pages/testing.py?x={x})")
#             x -= 1
#         with col2:   
#             st.image(data["coverImg"][x], width=200) 
#             with st.expander(f"Details {x}", expanded=False):  # Adding a unique key
#                 st.markdown(f"[Details](pages/testing.py?x={x})")
#             x -= 1
#         with col3:
#             st.image(data["coverImg"][x], width=200) 
#             with st.expander(f"Details {x}", expanded=False):  # Adding a unique key
#                 st.markdown(f"[Details](pages/testing.py?x={x})")
#             x -= 1
#         with col4:
#             st.image(data["coverImg"][x], width=200) 
#             with st.expander(f"Details {x}", expanded=False):  # Adding a unique key
#                 st.markdown(f"[Details](pages/testing.py?x={x})")
#             x -= 1
#         with col5:
#             st.image(data["coverImg"][x], width=200)
#             with st.expander(f"Details {x}", expanded=False):  # Adding a unique key
#                 st.markdown(f"[Details](pages/testing.py?x={x})")
#             x -= 1

# if __name__ == "__main__":
#     main()

import pandas as pd
import streamlit as st
import Un as Un
from streamlit_extras.switch_page_button import switch_page


Un.Nevigate()

from st_pages import hide_pages

hide_pages(["display"])
hide_pages(["testing"])

data = pd.read_csv("/Users/da-m1-09/Documents/GazaLMS/pages/Librarydata.csv")


def book_description_section(title, description, ratings, genres, price):
    st.write(f"Book Title: {title}")
    st.write(f"Description: {description}")
    st.write(f"Rating: {ratings}")
    st.write(f"Genres: {genres}")
    st.write(f"Price: {price}")

def main():
    st.markdown("<h1 style='text-align: center; color: blue;'>📚</h1>", unsafe_allow_html=True)
    st.title("Book Store App")
    
    if "x" not in st.session_state:
        st.session_state.x = 0

    x = 0
    while x < 100:  # Adjusted the loop condition to stop at 0
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(data["coverImg"][x], width=200) 
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")            
            x += 1
        with col2:   
            st.image(data["coverImg"][x], width=200) 
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing") 
            x += 1
        with col3:
            st.image(data["coverImg"][x], width=200) 
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing") 
            x += 1
        with col4:
            st.image(data["coverImg"][x], width=200) 
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing") 
            x += 1
        with col5:
            st.image(data["coverImg"][x], width=200)
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing") 
            x += 1

if __name__ == "__main__":
    main()



