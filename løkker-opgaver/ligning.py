#program for ligningen "y=3x^2+6x+9" som udskriver værdien x0-100
print('for y=3x^2 + 6x + 9 y er lig med = ')
for x in range(0,11):
    y=3*x**2+6*x+9
    print('')
    print('når x= '+ str(x)+' er:')
    print('y=' + str(y))