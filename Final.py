
import pandas as pd
import csv
from io import StringIO
input_file = "Cities.csv"
data = "NAME,DATE,TAVG\na,b,1\na,b,2\nc,d,3"
pd.read_csv(StringIO(data))

