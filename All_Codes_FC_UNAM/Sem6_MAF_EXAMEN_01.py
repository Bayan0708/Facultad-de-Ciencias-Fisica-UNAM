import sympy as sp

# Definir símbolos y función
x, y, z, a, b = sp.symbols('x y z a b')
f = 1 / sp.sqrt(a*x**2 + b**2*y**2 + z**2)

# Calcular segundas derivadas parciales
f_xx = sp.diff(f, x, 2)
f_yy = sp.diff(f, y, 2)
f_zz = sp.diff(f, z, 2)

# Calcular laplaciano
laplacian = f_xx + f_yy + f_zz

print("El laplaciano de la función es:")
print(laplacian)

# Resolver ∇^2(f) = 0 para a y b
solutions = sp.solve(laplacian, (a, b))
print("Las soluciones para a y b son:")
print(solutions)
