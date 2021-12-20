# Convert data cities.csv to html


import pandas as pd

# Read csv

cities = pd.read_csv("Instructions/Resources/cities.csv")

# save as html
cities.to_html("data.html")
