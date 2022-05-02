valores = {'I' : 1, 'V' : 5, 'X' : 10, 'L': 50, 'C' : 100, 'D' : 500, 'M' : 1000}


def conversion_numeros(num_romano):
    if(len(num_romano) == 1):   
        return valores[num_romano[0]]
    else:
        if(valores[num_romano[0]] >= valores[num_romano[1]]): 
            return conversion_numeros(num_romano[1:]) + valores[num_romano[0]] 
        else:  
            if(valores[num_romano[0]] < valores[num_romano[1]]): 
                return conversion_numeros(num_romano[1:]) - valores[num_romano[0]]
          

print(conversion_numeros('D'))
