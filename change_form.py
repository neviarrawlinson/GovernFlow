import streamlit as st

st.title("GovernFlow Change Request Form")

with st.form("change_form"):
    name = st.text_input("Your name")
    change_type = st.selectbox("Change type", ["Standard", "Normal", "Emergency"])
    description = st.text_area("Describe the change")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"Submitted change request by {name} ({change_type})")
