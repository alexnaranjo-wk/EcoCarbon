class RecommendationService:
    """
    Servicio encargado de generar recomendaciones ambientales.
    """

    def get_recommendations(self, emission_level):
        if emission_level == "Bajo":
            return [
                "Mantener hábitos de consumo responsable.",
                "Continuar usando iluminación eficiente."
            ]

        if emission_level == "Medio":
            return [
                "Desconectar equipos eléctricos que no estén en uso.",
                "Cambiar focos tradicionales por focos LED.",
                "Aprovechar la luz natural durante el día."
            ]

        return [
            "Reducir el uso de electrodomésticos de alto consumo.",
            "Revisar el estado de los equipos eléctricos.",
            "Implementar hábitos de ahorro energético.",
            "Considerar el uso de energías renovables."
        ]
