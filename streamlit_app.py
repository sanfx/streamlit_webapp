import streamlit as st

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
work_exp_page = st.Page(
    page="views/work_experience.py",
    title="Work Experience",
    icon=":material/work:",
)
chatbot_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon=":material/smart_toy:",
)

pg = st.navigation(
    {
        "Info": [about_page, work_exp_page],
        "Projects": [chatbot_page]
    }
)

st.logo("assets/logo.png")
st.sidebar.text("Made with ❤️ by Sanjeev")
# run the navigation
pg.run()