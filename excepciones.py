#Docs https://docs.python.org/3/tutorial/errors.html

try:
    #Zero:
    i = 1/0
    #Name:
    a = b
    #Type:
    b = "hello"
    b += 5
    #Value
    a = int('$%&')
except ZeroDivisionError as err:
    print('Handling run-time error, Zero:', err)
except NameError as err2:
    print('Handling run-time error, Name:', err2)
except TypeError as err3:
    print('Handling run-time error, Type:', err3)
except:
    print("Unexpected  error:", ValueError)
else:   #Ejecuta si no existe excepcion
    i = 1/2
    print(i)
finally:
    i= 10
    print(i, "Finally")