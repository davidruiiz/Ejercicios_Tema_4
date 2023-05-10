class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.largo = 0
    
    def __len__(self):
        return self.largo
    
    def __str__(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(valores)
    
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo
        self.largo += 1

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        print("Error: la función debe cambiar de signo en el intervalo [a, b]")
        return None
    x = ListaEnlazada()
    x.insertar(a)
    x.insertar(b)
    for i in range(1, max_iter+1):
        c = (a + b)/2
        fc = f(c)
        x.insertar(c)
        if abs(fc) < tol:
            return x, c, i
        if fa*fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    print("Error: se alcanzó el número máximo de iteraciones")
    return None, None, None

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    fx0 = f(x0)
    fx1 = f(x1)
    x = ListaEnlazada()
    x.insertar(x0)
    x.insertar(x1)
    for i in range(2, max_iter+1):
        x2 = x1 - fx1*(x1 - x0)/(fx1 - fx0)
        fx2 = f(x2)
        x.insertar(x2)
        if abs(fx2) < tol:
            return x, x2, i
        x0 = x1
        x1 = x2
        fx0 = fx1
        fx1 = fx2
    print("Error: se alcanzó el número máximo de iteraciones")
    return None, None, None

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    fx0 = f(x0)
    x = ListaEnlazada()
    x.insertar(x0)
    for i in range(1, max_iter+1):
        dfx0 = df(x0)
        if abs(dfx0) < tol:
            print("Error: derivada demasiado cercana a cero")
            return None, None, None
        x1 = x0 - fx0/dfx0
        fx1 = f(x1)
        x.insertar(x1)
        if abs(fx1) < tol:
            return x, x1, i
        x0 = x1
        fx0 = fx1
    print("Error: se alcanzó el número máximo de iteraciones")
   

def f(x):
    return x**3 + x + 16

def df(x):
    return 3*x**2 + 1

a = -5
b = 5
x0 = -5
x1 = 5
tol = 1e-6
max_iter = 100

print("Método de la bisección:")
x_b, sol_b, iter_b = biseccion(f, a, b, tol, max_iter)
print("Solución:", sol_b)
print("Iteraciones:", iter_b)
print("Secuencia:", x_b)

print("Método de la secante:")
x_s, sol_s, iter_s = secante(f, x0, x1, tol, max_iter)
print("Solución:", sol_s)
print("Iteraciones:", iter_s)
print("Secuencia:", x_s)

print("Método de Newton-Raphson:")
x_n, sol_n, iter_n = newton_raphson(f, df, x0, tol, max_iter)
print("Solución:", sol_n)
print("Iteraciones:", iter_n)
print("Secuencia:", x_n)