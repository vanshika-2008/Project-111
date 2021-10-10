import random
import csv
import pandas as pds
import plotly.figure_factory as pxfig
import plotly.graph_objects as pgo
import statistics as stats

df = pds.read_csv('studentMarks.csv')
data = df['Math_score'].tolist()
fig = pxfig.create_distplot([data],['Math Scores'],show_hist=False)
fig.show()
print('Population Mean ', stats.mean(data))
print('Population Standard Deviation : ', stats.stdev(data))

def Random_Means () :
    dataset = []
    for i in range(0,100) :
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    Mean = stats.mean(dataset)
    return Mean

Mean_List = []
for i in range(0,1000) :
    Set_Means = Random_Means()
    Mean_List.append(Set_Means)

sdev = stats.stdev(Mean_List)
Mean = stats.mean(Mean_List)
fsds,fsde = Mean-sdev,Mean+sdev
ssds,ssde = Mean-(2*sdev),Mean+(2*sdev)
tsds,tsde = Mean-(3*sdev),Mean+(3*sdev)

df = pds.read_csv('data1.csv')
data1= df['Math_score'].tolist()
Mean_Sample1 = stats.mean(data1)

df = pds.read_csv('data2.csv')
data2= df['Math_score'].tolist()
Mean_Sample2 = stats.mean(data2)

df = pds.read_csv('data3.csv')
data3= df['Math_score'].tolist()
Mean_Sample3 = stats.mean(data3)

fig = pxfig.create_distplot([Mean_List],['Math Scores'],show_hist=False)
fig.add_trace(pgo.Scatter(x= [Mean,Mean],y=[0,0.17],mode = 'lines',name = 'Mean'))
fig.add_trace(pgo.Scatter(x= [fsds,fsds],y=[0,0.17],mode = 'lines',name = 'fsds'))
fig.add_trace(pgo.Scatter(x= [fsde,fsde],y=[0,0.17],mode = 'lines',name = 'fsde'))
fig.add_trace(pgo.Scatter(x= [ssds,ssds],y=[0,0.17],mode = 'lines',name = 'ssds'))
fig.add_trace(pgo.Scatter(x= [ssde,ssde],y=[0,0.17],mode = 'lines',name = 'ssde'))
fig.add_trace(pgo.Scatter(x= [tsds,tsds],y=[0,0.17],mode = 'lines',name = 'tsds'))
fig.add_trace(pgo.Scatter(x= [tsde,tsde],y=[0,0.17],mode = 'lines',name = 'tsde'))
fig.add_trace(pgo.Scatter(x= [Mean_Sample1,Mean_Sample1],y=[0,0.17],mode = 'lines',name = 'Mean 1'))
fig.add_trace(pgo.Scatter(x= [Mean_Sample2,Mean_Sample2],y=[0,0.17],mode = 'lines',name = 'Mean 2'))
fig.add_trace(pgo.Scatter(x= [Mean_Sample3,Mean_Sample3],y=[0,0.17],mode = 'lines',name = 'Mean 3'))

fig.show()
print('Sampling Mean ', stats.mean(Mean_List))
print('Sampling Standard Deviation : ', stats.stdev(Mean_List))
Z_Score1 = (Mean-Mean_Sample1)/(sdev)
Z_Score2 = (Mean-Mean_Sample2)/(sdev)
Z_Score3 = (Mean-Mean_Sample3)/(sdev)

print(Z_Score1,Z_Score2,Z_Score3)