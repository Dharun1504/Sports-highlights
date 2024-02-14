def modifyTS(a):
    t1 = a[0] - 2
    if(t1 < 0):
        t1 = 0
    return [t1, a[1] + 2]

def checkOverLap(a, b):
    if(a[1] > b[0]):
        b[0] = a[1]
    return b 

def check(timestamps):
    t = []
    for i in timestamps:
        if(len(t) != 0):
            t.append(checkOverLap(t[-1], modifyTS(i['timestamp'])))
        else:
            t.append(modifyTS(i['timestamp']))
    p = 0
    for i in timestamps:
        i["timestamp"] = t[p]
        p += 1
    return timestamps
