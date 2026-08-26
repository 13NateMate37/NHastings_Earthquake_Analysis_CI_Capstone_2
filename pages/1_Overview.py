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

# Storing variables to loop through
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Event Count",
        value= f"{total_events:,}"
    )

with col2:
    st.metric(
        label="Average Magnitude",
        value= f"{average_magnitude:.2f}"
    )

with col3:
    st.metric(
        label="Maximum Magnitude",
        value= f"{max_magnitude:.1f}"
    )

with col4:
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
