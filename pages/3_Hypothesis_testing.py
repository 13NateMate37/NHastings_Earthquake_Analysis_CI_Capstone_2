import pandas as pd
import streamlit as st
import plotly.express as px

from HelperFuncs import loadDataframe
dataframe = loadDataframe()


st.title("Hypothesis Testing")

st.write(
    """This page presents the statistical tests used in evaluting the hypotheses"""
)

st.subheader("H1 - Magnitude and Depth")
st.markdown(
    """
    **Hypothesis:**   * Earthquake magnitude and depth operate as statistically independent features,
      meaning depth cannot serve as an indicator of magnitude when classifying high-severity.
    
    Two correlation tests were used:
    **Pearson Correlation** - to test the linear relationshp.
    **Spearman Rank Correlation** - to test the monotonic relationship. 
    """
)

# More metric cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Pearson r",
        "0.017"
        )
with col2:
    st.metric(
        "Pearson p-value",
        "0.5895"
    )
with col3:
    st.metric(
        "Spearman p",
        "0.0096"
        )
with col4:
    st.metric(
        "Spearman p-value",
        "0.0025"
    )

st.markdown(

    """
    Result: The Pearson test found no statistically significant linear
    relationship between magnitude and depth. The Spearman test identified
    a statistically significant positive monotonic relationship; however,
    the correlation coefficient was extremely weak.

    Conclusion: The findings provide limited statistical support for a
    relationship between magnitude and depth, but the relationship is too
    weak to be considered practically meaningful.
    """
)

st.info(
    """
    H1 Result: Limited Support

    Depth has very little practical relationship with earthquake magnitude
    within this dataset.
    """
)

st.divider()

