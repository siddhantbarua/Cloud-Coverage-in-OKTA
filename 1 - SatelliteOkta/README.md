# Satellite Implementation
This project uses the satellite image published by IMD to find out the cloud cover. The script gives out the cloud cover as percentage as well as okta units.

## Installation
To run this script, one needs to have MATLAB installed on the computer, along with a licence to run MATLAB.

## Usage

```matlab 
[cent, okta]=getOkta('City');
[cent, okta]=getOkta('Latitude','Longitude');
```

The variable cent stores the cloud cover in percentage and okta variable gives its okta unit equivalent.
The input to the function can be a city or a coordinates, which follows the convention as North and East coordinates are positive and so on.

When city is provided as input it uses the cities.csv file to find out its coordinates and use it to map the city on the image.

```matlab 
[cent, okta]=getOktaHis('City');
[cent, okta]=getOktaHis('Latitude','Longitude');
```
The given function can provide you with the graph of cloud cover for the past 6 hours, the variables cent and okta returns a vector of cloud cover values in half an hour intervals.