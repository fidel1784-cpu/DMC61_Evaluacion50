def calcular_oro_recuperado(tonelaje, ley_oro, recuperacion):
    """
    Calcula la cantidad estimada de oro recuperado.

    Parámetros:
    tonelaje: toneladas de mineral procesado
    ley_oro: ley de oro en gramos por tonelada
    recuperacion: recuperación metalúrgica en porcentaje

    Retorna:
    gramos contenidos, gramos recuperados y onzas recuperadas
    """

    gramos_contenidos = tonelaje * ley_oro
    gramos_recuperados = gramos_contenidos * (recuperacion / 100)
    onzas_recuperadas = gramos_recuperados / 31.1035

    return {
        "gramos_contenidos": gramos_contenidos,
        "gramos_recuperados": gramos_recuperados,
        "onzas_recuperadas": onzas_recuperadas
    }
