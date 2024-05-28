import matplotlib.pyplot as plt
import numpy as np


temperaturas = [2.95, 2.96, 21.6, 23.0, 23.5, 24.80, 24.80, 26.2, 27.0, 27.74, 28.1, 28.1,
                28.5, 28.7, 29.9, 30.50, 30.7, 31.4, 32.1, 32.2, 32.3, 32.5, 34.3, 39.7]


media = sum(temperaturas) / len(temperaturas)


varianza = sum((x - media) ** 2 for x in temperaturas) / len(temperaturas)


desviacion_estandar = varianza ** 0.5


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(temperaturas, bins=10, color='skyblue', edgecolor='black')
plt.title('Histograma de Temperaturas')
plt.xlabel('Temperatura')
plt.ylabel('Frecuencia')

plt.subplot(1, 2, 2)
freq, bins, _ = plt.hist(temperaturas, bins=10, color='lightgreen', edgecolor='black', alpha=0)
bin_centers = np.mean(np.vstack([bins[1:], bins[:-1]]), axis=0)
plt.plot(bin_centers, freq, marker='o', linestyle='-')
plt.title('Polígono de Frecuencia')
plt.xlabel('Temperatura')
plt.ylabel('Frecuencia')


plt.axhline(freq.max(), color='red', linestyle='dashed', linewidth=1)
plt.text(28, freq.max() + 0.5, f'Media: {media:.2f}', color='red')

plt.tight_layout()
plt.show()

print(f'Varianza: {varianza:.2f}')
print(f'Desviación Estándar: {desviacion_estandar:.2f}')
