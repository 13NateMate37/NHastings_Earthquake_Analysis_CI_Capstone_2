import pandas as pd
import streamlit as st
import plotly.express as px

from HelperFuncs import loadDataframe
dataframe = loadDataframe()

st.title("Earthquake Overview")
st.write(
    """
    This page provides an overview of the cleamed 'earthquake_1995_2023' dataset from C. Chauhan. 
    Its total event count, recorded magnitudes, tsunami generation, high severity counts and patterns over time.  
    """
)

# Creating the metrics to display
total_events = len(dataframe)
average_magnitude = dataframe["magnitude"].mean()
max_magnitude = dataframe["magnitude"].max()
tsunami_event_total = dataframe["tsunami"].sum()
high_severity_count = dataframe["high_severity"].sum()
median_depth = dataframe["depth"].median()
tsunami_pct = (tsunami_event_total / total_events *100)
high_severity_pct = (high_severity_count / total_events *100

                     )
# Storing variables to visual columns
Mcol1, Mcol2, Mcol3, Mcol4 = st.columns(4)

with Mcol1:
    st.metric(
        label="Total Event Count",
        value= f"{total_events:,}"
    )

with Mcol2:
    st.metric(
        label="Average Magnitude",
        value= f"{average_magnitude:.2f}"
    )

with Mcol3:
    st.metric(
        label="Maximum Magnitude",
        value= f"{max_magnitude:.1f}"
    )

with Mcol4:
    st.metric(
        label="Median Depth",
        value= f"{max_magnitude:.1f}km"
    )

# Yearly summary 
yearly_event_occurance = dataframe.groupby("year").size().reset_index(name="Events")

# Plot it

fig_yearly_occ = px.line(
    yearly_event_occurance,
    x="year",
    y="Events",
    markers=True,
    title="Recorded earthquake events by year"
)

fig_yearly_occ.update_layout(
    xaxis_title="Year",
    yaxis_title="Event count"
)
st.plotly_chart(
    fig_yearly_occ,
    use_container_width=True
)

# Magnitude and depth distributions
# Storing variables to visual columns

md_col1, md_col2 = st.columns(2)

with md_col1:
    fig_magnitude = px.histogram(
        dataframe,
        x="magnitude",
        nbins=20,
        title="Magnitude distribution"
    )
    fig_magnitude.update_layout(
        xaxis_title="Magnitude",
        yaxis_title="Event count"
    )
    st.plotly_chart(
    fig_magnitude,
    use_container_width=True
    )
    st.caption(
    "Magntiude's distribution is skewed to the positive, " \
    "showing that high severity events happen no where nearly" \
    " as often as mid and low severity event"
)



with md_col2:
    fig_dpeth = px.histogram(
        dataframe,
        x="depth",
        nbins=30,
        title="Depth distribution"
    )
    fig_dpeth.update_layout(
        xaxis_title="Depth (Km)",
        yaxis_title="Event count"
    )
    st.plotly_chart(
    fig_dpeth,
    use_container_width=True
    )

    st.caption(
    "Depth's distribution is heavily skewed to the positive, " \
    "showing that most events do tend to take place in shallow depths"
)

st.divider()
st.subheader("Key overview and findings")
st.markdown(
    f"""
- The dataset contains **{total_events:,} events**.
- The average recorded magnitude is **{average_magnitude:.2f}**.
- The max recorded magnitude is **{max_magnitude:.1f}**.
-  **{tsunami_event_total:,}** Tsunami events.
- **{high_severity_count:,}** events classed as high severity.
- Median recorded depth of **{median_depth:.1f}km**
"""
)