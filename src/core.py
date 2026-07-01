class CarbonFootprintCalculator:
    """
    Clase principal para calcular la huella de carbono
    generada por el consumo eléctrico.
    """

    EMISSION_FACTOR = 0.385

    def calculate_co2(self, consumption_kwh):
        """
        Calcula las emisiones de CO2 en kilogramos.
        """
        self._validate_consumption(consumption_kwh)
        return round(consumption_kwh * self.EMISSION_FACTOR, 2)

    def classify_emission(self, co2_kg):
        """
        Clasifica el nivel de emisión de CO2.
        """
        if co2_kg <= 100:
            return "Bajo"
        elif co2_kg <= 250:
            return "Medio"
        return "Alto"

    def _validate_consumption(self, consumption_kwh):
        """
        Valida que el consumo sea un número positivo y coherente.
        """
        if not isinstance(consumption_kwh, (int, float)):
            raise ValueError("El consumo debe ser un número.")

        if consumption_kwh < 0:
            raise ValueError("El consumo no puede ser negativo.")

        if consumption_kwh > 100000:
            raise ValueError("El consumo ingresado es demasiado alto.")
