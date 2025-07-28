#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

class EVRecommender:
   # A class to recommend electric vehicles (EVs) based on user criteria: budget, desired range, and minimum battery capacity.
   
    
    def __init__(self, data_path):
        self.df = pd.read_excel(data_path)
        # Drop rows with missing values in critical columns
        self.df = self.df.dropna(subset=[
            'Minimal price (gross) [PLN]',
            'Range (WLTP) [km]',
            'Battery capacity [kWh]'
        ])
    
    def recommend_evs(self, budget, desired_range, min_battery_capacity):

        # Filter EVs that meet the criteria
        filtered = self.df[
            (self.df['Minimal price (gross) [PLN]'] <= budget) &
            (self.df['Range (WLTP) [km]'] >= desired_range) &
            (self.df['Battery capacity [kWh]'] >= min_battery_capacity)
        ]
        
        # Sort by price ascending to prioritize affordability
        filtered_sorted = filtered.sort_values(by='Minimal price (gross) [PLN]')
        
        
        result = filtered_sorted[[
            'Car full name',
            'Minimal price (gross) [PLN]',
            'Range (WLTP) [km]',
            'Battery capacity [kWh]'
        ]]

        # Return EVs
        return result


    def recommend_from_user_input(self):
        # Get inputs from the user
        try:
            budget = float(input("Enter your budget (in PLN): "))
            desired_range = float(input("Enter desired minimum range (in km): "))
            min_battery = float(input("Enter minimum battery capacity (in kWh): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            return
        
        # Get recommendations
        result = self.recommend_evs(budget, desired_range, min_battery)

        if result.empty:
            print("No EVs found matching your criteria.")
        else:
            print("\nRecommended EVs:")
            print(result.to_string(index=False))

