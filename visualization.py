
import logging

from reportlab.graphics.charts.spider import SpiderChart
from reportlab.graphics.shapes import Drawing, Rect, Line, String
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib import colors
from reportlab.graphics import renderPDF

# Configuración de logging específica para visualizaciones
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('imp.visualization')


class IMPVisualizer:
    def __init__(self):
        self.width = 400
        self.height = 200
        logger.info("Inicializando IMPVisualizer")

    def create_type_scores_chart(self, type_scores):
        """
        Crea un gráfico de barras mejorado para las puntuaciones por tipo
        """
        try:
            logger.info("Creando gráfico de puntuaciones por tipo")
            drawing = Drawing(self.width, self.height)

            # Configuración básica del gráfico
            bc = VerticalBarChart()
            bc.x = 50
            bc.y = 50
            bc.height = 125
            bc.width = 300

            # Paleta de colores moderna
            COLORS = {
                'bar_fill': colors.HexColor('#4e73df'),  # Azul moderno
                'bar_hover': colors.HexColor('#2e59d9'),  # Azul oscuro para bordes
                'grid': colors.HexColor('#eaecf4'),  # Gris muy claro para la grilla
                'text': colors.HexColor('#5a5c69'),  # Gris oscuro para texto
                'reference': colors.HexColor('#e74a3b')  # Rojo moderno para línea de referencia
            }

            # Configuración del eje de valores
            bc.valueAxis.strokeColor = COLORS['grid']
            bc.valueAxis.gridStrokeColor = COLORS['grid']
            bc.valueAxis.labelTextFormat = '%d%%'
            bc.valueAxis.labels.fontSize = 8
            bc.valueAxis.strokeWidth = 0.5
            bc.valueAxis.gridStrokeWidth = 0.5
            bc.valueAxis.labels.fontName = 'Helvetica'
            bc.valueAxis.labels.fillColor = COLORS['text']

            # Configuración del eje de categorías
            bc.categoryAxis.strokeColor = COLORS['grid']
            bc.categoryAxis.gridStrokeColor = COLORS['grid']
            bc.categoryAxis.strokeWidth = 0.5
            bc.categoryAxis.gridStrokeWidth = 0
            bc.categoryAxis.labels.fontName = 'Helvetica-Bold'
            bc.categoryAxis.labels.fontSize = 8
            bc.categoryAxis.labels.fillColor = COLORS['text']

            # Procesamos los datos
            data = [[]]
            labels = []
            type_labels = {
                'P': 'Rendimiento',
                'V': 'Variedad',
                'A': 'Adaptabilidad',
                'S': 'Simetría',
                'F': 'Fluidez'
            }

            for type_key, scores in type_scores.items():
                try:
                    percentage = scores['percentage']
                    data[0].append(percentage)
                    labels.append(type_labels[type_key])
                    logger.info(f"Datos procesados - Tipo: {type_key}, Valor: {percentage}%")
                except KeyError as e:
                    logger.error(f"Error al procesar tipo {type_key}: {str(e)}")
                    continue

            logger.info(f"Datos finales - Values: {data[0]}, Labels: {labels}")

            # Configuración del gráfico
            bc.data = data
            bc.categoryAxis.categoryNames = labels
            bc.valueAxis.valueMin = 0
            bc.valueAxis.valueMax = 100
            bc.valueAxis.valueStep = 20

            # Configuración de etiquetas del eje
            bc.categoryAxis.labels.boxAnchor = 'n'
            bc.categoryAxis.labels.dx = 0
            bc.categoryAxis.labels.dy = -5
            bc.categoryAxis.labels.angle = 0

            # Estilo de las barras
            bc.bars[0].fillColor = COLORS['bar_fill']
            bc.bars[0].strokeColor = COLORS['bar_hover']
            bc.bars[0].strokeWidth = 1
            bc.barWidth = 0.75

            # Añadir el gráfico base
            drawing.add(bc)
            logger.info("Gráfico base añadido")

            # Añadir línea de referencia
            line = Line(
                bc.x, bc.y + bc.height,
                      bc.x + bc.width, bc.y + bc.height,
                strokeColor=COLORS['reference'],
                strokeWidth=1,
                strokeDashArray=[4, 2]
            )
            drawing.add(line)
            logger.info("Línea de referencia añadida")

            # Añadir etiquetas de valor en las barras
            for i, value in enumerate(data[0]):
                bar_x = bc.x + (i + 0.5) * (bc.width / len(data[0]))
                bar_height = bc.height * (value / 100)

                # Etiqueta de porcentaje
                label = String(
                    bar_x,
                    bc.y + bar_height + 5,
                    f'{value:.1f}%',
                    fontSize=9,
                    fontName='Helvetica-Bold',
                    fillColor=COLORS['text'],
                    textAnchor='middle'
                )
                drawing.add(label)
                logger.info(f"Etiqueta añadida para valor {value}")

            # Título y subtítulo
            title = String(
                self.width / 2,
                self.height - 20,
                'Puntuaciones por Tipo de Habilidad',
                fontSize=12,
                fontName='Helvetica-Bold',
                fillColor=COLORS['text'],
                textAnchor='middle'
            )
            drawing.add(title)

            subtitle = String(
                self.width / 2,
                self.height - 35,
                'Porcentajes alcanzados en cada área',
                fontSize=8,
                fontName='Helvetica',
                fillColor=COLORS['text'],
                textAnchor='middle'
            )
            drawing.add(subtitle)

            logger.info("Gráfico de puntuaciones completado exitosamente")
            return drawing

        except Exception as e:
            logger.error(f"Error al crear gráfico de puntuaciones: {str(e)}", exc_info=True)
            return Drawing(self.width, self.height)

    def create_section_scores_chart(self, section_scores):
        try:
            logger.info("Creando gráfico de perfil por secciones")

            drawing = Drawing(400, 300)  # Aumentamos el tamaño para evitar superposición

            # Paleta de colores modernizada
            COLORS = {
                'background': colors.HexColor('#E3ECFC'),  # Azul claro pastel para el fondo
                'main': colors.HexColor('#4E73DF'),  # Azul principal vibrante
                'fill': colors.HexColor('#AFC8F5'),  # Azul suave para relleno
                'grid': colors.HexColor('#BFD3F2'),  # Azul grisáceo para la grilla
                'text': colors.HexColor('#374151'),  # Gris oscuro para el texto
                'highlight': colors.HexColor('#1E40AF')  # Azul profundo para detalles
            }

            # Configuración del gráfico
            spider = SpiderChart()
            spider.x = 50
            spider.y = 50  # Ajustado para centrar mejor
            spider.width = 300
            spider.height = 200

            # Estilo del gráfico
            spider.strands[0].strokeColor = COLORS['main']
            spider.strands[0].strokeWidth = 2
            spider.strands[0].fillColor = COLORS['fill']
            spider.spokes.strokeColor = COLORS['grid']
            spider.spokes.strokeWidth = 0.5
            spider.spokeLabels.fontName = 'Helvetica-Bold'
            spider.spokeLabels.fontSize = 10  # Aumentado para mayor legibilidad
            #spider.labelRadius = 1.3  # Aumentado para separar más las etiquetas

            # Mapeo de nombres
            section_mapping = {
                'Posición Boca Arriba (Decúbito Supino)': 'Boca Arriba',
                'Posición Boca Abajo (Decúbito Prono)': 'Boca Abajo',
                'Posición Sentada (Sedestación)': 'Sentada',
                'Posición de Pie (Bipedestación) y Marcha': 'De Pie',
                'Alcance, agarre y manipulación de objetos durante sedestación': 'Manipulación',
                'General: Ítems observados durante la evaluación': 'General'
            }

            # Valores máximos por sección
            total_possible = {
                'Boca Arriba': 80,
                'Boca Abajo': 60,
                'Sentada': 50,
                'De Pie': 70,
                'Manipulación': 40,
                'General': 20
            }

            percentages = []
            labels = []
            for long_name, score in section_scores.items():
                short_name = section_mapping.get(long_name)
                if short_name and short_name in total_possible:
                    try:
                        score_value = float(score)
                        max_value = total_possible[short_name]
                        percentage = (score_value / max_value) * 100
                        percentages.append(percentage)
                        labels.append(short_name)
                        logger.info(f"Sección {short_name}: {percentage:.1f}%")
                    except ValueError as e:
                        logger.error(f"Error procesando {short_name}: {e}")
                        continue

            if not percentages:
                logger.error("No hay datos válidos para generar el gráfico")
                return Drawing(400, 300)

            spider.data = [percentages]
            spider.labels = labels
            drawing.add(spider)

            # Título y subtítulo
            title = String(200, 280, 'Perfil de desarrollo',
                           fontSize=14, fontName='Helvetica-Bold', fillColor=COLORS['text'], textAnchor='middle')
            drawing.add(title)


            logger.info("Gráfico de secciones completado exitosamente")
            return drawing

        except Exception as e:
            logger.error(f"Error al crear gráfico de secciones: {str(e)}", exc_info=True)
            return Drawing(400, 300)
