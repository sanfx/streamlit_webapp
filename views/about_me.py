import streamlit as st

# Local imports
from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
    """Display contact form."""
    contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile.jpeg", width=230)
with col2:
    st.title("Sanjeev Kumar", anchor=False)
    st.write(
        "Software Developer with experience in scripting, testing and software design. " +
        "Integrates python stack knowledge for client satisfaction." +
        "Adapts well to projects of varied scopes and sizes for reliable end-to-end development."
    )
    if st.button("📧 Contact Me"):
        show_contact_form()

# Experience and Qualification
st.write("\n")
st.subheader("Experience and Skills")
st.write(
    """
    - Linux Shell Scripting & Python,

    - TDD using unittest, pytest and pymox,

    - Hand on expereince with Docker, GIT, TMUX, GDB, Python Debugging,

    - CI/CD using Jenkins for automation and deployment using bitbucket

    - Hashicorp Terraform and Vault, Google App Engine, Confluence API

    - Nuke Tools Development for Films Pipeline using Nuke Python API
    """
)