# Intro_to_DS_project
This is a repository for the "Introduction to data science" course project.

The topic is on predicting the price of spot-electricity in Finland.

# 2.10.2024 MoM
- Holidays included
- Electricity production and consumption for 2024
- Electricity production and consumptions forecast API taken into use, 24 hours
- Weather forecast API is also in use, 14 day forecast

- Outliers, when new features in use / Justify removal of high/very low price samples
- Time series model fitting function to be made still /Ville
- Metrics to be decided /Ville
- No nuclear or import/export due to lack of forecasts
- Still descriptive statistics / EDA **EVERYONE**
- Skip additional weather measurements from different locations, can be done later
- ADF to be done /Ville

- Fingrid API further studies, forecasts /Emil

- Machine learning models /Ahsan
- File splitting
    - Data preprocessing and EDA 
    - Time series modeling
    - Machine learning
    - Forecasting
    - User interface for checking the prediction

# 25.9.2024 MoM
Planning and distribution of work
- Outlier removing, -50 cent day to be removed **Ahsan**
- Large positive prices, what happens if removed? How can we justify? **Ahsan**
- More input variables, keep all the data in the same dataframe **Ahsan**
- Create a function that fits time series model based on **Ville**
  - given start and end date
  - columns of the data frame
  - parameters of the model (for example, order of different terms)
- Evaluation of model, what is a good metric? One-day prediction is evaluated **Ville**
- Add "holiday" as binary input variable
- Adding more input variables, nuclear power (no forecasts available?) and import/export to other countries, electricity consumption prediction, use average per hour **Emil**
- Descriptive statistics, mean/variance/modes. Examine for whole data vs seasonal (split into days/months/years)? **All of us!!**
- Consider adding more measurements of temperature and/or wind from different stations (where are the big solar plants and wind parks in Finland)
- What variables can we use if we need their predictions?
- Carry out Augmented Dickey-Fuller (ADF) Test to check for stationarity of time series -> Tells if differencing is required in the model **Ville**
- EDA on time series model **Ville**
- weather forecast: given location (coordinates or city name), desired measurements (temperature, wind), and length of forecase return data: open-meteo API **Ahsan**
- Fingrid API: given length of forecast, return electricity consumption and production forecast data **Emil**

# 25.9.2024 Web page ideas
- Give prediction for one hour to week, user set value
- Possibility to see prediction results from the past and compare with actual price

# Participants
The students participating in this project are

Ville Pirsto
Emil Tigerstedt
Ahsan Abbas
