import numpy as np
import pandas as pd
from apyori import apriori

df=pd.read_csv(open('D:/desktop/Content DS/GroceryStoreDataset.csv','rb'))

#convert data in the form of list
record=[]
for i in range(0,19):
    record.append([str(df.values[i,j]) for j in range(0,4)])

#build apriori model

ass_rule=apriori(record,min_support=0.2,min_confidence=0.39,min_lift=0.01,min_length=2)
ass_result=list(ass_rule)

#print the number of rule generated
print(len(ass_result))

#check the rule

print(ass_result)


conf=[]
support=[]
lift=[]
product=[]

for i in range(len(ass_result)):
        product.append(ass_result[i][0])
        support.append(ass_result[i][1])
        conf.append(ass_result[i][2][0][2])
        lift.append(ass_result[i][2][0][3])
        

productDF=pd.DataFrame(product,columns=['Product 1','Product 2','Product 3'])
supportDF=pd.DataFrame(support,columns=['Support'])
confidenceDF=pd.DataFrame(conf,columns=['Confidence'])
liftDF=pd.DataFrame(lift,columns=['Lift'])


d1=productDF.join(supportDF)
d2=d1.join(confidenceDF)
FinalDF=d2.join(liftDF)











