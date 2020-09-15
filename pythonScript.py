# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import .csv
df = pd.read_csv('Data/airQualityReformatted.csv')

# Line Graph
plt.scatter(df.CO2, df.UnitsSold)

# Line Plot Title
plt.title('CO2 for Most Popular Cars Sold in 2019')

# Axis Labels
plt.xlabel('Grams of CO2 per Mile Produced')
plt.ylabel('Number of Cars Sold In U.S.')

# X & Y Tick Adjustments

plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           ['Toyota Corolla - 304,850',
            'Honda Civic - 325,650',
            'Toyota Camry - 336,978',
            'Chevrolet Equinox - 346,048',
            'Nissan Rogue - 350,447',
            'Honda C-RV - 384,168',
            'Toyota Rav4 - 448,071',
            'Chevrolet Silverado - 575,600',
            'Ram Pickup - 663,694',
            'Ford F-Series - 896,526'])

# Show Scatter Plot
plt.show()