class MuestraMineral:
    """
    Clase que representa una muestra mineral registrada.
    """

    def __init__(
        self,
        codigo,
        zona,
        ley_oro,
        tonelaje
    ):
        self.codigo = codigo
        self.zona = zona
        self.ley_oro = ley_oro
        self.tonelaje = tonelaje

    def calcular_oro_contenido(self):
        """
        Calcula el oro contenido en gramos.
        """
        return self.ley_oro * self.tonelaje

    def actualizar(
        self,
        zona,
        ley_oro,
        tonelaje
    ):
        """
        Actualiza los datos de la muestra.
        """
        self.zona = zona
        self.ley_oro = ley_oro
        self.tonelaje = tonelaje

    def obtener_datos(self):
        """
        Retorna los datos de la muestra como diccionario.
        """
        return {
            "Código": self.codigo,
            "Zona": self.zona,
            "Ley de oro (g/t)": self.ley_oro,
            "Tonelaje (t)": self.tonelaje,
            "Oro contenido (g)": self.calcular_oro_contenido()
        }
