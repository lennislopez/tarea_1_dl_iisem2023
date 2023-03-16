#FUNCIONES

def producto(bin1,bin2):
    return(sumatotal(multiplicacion(bin1,bin2)))        #devuelve string

def sumatotal(lista):
    lista2=[]
    #print(lista)
    lista=preparalista(lista)
    #print(lista)
    acarreo=0
    newnum=''
    i=0
    listalen=len(lista)
    while i<listalen:
        str1=lista[0]
        str2=lista[1]
        #print('str1',str1,'str2',str2,'i',i,'len(lista)',len(lista))
        j=len(str1)-1
        while j>=0:
            acarreo,bit=suma(acarreo,str1[j],str2[j])
            newnum=bit+newnum
            j=j-1
            #print('acarreo',acarreo,'bit',bit,'j',j,'newnum',newnum)
        lista2.append(newnum)
        #print(lista,'lista antes')
        if len(lista)>2:
            lista=lista2+lista[2:]
        else:
            return newnum
        #print(lista,'lista despues')
        i=i+1
        newnum=''
        lista2=[]

def astring(lista):     #lista de enteros a lista de strings
    newlist=[]
    for i in lista:
        if i==0:
            newlist.append(str(i)*len(str(lista[-1])))      #garantiza completar el cero
        else:
            newlist.append(str(i))
    #print(newlist)
    return newlist

#def suma2(lista):
#    acarreo=0
#    newnum=''
#    i=0
#    while i<len(lista):
#        str1=lista[i]
#        if i+1==len(lista):
#            return lista
#        str2=lista[i+1]
#        print(str1,str2)
#        j=len(str1)-1
#        while j>=0:
#            acarreo,bit=suma(acarreo,str1[j],str2[j])
#            newnum=bit+newnum
#            j=j-1
#            print(newnum)
#            lista2=[newnum]
#        lista=lista2+lista[1:]
#        i=i+1
#    return lista

def preparalista(lista):                    #agrega ceros para operar suma
    i=0
    newlist=[]
    j=len(lista)
    while i<len(lista):
        x=('0'*j)+lista[i]+('0'*i)
        newlist.append(x)
        i=i+1
        j=j-1
    return newlist                        #retorna una lista

def suma(stracarreo,string1,string2):       #toma el acarreo mas los dos terminos de los
    acarreo=int(stracarreo)                 #sumandos y los suma
    entero1=int(string1)                    #devuelve el acarreo y el nuevo termino
    entero2=int(string2)
    resultado=acarreo+entero1+entero2
    if resultado==0:
        return('0','0')
    elif resultado==1:
        return('0','1')
    elif resultado==2:
        return('1','0')
    else:
        return('1','1')

#def completar(entero):          #rellena con ceros los bits restantes
#    string=str(entero)
#    while len(string)<8:
#        string='0'+string
#    return (string)

def multiplicacion(A,B):        #multiplica ambos binarios
    print(A,B)
    Z=[]
    strA=str(A)
    strB=str(B)    
    if A>=B:                    #acomoda factores de tal forma que hayan menos sumandos
        i=len(strB)-1
        while i>=0:
            p=int(strB[i])*A
            #p=completar(p)
            Z.append(p)
            i=i-1
        print(Z)
        return astring(Z)
    else:
        i=len(strA)-1
        while i>=0:
            p=int(strA[i])*B
            #p=completar(p)
            Z.append(p)
            i=i-1
        print(Z)
        return astring(Z)                   #retorna una lista con los numeros a sumar

def split(lista):               #divide el numero en dos partes: entera y fraccionaria
    ent=[]
    fra=[]
    cont=0
    for i in lista:
        if i=='.':
            fra=lista[cont+1:]
            return ent,fra
        else:
            ent.append(i)
        cont=cont+1
    if fra==[]:
        fra=['0']
    return(ent,fra)             #devuelve dos listas            

def revision(string):
    x=list(string)
    if x[0]=='b':               #cambia el prefijo del numero al formato
        if x[1]=='-':                   
            x=x[2:]
        else:
            x=x[1:]
        return(x,'BIN')
    elif x[0]=='h':
        
        if x[1]=='-':
            x=x[2:]
        else:
            x=x[1:]
        return(x,'HEX')
    else:
        if x[0]=='d':
            if x[1]=='-':
                x=x[2:]
            else:
                x=x[1:]
        else:
            if x[0]=='-':
                if x[1]=='.':
                    x=['-','0','.']+x[2:]
                else:
                    x=x[1:]
            elif x[0]=='.':
                x=['0']+x
        return(x,'DEC')         #sale una lista

def listaAstring(lista):        #de lista a string
    string=''
    for ele in lista:
        string+=ele
    return string

def listaAentero(lista):        #de lista a entero
    str1=''
    for ele in lista:
        str1+=ele
    entero=int(str1)            #0 no es admitido en esta funcion
    return entero

def listaAflotante(lista):        #de lista a entero
    str1='0.'
    for ele in lista:
        str1+=ele
    flotante=float(str1)            #0 no es admitido en esta funcion
    return flotante

def cambio(string):             #cambia caracteres HEX a DEC
    d={'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}
    newlist=[]
    y,a=revision(string)
    for i in y:
        if i in d.keys():
            newlist.append(d[i])
        else:
            newlist.append(i)
    return newlist

def sumaele(lista):             #suma los valores de una lista y convierte a string
    num=0
    i=0
    while i<len(lista):
        num=num+int(lista[i])
        i=i+1
    string=str(num)
    return string

def sumaelefloat(lista):             #suma los valores de una lista y convierte a string
    num=0
    i=0
    while i<len(lista):
        num=num+float(lista[i])
        i=i+1
    string=str(num)
    return string

def fraccionHEXDEC(string):    #conversion HEX a DEC
    lista=cambio(string)
    newlist=[]
    j=-1
    for i in lista:
        e=j
        x=int(i)
        num=x*pow(16,e)
        string=str(num)
        newlist.append(string)
        j=j-1
    string=(sumaelefloat(newlist))
    lista2=list(string)
    string=listaAstring(lista2[2:])
    return(string)

def conversionHEXDEC(string):    #conversion HEX a DEC
    lista=cambio(string)
    newlist=[]
    j=0
    for i in lista:
        e=len(lista)-(j+1)
        x=int(i)
        num=x*pow(16,e)
        string=str(num)
        newlist.append(string)
        j=j+1
    string=(sumaele(newlist))
    return(string)

def conversionDECBIN(string):   #conversion DEC a BIN
    invnum=[]
    y,a=revision(string)
    if y==['0']:                #0 como excepcion para listaAentero
        return y
    y=listaAentero(y)
    while y>=1:
        r=y%2
        s=str(r)
        invnum.append(s)
        y=y//2
    num=list(reversed(invnum))
    return(num)                 #sale una lista

def fraccionDECBIN(string):     #conversion fraccion DEC a BIN
    newlist=[]
    string='0.'+string
    y=float(string)
    while 0<y<=1:
        n=y*2
        if n>=1:         
            newlist.append('1')
            y=n-1
        else:
            newlist.append('0')
            y=n
    return newlist      
    
def tamano(lista):              #comprueba que el tamano del
    cont=0                      #numero sea maximo de 8 bits en binario
    for i in lista:
        if i=='b' or i=='d' or i=='h' or i=='-' or i=='.':
            cont=cont+1
    tamano=len(lista)-cont
    if tamano>8:
        return(False)
    else:
        return tamano

def signo(lista):               #determina el signo del numero
    if len(lista)==1:
        return True
    elif (lista[0]=='-') or (lista[1]=='-'):
        return False
    else:
        return True    

def comprobacion(string):       #revisa que el numero sea ingresado de forma correcta
    lista=['b','d','h','-','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    y=list(string)
    cont=0
    for i in y:
        if i=='.':
            cont=cont+1
            if cont==2:
                return False
    i=0
    while i<len(y):
        if (len(y)==1) and (y[0] not in lista[5:15]):
            return(False)
        elif (y[i] not in lista):
            return(False)
        else:
            i=i+1
    if (y[0]=='b') and (y[1] in lista[3:6]):
        i=2
        while i<len(y):
            if y[i] in lista[4:6]:
                i=i+1
            else:
                return(False)
    elif (y[0]=='h') and (y[1] in lista[3:]):
        i=2
        while i<len(y):
            if y[i] in lista[4:]:
                i=i+1
            else:
                return(False)
    elif ((len(y)==1) and (y[0] in lista[5:15])) or ((y[0]=='d') and (y[1] in lista[3:15])) or ((y[0] in lista[3:15]) and (y[1] in lista[4:15])):
        i=2
        while i<len(y):
            if y[i] in lista[4:15]:
                i=i+1
            else:
                return(False)
    else:
        return(False)                

def num(x):
    if comprobacion(x)==False:
        print('Valor no permitido.\nRevise el formato y vuelva a introducir el numero.')
        return False
    else:
        lista,tipo=revision(x)
        if tipo=='BIN':
            print('Numero binario')
            if signo(list(x))==True:
                print('Positivo')
                SIGNO=True
            elif signo(list(x))==False:
                print('Negativo')
                SIGNO=False
            if tamano(list(x))==False:
                print('Numero excede los 8 bits.')
                return False
            else:
                print(tamano(list(x)),'bits')
                lentera,lfraccionaria=split(lista)
                #print('Parte entera:',listaAentero(lentera),'\nParte fraccionaria:',listaAentero(lfraccionaria))
            NUMBIN=int(listaAstring(lista))
            return NUMBIN,SIGNO        
        elif tipo=='DEC':
            print('Numero decimal')
            lentera,lfraccionaria=split(lista)
            entera,fraccion=listaAstring(lentera),listaAstring(lfraccionaria)
            lista=conversionDECBIN(entera)+['.']+fraccionDECBIN(fraccion)
            print('En binario:',listaAentero(conversionDECBIN(entera)))
            if signo(list(x))==True:
                print('Positivo')
                SIGNO=True
            elif signo(list(x))==False:
                print('Negativo')
                SIGNO=False
            if tamano(lista)==False:
                print('Numero excede los 8 bits.')
                return False
            else:
                print(tamano(lista),'bits')
                #print('Parte entera:',listaAentero(lentera),'\nParte fraccionaria:',listaAentero(lfraccionaria))
            NUMBIN=listaAentero(conversionDECBIN(entera))
            return NUMBIN,SIGNO
        elif tipo=='HEX':
            print('Numero hexadecimal')
            lentera,lfraccionaria=split(lista)
            entera,fraccion=listaAstring(lentera),listaAstring(lfraccionaria)
            lista=conversionDECBIN(conversionHEXDEC(entera))+['.']+fraccionDECBIN(fraccionHEXDEC(fraccion))
            print('En binario:',listaAentero(conversionDECBIN(conversionHEXDEC(entera))))
            if signo(list(x))==True:
                print('Positivo')
                SIGNO=True
            elif signo(list(x))==False:
                print('Negativo')
                SIGNO=False
            if tamano(lista)==False:
                print('Numero excede los 8 bits.')
                return False
            else:
                print(tamano(lista),'bits')          
                #print('Parte entera:',listaAentero(cambio(entera)),'\nParte fraccionaria:',listaAentero(cambio(fraccion)))    
            NUMBIN=listaAentero(conversionDECBIN(conversionHEXDEC(entera)))
            return NUMBIN,SIGNO
        
########################################################################################

#MAIN
print('\n\nMULTIPLICADOR BINARIO\n\n')
print('Especificación de entrada:\n\n')
print('1. Maximo 8 bits por factor a multiplicar')
print('2. Los valores de cada factor (2 factores exclusivamente)')
print('3. Los factores se pueden expresar en notación decimal, hexadecimal y binario.')
print('4. Para indicar la base numérica de los factores, se utilizará una letra delante')
print('del número de la siguiente forma: d25, h2A y b10. La letra d indica un número en')
print('decimal, h indica hexadecimal y b de binario')
print('5. En caso de no indicarlo, se tomará el número como decimal\n\n')

while True:    
    x=str(input('||||||||||||||||||||||\nINGRESE PRIMER FACTOR:\n'))
    if x==0:
        num1=0
        continue
    elif x==1:
        num1==1
    elif num(x) != False:
        num1,sig1=num(x)
        print(num1,'|',sig1)
    else:
        continue
    x=str(input('-----------------------\nINGRESE SEGUNDO FACTOR:\n'))
    if x==0:
        num2=0
        continue
    elif x==1:
        num2=1
    elif num(x) != False:
        num2,sig2=num(x)
        print(num2,'|',sig2)
    else:
        continue
    if sig1!=sig2:
        sig=-1
    else:
        sig=1
    #print(num1,num2)
    if num1==1:
        print('\nEl PRODUCTO ES',sig*num1*num2)
    elif num2==1:
        print('\nEl PRODUCTO ES',sig*num1*num2)
    else:
        print('\nEl PRODUCTO ES',sig*int(producto(num1,num2)))
print('\nFin de programa\n')
