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

h2col1, h2col2, h2col3 = st.columns(3)

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
    **Cliff's Delta:** Negligible effact size
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

st.markdown("### Magnitude Type and Tsunami Generation")

h2acol1, h2acol2 = st.columns(2)

with h2acol1:
    st.metric(
        "Chi-square p-value",
        "< 0.001"
    ) 
with h2acol２:
    st.metric(
        "Significance Level",
        "0.05"
    ) 
st.markdown(
    """ 
    **Interpretation:** The Chi-square test found statistical
    significance in the association between magnitude type and tsunami generation.
    As the p-value is below the significance level of 0.05, the null
    hypothesis of no association is rejected.

    This suggests that tsunami occurrence is not distributed equally
    across the different magnitude types.
    """
)
st.info(
    """
    **Magnitude Type Result:** Statistically significant association

    Magnitude type provides more useful for distinguishing events that do generate 
    a tsunami rather than the earthquake depth within this dataset.
    """
)

st.markdown("### H2 Conclusion")

st.markdown(
    """
    The results provide mixed evidence for H2. Earthquake depth showed no
    statistically significance between tsunami and non-tsunami events. 
    Meanwhile magnitude type displayed a statistically significant 
    association with tsunami generation.

    Therefore, magnitude type appears to provide more useful information
    about tsunami occurrence than earthquake depth within this dataset.
    """
)
st.info(
    """
    H2 Result: Partially Supported

    Depth was not significantly different between the groups, while
    magnitude type showed a significant association with tsunami generation.
    """
)

st.divider()

