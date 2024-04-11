import streamlit as st
from st_pages import hide_pages
import streamlit as st
import Un as Un

Un.Nevigate()

#if st.button("logout"):
    #st.session_state.loggedin = ""
    


def about_bookstore():
    st.title('About GAZA library')
    st.markdown('''
    <p style="font-size: 12px;">
    Welcome to GAZA library, where literature meets convenience. 
    We're an online bookstore dedicated to providing readers with a seamless and enjoyable experience in discovering, 
    renting, and purchasing their favorite books.
    </p>
    
    <h3 style="font-size: 12px;">Our Mission</h3>
    <p style="font-size: 12px;">
    At GAZA library, our mission is to foster a love for reading by making books more accessible and affordable to everyone. 
    We believe that literature has the power to inspire, educate, and entertain, and we're committed to connecting readers with the stories that resonate with them.
    </p>

    <h3 style="font-size: 12px;">What We Offer</h3>
    <ul style="font-size: 12px;">
        <li>Vast Selection: Explore our extensive catalog featuring a diverse range of genres, from timeless classics to contemporary bestsellers. Whether you're into fiction, non-fiction, romance, mystery, or sci-fi, we have something for every reader's taste.</li>
        <li>Convenient Rentals: Don't want to commit to buying a book? No problem! With our rental service, you can enjoy your favorite reads for a fraction of the cost. Simply choose the rental option at checkout and return the book when you're done.</li>
        <li>Secure Payments: Shop with confidence knowing that your transactions are safe and secure. We utilize state-of-the-art encryption technology to protect your personal and financial information at every step of the process.</li>
        <li>Responsive Support: Have a question or need assistance? Our dedicated customer support team is here to help. Whether it's recommending a book, tracking an order, or resolving an issue, we're committed to providing prompt and friendly assistance to ensure your satisfaction.</li>
    </ul>

    <h3 style="font-size: 12px;">Our Story</h3>
    <p style="font-size: 12px;">
    GAZA lbrary was founded with a passion for literature and a vision to revolutionize the way people discover and enjoy books. 
    What started as a small idea has grown into a thriving online community of book lovers united by their shared love for reading.
    </p>

    <h3 style="font-size: 12px;">Get in Touch</h3>
    <p style="font-size: 12px;">
    We love hearing from our customers! Whether you have feedback, suggestions, or just want to say hello, we'd love to hear from you. 
    Feel free to reach out to us via email, phone, or social media.
    </p>

    <p style="font-size: 12px;">Thank you for choosing GAZA library as your go-to destination for all things books. Happy reading!</p>
    ''', unsafe_allow_html=True)


    st.title('gazalib@gaza12com')
    st.title('01111111111')
    st.title('gazalabrary.co.za')
    
    
about_bookstore()

    
    
    
