import streamlit as st
import pandas as pd
from st_pages import hide_pages
import Un as Un

Un.Nevigate()

#if st.button("logout"):
    #st.session_state.loggedin = ""
     
        
        
# Load the existing dataset
books_df = pd.read_csv("/Users/da-m1-09/Documents/GazaLMS/pages/Librarydata.csv", sep=",")

# Function to add a book to the dataset
def add_book(series, title, author, rating, description, language, isbn, genres, year, edition, pages, publisher, publishDate, characters, bookFormat, firstPublishDate, price, condition):
    global books_df
    new_row = {
        "title": title,
        "series": series,
        "publishDate": publishDate,
        "Characters": characters,
        "bookFormat": bookFormat,
        "firstPublishDate": firstPublishDate,
        "price": price,
        "author": author,
        "rating": rating,
        "description": description,
        "language": language,
        "isbn": isbn,
        "genres": genres,
        "Year": year,
        "edition": edition,
        "pages": pages,
        "publisher": publisher,
        "condition": condition,
    }
    books_df = books_df._append(new_row, ignore_index=True)
    # Write the updated dataset back to CSV
    books_df.to_csv("dataset_5551.csv", index=False)

def main():
    st.title("Gaza Library Management System")
    st.header("Add Book")
    title = st.text_input("Title:")
    author = st.text_input("Author:")
    rating = st.text_input("Rating:")
    description = st.text_area("Description:")
    language = st.text_input("Language:")
    isbn = st.text_input("ISBN:")
    genres = st.text_input("Genres (comma-separated):")
    year = st.text_input("Year:")
    edition = st.text_input("Edition:")
    pages = st.text_input("Pages:")
    publisher = st.text_input("Publisher:")
    series = st.text_input("series:")
    price = st.text_input("price:")
    bookFormat = st.text_input("bookFormat:")
    firstPublishDate = st.text_input("firstPublishDate:")
    publishDate = st.text_input("publishDate:")
    condition = st.text_input("condition:")

    if st.button("Add"):
        add_book(series, title, author, rating, description, language, isbn, genres, year, edition, pages, publisher, publishDate, "", bookFormat, firstPublishDate, price, condition)
        st.success("Book added successfully.")

if __name__ == "__main__":
    main()


        