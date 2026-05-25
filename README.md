# Lab 8 – Simulación del problema del coleccionista

Simulaciones de Monte Carlo para modelar la compra de sobres de estampas bajo distintas condiciones de presupuesto y estrategia de compra.

## Estructura del repositorio

```
Lab8Prob/
├── e3.py                  # Script Python de la Etapa 3
├── e3.ipynb               # Notebook con código + análisis documentado
├── e3_barras.png          # Gráfica generada por la Etapa 3
├── e4.py                  # Script Python de la Etapa 4
├── histogramas_parte_a.png  # Histogramas de sobres por K (Etapa 4)
├── probabilidades_parte_b.png  # Probabilidad de éxito vs M por K (Etapa 4)
└── analisis_e4.md         # Respuestas a las preguntas de análisis (Etapa 4)
```

## Etapa 3 – Incorporación del presupuesto y costo

### Parámetros

| Parámetro | Valor |
|---|---|
| Estampas del álbum (N) | 100 |
| Estampas por sobre (S) | 7 |
| Precio por sobre | Q 9.50 |
| Presupuesto total | Q 1,000 |
| Simulaciones (R) | 10,000 |
| Semilla | 2026 |

### Resultados principales

| Métrica | Valor |
|---|---|
| P(completar el álbum) | 94.36% |
| E[sobres comprados] | 73.56 |
| E[estampas distintas \| no completó] | 98.97 |

### Comparativa de estrategias de compra

| Estrategia | Sobres | Costo | P(completar) |
|---|---|---|---|
| Sobres sueltos (máx. con Q 1,000) | 105 | Q 997.50 | 94.36% |
| Caja (104 sobres) | 104 | Q 975.00 | 93.42% |
| **Mixto (caja + 2 sueltos)** | **106** | **Q 994.00** | **94.40%** |

La estrategia mixta es la óptima: comprar la caja y reinvertir el sobrante en sobres sueltos maximiza la probabilidad de completar el álbum dentro del presupuesto.


## Etapa 4 – Efecto del intercambio de repetidas

### Parámetros

| Parámetro | Valor |
|---|---|
| Estampas del álbum (N) | 100 |
| Estampas por sobre (S) | 7 |
| Simulaciones por configuración (R) | 10,000 |
| Semilla | 2026 |
| Valores de K evaluados | 1, 2, 5, 10 |
| Valores de M evaluados (Parte B) | 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70 |

### Resultados Parte A – Sobres para completar el álbum

| Configuración | Media sobres | Desv. estándar | Reducción |
|---|---|---|---|
| Sin intercambio | 72.241 | 17.213 | — |
| K = 1 | 15.000 | 0.000 | 79.24% |
| K = 2 | 19.851 | 0.542 | 72.52% |
| K = 5 | 28.086 | 1.426 | 61.12% |
| K = 10 | 35.195 | 2.462 | 51.28% |

### Resultados Parte B – Sobres mínimos por umbral de probabilidad

| K | P ≥ 50% | P ≥ 75% | P ≥ 90% |
|---|---|---|---|
| K = 1 | M = 20 | M = 20 | M = 20 |
| K = 2 | M = 20 | M = 20 | M = 20 |
| K = 5 | M = 30 | M = 30 | M = 30 |
| K = 10 | M = 35 | M = 40 | M = 40 |

### Conclusiones del análisis

Reducir K tiene un impacto no lineal: el mayor beneficio ocurre al pasar de no tener intercambio a cualquier forma de canje. Con K = 2 se ahorran en promedio ~52 sobres respecto al caso sin intercambio, equivalentes a Q 497.71. A partir de K = 2, la mejora marginal al bajar más K es reducida, ya que el límite teórico mínimo de 15 sobres (⌈100/7⌉) impone un techo que ningún mecanismo puede superar. La estrategia más rentable en costo por estampa nueva obtenida por canje es K = 1 (Q 1.36 por estampa), aunque K = 2 ofrece el mejor equilibrio entre ahorro y viabilidad práctica.


## Requisitos

```
matplotlib
```
