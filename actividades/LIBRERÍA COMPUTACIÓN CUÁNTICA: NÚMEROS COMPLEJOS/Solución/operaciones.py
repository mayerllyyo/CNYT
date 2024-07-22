import math

def suma(a,b):
    pr = a[0] + b[0]
    pi = a[1] + b[1]
    return (pr,pi)

def Producto(a,b):
    pr = (a[0]*b[0]) - (a[1]*b[1])
    pi = (a[0]*b[1]) + (a[1]*b[0])
    return (pr, pi)

def resta(a,b):
    pr = a[0] - b[0]
    pi = a[1] - b[1]
    return (pr, pi)

def Division(a,b):
    pr = (a[0]*b[0] + a[1]*b[1])/(b[0]**2+b[1]**2)
    pi = (b[0]*a[1] - a[0]*b[1])/(b[0]**2+b[1]**2)
    return (pr, pi)
def Modulo(a):
    pr = math.sqrt((a[0]**2 + a[1]**2))
    return (pr)
def conjugado(a):
    pr = a[0]
    pi = -a[1]
    return (pr,pi)
def polar_a_cartesiano(a):
    pr = a[0]*math.cos(a[1])
    pi = a[0]*math.sin(a[1])
    return pr,pi
def cartesiano_a_polar(a):
    pr = Modulo(a)*math.cos(fase(a))
    pi = Modulo(a)*math.sin(fase(a))
    return pr,pi
def fase(a):
    fase =  math.atan(a[1]/ a[0])
    return fase
def main():
    a = 1,1
    b = 5,-2
    print(conjugado(a))
    print(cartesiano_a_polar(b))


if __name__ =='__main__':
    main()