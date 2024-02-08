import csv
import pandas
import statistics
import matplotlib.pyplot as plt


df = pandas.read_csv('alt2Project.csv')

# Filter out the column, value_eur
study_values = df['Time_Studying ']
phone_time = df['Phone']
sunday = df['Sunday']
monday = df['Monday']
tuesday = df['Tuesday']
wednesday = df['Wednesday']
thursday = df['Thursday']


mean_value_study = round(statistics.mean(study_values), 2)
print("Mean Value Study:", mean_value_study)

mean_value_phone = round(statistics.mean(phone_time), 2)
print("Mean Value Phone:", mean_value_phone)

mean_value_sunday = round(statistics.mean(sunday), 2)
print("Mean Value Sunday:", mean_value_sunday)

mean_value_tuesday = round(statistics.mean(tuesday), 2)
print("Mean Value Tuesday:", mean_value_tuesday)

mean_value_wednesday = round(statistics.mean(wednesday), 2)
print("Mean Value Wednesday:", mean_value_wednesday)

mean_value_thursday = round(statistics.mean(thursday), 2)
print("Mean Value Thursday:", mean_value_thursday)


#showing the previous data average in a pie chart 
labels = 'mean_value_study', 'mean_value_phone', 'mean_value_sunday','mean_value_tuesday', 'mean_value_wednesday', 'mean_value_thursday'
sizes = [mean_value_study, mean_value_phone, mean_value_sunday, mean_value_tuesday, mean_value_wednesday, mean_value_thursday]
colors = ['pink', 'violet', 'blue', 'purple', 'yellow', 'red']
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # explode 1st slice
# Plot the Pie Chart 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
#plt.axis('equal')
plt.show()

