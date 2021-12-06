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

#get queens data
queens = df.loc[df['Borough'] == 'Queens']
#print(queens)
#got total from amount of rows
total_applications_queens = queens.shape[0]
print("Total applications submitted for Queens: ", total_applications_queens)
#get all sidewalk seatings for queens
sidewalk_seatings_queens = queens['Approved for Sidewalk Seating'].value_counts()
print("Queens Sidewalk Seating Application Results: ")
#get approval percentage for sidewalk seatings for queens
print(sidewalk_seatings_queens)
sidewalk_acceptance_rate_queens = (2275 / total_applications_queens) * 100 
sidewalk_acceptance_rate_queens = round(sidewalk_acceptance_rate_queens, 2)
print("Percentage of sidewalk seating applications approved for Queens :", sidewalk_acceptance_rate_queens, "%")
#get queens roadwalk seatings 
roadwalk_seatings_queens = queens['Approved for Roadway Seating'].value_counts()
print("Roadwalk Seating Application Results for Queens : ", roadwalk_seatings_queens)
roadwalk_acceptance_rate_queens = (1601/ total_applications_queens) * 100 
roadwalk_acceptance_rate_queens = round(roadwalk_acceptance_rate_queens, 2)
print("Percentage of roadwalk seating applications approved for Queens : ", roadwalk_acceptance_rate_queens, "%")

# get manhattan data 
manhattan = df.loc[df['Borough'] == 'Manhattan']
#print(manhattan)
total_applications_manhattan = manhattan.shape[0]
print("Total applications submitted for Manhattan: ", total_applications_manhattan)
#get all sidewalk seatings for manhattan
sidewalk_seatings_manhattan = manhattan['Approved for Sidewalk Seating'].value_counts()
print("Manhattan Sidewalk Seating Application Results: ", sidewalk_seatings_manhattan)
#get approval percentage for sidewalk seatings for manhattan
sidewalk_acceptance_rate_manhattan = (5187 / total_applications_manhattan) * 100 
sidewalk_acceptance_rate_manhattan = round(sidewalk_acceptance_rate_manhattan, 2)
print("Percentage of sidewalk seating applications approved for Manhattan :", sidewalk_acceptance_rate_manhattan, "%")
#get manhattan roadwalk seatings 
roadwalk_seatings_manhattan = manhattan['Approved for Roadway Seating'].value_counts()
print("Roadwalk Seating Application Results for Manhattan : ", roadwalk_seatings_manhattan)
roadwalk_acceptance_rate_manhattan = (4176/ total_applications_manhattan) * 100 
roadwalk_acceptance_rate_manhattan = round(roadwalk_acceptance_rate_manhattan, 2)
print("Percentage of roadwalk seating applications approved for Manhattan : ", roadwalk_acceptance_rate_manhattan, "%")

#get brooklyn data 
brooklyn = df.loc[df['Borough'] == 'Brooklyn']
#print(brooklyn)
total_applications_brooklyn = brooklyn.shape[0]
print("Total applications submitted for Brooklyn: ", total_applications_brooklyn)
#get all sidewalk seatings for brooklyn 
sidewalk_seatings_brooklyn = brooklyn['Approved for Sidewalk Seating'].value_counts()
print("Brooklyn Sidewalk Seating Application Results: ", sidewalk_seatings_brooklyn)
#get approval percentage for sidewalk seatings for brooklyn
sidewalk_acceptance_rate_brooklyn = (2675 / total_applications_brooklyn) * 100 
sidewalk_acceptance_rate_brooklyn = round(sidewalk_acceptance_rate_brooklyn, 2)
print("Percentage of sidewalk seating applications approved for Brooklyn :", sidewalk_acceptance_rate_brooklyn, "%")
#get brooklyn roadwalk seatings 
roadwalk_seatings_brooklyn = brooklyn['Approved for Roadway Seating'].value_counts()
print("Roadwalk Seating Application Results for Brooklyn : ", roadwalk_seatings_brooklyn)
roadwalk_acceptance_rate_brooklyn = (2060/ total_applications_brooklyn) * 100 
roadwalk_acceptance_rate_brooklyn = round(roadwalk_acceptance_rate_brooklyn, 2)
print("Percentage of roadwalk seating applications approved for Brooklyn : ", roadwalk_acceptance_rate_brooklyn, "%")

#get bronx data 
bronx = df.loc[df['Borough'] == 'Bronx']
#print(bronx)
total_applications_bronx = bronx.shape[0]
print("Total applications submitted for the Bronx: ", total_applications_bronx)
#get all sidewalk seatings for bronx
sidewalk_seatings_bronx = bronx['Approved for Sidewalk Seating'].value_counts()
print("Bronx Sidewalk Seating Application Results: ", sidewalk_seatings_bronx)
#get approval percentage for sidewalk seatings for bronx
sidewalk_acceptance_rate_bronx = (648 / total_applications_bronx) * 100 
sidewalk_acceptance_rate_bronx = round(sidewalk_acceptance_rate_bronx, 2)
print("Percentage of sidewalk seating applications approved for the Bronx :", sidewalk_acceptance_rate_bronx, "%")
#get bronx roadwalk seatings 
roadwalk_seatings_bronx = bronx['Approved for Roadway Seating'].value_counts()
print("Roadwalk Seating Application Results for the Bronx : ", roadwalk_seatings_bronx)
roadwalk_acceptance_rate_bronx = (402/ total_applications_bronx) * 100 
roadwalk_acceptance_rate_bronx = round(roadwalk_acceptance_rate_bronx, 2)
print("Percentage of roadwalk seating applications approved for the Bronx : ", roadwalk_acceptance_rate_bronx, "%")

#get staten island data
staten_island = df.loc[df['Borough'] == 'Staten Island']
#print(staten_island)
total_applications_staten_island = staten_island.shape[0]
print("Total applications submitted for Staten Island : ", total_applications_staten_island)
#get all sidewalk seatings for bronx
sidewalk_seatings_staten_island = staten_island['Approved for Sidewalk Seating'].value_counts()
print("Staten Island Sidewalk Seating Application Results: ", sidewalk_seatings_staten_island)
#get approval percentage for sidewalk seatings for staten island
sidewalk_acceptance_rate_staten_island = (178 / total_applications_staten_island) * 100 
sidewalk_acceptance_rate_staten_island = round(sidewalk_acceptance_rate_staten_island, 2)
print("Percentage of sidewalk seating applications approved for Staten Island :", sidewalk_acceptance_rate_staten_island, "%")
#get staten island roadwalk seatings 
roadwalk_seatings_staten_island = staten_island['Approved for Roadway Seating'].value_counts()
print("Roadwalk Seating Application Results for Staten Island : ", roadwalk_seatings_staten_island)
roadwalk_acceptance_rate_staten_island = (96/ total_applications_staten_island) * 100 
roadwalk_acceptance_rate_staten_island = round(roadwalk_acceptance_rate_staten_island, 2)
print("Percentage of roadwalk seating applications approved for Staten Island : ", roadwalk_acceptance_rate_staten_island, "%")


