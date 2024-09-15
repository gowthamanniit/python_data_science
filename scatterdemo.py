import pandas as pd
import matplotlib.pyplot as plot
data=pd.read_csv("yourdata.csv")
plot.scatter(data["weekday"],data["collection"])
plot.show()
