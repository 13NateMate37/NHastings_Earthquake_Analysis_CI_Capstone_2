# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Earthquake Analysis

**Earthquake Analysis** is an introspective analysis of the thresholds of earthquake events, their classification and 
which combinations of their features need to be recognised collectively as high severity. 


## Dataset Content

Sourced from Kaggle user Chirag Chauhan (https://www.kaggle.com/datasets/warcoder/earthquake-dataset/data) 

Kaggle description:

Datasets contain records of 782 earthquakes from 1/1/2001 to 1/1/2023. The meaning of all columns is as follows:

    title: title name given to the earthquake
    magnitude: The magnitude of the earthquake
    date_time: date and time
    cdi: The maximum reported intensity for the event range
    mmi: The maximum estimated instrumental intensity for the event
    alert: The alert level - “green”, “yellow”, “orange”, and “red”
    tsunami: "1" for events in oceanic regions and "0" otherwise
    sig: A number describing how significant the event is. Larger numbers indicate a more significant event. This value is determined on a number of factors, including: magnitude, maximum MMI, felt reports, and estimated impact
    net: The ID of a data contributor. Identifies the network considered to be the preferred source of information for this event.
    nst: The total number of seismic stations used to determine earthquake location.
    dmin: Horizontal distance from the epicenter to the nearest station
    gap: The largest azimuthal gap between azimuthally adjacent stations (in degrees). In general, the smaller this number, the more reliable is the calculated horizontal position of the earthquake. Earthquake locations in which the azimuthal gap exceeds 180 degrees typically have large location and depth uncertainties
    magType: The method or algorithm used to calculate the preferred magnitude for the event
    depth: The depth where the earthquake begins to rupture
    latitude / longitude: coordinate system by means of which the position or location of any place on Earth's surface can be determined and described
    location: location within the country
    continent: continent of the earthquake hit country
    country: affected country



## Business Requirements

* Humanitarian Aid and Disaster Response organisations need to be able to classify and predict high severity earthquake events, as well which characteristics lead to tsunami generation, to enable more effecient operational planning and resource allocation.   


## Hypothesis and how to validate?


H1 - Magnitude and Depth
   * Earthquake magnitude and depth operate as statistically independent features, meaning depth cannot serve as an indicator of magnitude when classifying high-severity.

   * Validaiton: 
   
   - Pearson Correlation and Spearman Rank correlation tests 
   - Visualise the relationships between magnitude and depth and then check them against the localised intensity (mmi)



H2 - Tsunami Generating Characteristics
   * Earthquakes that generate a tsunami occur at significantly lower depths and are triggered by specific fault mechanisms (magType), as opposed to ones that don't.    

   * Validation:
   
   - Visualise confirmed tsnuami generation agasint depth to see how they correlate
   - 2 sample T-test/Mann-Whitney U Test on the average depth for tsunami generators and non generators
   - Chi-Square Test for the fault mechanism types against the confirmed tsunami generators to confirm whether a certain type is more
   responsible than others


H3 - Classification and Predicitons
   * Machine learning models that are trained solely on the immediate, real-time seismic traits (magnitude, depth, latitude, longitude, magType) can accurately classify high severity events before the crowdsourced data becomes available. Resulting in swifter repsonse allocation

   * Validation:
   
   - Engineer a classification target in binary (0 low severity, 1 high severity) based on a decided threshold rule
   - Test a feature set of the immediate real-time aspects ("magnitude, depth, latitude, longitude, magType") to predict severity.Dropping post event calculate classification as that will act as a cheatsheet. 
   - Train a Logistic Regression model as a baseline and a Random Forest model for comparison. Calculate the Recall score on the test data for an evaluation on it performance, aiming for an 85% accuracte prediction rate.          


## Project Plan

* ETL - Extract the raw data and inspect it
      - Identify and apply necssary transformations
      - Double check and load the edited data into a seperate .csv

* EDA - Explore and visualise the characteristics of the target features 
      - Identify what methods need to be used in hypothesis testing (Parametric/Non-parametric)

* Testing and ML - Run statistical tests for each hypothesis with visualisation and summary 
                 - Use an ML model to test high severity event prediction

* Dashboard - Choose a platform create a dashbaord for the project


## The rationale to map the business requirements to the Data Visualisations

### Investigate the Relationship Between Earthquake Magnitude and Depth
* Visualisations: Distribution plots and magnitude vs depth scatter plot.  
- Rationale: Distribution plots show the spread of each variable, while the scatter plot allows patterns and relationships between magnitude and depth to be identified.

### Investigate Earthquake Characteristics Associated with Tsunami Occurrence
* Visualisations: Depth box plot, magnitude type bar plot and magnitude/depth scatter plot by tsunami status.  
- Rationale: These plots compare tsunami and non-tsunami events across depth, magnitude type and multiple earthquake characteristics.

### Determine Whether Earthquake Characteristics Can Predict High-Severity Events
* Visualisations: Model comparison, confusion matrix and feature importance.  
- Rationale: These visualisations compare model performance, highlight correct and incorrect predictions, and identify the features contributing most to high-severity classification.

## Analysis techniques used

* Pandas tools (.describe, .info, .dtypes, .usnull etc) whre used for the inspection process for identifying transformations. Research with AI assistance helped inform the value imputations.

* Features where engineered for the models to have clearer targets to read. 

 - mag_depth_interaction combines two continuous features so the model can check for any linear and non-linear correltaions.
 - depth_cat groups the depth ranges into categories making for easier an comparision bewteen ranges.
 - high_severity rule uses a combination of measurments(mmi 7+, sig 875+ and alert of orange-red) with values which depict a high severity event. Tells the model what makes an event high severity.
    

* For checking distrubutions of 'magnitude' and 'depth' I used histplots for the visuals, marking the first standard deviation ranges and plotted the kde curve, along side a printed aggregated statistial summary

* Scatterplots where used to inspect what relationship 'magnitude' and 'depth' have, then coloured it by 'mmi' to view if they corrrelate to high severity    

* Countplots where used to view the spread of 'magType' and 'tsunami' split. It was slo used used to view thhe relationship between 'magType' and 'tsunami'

* The dataset wasn't limiting in itself. It was my knowledge on the subject how to handle the information within the dataset

* Chatpgt and Gemini were used for ideation and refining which hypotheses I should use. Gemini was used for quick and direct lookup of information relating to subject. Informing me of things like 'Null-island' artifacts, the depth ranges from surface crust to subduction depths.

* Gemini and Co-pilot were used for some of the plotting code and used to guide me through the Machine Learning and model fitting as my own level of implementaion wasn't up to scratch

* Chatpgt helped me with putting together a streamlit dashboard when the one with PoweBi wasn't going so well

## Dashboard Design 

The Streamlit dashboard was developed as a four-page application
designed to communicate the project’s findings in a logical progression,
moving from a high-level overview of the earthquake dataset through
exploratory analysis and statistical hypothesis testing to the final
machine-learning results.

Page 1 — Earthquake Overview

The Overview page provides an introduction to the dataset and allows the
user to quickly understand its main characteristics before progressing
to the more detailed analysis.

The page includes KPI metrics displaying the total number of earthquake
events, average and maximum magnitude, median earthquake depth, number
of tsunami-associated events, and number of high-severity events.

A line chart displays the distribution of recorded earthquake events
across the study period, while histograms show the distributions of
earthquake magnitude and depth. A key findings section summarises the
main observations from the page in plain language.

This page is primarily intended to provide context and make the dataset
accessible to both technical and non-technical users.

Page 2 — Exploratory Data Analysis

The EDA page explores the main relationships identified during the
exploratory analysis and provides visual evidence for the questions
investigated later through statistical testing.

The page includes:

-   A scatter plot comparing earthquake magnitude and depth.
-   A box plot comparing earthquake depth between tsunami and non-tsunami events.
-   A grouped bar chart comparing tsunami occurrence across magnitude types.
-   A multivariate scatter plot displaying magnitude and depth by tsunami status.
-   Supporting captions and an EDA summary explaining the main patterns identified.

The visualisations were selected based on the final exploratory analysis
rather than strictly following the initial dashboard plan. Where
necessary, visualisation choices were revised during development to
ensure that the final charts communicated the relationships clearly.

Page 3 — Hypothesis Testing

The Hypothesis Testing page translates the visual patterns identified
during EDA into statistical evidence.

For the relationship between magnitude and depth, the dashboard presents
the Pearson and Spearman correlation coefficients and their p-values.
The results demonstrate no statistically significant linear
relationship, while Spearman identifies a statistically significant but
extremely weak monotonic relationship.

For tsunami occurrence, the page presents the Mann–Whitney U test result
for earthquake depth alongside the Cliff’s Delta interpretation. These
results show no statistically significant or practically meaningful
difference in depth between tsunami and non-tsunami events. The
Chi-square result is also presented, showing a statistically significant
association between magnitude type and tsunami occurrence.

The final section presents the results of the machine-learning
hypothesis, comparing model recall against the project’s predefined 85%
recall target.

Each statistical result is accompanied by a plain-language
interpretation so that users are not required to understand p-values,
correlation coefficients or statistical tests independently.

Page 4 — High-Severity Earthquake Prediction

The Severity Prediction page provides a more detailed examination of the
machine-learning stage of the project.

The page compares the Logistic Regression baseline with the Random
Forest model using accuracy, recall and F1 score. Random Forest was the
stronger model, achieving 78.50% accuracy, 76.84% recall and an F1 score
of 0.77, compared with 68.50% accuracy, 61.05% recall and an F1 score of
0.65 for Logistic Regression.

A confusion matrix provides further detail on the Random Forest
predictions. Of the 200 test observations, the model correctly
classified 84 non-high-severity and 73 high-severity events, while
producing 21 false positives and 22 false negatives.

A feature-importance visualisation shows that magnitude, longitude,
latitude and depth contributed most strongly to the Random Forest’s
predictions. This is presented as model importance rather than evidence
of physical causation.

The page concludes by comparing the Random Forest’s 76.84% recall with
the project’s required 85% target, clearly communicating that the model
demonstrated predictive potential but did not achieve the predefined
performance requirement.

Communicating Insights to Different Audiences

The dashboard was designed to make the same analysis understandable to
both technical and non-technical audiences.

For non-technical users, KPI cards, charts, descriptive headings and
short written interpretations communicate the key findings without
requiring knowledge of Python, statistical testing or machine learning.
Technical terms such as recall, false negatives and statistical
significance are accompanied by explanations of what they mean in the
context of the project.

For technical users, the dashboard retains the numerical evidence behind
the conclusions, including correlation coefficients, p-values,
effect-size interpretation, model evaluation metrics, the confusion
matrix and feature importance.


## Conclusion

This project explored relationships between earthquake magnitude, depth, tsunami occurrence and high-severity events using EDA, statistical testing and Machine Learning.

The analysis found little practical relationship between magnitude and depth, while depth also showed no significant difference between tsunami and non-tsunami events. In contrast, magnitude type showed a statistically significant association with tsunami occurrence. For high-severity prediction, Random Forest outperformed Logistic Regression, achieving 78.50% accuracy, 76.84% recall and an F1 score of 0.77. However, recall remained below the project's 85% target, indicating that further model development would be required.

Overall, the project demonstrates how statistical analysis, Machine Learning and interactive visualisation can be combined to identify and communicate meaningful patterns within earthquake data.


## Main Data Analysis Libraries

* Pandas - ETL, EDA, H-testing, ML
* Numpy - ETL
* Seaborn - EDA, H-testing, ML
* Matplotlib - EDA, H-testing, ML
* Scipy - H-testing
* Scikitlearn - H-testing, ML

## Credits

* Dataset - https://www.kaggle.com/datasets/warcoder/earthquake-dataset/data - Chirag Chauhan

* Vasi and Rory - Tutors who aided in my understandings and provided feedback for progression

* Friends John & James for explaining mathemtical concepts, providing advice and project format assiatance

* Ai's Chatgpt and Gemini where use across the length of the project, for ideation and direct project support, both technical (code/methods) and topic comprehension. 

* Code Institutes course notebooks where used for code as well. Having directly used the plotting exmaple from 'Descriptive Statistics Topic 3: Variability'.


