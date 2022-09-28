N = int(input())
math = []
phy = []
che = []
m_p = []
p_c = []
c_m = []
for n in range(N):
    value = list(map(int,input().split()))
    math.append(value[0])
    phy.append(value[1])
    che.append(value[2])
    m_p.append(value[0]*value[1])
    p_c.append(value[1]*value[2])
    c_m.append(value[2]*value[0])
    

    
def corr(X,Y,X_Y):
    sumaxy = sum(X_Y)
    sumax = sum(X)
    sumay = sum(Y)
    n = len(X)
    numerador = (n*sumaxy) - (sumax*sumay)
    #cosas del denominador
    sumax2 = sum(list(map(lambda x:x**2,X)))
    sumay2 = sum(list(map(lambda y:y**2,Y)))
    
    sumax_2 = sumax**2
    sumay_2 = sumay**2
    
    denominador = ((n*sumax2 - sumax_2)*(n*sumay2 - sumay_2))**(1/2)
    return numerador/denominador

print(round(corr(math,phy,m_p),2))
print(round(corr(phy,che,p_c),2))
print(round(corr(che,math,c_m),2))
