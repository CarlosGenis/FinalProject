#Carlos Genis
#Resources:  Used python.org as a reminder of Python 3 print statements.
#carlos.genis34@myhunter.cuny.edu 
import pandas as pd 

#read file 
df = pd.read_csv('Open_Restaurant_Applications.csv')
#print (df)
#got total from amount of rows
total_applications = df.shape[0]
print("Total applications submittted: ", total_applications)
#get all sidewalk seatings
sidewalk_seatings = df['Approved for Sidewalk Seating'].value_counts()
print("Sidewalk Seating Application Results: ")
print(sidewalk_seatings)
#get all roadwalk seatings 
roadwalk_seatings = df['Approved for Roadway Seating'].value_counts()
print("Roadwalk Seating Application Results: ", roadwalk_seatings)
