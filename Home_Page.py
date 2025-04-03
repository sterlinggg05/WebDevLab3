import streamlit as st

# Title of App
st.title("Music Explorer - Web Development Lab03")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 20, Web Development - Section B")
st.subheader("Sterling Williams, Hyejin Shim, Nadine Tse")
st.image("images\music.png", width=500)


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. Upcoming Events: A musical event search tool that can query events by artists. Provides specific dates and locations to performances
#       2. User trackings and events: A simulator using the Google Gemini API. A script is generated from the review of the past artists concert you attended.
#       3. Past Events: A music expert chatbot that you can ask your pressing questions about the last time the artists performed in Georgia.

st.markdown("🎹 Welcome to Our App!")
st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. Upcoming Events: A musical event search tool that can query events by artists. Provides specific dates and locations to performances
2. User trackings and events: A simulator using the Google Gemini API. A script is generated from the review of the past artists concert you attended.
3. Past Events: A music expert chatbot that you can ask your pressing questions about the last time the artists performed in Georgia.

""")

