import random as rd
from math import ceil
from statistics import mean, pstdev

import matplotlib.pyplot as plt

SEED = 2026
TOTAL_ESTAMPAS = 100
ESTAMPAS_POR_SOBRE = 7
SIMULACIONES = 10000
VALORES_K = [1, 2, 5, 10]
VALORES_M = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
UMBRALES_PROB = [0.50, 0.75, 0.90]
PRECIO_SOBRE = 9.50

rd.seed(SEED)


# ===== funciones auxiliares (reutilizadas del ejercicio 1) =====


def inicializar_album():
    album = {}
    for i in range(1, TOTAL_ESTAMPAS + 1):
        album[i] = False
    return album


def inicializar_repetidas():
    repetidas = {}
    for i in range(1, TOTAL_ESTAMPAS + 1):
        repetidas[i] = 0
    return repetidas


def crear_estampas(n):
    return list(range(1, n + 1))


def abrir_sobre(mi_album, mis_cartas, estampas_diferentes):
    contenido = rd.sample(estampas_diferentes, ESTAMPAS_POR_SOBRE)
    for estampa in contenido:
        if not mi_album[estampa]:
            mi_album[estampa] = True
        else:
            mis_cartas[estampa] += 1


# ===== logica de intercambio =====


def aplicar_intercambio(mi_album, mis_cartas, k):
    """
    Canjea grupos de K estampas repetidas por 1 estampa nueva (que falte en el album).
    Se repite mientras haya suficientes repetidas y queden estampas faltantes.
    """
    total_repetidas = sum(mis_cartas.values())

    while total_repetidas >= k:
        faltantes = [i for i in range(1, TOTAL_ESTAMPAS + 1) if not mi_album[i]]

        if not faltantes:
            break

        nueva_estampa = rd.choice(faltantes)
        mi_album[nueva_estampa] = True

        # Consumir exactamente K repetidas
        por_consumir = k
        for estampa in list(mis_cartas.keys()):
            if por_consumir == 0:
                break
            if mis_cartas[estampa] > 0:
                quitar = min(mis_cartas[estampa], por_consumir)
                mis_cartas[estampa] -= quitar
                por_consumir -= quitar

        total_repetidas = sum(mis_cartas.values())


# ===== ejercicio 4 - parte A =====


def completar_album_con_intercambio(k):
    """
    Simula la compra de sobres hasta completar el album con regla de intercambio K.
    Si k es None, no se aplica intercambio.
    Retorna el numero de sobres necesarios.
    """
    estampas_diferentes = crear_estampas(TOTAL_ESTAMPAS)
    mi_album = inicializar_album()
    mis_cartas = inicializar_repetidas()
    sobres = 0

    while not all(mi_album.values()):
        abrir_sobre(mi_album, mis_cartas, estampas_diferentes)
        sobres += 1
        if k is not None:
            aplicar_intercambio(mi_album, mis_cartas, k)

    return sobres


def simular_parte_a(valores_k, simulaciones):
    """
    Para cada K, realiza R simulaciones hasta completar el album.
    Retorna diccionario con listas de sobres por K (y None para sin intercambio).
    """
    resultados = {}

    # Sin intercambio
    sobres_sin = []
    for _ in range(simulaciones):
        sobres_sin.append(completar_album_con_intercambio(None))
    resultados[None] = sobres_sin

    # Con intercambio para cada K
    for k in valores_k:
        sobres_k = []
        for _ in range(simulaciones):
            sobres_k.append(completar_album_con_intercambio(k))
        resultados[k] = sobres_k

    return resultados


def calcular_estadisticas_parte_a(resultados):
    """Calcula media, std y reduccion porcentual para cada K."""
    media_sin = mean(resultados[None])
    estadisticas = {
        None: {
            "media": media_sin,
            "std": pstdev(resultados[None]),
            "reduccion_porcentual": 0.0,
        }
    }
    for k in VALORES_K:
        media_k = mean(resultados[k])
        std_k = pstdev(resultados[k])
        reduccion = (media_sin - media_k) / media_sin * 100
        estadisticas[k] = {
            "media": media_k,
            "std": std_k,
            "reduccion_porcentual": reduccion,
        }
    return estadisticas


def ejecutar_parte_a():
    resultados = simular_parte_a(VALORES_K, SIMULACIONES)
    estadisticas = calcular_estadisticas_parte_a(resultados)

    return {
        "resultados": resultados,
        "estadisticas": estadisticas,
    }


# ===== ejercicio 4 - parte B =====


def album_completo_con_m_sobres_e_intercambio(m, k):
    """
    Compra exactamente M sobres con regla de intercambio K.
    Si k es None, no se aplica intercambio.
    Retorna 1 si el album se completo, 0 si no.
    """
    estampas_diferentes = crear_estampas(TOTAL_ESTAMPAS)
    mi_album = inicializar_album()
    mis_cartas = inicializar_repetidas()

    for _ in range(m):
        if all(mi_album.values()):
            break
        abrir_sobre(mi_album, mis_cartas, estampas_diferentes)
        if k is not None:
            aplicar_intercambio(mi_album, mis_cartas, k)

    return int(all(mi_album.values()))


def estimar_probabilidades_parte_b(valores_k, valores_m, simulaciones):
    """
    Para cada (K, M), estima P(completar album con M sobres y regla K).
    Retorna diccionario anidado: probabilidades[k][m].
    """
    probabilidades = {}

    # Sin intercambio
    probabilidades[None] = {}
    for m in valores_m:
        exitos = sum(
            album_completo_con_m_sobres_e_intercambio(m, None)
            for _ in range(simulaciones)
        )
        probabilidades[None][m] = exitos / simulaciones

    # Con intercambio
    for k in valores_k:
        probabilidades[k] = {}
        for m in valores_m:
            exitos = sum(
                album_completo_con_m_sobres_e_intercambio(m, k)
                for _ in range(simulaciones)
            )
            probabilidades[k][m] = exitos / simulaciones

    return probabilidades


def primer_m_que_supera_umbral(probabilidades_k, valores_m, umbral):
    """Retorna el primer M que supera el umbral dado."""
    for m in valores_m:
        if probabilidades_k[m] >= umbral:
            return m
    return None


def calcular_sobres_para_umbrales(probabilidades, valores_k, valores_m, umbrales):
    """Determina el M minimo para cada K y cada umbral de probabilidad."""
    resultado = {}
    for k in valores_k:
        resultado[k] = {}
        for umbral in umbrales:
            m_necesario = primer_m_que_supera_umbral(
                probabilidades[k], valores_m, umbral
            )
            resultado[k][umbral] = m_necesario
    return resultado


def ejecutar_parte_b():
    probabilidades = estimar_probabilidades_parte_b(VALORES_K, VALORES_M, SIMULACIONES)
    sobres_umbrales = calcular_sobres_para_umbrales(
        probabilidades, VALORES_K, VALORES_M, UMBRALES_PROB
    )

    return {
        "probabilidades": probabilidades,
        "sobres_umbrales": sobres_umbrales,
    }


# ===== preguntas de analisis =====


def calcular_ahorro_en_quetzales(media_sin, media_k):
    """Calcula el ahorro promedio en quetzales para un K vs sin intercambio."""
    sobres_ahorrados = media_sin - media_k
    return sobres_ahorrados, sobres_ahorrados * PRECIO_SOBRE


def calcular_incremento_probabilidad_entre_k(probabilidades, m_fijo):
    """
    Para un M fijo, calcula el incremento de probabilidad al mejorar K.
    Retorna diferencias entre K=10->K=5, K=5->K=2, K=2->K=1.
    """
    pares = [(10, 5), (5, 2), (2, 1)]
    incrementos = {}
    for (k_mayor, k_menor) in pares:
        diferencia = probabilidades[k_menor][m_fijo] - probabilidades[k_mayor][m_fijo]
        incrementos[(k_mayor, k_menor)] = diferencia
    return incrementos


# ===== visualizaciones =====


def graficar_histogramas_parte_a(resultados):
    """
    Histogramas superpuestos del numero de sobres para completar el album
    para cada valor de K y el caso sin intercambio.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    colores = {None: "gray", 1: "#e74c3c", 2: "#e67e22", 5: "#3498db", 10: "#2ecc71"}
    etiquetas = {None: "Sin intercambio", 1: "K = 1", 2: "K = 2", 5: "K = 5", 10: "K = 10"}

    claves = [None] + VALORES_K
    for clave in claves:
        ax.hist(
            resultados[clave],
            bins=30,
            alpha=0.55,
            color=colores[clave],
            label=etiquetas[clave],
            edgecolor="white",
            linewidth=0.4,
        )

    ax.set_xlabel("Número de sobres para completar el álbum", fontsize=12)
    ax.set_ylabel("Frecuencia", fontsize=12)
    ax.set_title(
        "Distribución de sobres necesarios según regla de intercambio (K)",
        fontsize=13,
        fontweight="bold",
    )
    ax.legend(fontsize=11)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig("histogramas_parte_a.png", dpi=150)
    plt.close()


def graficar_probabilidades_parte_b(probabilidades):
    """
    Grafica de lineas: eje x = M, eje y = P(exito), una curva por K.
    Incluye la curva de referencia sin intercambio.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    colores = {None: "gray", 1: "#e74c3c", 2: "#e67e22", 5: "#3498db", 10: "#2ecc71"}
    estilos = {None: "--", 1: "-", 2: "-", 5: "-", 10: "-"}
    marcadores = {None: "o", 1: "s", 2: "^", 5: "D", 10: "v"}
    etiquetas = {None: "Sin intercambio", 1: "K = 1", 2: "K = 2", 5: "K = 5", 10: "K = 10"}

    claves = [None] + VALORES_K
    for clave in claves:
        probs = [probabilidades[clave][m] for m in VALORES_M]
        ax.plot(
            VALORES_M,
            probs,
            color=colores[clave],
            linestyle=estilos[clave],
            marker=marcadores[clave],
            label=etiquetas[clave],
            linewidth=2,
            markersize=6,
        )

    # Lineas de referencia para umbrales
    for umbral, estilo, color in zip(
        UMBRALES_PROB, [":", "--", "-."], ["#95a5a6", "#7f8c8d", "#2c3e50"]
    ):
        ax.axhline(y=umbral, linestyle=estilo, color=color, alpha=0.6,
                   label=f"Umbral {umbral:.0%}")

    ax.set_xlabel("Número de sobres comprados (M)", fontsize=12)
    ax.set_ylabel("Probabilidad de completar el álbum", fontsize=12)
    ax.set_title(
        "Probabilidad de éxito vs. Sobres comprados para distintos K",
        fontsize=13,
        fontweight="bold",
    )
    ax.set_ylim(-0.05, 1.05)
    ax.set_xticks(VALORES_M)
    ax.legend(fontsize=10, loc="upper left")
    ax.grid(linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig("probabilidades_parte_b.png", dpi=150)
    plt.close()


# ===== ejecucion principal =====

print("Ejecutando Parte A (simulacion hasta completar)...")
resultados_a = ejecutar_parte_a()
print("Ejecutando Parte B (probabilidad con M fijo)...")
resultados_b = ejecutar_parte_b()

estadisticas = resultados_a["estadisticas"]
media_sin = estadisticas[None]["media"]

# ===== impresion de resultados =====

print("Ejercicio 4")
print("Efecto del intercambio de repetidas")

print("\nParte A")
print(
    f"Sin intercambio:  media = {media_sin:.3f}, "
    f"std = {estadisticas[None]['std']:.3f}"
)
for k in VALORES_K:
    est = estadisticas[k]
    print(
        f"K = {k:2d}:  media = {est['media']:.3f}, "
        f"std = {est['std']:.3f}, "
        f"reduccion = {est['reduccion_porcentual']:.2f}%"
    )

print("\n\nParte B")
header = f"{'M':>4}   {'Sin K':>7}"
for k in VALORES_K:
    header += f"   {'K='+str(k):>7}"
print(header)
for m in VALORES_M:
    fila = f"{m:>4}   {resultados_b['probabilidades'][None][m]:>7.4f}"
    for k in VALORES_K:
        fila += f"   {resultados_b['probabilidades'][k][m]:>7.4f}"
    print(fila)

print("\n\nSobres minimos para alcanzar umbral de probabilidad")
for k in VALORES_K:
    print(f"\nK = {k}")
    for umbral in UMBRALES_PROB:
        m_nec = resultados_b["sobres_umbrales"][k][umbral]
        print(f"  P >= {umbral:.0%}   M = {m_nec}")


print("Generando visualizaciones...")
graficar_histogramas_parte_a(resultados_a["resultados"])
graficar_probabilidades_parte_b(resultados_b["probabilidades"])
print("Graficas guardadas: histogramas_parte_a.png, probabilidades_parte_b.png")
