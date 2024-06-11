# Geolocation Data Analysis

This is a self project that aims to do data analysis to help in suggesting housing locations for students in a city.

## Step by Step Explanation

### Data Collection and Preparation

1. **Download Student Data:**
   - Use this [Kaggle link](https://www.kaggle.com/datasets/borapajo/food-choices?resource=download) to download the student data.
   
2. **Data Cleaning:**
   - Remove unnecessary columns and null values.
   
3. **Data Visualization:**
   - Visualize the data using box plots to understand its distribution and identify any outliers.

### Getting Location Data

1. **Generate API Key:**
   - Go to [Foursquare](https://foursquare.com) and generate an API key.
   
2. **Fetch and Store Location Data:**
   - Use the API key to fetch location data and store it in a JSON file called `geo_data.json`.
   
3. **Convert JSON to DataFrame:**
   - Convert the JSON data to a DataFrame for further analysis.

### K-Means Clustering

1. **Extract Neighbouring Places Data:**
   - Extract the data of the neighbouring places and store them in a DataFrame.

2. **Perform K-Means Clustering:**
   - Use the `scikit-learn` library to perform K-Means clustering.

3. **Visualize Clusters:**
   - Plot the clusters on a map using the `Folium` library.

4. **Print Cluster Stats:**
   - Print the statistics of the clusters to help decide which type of user will prefer what location.
### Note:

Currently, the script in `generate_geo_data.py` has the query to generate the data for New York. If you want data for any other city, you can use the coordinates of that city. The general URL will be:

url = "https://api.foursquare.com/v3/places/search?ll=latitude%2Clongitude"
