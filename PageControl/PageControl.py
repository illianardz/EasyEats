import streamlit as st

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "login_page"

# Routing logic
if st.session_state.page == "login_page":
    import Log_In
    Log_In.main()
elif st.session_state.page == "other_page":
    import RecipeGenerator
    RecipeGenerator.main()