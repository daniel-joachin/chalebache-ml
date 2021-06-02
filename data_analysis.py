import requests
import numpy as np
import json
import matplotlib.pyplot as plt

API_URL='http://localhost:3030/api/potholes/batch'

r = requests.get(API_URL)
response = r.json()
print(response)

#Declaring arrays to order data
#Pothole
x_acce=[]
y_acce=[]
z_acce=[]
time=[]
x_gyro=[]
y_gyro=[]
z_gyro=[]

#No pothole
x1_acce=[]
y1_acce=[]
z1_acce=[]
time1=[]
x1_gyro=[]
y1_gyro=[]
z1_gyro=[]

#Index of entries
pothole_ind=-1
nopothole_ind=-1

for entry in response:
    pothole_flag=0
    print("pothole: "+str(pothole_ind))
    print("no pothole: "+str(nopothole_ind))
    if(entry['accelerometer']==[]):
            continue
    for acce_data in entry['accelerometer']:
        #print(acce_data)
        if not pothole_flag:
            #print("pothole")
            pothole=acce_data['pothole']
            if pothole:
                x_acce.append([])
                y_acce.append([])
                z_acce.append([])
                time.append([])
                pothole_ind+=1
            else:
                x1_acce.append([])
                y1_acce.append([])
                z1_acce.append([])
                time1.append([])
                nopothole_ind+=1
            #print(x_acce)
            pothole_flag=1
        if pothole:
            x_acce[pothole_ind].append(acce_data['data'][0])
            y_acce[pothole_ind].append(acce_data['data'][1])
            z_acce[pothole_ind].append(acce_data['data'][2])
            time[pothole_ind].append(acce_data['time'])
        else:
            x1_acce[nopothole_ind].append(acce_data['data'][0])
            y1_acce[nopothole_ind].append(acce_data['data'][1])
            z1_acce[nopothole_ind].append(acce_data['data'][2])
            time1[nopothole_ind].append(acce_data['time'])
    '''print(x_acce)
    print(y_acce)
    print(z_acce)
    print(time_acce)'''
    pothole_flag=0
    for gyro_data in entry['gyroscope']:
        #print(gyro_data)
        if not pothole_flag:
            pothole=gyro_data['pothole']
            if pothole:
                x_gyro.append([])
                y_gyro.append([])
                z_gyro.append([])
            else:
                x1_gyro.append([])
                y1_gyro.append([])
                z1_gyro.append([])
            pothole_flag=1
        if pothole:
            x_gyro[pothole_ind].append(gyro_data['data'][0])
            y_gyro[pothole_ind].append(gyro_data['data'][1])
            z_gyro[pothole_ind].append(gyro_data['data'][2])
        else:
            x1_gyro[nopothole_ind].append(gyro_data['data'][0])
            y1_gyro[nopothole_ind].append(gyro_data['data'][1])
            z1_gyro[nopothole_ind].append(gyro_data['data'][2])

#print(time_acce)
#print(time_gyro)

#Saving pothole trainning data
with open("training data/x_acce_pothole.txt", "w") as fp:
    json.dump(x_acce, fp)
with open("training data/y_acce_pothole.txt", "w") as fp:
    json.dump(y_acce, fp)
with open("training data/z_acce_pothole.txt", "w") as fp:
    json.dump(z_acce, fp)
with open("training data/x_gyro_pothole.txt", "w") as fp:
    json.dump(x_gyro, fp)
with open("training data/y_gyro_pothole.txt", "w") as fp:
    json.dump(y_gyro, fp)
with open("training data/z_gyro_pothole.txt", "w") as fp:
    json.dump(z_gyro, fp)
with open("training data/time_pothole.txt", "w") as fp:
    json.dump(time, fp)

#Saving no pothole trainning data
with open("training data/x_acce_nopothole.txt", "w") as fp:
    json.dump(x1_acce, fp)
with open("training data/y_acce_nopothole.txt", "w") as fp:
    json.dump(y1_acce, fp)
with open("training data/z_acce_nopothole.txt", "w") as fp:
    json.dump(z1_acce, fp)
with open("training data/x_gyro_nopothole.txt", "w") as fp:
    json.dump(x1_gyro, fp)
with open("training data/y_gyro_nopothole.txt", "w") as fp:
    json.dump(y1_gyro, fp)
with open("training data/z_gyro_nopothole.txt", "w") as fp:
    json.dump(z1_gyro, fp)
with open("training data/time_nopothole.txt", "w") as fp:
    json.dump(time1, fp)

#Graphing to analyse our data acce pothole
fig, axs = plt.subplots(3)
fig.tight_layout(pad=3.0)

axs[0].plot(time[0],x_acce[0],'tab:blue')
axs[0].set_title('X')

axs[1].plot(time[0],y_acce[0],'tab:red')
axs[1].set_title('Y')

axs[2].plot(time[0],z_acce[0],'tab:green')
axs[2].set_title('Z')

for ax in axs:
    ax.set(xlabel='Time', ylabel='Value')

plt.show()

#Graphing to analyse our data gyro
fig, axs = plt.subplots(3)
fig.tight_layout(pad=3.0)

axs[0].plot(time[20],x_gyro[20],'tab:blue')
axs[0].set_title('X')

axs[1].plot(time[20],y_gyro[20],'tab:red')
axs[1].set_title('Y')

axs[2].plot(time[20],z_gyro[20],'tab:green')
axs[2].set_title('Z')

for ax in axs:
    ax.set(xlabel='Time', ylabel='Value')

plt.show()

#Graphing to analyse our data acce no pothole
fig, axs = plt.subplots(3)
fig.tight_layout(pad=3.0)

axs[0].plot(time1[20],x1_acce[20],'tab:blue')
axs[0].set_title('X')

axs[1].plot(time1[20],y1_acce[20],'tab:red')
axs[1].set_title('Y')

axs[2].plot(time1[20],z1_acce[20],'tab:green')
axs[2].set_title('Z')

for ax in axs:
    ax.set(xlabel='Time', ylabel='Value')

plt.show()