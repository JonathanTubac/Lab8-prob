# Lab 8 – Simulación del problema del coleccionista

Simulaciones de Monte Carlo para modelar la compra de sobres de estampas bajo distintas condiciones de presupuesto y estrategia de compra.

## Estructura del repositorio

```
Lab8Prob/
├── e3.py          # Script Python de la Etapa 3
├── e3.ipynb       # Notebook con código + análisis documentado
└── e3_barras.png  # Gráfica generada por la simulación
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

## Requisitos

```
numpy
matplotlib
```
