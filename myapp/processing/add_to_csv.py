"""Adds records to a csv file"""
import os
import pandas as pd

def add_student_score(name, math_score, english_score):

    new_data  = {
        'name': [name],
        'math_score': [math_score],
        'english_score': [english_score]
    }

    # converts dictionary to dataframe
    new_df = pd.DataFrame(new_data)

    if os.path.exists("records.csv"):
        new_df.to_csv("records.csv", mode='a', header=False, index=False)
    else:
        new_df.to_csv("records.csv", mode='w', header=True, index=False)