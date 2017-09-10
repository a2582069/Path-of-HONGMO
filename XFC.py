import cmath
def E(a,b,index):
    ee = 0
    for i in range(0,index):
        ee = ee+a[i]*b[i]
    return ee

def Ex(a,index):
    ee = 0
    for i in range(0,index):
        ee = ee+a[i]
    ee = ee / (index)
    return ee

def COF(a,b,c,d,index):
    Eab = E(a,b,index)
    Ecd = E(c,d,index)
    Exy = 0
    for i in range(0,index):
        Exy = Exy + a[i]*c[i]
    Exy = Exy/(index)
    return Exy - Eab*Ecd

def COFx(a,c,index):
    Eab = Ex(a,index)
    Ecd = Ex(c,index)
    Exy = 0
    for i in range(0,index):
        Exy = Exy + a[i]*c[i]
    Exy = Exy/(index)
    return Exy - Eab*Ecd

index = 10#lenth
a = [1,2,3,4,5,6,7,8,9,10]
b = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

c = [1,2,3,4,5,6,7,8,9,10]
d = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

a1 = [1.1,1.9,3]
b1 = [5.0,10.4,14.6]
Eab = E(a,b,index)
Ecd = E(c,d,index)
print Eab
print Ecd
print COF(a,b,c,d,index)

print Ex(a1,3)
print Ex(b1,3)
print COFx(a1,b1,3)