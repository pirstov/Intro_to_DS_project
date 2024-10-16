# Intro_to_DS_project
This is a repository for the "Introduction to data science" course project.

The topic is on predicting the price of spot-electricity in Finland.

# 16.10.2024
- Random forest found good, TPOT helped
- Deliverables, website and technical report
- Structure
    1. Introduction (topic, "explanation on how were things done", inside intro or separately before canvas)
    2. Mini-project canvas
    3. Address each of the parts in the canvas in order, left-to-right, top-to-bottom. For each part, consider the list below and also the moodle deliverables page.
    4. Learning outcomes
    5. Summary
- Technical report, lets use Latex
    - Mini-project canvas
    - Consider adding some of the data preprocessing figures / exploratory analysis results
    - Timeline: use MoMs as backup material
    - Discuss data, where and what. How was the data processed?
    - Data APIs, what kind and how?
    - What didn't work? Many things, time series model & XGBoost
    - Data limitations, forecasts not necessarily available for interesting inputs (nuclear power etc.)
    - Delta from initial plan: different predictor, different input variables
    - If anything comes to mind, "what would you have done differently now?"
    - More / better input variables. More weather measurements across Finland
    - Explanation on how were things done:
        - Telegram used for communication, weekly in-person meetings at Campus
        - Version control, git with clear repository structure (split implementation into files for each step)
        - Language: python
        - Format: jupyter notebooks
    - Learning outcomes:
        - Data preprocessing: data to correct form
        - Familiarizing ourselves with different AI models
        - Learning to use APIs
        - Getting comfortable with version control, Git
        - Collaboration
        - Prediction is difficult!
        - Planning short business pitches
     
- Website Ahsan
- User settings:
      - Length of forecast/prediction
      - Buttons for setting the x-axis (one week future, previous week, previous month, previous year)
      - Interactive figure
          - x- and y- axes can be adjusted and shifted so that the user can look at the upcoming prediction or last week
      - Average fixed price included for reference
      - next-day electricity prices when available
      - Prediction from random forest

# 9.10.2024 MoM pt. 2
- EDA, correlations between variables and spot price / Emil
- model parameterization, how to increase "random" behavior / Ville
- Add holidays into model / Ville
- Random forest model / Ahsan
- Model trying / Emil
- Data preprocessing and model split into separate files / Ville
- Create a ppt, add to repo and sketch out / Everyone

# 9.10.2024 MoM on spotlight presentation
- Spotlight session planning, 3 minutes
- Structure: CHALLENGE / SOLUTION / WHY
    - Problem/challenge: Many people in Finland are using spot price. Spot prices available one day prior, would be nice to have information for a longer period to plan electricity consumption better
    - Examples: upcoming trip, preparations such as charging car, washing laundry, sauna etc.
    - Slide ideas: figure of electricity contract types in Finland / Spot price vs fixed prices example figure / figure highlighting that prices are available only one day prior
      
    - Solution: long-term (2-7 days) predictions
    - How: use AI/predictive models
    - where can the customer see this, webpage?
    - Slide ideas: Insert a nice hand-picked example here 
    
    - Why:
    - business motivation, save money by enabling long-term planning of electricity usage 
    - Peace of mind, less stressing over how the prices will evolve in the near future
    - Avoid surprises in the form of sudden long-lasting price hikes
    - Slides: same figure as previous slide, but with plan of activities to optimize savings
      
# 2.10.2024 MoM
- Holidays included
- Electricity production and consumption for 2024
- Electricity production and consumptions forecast API taken into use, 24 hours
- Weather forecast API is also in use, 14 day forecast

- Outliers, when new features in use / Justify removal of high/very low price samples
- Time series model fitting function to be made still /Ville
- Metrics to be decided /Ville
- No nuclear or import/export due to lack of forecasts
- Still descriptive statistics / EDA **EVERYONE** OK
- Skip additional weather measurements from different locations, can be done later
- ADF to be done /Ville OK

- Fingrid API further studies, forecasts /Emil OK

- Machine learning models /Ahsan OK
- File splitting
    - Data preprocessing and EDA 
    - Time series modeling
    - Machine learning OK
    - Forecasting OK
    - User interface for checking the prediction

# 25.9.2024 MoM
Planning and distribution of work
- Outlier removing, -50 cent day to be removed **Ahsan**
- Large positive prices, what happens if removed? How can we justify? **Ahsan**
- More input variables, keep all the data in the same dataframe **Ahsan** 
- Create a function that fits time series model based on **Ville** TBD
  - given start and end date
  - columns of the data frame
  - parameters of the model (for example, order of different terms)
- Evaluation of model, what is a good metric? One-day prediction is evaluated **Ville** MAE used so far
- Add "holiday" as binary input variable OK
- Adding more input variables, nuclear power (no forecasts available?) and import/export to other countries, electricity consumption prediction, use average per hour **Emil** OK
- Descriptive statistics, mean/variance/modes. Examine for whole data vs seasonal (split into days/months/years)? **All of us!!**
- Consider adding more measurements of temperature and/or wind from different stations (where are the big solar plants and wind parks in Finland)
- What variables can we use if we need their predictions?
- Carry out Augmented Dickey-Fuller (ADF) Test to check for stationarity of time series -> Tells if differencing is required in the model **Ville** OK
- EDA on time series model **Ville** OK
- weather forecast: given location (coordinates or city name), desired measurements (temperature, wind), and length of forecase return data: open-meteo API **Ahsan** OK
- Fingrid API: given length of forecast, return electricity consumption and production forecast data **Emil** OK

# 25.9.2024 Web page ideas
- Give prediction for one hour to week, user set value
- Possibility to see prediction results from the past and compare with actual price

# Participants
The students participating in this project are

Ville Pirsto
Emil Tigerstedt
Ahsan Abbas
