import pandas as pd
import matplotlib.pyplot as mp
collect_data=pd.read_csv("gender_submission.csv")
print("Collect data set:",collect_data)
collect_data.rename(columns={"Passengerld":"Id","Survived":"Status for clarity"},inplace=True),
print("Renamed column name:",collect_data)
print("The Collect data from the Top:",collect_data.head()) 
print("The Collect data from the Bottom:",collect_data.tail())
print("Collect dataset information:",collect_data.info())
print("Count:",collect_data.shape)
Non_survived=collect_data[collect_data["Status for clarity"]==0].head(10)
print("10 Non-Survived:",Non_survived)
survived=collect_data[collect_data["Status for clarity"]==1].head(10)
print("Top 10 Survived:",survived)
Total_count=collect_data["Status for clarity"].value_counts()
survived_count=Total_count[1]
Nonsurvived_count=Total_count[0]
print("Total Survived:",survived_count)
print("Total Not Survived:",Nonsurvived_count)
Total_passengers=len(collect_data)
percentage_of_survived_passengers=(survived_count/Total_passengers)*100
percentage_of_Nonsurvived_passengers=(Nonsurvived_count/Total_passengers)*100
print("Percentage Survived:",percentage_of_survived_passengers)
print("Percentage Non Survived:",percentage_of_Nonsurvived_passengers)
Total_count.plot(kind='bar',color=["red","skyblue"])
mp.xlabel("Status")
mp.ylabel("No of persons")
mp.title("Survived vs non survived")
mp.xticks(rotation=0)
mp.show()
