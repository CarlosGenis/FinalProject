#Carlos Genis
#Resources:  Used python.org as a reminder of Python 3 print statements.
#carlos.genis34@myhunter.cuny.edu 
import pandas as pd 

#read file 
df = pd.read_csv('Open_Restaurant_Applications.csv')
#print (df)
#got total from amount of rows
total_applications = df.shape[0]
print("Total applications submitted:", total_applications)
#get all sidewalk seatings
sidewalk_seatings = df['Approved for Sidewalk Seating'].value_counts()
print("Sidewalk Seating Application Results: ")
#get approval percentage for sidewalk seatings 
print(sidewalk_seatings)
sidewalk_acceptance_rate = (10963 / total_applications) * 100 
sidewalk_acceptance_rate = round(sidewalk_acceptance_rate, 2)
print("Percentage of sidewalk seating applications approved:", sidewalk_acceptance_rate, "%")


#get all roadwalk seatings 
roadwalk_seatings = df['Approved for Roadway Seating'].value_counts()
print("Roadwalk Seating Application Results: ", roadwalk_seatings)
roadwalk_acceptance_rate = (8335/ total_applications) * 100 
roadwalk_acceptance_rate = round(roadwalk_acceptance_rate, 2)
print("Percentage of roadwalk seating applications approved: ", roadwalk_acceptance_rate, "%")