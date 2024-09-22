import streamlit as st
from utils import execute_query
# from pages import Dashboard, Student_info, Customer_info, Add_record

# Set the page configuration (title, favicon, layout, etc.)
st.set_page_config(
    page_title="Φ Maths & Statistics Lab Dashboard",
    page_icon=":material/home:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# st.title("Φ Εργαστήριο Μαθηματικών")
# st.image('/static/logo_math_long_wb_nowww.png')

# # Sidebar navigation
# st.sidebar.title("Navigation")
# pages = {
#     "Dashboard": Dashboard,
#     "Student Info": Student_info,
#     "Customer Info": Customer_info,
#     "Add Records": Add_record
# }

# # Select the page to display
# selected_page = st.sidebar.selectbox("Select a page:", pages.keys())

# # Render the selected page
# pages[selected_page].show()

