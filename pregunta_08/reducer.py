#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import itertools 


if __name__ == '__main__':

    curkey = None
    suma = 0
    conteo = 0
    
    for line in sys.stdin:

        key, val, cont = line.split("\t") 
        val = float(val)
        cont = float(cont) 
        if key == curkey:
            
            suma += val
            conteo += cont
        else:
            
            if curkey is not None:
                
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, float(suma/conteo)))  

            curkey = key
            suma = val 
            conteo = cont 
            promedio= float(float(val)/float(conteo)) 
            
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, float(suma/conteo))) 
