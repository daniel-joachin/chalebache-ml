import json
import matplotlib.pyplot as plt
import numpy as np
import statistics as st
from sklearn import svm
from numpy.core.records import array
from sklearn.neighbors import KNeighborsClassifier

def createWindows(response):
    #arrays para almacenar los datos de cada eje provenientes de la aplicación móvil
    x_acce = []
    y_acce = []
    z_acce = []
    time = []
    location_lon = []
    location_lat = []
    pothole_ind = -1
    #iteramos sobre la respuesta para acomodar los datos de manera más conveniente
    for entry in response:
        append_flag=0
        if(entry['accelerometer'] == []):
                continue
        for acce_data in entry['accelerometer']:
            if not append_flag:
                append_flag=True
                x_acce.append([])
                y_acce.append([])
                z_acce.append([])
                time.append([])
                location_lon.append([])
                location_lat.append([])
                pothole_ind += 1    
                pothole_flag = 1
            x_acce[pothole_ind].append(acce_data['data'][0])
            y_acce[pothole_ind].append(acce_data['data'][1])
            z_acce[pothole_ind].append(acce_data['data'][2])
            time[pothole_ind].append(acce_data['time'])
            location_lon[pothole_ind].append(acce_data['location']['long'])
            location_lat[pothole_ind].append(acce_data['location']['lat'])
                
    #create windows
    windows = [] #aqui vamos a almacenar cada ventana 
    current = 0 #indice para saber en que dato vamos de la grabación
    winSize = 15 #tamaño en datos de cada ventana
    print("Records: ", len(x_acce))
    for i in range(0, len(x_acce)):
        print("Samples per record : "+str(len(x_acce[i])))
        for j in range(0, len(x_acce[i]) // winSize): # Creamos tantas ventanas como nos permita la cantidad de datos, con división de piso en caso de no ser exactos
            window = [] #ventana donde almacenaremos el array de [x, y, z, time]
            arrayX = [] 
            arrayY = []
            arrayZ = []
            arrayTime = []
            arrayLocationLon = []
            arrayLocationLat = []
            for k in range(0, winSize):
                #insertado individual de datos en cada ventana, se realiza n veces según el tamaño deseado de la ventana
                arrayX.append(x_acce[i][current + k])
                arrayY.append(y_acce[i][current + k])
                arrayZ.append(z_acce[i][current + k])
                arrayTime.append(time[i][current + k])
                arrayLocationLon.append(location_lon[i][current + k])
                arrayLocationLat.append(location_lat[i][current + k])
            current += 15
            window.append(arrayX)
            window.append(arrayY)
            window.append(arrayZ)
            window.append(arrayTime)
            window.append(arrayLocationLon)
            window.append(arrayLocationLat)
            windows.append(window)
            
    return windows #regresamos n arrays correspondientes al número de grabaciones en la response, con m ventanas en su formato de array

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

def modelTraining():
    #arrays to fit the model
    x=[]
    y=[] #1 for pothole, 2 for no pothole

    with open("windows/windows_nopothole.txt", "r") as fp:
            nopothole = json.load(fp)

    with open("windows/windows_pothole.txt", "r") as fp:
            pothole = json.load(fp)

    for window in pothole:
        x.append(calculation(window))
        y.append(1)
    for window in nopothole:
        x.append(calculation(window))
        y.append(2)

    x_np = np.array(x)
    y_np = np.array(y)
    
    clf_knn = KNeighborsClassifier(n_neighbors=7)
    clf_knn.fit(x_np,y_np)
    #clf_linear = svm.SVC(kernel = 'linear')
    #clf_linear.fit(x_np, y_np)
    return clf_knn


def predict(window, model):
    pred = model.predict([calculation(window)])
    print("Window predited as: ", pred)
    return pred


def potholeOrNotPothole(modelo,windows):
    #array to return, contains the location of the pothole windows
    locations = []
    previous = 0
    detecting=False
    print("Number of windows: "+str(len(windows)))
    print("1=pothole\n2=no pothole")
    for i in range(0, len(windows)):
        var = predict(windows[i], modelo)
        #Checks consecutive pothole windows, our pothole condition
        if (var == previous and var != [1]):
            #Conditional to verify if you are already dectecting (for potholes that detect 3 or more consecutive pothole windows)
            if not detecting:
                pothole_lon=windows[i][4][0]
                pothole_lat=windows[i][5][0]
                locations.append({"long":pothole_lon,"lat":pothole_lat})
            detecting=True
        elif(var != previous and detecting):
            detecting=False
        previous = var
    return locations
