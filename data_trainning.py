import json
import statistics as st
import numpy as np
from sklearn import svm

with open("windows/windows_nopothole.txt", "r") as fp:
        nopothole = json.load(fp)

with open("windows/windows_pothole.txt", "r") as fp:
        pothole = json.load(fp)

#arrays to fit the model
x=[]
y=[] #1 for pothole, 2 for no pothole

#Obtain x mean
#Obtain y mean
#Obtain z mean
#Obtain x standard deviation
#Obtain y standard deviation
#Obtain z standard deviation

def calculation(window):
    #x mean
    x_mean = st.mean(window[0])
    #y mean
    y_mean = st.mean(window[1])
    #z mean
    z_mean = st.mean(window[2])
    #x standard deviation
    x_stdev = st.stdev(window[0])
    #y standard deviation
    y_stdev = st.stdev(window[1])
    #z standard deviation
    z_stdev = st.stdev(window[2])
    return [x_mean,y_mean,z_mean, x_stdev,y_stdev,z_stdev]
    

for window in pothole:
    #print("window: "+str(window))
    x.append(calculation(window))
    y.append(1)
for window in nopothole:
    x.append(calculation(window))
    y.append(2)

print(x[len(x)-5])

x_np = np.array(x)
y_np = np.array(y)

clf_linear = svm.SVC(kernel = 'linear')
clf_linear.fit(x_np, y_np)

pred = clf_linear.predict([x[len(x)-5]])
print(pred)

test=[[1.1209999322891235, 0.666700005531311, -1.538100004196167, -1.4865999221801758, -0.00969999935477972, 1.5194000005722046, 1.5194000005722046, 0.3546999990940094, -1.7628999948501587, -1.055799961090088, -1.990899920463562, -1.8550999164581299, -2.696499824523926, -2.696499824523926, -1.7003999948501587], [0.8535999655723572, 0.15779998898506165, -0.9716999530792236, -0.44099998474121094, 3.561699867248535, 2.3252999782562256, 2.3252999782562256, 2.3420000076293945, 1.4957000017166138, 3.062700033187866, 3.90310001373291, 4.3954997062683105, 1.2563999891281128, 1.2563999891281128, 5.672100067138672], [0.3174999952316284, 2.1045000553131104, 0.8501999974250793, 2.2367000579833984, 0.32029998302459717, 0.9368000030517578, 0.9368000030517578, 3.714900016784668, -0.7728999853134155, 2.4535999298095703, 5.344399929046631, 2.7135000228881836, 1.92739999294281, 1.92739999294281, 7.079799652099609], [6.207, 6.225, 6.24, 6.258, 6.275, 6.292, 6.309, 6.324, 6.341, 6.358, 6.376, 6.393, 6.409, 6.425, 6.441]]
pred = clf_linear.predict([calculation(test)])
print(pred)
