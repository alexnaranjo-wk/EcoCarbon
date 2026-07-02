from src.núcleo import CarbonFootprintCalculator


def test_calculate_co2():
    calculator = CarbonFootprintCalculator()
    result = calculator.calculate_co2(350)
    assert result == 134.75


def test_negative_consumption():
    calculator = CarbonFootprintCalculator()

    try:
        calculator.calculate_co2(-10)
    except ValueError as error:
        assert str(error) == "El consumo no puede ser negativo."
