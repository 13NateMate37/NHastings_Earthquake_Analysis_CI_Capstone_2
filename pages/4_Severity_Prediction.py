import pandas as pd
import streamlit as st
import plotly.express as px

from HelperFuncs import loadDataframe
dataframe = loadDataframe()

st.title("High-Severity Earthquake Prediction")

st.write(
    """
    This page examines the performance of the machine-learning models
    developed to classify high-severity earthquake events.
    """
)
st.subheader("Prediction Objective")

st.markdown(
    """
    The Machine-Learning task aimed to classify earthquake events as
    either high severity or not high severity using the available
    real-time earthquake characteristics.

    Two classification models were compared:

    
Logistic Regression — used as the baseline model.
Random Forest — used to investigate whether a more complex
  model could improve classification performance.

    The project set a target of at least 85% recall for identifying
    high-severity events.
    """
)

model_results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Random Forest"
    ],
    "Accuracy": [
        68.50,
        78.50
    ],
    "Recall": [
        61.05,
        76.84
    ],
    "F1 Score": [
        65.00,
        77.00
    ]
})

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Accuracy",
        "78.50%"
    )

with col2:
    st.metric(
        "Recall",
        "76.84%"
    )

with col3:
    st.metric(
        "F1 Score",
        "0.77"
    )

with col4:
    st.metric(
        "Recall Target",
        "85%"
    )

model_res_plot = model_results.melt(
    id_vars="Model",
    var_name="Metric",
    value_name="Score"
)

fig_model_res = px.bar(
    model_res_plot,
    x="Metric",
    y="Score",
    color="Model",
    barmode="group",
    title="Logistic Regression vs Random Forest"
)

fig_model_res.update_layout(
    xaxis_title="Performance Metric",
    yaxis_title="Score (%)",
    legend_title="Model"
)

st.plotly_chart(
    fig_model_res,
    use_container_width=True,
    key="severity_model_comparison"
)

st.caption(
    """
    Random Forest outperformed Logistic Regression across accuracy,
    recall and F1 score. However, its recall remained below the
    project's required 85% target.
    """
)
st.info(
    """
    **Why recall is important:** A False Negative occurs when a genuine
    high-severity earthquake is classified as not high severity. Higher
    recall means the model successfully identifies a greater proportion
    of the high-severity events.
    """
)

confusion_data = [
    [84, 21],
    [22, 73]
]

fig_cm = px.imshow(
    confusion_data,
    text_auto=True,
    x=["Predicted: Not High", "Predicted: High"],
    y=["Actual: Not High", "Actual: High"],
    title="Random Forest Confusion Matrix"
)

st.plotly_chart(
    fig_cm,
    use_container_width=True,
    key="random_forest_confusion_matrix"
)

st.markdown(
    """
    The Random Forest correctly classified 84 non-high-severity events
    and 73 high-severity events.

    It incorrectly classified 21 non-high-severity events as high severity
    and missed 22 genuinely high-severity events.

    The 22 false negatives are especially important because they represent
    high-severity earthquakes that the model failed to identify. These missed
    events contribute to the model's recall remaining below the project's
    85% target.
    """
)

feature_importance = pd.DataFrame({
    "Feature": [
        "Magnitude",
        "Longitude",
        "Latitude",
        "Depth",
        "magType_mww",
        "magType_mwc",
        "magType_mwb",
        "magType_mw",
        "magType_mb",
        "magType_md",
        "magType_ms",
        "magType_ml"
    ],
    "Importance": [
        0.261501,
        0.246031,
        0.230671,
        0.207811,
        0.015013,
        0.013695,
        0.010441,
        0.008796,
        0.002821,
        0.001821,
        0.001092,
        0.000309
    ]
})

fig_importance = px.bar(
    feature_importance,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Random Forest Feature Importance"
)
fig_importance.update_layout(
    xaxis_title="Feature Importance",
    yaxis_title="Feature",
    yaxis={
        "categoryorder": "total ascending"
    }
)
st.plotly_chart(
    fig_importance,
    use_container_width=True,
    key="random_forest_feature_importance"
)
st.markdown(
    """
    Magnitude was the most important individual feature used by the
    Random Forest model, followed by longitude, latitude and depth.

    These four numerical features accounted for the majority of the model's
    feature importance, while the individual encoded magnitude-type features
    contributed comparatively little to the model's predictions.
    """
)
st.caption(
    """
    Feature importance describes how useful a variable was to the Random
    Forest when making predictions. It does not mean that the feature
    causes an earthquake to be high severity.
    """
)

st.divider()
st.subheader("Model Conclusion")

st.markdown(
    """
    Random Forest provided the strongest classification performance,
    outperforming the Logistic Regression baseline across the main
    evaluation metrics.

    The Random Forest achieved 78.50% accuracy, 76.84% recall
    and an F1 score of 0.77. Its confusion matrix showed that the
    model correctly identified 73 of 95 high-severity events, while
    22 high-severity events were missed.

    Feature importance showed that magnitude, longitude, latitude and
    depth contributed most strongly to the Random Forest's predictions.

    However, the model's 76.84% recall remained below the project's
    target of 85%. Therefore, although the model demonstrates predictive
    potential, further development would be required to meet the project's
    defined performance requirement.
    """
)

st.warning(
    """
    Final Model Result: Random Forest was the strongest model,
    but its 76.84% recall did not achieve the required 85% target.
    """
)