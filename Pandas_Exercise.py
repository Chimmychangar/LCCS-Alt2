import statistics
import pandas


# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('ATEEZPRESENT.csv')


# Filter out the column, value_eur
Ateez = df['Ateez']
Bouncy = df['Bouncy']
Thanx  = df['Thanx ']
Guerrila  = df['Guerrila']
print(Ateez, Bouncy, Thanx, Guerrila )
