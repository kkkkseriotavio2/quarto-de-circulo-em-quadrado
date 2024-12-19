import matplotlib.pyplot as plt
import numpy as np
import random

# Configurações do quadrado
square_side = 1  # Lado do quadrado
circle_radius = 1  # Raio do quarto de círculo
circle_center = (0, 0)  # Centro do círculo

# Coordenadas aleatórias para o ponto final fora do círculo
while True:

    x_random = random.uniform(0, square_side)
    y_random = random.uniform(0, square_side)
    if np.sqrt(x_random**2 + y_random**2) > circle_radius:  # Dentro do círculo
        break

# Criar os dados do quarto de círculo
theta = np.linspace(0, np.pi / 2, 100)
circle_x = circle_radius * np.cos(theta)
circle_y = circle_radius * np.sin(theta)

# Plotar o quadrado, o quarto de círculo e a linha
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], 'v-', label="Quadrado")  # Quadrado
ax.plot(circle_x, circle_y, 'b-', label="Quarto de Círculo")  # Quarto de círculo
ax.plot([0, x_random], [0, y_random], 'k-', label="Linha")  # Linha
ax.scatter(x_random, y_random, color='black', zorder=5, label=f"Ponto Final ({x_random:.2f}, {y_random:.2f})")  # Ponto final

# Configurações do gráfico
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
ax.set_aspect('equal')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.legend()
plt.title("Quadrado com Quarto de Círculo e Linha")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# Coordenadas do ponto final
(x_random, y_random)
