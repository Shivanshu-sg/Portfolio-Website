import streamlit as st

about_page = st.Page(
    page="./views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",  
    default=True
)

diabetes_page = st.Page(
    page="./views/diabetes_prediction.py",
    title="Diabetes Prediction",
    icon=":material/health_and_safety:"
)

pg = st.navigation({
    "Info" : [about_page],
    "Projects" : [diabetes_page]
})

pg.run()