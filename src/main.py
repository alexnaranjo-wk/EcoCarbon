from core import CarbonFootprintCalculator
from recommendations import RecommendationService


def main():
    calculator = CarbonFootprintCalculator()
    recommendation_service = RecommendationService()

    try:
        consumption = float(input("Ingrese el consumo eléctrico mensual en kWh: "))

        co2_result = calculator.calculate_co2(consumption)
        emission_level = calculator.classify_emission(co2_result)
        recommendations = recommendation_service.get_recommendations(emission_level)

        print("\n--- Resultado del cálculo ---")
        print(f"Consumo ingresado: {consumption} kWh")
        print(f"Huella de carbono estimada: {co2_result} kg CO2")
        print(f"Nivel de emisión: {emission_level}")

        print("\nRecomendaciones:")
        for recommendation in recommendations:
            print(f"- {recommendation}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
