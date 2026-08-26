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
   * Earthquake magnitude and depth operate as statistically independent features, meaning focal depth cannot serve as an indicator of magnitude when classifying high-severity.

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
                 


## The rationale to map the business requirements to the Data Visualisations

* List your business requirements and a rationale for mapping them to the Data Visualisations


## Analysis techniques used

* List the data analysis methods used and explain limitations or alternative approaches.
* How did you structure the data analysis techniques? Justify your response.
* Did the data limit you, and did you use an alternative approach to meet these challenges?
* How did you use generative AI tools to help with ideation, design thinking and code optimisation?

## Dashboard Design (optional)

* Feel free to delete this section if this is a data visualisation only (unit 1 or 2) project submission.
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during project development, you may revisit your dashboard plan to update a feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

## Unfixed Bugs

* Please list any unfixed bugs and explain why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap

* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 



## Main Data Analysis Libraries

* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials; however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section into Content and Media, depending on what you include in your project. 

### Content 

- The text for the Home page was taken from the Wikipedia Article A
- Instructions on how to implement form validation were taken from a [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



