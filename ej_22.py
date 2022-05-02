mochila = ['Sable de luz','Pala','Metro','Casco','Llave',]
cont = 0

def usar_la_fuerza(vector):  
    if(len(vector) == 0):
        return 0
    else:
        if(vector[0] == 'Sable de luz'):
            return 1 
        else:
            global cont
            cont +=1
        return usar_la_fuerza(vector[1:])              


if(usar_la_fuerza(mochila) == 1):    
    print('Hay sable de luz')
    print('Se sacaron' , cont , 'objetos')
else:
    print('No hay sable de luz')
