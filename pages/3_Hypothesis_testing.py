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
    **Hypothesis:** Earthquake magnitude and depth operate as statistically independent features,
      meaning depth cannot serve as an indicator of magnitude when classifying high-severity.
    
    Two correlation tests were used:
    **Pearson Correlation** - to test the linear relationshp.
    **Spearman Rank Correlation** - to test the monotonic relationship. 
    """
)

# More metric cards
h1col1, h1col2, h1col3, h1col4 = st.columns(4)

with h1col1:
    st.metric(
        "Pearson r",
        "0.017"
        )
with h1col2:
    st.metric(
        "Pearson p-value",
        "0.5895"
    )
with h1col3:
    st.metric(
        "Spearman p",
        "0.0096"
        )
with h1col4:
    st.metric(
        "Spearman p-value",
        "0.0025"
    )

st.markdown(

    """
    Result: The Pearson test found no statistically significant for a linear
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
    H1 Result: Failure to support

    Depth has very little practical relationship with earthquake magnitude
    within this dataset.
    """
)

st.divider()

st.subheader("H2: Earthquake Characteristics and Tsunami Generation")

st.markdown(
    """
    **Hypothesis:** Earthquakes that generate a tsunami occur at significantly lower depths 
    and are triggered by specific fault mechanisms (magType), as opposed to ones that don't.
    
    Two relationships were investigated:
    **Depth vs Tsunami Genertion** 
    **Magnitude type vs Tsunami Generation**
    """
)

st.markdown("### Depth and Tsunami Generation")

h2col1, h2col2, h2col3 = st.coluns(3)

with h2col1:
    st.metric(
        "Tsunmai Event Median Depth",
        "28 km"
    ) 
with h2col２:
    st.metric(
        "Non-Tsunmai Event Median Depth",
        "30 km"
    ) 
with h2col3:
    st.metric(
        "Mann-Whitney p=value",
        "0.8516"
    )

st.markdown(
    """
    Cliff's Delta:** Negligible effact size
    **Interpretation:** The Mann-Whitney U test found no statical significance 
    in depth bewtween tsunami events and non-tsunami events. Cliff's Delta also found 
    depth to have little to no relevance. 
"""
) 

st.info(
    """
    **Depth Result: ** No significance 
    Earthquake dpeth alone is not a reliable indicator for the event to generate a tsunami. 
    """
)

