import streamlit as st
from datetime import datetime



if __name__ == "__main__":

    st.title("STOPOVER Search Engine")
    #st.write("Welcome to the home page!")

    st.write("")  # Add some space
    
    # Center the components
    st.write("<style>div.row-widget.stRadio > div{flex-direction:row;justify-content:center;}</style>", unsafe_allow_html=True)
    
    # Create a single line for inputs and button
    col1, col2, col3, col4 = st.columns([0.2, 0.2, 0.2, 0.1])
    
    with col1:
        st.markdown('<div class="overlay" style="text-align:center;">DEPARTURE</div>', unsafe_allow_html=True)
        departure = st.text_input("", "")
    
    with col2:
        st.markdown('<div class="overlay" style="text-align:center;">STOPOVER AT</div>', unsafe_allow_html=True)
        stopover = st.text_input(" ", "")
    
    with col3:
        st.markdown('<div style="text-align:center;">Departure Date</div>', unsafe_allow_html=True)
        date = st.date_input("", min_value=datetime.now().date())    
    with col4:
        st.write("")  # Add some space
        st.write("")  # Add some space
        st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
        if st.button("GO"):
            pass#search_flights(departure, stopover, date)
        #st.markdown('</div>', unsafe_allow_html=True)