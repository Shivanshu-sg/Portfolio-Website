import streamlit as st

#-------Hero Section-------
col1, col2 = st.columns(2, gap="small",vertical_alignment="center")
with col1:
    st.image("./assets/my_image.png", width=200)

with col2:
    st.title("Hi, I'm Shivanshu", anchor=False)
    st.write("BS Degree from IIT Madras")
    st.write("Data Science and AI Enthusiast")

st.markdown("<br>", unsafe_allow_html=True) 
with st.container():
    #-------Qualifications Section-------
    st.subheader("Qualifications", anchor=False)
    st.write(
        """
        - BS Degree in Data Science and Programming from IIT Madras
        - Machine Learing Specialiszation course from Udemy
        """
    )

    #---------Skills Section----------
    st.subheader("Skills", anchor=False)
    st.write(
        """
        - Python (scikit-learn, pandas, numpy, matplotlib, seaborn)
        - Machine Learning (Regression, Classification, Ensemble Learning)
        - Basic Web Development (HTML, CSS, JavaScript)
        """
    )

