import pandas as pd
import streamlit as st
import plotly.express as px

from HelperFuncs import loadDataframe
dataframe = loadDataframe()

st.title("Exploratory Data Analysis")
st.write(
    """
    This page explores the realtionships between an earthquakes 'magnitude' and its 'depth'.
    As well as the relationship betweens tsunami generataion and its 'depth', as well as the fault type that trigger the event.
"""
)

st.subheader("Magnitude vs Depth")

fig_mag_depth = px.scatter(
    dataframe,
    x="depth",
    y="magnitude",
    opacity=0.5,
    title="Earthquake Magnitude vs Depth"
)

st.plotly_chart(
    fig_mag_depth,
    use_container_width=True,
    key="eda_mag_depth"
)

st.caption(
    """The scatterplot shows little obvious linear relationship 
    bewteen an earthquake's magnitude and its depth"""
)

st.subheader("Depth by Tsunami Generation")

fig_dpeth_tsunami = px.box(
    dataframe,
    x="tsunami",
    y="depth",
    points="outliers",
    title="Depth's affect on Tsunami Generation"
)

st.plotly_chart(
    fig_dpeth_tsunami,
    use_container_width=True,
    key="eda_depth_tsunami"
)

st.caption(
    """Events that generate tsunamis show a distribution across depths very similar to thos that do not.
    Suggesting that depth alone is not a distinguish tsunami generation in earthquake events
    """
)

magType_tsunami = (
    dataframe.groupby(["magType", "tsunami"]).size().reset_index(name="count")
)

magType_tsunami["tsunami"] = magType_tsunami["tsunami"].map({0: "No tsunami", 1: "tsunami"})

fig_magType_tsunami = px.bar(
    magType_tsunami,
    x="magType",
    y="count",
    color="tsunami",
    barmode="group",
    title="Fault Mechanism type and Tsunami Generation"
)

fig_magType_tsunami.update_layout(
    xaxis_title="Magnitude type",
    yaxis_title="Number of events",
    legend_title="Tsunami Generation"
)

st.plotly_chart(
    fig_magType_tsunami,
    use_container_width=True,
    key="edamagType_tsunami"
)
st.caption(
  """
  Tsunami generation varies across magnitude types, with certain types 
  showing increased chances of generating a tsunami than others, mww and Mi.
  """
  )

st.subheader("Magnitude and Depth by Tsunami Generation")

fig__mag_dpeth_tsu = px.scatter(
    dataframe,
    x="depth",
    y="magnitude",
    color="tsunami",
    opacity=0.6,
    title="Magnitude vs Depth by Tsunami Generation"
)

st.plotly_chart(
    fig__mag_dpeth_tsu,
    use_container_width=True,
    key="eda_mag_depth_tsu"
)

st.caption(
    """
    Tsunami generating events overlap considerably acorss 'magnitude 
    and 'depth'. Showing that the fault mechansim is more suitable for predicting a tsunami.
    """
)

st.divider()
st.subheader(
    """
    Magnitude and depth show very little to no linear realtionship.
    """
)
st.subheader(
    """
    Tsunami generating events posses very similar characteristics to those that do not.
    """
)
