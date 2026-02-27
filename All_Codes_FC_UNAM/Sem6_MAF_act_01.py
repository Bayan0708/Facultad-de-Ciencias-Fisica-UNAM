import sympy as sp

# Definición de variables y funciones simbólicas
r, theta, phi = sp.symbols('r theta phi')
h_r, h_theta, h_phi = sp.symbols('h_r h_theta h_phi')
f = sp.Function('f')(r, theta, phi)
a, b, c = sp.symbols('a b c', cls=sp.Function)

# Expresiones de los operadores diferenciales en coordenadas esféricas
# Divergencia
divergence_expression = (1/(h_r*h_theta*h_phi)) * (
    sp.diff(h_theta*h_phi*sp.diff(f*r**2, r), r) +
    sp.diff(h_r*h_phi*sp.diff(f*sp.sin(theta), theta), theta) +
    sp.diff(h_r*h_theta*sp.diff(f, phi), phi)
)
# Rotacional
rotational_expression = (1/(h_r*h_theta*h_phi)) * sp.Matrix([
    [(1/(r*sp.sin(theta)))*sp.diff(h_phi*c(r, theta, phi), theta) - sp.diff(h_theta*c(r, theta, phi), phi)],
    [sp.diff(h_r*c(r, theta, phi), phi) - sp.diff(h_phi*a(r, theta, phi), r)],
    [(1/r)*(sp.diff((r*h_theta*b(r, theta, phi)), r) - sp.diff(h_r*b(r, theta, phi), theta))]
])
# Laplaciano
laplacian_expression = (1/(h_r*h_theta*h_phi)) * (
    sp.diff(h_r*h_theta*h_phi*sp.diff(f, r), r) / (r**2*sp.sin(theta)) +
    sp.diff(h_r*h_theta*h_phi*sp.diff(sp.sin(theta)*sp.diff(f, theta), theta), theta) / (r**2*sp.sin(theta)) +
    sp.diff(h_r*h_theta*h_phi*sp.diff(f, phi), phi) / (r**2*sp.sin(theta))
)
# Gradiente
gradient_expression = sp.Matrix([
    [1/(h_r)*sp.diff(f, r)],
    [1/(h_theta*r)*sp.diff(f, theta)],
    [1/(h_phi*r*sp.sin(theta))*sp.diff(f, phi)]
])

# Mostrar los resultados
print("Divergencia:")
sp.pprint(divergence_expression)
print("\nRotacional:")
sp.pprint(rotational_expression)
print("\nLaplaciano:")
sp.pprint(laplacian_expression)
print("\nGradiente:")
sp.pprint(gradient_expression)
