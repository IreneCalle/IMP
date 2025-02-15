# scoring.py

from typing import Dict, Any, Tuple, List
from config import (
    ALL_ITEMS,
    OBSERVED_ITEMS,
    PROVOKED_ITEMS,
    TEST_SECTIONS,
    SECTION_WEIGHTS
)


class IMPValidator:
    """
    Validador de datos del formulario IMP.
    """

    @staticmethod
    def validate_form_data(data: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Valida los datos del formulario.
        """
        try:
            # Validación de campos básicos
            required_fields = {
                'patientId': 'ID del paciente',
                'evaluationDate': 'Fecha de evaluación',
                'evaluator': 'Evaluador'
            }

            for field, name in required_fields.items():
                if not data.get(field):
                    return False, f"El campo {name} es obligatorio"

            # Validación de ítems
            for item_name, item_config in ALL_ITEMS.items():
                if item_name in data and data[item_name]:
                    try:
                        value = int(data[item_name])
                        valid_values = [opt['value'] for opt in item_config['options']]
                        if value not in valid_values:
                            return False, f"Valor inválido para {item_config['title']}"
                    except ValueError:
                        return False, f"Valor no numérico para {item_config['title']}"

            return True, ""

        except Exception as e:
            return False, f"Error en la validación: {str(e)}"


class IMPScorer:
    """
    Calculador de puntuaciones de la escala IMP.
    """

    def calculate_score(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calcula las puntuaciones totales y por tipo.
        """
        scores = {}

        # Calcular puntuación para cada sección
        for section in TEST_SECTIONS.keys():
            scores[section] = self._calculate_section_score(data, section)

        # Calcular totales por tipo de habilidad
        type_scores = self._calculate_type_scores(data)
        scores['type_scores'] = type_scores

        # Calcular totales por tipo de ítem observado/provocado
        scores['observed'] = sum(
            int(data.get(item, 0))
            for item in OBSERVED_ITEMS
            if item in data
        )

        scores['provoked'] = sum(
            int(data.get(item, 0))
            for item in PROVOKED_ITEMS
            if item in data
        )

        # Cálculo del total
        scores['total'] = sum(
            int(data.get(item, 0))
            for item in ALL_ITEMS
            if item in data
        )

        return scores

    def _calculate_section_score(self, data: Dict[str, Any], section: str) -> float:
        """
        Calcula la puntuación para una sección específica.
        """
        score = 0
        section_info = TEST_SECTIONS[section]

        for item_name, item_config in ALL_ITEMS.items():
            if (item_config['section'] == section and
                    item_name in data and
                    data[item_name] and
                    item_config['number'] >= section_info['start'] and
                    item_config['number'] <= section_info['end']):
                try:
                    score += int(data[item_name])
                except (ValueError, TypeError):
                    continue

        return score

    def _calculate_type_scores(self, data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """
        Calcula las puntuaciones por tipo de habilidad (P, V, A, S, F)
        """
        type_scores = {
            'P': {'total': 0, 'max': 0, 'percentage': 0},
            'V': {'total': 0, 'max': 0, 'percentage': 0},
            'A': {'total': 0, 'max': 0, 'percentage': 0},
            'S': {'total': 0, 'max': 0, 'percentage': 0},
            'F': {'total': 0, 'max': 0, 'percentage': 0}
        }

        for item_name, item_info in ALL_ITEMS.items():
            if item_name in data and data[item_name]:
                item_type = item_info['type']
                try:
                    value = int(data[item_name])
                    # Encontrar el valor máximo posible para este ítem
                    max_value = max(opt['value'] for opt in item_info['options'] if 'value' in opt)

                    type_scores[item_type]['total'] += value
                    type_scores[item_type]['max'] += max_value
                except (ValueError, TypeError):
                    continue

        # Calcular porcentajes
        for type_key in type_scores:
            if type_scores[type_key]['max'] > 0:
                type_scores[type_key]['percentage'] = round(
                    (type_scores[type_key]['total'] / type_scores[type_key]['max']) * 100, 1
                )

        return type_scores

    def interpret_score(self, total_score: int, age_weeks: int = None) -> str:
        """
        Provee una interpretación básica basada en el porcentaje de la puntuación total.
        """
        # Calculamos el máximo posible (suma de los valores máximos de cada ítem)
        max_possible = sum(
            max(opt['value'] for opt in item_info['options'] if 'value' in opt)
            for item_info in ALL_ITEMS.values()
        )

        percentage = (total_score / max_possible) * 100 if max_possible > 0 else 0

        if percentage < 25:
            return "La puntuación indica que se recomienda evaluación detallada."
        elif percentage < 50:
            return "La puntuación indica que se recomienda seguimiento cercano."
        elif percentage < 75:
            return "La puntuación indica un rendimiento dentro de lo esperado."
        else:
            return "La puntuación indica un rendimiento por encima de lo esperado."

    def get_detailed_analysis(self, scores: Dict[str, Any], age_weeks: int = None) -> Dict[str, Any]:
        """
        Genera análisis detallado de puntuaciones.
        """
        return {
            'scores': scores,
            'section_scores': {
                section: scores.get(section, 0)
                for section in TEST_SECTIONS.keys()
            },
            'type_scores': scores.get('type_scores', {}),
            'total_score': scores.get('total', 0),
            'interpretation': self.interpret_score(scores.get('total', 0)),
            'percentile': 'N/A'  # Mantenemos este campo pero lo marcamos como no aplicable
        }