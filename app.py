# app.py
from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
from scoring import IMPValidator, IMPScorer
from pdf_generator import IMPReportGenerator
from config import OBSERVED_ITEMS, PROVOKED_ITEMS, ALL_ITEMS, TEST_SECTIONS
import logging
import io
from reportlab.pdfgen import canvas

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Inyectamos el año actual en todas las plantillas
@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

# Clase para manejar errores de la aplicación
class IMPError(Exception):
    pass

@app.route('/form')
def evaluation_form():
    """Ruta que muestra el formulario de evaluación"""
    try:
        return render_template(
            'form.html',
            observed_items=[item for item_name, item in ALL_ITEMS.items() if item_name in OBSERVED_ITEMS],
            provoked_items=[item for item_name, item in ALL_ITEMS.items() if item_name in PROVOKED_ITEMS]
        )
    except Exception as e:
        logger.error(f"Error en la ruta del formulario: {str(e)}")
        return jsonify({'error': 'Error interno del servidor'}), 500

@app.route('/')
def index():
    """Ruta principal que muestra la página de inicio"""
    try:
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error en la ruta principal: {str(e)}")
        return jsonify({'error': 'Error interno del servidor'}), 500


@app.route('/evaluate', methods=['POST'])
def evaluate():
    """
    Procesa el formulario de evaluación y retorna los resultados.
    Incluye validación de datos y cálculo de puntuaciones.
    """
    try:
        data = request.form.to_dict()
        logger.info(f"Recibida solicitud de evaluación para paciente ID: {data.get('patientId', 'Desconocido')}")

        # Validamos los datos recibidos
        validator = IMPValidator()
        is_valid, error_message = validator.validate_form_data(data)
        if not is_valid:
            logger.warning(f"Validación fallida: {error_message}")
            return jsonify({'error': error_message}), 400

        # Calculamos las puntuaciones
        scorer = IMPScorer()
        scores = scorer.calculate_score(data)
        interpretation = scorer.interpret_score(
            scores['total'],
            int(data['age_weeks'])
        )
        detailed_analysis = scorer.get_detailed_analysis(scores, int(data['age_weeks']))

        logger.info(f"Evaluación completada con éxito para paciente ID: {data.get('patientId', 'Desconocido')}")

        return jsonify({
            'status': 'success',
            'scores': scores,
            'interpretation': interpretation,
            'detailed_analysis': detailed_analysis
        })

    except IMPError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"Error durante la evaluación: {str(e)}")
        return jsonify({'error': 'Error interno del servidor'}), 500


@app.route('/download_blank_form')
def download_blank_form():
    """
    Genera y devuelve un formulario IMP en blanco en formato PDF.
    """
    try:
        logger.info("Generando formulario IMP en blanco")
        pdf_generator = IMPReportGenerator()
        pdf_bytes = pdf_generator.generate_blank_form()

        return send_file(
            io.BytesIO(pdf_bytes),
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f'IMP_formulario_{datetime.now().strftime("%Y%m%d")}.pdf'
        )
    except Exception as e:
        logger.error(f"Error generando formulario en blanco: {str(e)}")
        return jsonify({'error': 'Error generando el formulario'}), 500


@app.route('/download_results', methods=['POST'])
def download_results():
    """
    Genera y devuelve un informe PDF con los resultados de la evaluación.
    """
    try:
        data = request.form.to_dict()
        logger.info(f"Generando informe de resultados para paciente ID: {data.get('patientId', 'Desconocido')}")

        # Validamos los datos nuevamente
        validator = IMPValidator()
        is_valid, error_message = validator.validate_form_data(data)
        if not is_valid:
            raise IMPError(error_message)

        # Calculamos resultados
        scorer = IMPScorer()
        scores = scorer.calculate_score(data)
        interpretation = scorer.interpret_score(
            scores['total'],
            int(data['age_weeks'])
        )
        detailed_analysis = scorer.get_detailed_analysis(scores, int(data['age_weeks']))

        # Generamos PDF
        pdf_generator = IMPReportGenerator()
        pdf_bytes = pdf_generator.generate_results_report(
            data, scores, interpretation, detailed_analysis
        )

        return send_file(
            io.BytesIO(pdf_bytes),
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f'IMP_resultados_{data.get("patientId", "desconocido")}_{datetime.now().strftime("%Y%m%d")}.pdf'
        )

    except IMPError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"Error generando informe de resultados: {str(e)}")
        return jsonify({'error': 'Error generando el informe de resultados'}), 500


@app.errorhandler(404)
def not_found_error(error):
    """Maneja errores 404 - Página no encontrada"""
    return jsonify({'error': 'Página no encontrada'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Maneja errores 500 - Error interno del servidor"""
    logger.error(f"Error interno del servidor: {str(error)}")
    return jsonify({'error': 'Error interno del servidor'}), 500


if __name__ == '__main__':
    # Configuración para desarrollo
    app.config['JSON_SORT_KEYS'] = False  # Mantiene el orden de las claves en JSON
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # JSON formateado en desarrollo

    # Iniciamos la aplicación
    app.run(debug=True)