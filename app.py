import streamlit as st 

st.set_page_config(
    page_title="Earthquake Analysis",
    page_icon="🌍",
    layout="wide"
)

st.title("Earthquake Analysis")
st.subheader("Earthquake characteristics, tsunami generation and severity prediction")

st.write(
    """
    This dashboard presents the results of an analysis of
    earthquake events recorded between 1995 and 2023.

    Use the navigation menu to explore the dataset, statistical
    hypotheses and prediction model.
    """
)