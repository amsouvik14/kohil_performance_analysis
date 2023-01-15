import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Read the csv file
df=pd.read_csv("Kohlirun.csv")
print(df.head(10))
# Find total number of runs Kohli has scored
total_runs=df["Runs"].sum()
no_of_matches=len(df["Runs"])
print(f"Total number of runs kohli has scored in {no_of_matches} is {total_runs}")
# Average number of runs he has scored
avg_runs=df["Runs"].mean()
print(f"Average runs of lohli in {no_of_matches} is: ",int(avg_runs))
#Numbwr of matches he has played in different position
position=df["Pos"].unique()
print(position)

df["Pos"]=df["Pos"].map({
    3.0:"Batting at 3",
    4.0:"Batting at 4",
    2.0:"Batting at 2",
    1.0:"Batting at 1",
    7.0:"Batting at 7",
    5.0:"Batting at 5",
    6.0:"Batting at 6"
})
print(df[["Runs","Pos","Opposition"]].head(10))
pos_counts=df["Pos"].value_counts()
print(pos_counts)
print(type(pos_counts))
pos_values=pos_counts.values
pos_labels=pos_counts.index
print(pos_values)

fig=plt.figure(figsize=(10,7))
plt.pie(pos_values,labels=pos_labels)
plt.show()
def show_pie_plot(df,key): # Generalised form of drawing 
    counts=df[key].value_counts()
    count_value=counts.values
    count_labels=counts.index
    fig=plt.figure(figsize=(10,7))
    plt.pie(count_value,labels=count_labels)
    plt.show()
show_pie_plot(df,"Pos")
show_pie_plot(df,"Opposition")
show_pie_plot(df,"Ground")
#Total runs socred in different position
runs_at_pos=df.groupby("Pos")["Runs"].sum()
runs_at_pos_values=runs_at_pos.values
runs_at_pos_labels=runs_at_pos.index
fig=plt.figure(figsize=(10,7))
plt.pie(runs_at_pos_values,labels=runs_at_pos_labels)
plt.show()
# Total sixes with diff opposition
six_at_opponent=df.groupby("Opposition")["6s"].sum()
six_at_opponent_values=six_at_opponent.values
six_at_opponent_labels=six_at_opponent.index
fig=plt.figure(figsize=(10,7))
plt.pie(six_at_opponent_values,labels=six_at_opponent_labels)
plt.show()
# No of centuries scored by Kohli in first innings
centuries=df.query("Runs >= 100")
#print(centuries)
innings=centuries["Inns"]
tons=centuries["Runs"]
fig=plt.figure(figsize=(10,7))
plt.bar(innings,tons,color='blue',width=0.2)
plt.show()