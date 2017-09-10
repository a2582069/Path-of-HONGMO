weight = [0,2,2,6,5,4,0]
value =  [0,6,3,5,4,6,0]
Max_weight = 10

f = [[] for i in range(13)]
for i in range(0,13):
    for j in range(0,13):
        f[i].append(0)
#print f

def _bag():
    for i in range(1,6):
        for j in range(1,11):
            if weight[i] <= j:
                f[i][j] = max(f[i][j], f[i][j] - weight[i + 1] + value[i + 1])
                print 'i = ' + str(i) + 'j = ' + str(j) + 'ans = ' + str(f[i][j])
            else:
                f[i][j]=f[i-1][j]
                print 'i = ' + str(i) + 'j = ' + str(j) + 'ans = ' + str(f[i][j])
    for i in range(1,4):
        for j in range(1,10):
            print f[i][j]


_bag()