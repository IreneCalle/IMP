# pdf_generator.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from typing import Dict, Any, List
import io
from datetime import datetime
from config import OBSERVED_ITEMS, PROVOKED_ITEMS, ALL_ITEMS, TEST_SECTIONS
from visualization import IMPVisualizer
import logging

logger = logging.getLogger('imp.pdf_generator')
COLORS = {
    'background': colors.HexColor('#E3ECFC'),  # Azul claro pastel
    'main': colors.HexColor('#4E73DF'),        # Azul principal vibrante
    'fill': colors.HexColor('#AFC8F5'),        # Azul suave para relleno
    'grid': colors.HexColor('#BFD3F2'),        # Azul grisáceo para la grilla
    'text': colors.HexColor('#374151'),        # Gris oscuro para el texto
    'highlight': colors.HexColor('#1E40AF')    # Azul profundo para detalles
}


class IMPReportGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=13,
            spaceAfter=10,
            alignment=1
        )
        self.subtitle_style = ParagraphStyle(
            'CustomSubTitle',
            parent=self.styles['Heading2'],
            fontSize=12,
            spaceAfter=8
        )
        self.normal_style = ParagraphStyle(
            'CustomNormal',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceBefore=6,
            spaceAfter=6
        )

    def _create_header(self, story: List, title: str) -> None:
        story.append(Paragraph(title, self.title_style))
        story.append(Spacer(1, 20))

    def _create_basic_info_section(self, story: List, is_blank: bool = True, data: Dict = None) -> None:
        if is_blank:
            basic_data = [
                ["ID Paciente: _________________", "Fecha: _________________"],
                ["Edad (semanas): _____________", "Evaluador: _____________"]
            ]
        else:
            basic_data = [
                [f"ID Paciente: {data.get('patientId', '')}", f"Fecha: {data.get('evaluationDate', '')}"],
                [f"Edad (semanas): {data.get('age_weeks', '')}", f"Evaluador: {data.get('evaluator', '')}"]
            ]

        table = Table(basic_data, colWidths=[4 * inch, 4 * inch])
        table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, COLORS['grid']),  # Azul grisáceo en lugar de gris
            ('PADDING', (0, 0), (-1, -1), 4),
            ('BACKGROUND', (0, 0), (-1, 0), COLORS['fill']),  # Azul claro en lugar de lightgrey
            ('TEXTCOLOR', (0, 0), (-1, -1), COLORS['text'])  # Texto en gris oscuro
        ]))
        story.append(table)
        story.append(Spacer(1, 20))

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
    def generate_blank_form(self) -> bytes:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )

        def add_header_footer(canvas, doc):
            canvas.saveState()
            canvas.setFont('Helvetica', 8)
            canvas.setFillColor(colors.gray)
            # Título en la parte superior
            canvas.drawString(72, A4[1] - 40, "Evaluación del Rendimiento Motor Infantil (IMP)")
            # Número de página en la parte inferior
            page_num = canvas.getPageNumber()
            canvas.drawString(A4[0] - 85, 30, f"Página {page_num}")
            canvas.restoreState()
        story = []

        # Crear estilo para las opciones
        options_style = ParagraphStyle(
            'Options',
            parent=self.styles['Normal'],
            fontSize=9,
            leftIndent=20,
            spaceBefore=2,
            spaceAfter=2
        )

        # Encabezado
        self._create_header(story, "Formulario de Evaluación IMP")
        self._create_basic_info_section(story)

        # Organizamos los ítems por sección
        for section_name, section_info in TEST_SECTIONS.items():
            story.append(Spacer(1, 10))
            story.append(Paragraph(section_info['title'], self.subtitle_style))
            story.append(Spacer(1, 3))

            # Filtrar y ordenar ítems de esta sección
            section_items = []
            for item_name, item_info in ALL_ITEMS.items():
                if (item_info['section'] == section_name and
                        (item_name in OBSERVED_ITEMS or item_name in PROVOKED_ITEMS)):
                    section_items.append((item_name, item_info))

            # Ordenar por número
            section_items.sort(key=lambda x: x[1]['number'])

            # Añadir ítems ordenados
            for item_name, item_info in section_items:
                story.append(Paragraph(
                    f"{item_info['number']}. {item_info['title']}: ",
                    self.normal_style
                ))

                # Opciones del ítem
                options_text = []
                for opt in item_info['options']:
                    if 'value' in opt and 'text' in opt:
                        options_text.append(f"[{opt['value']}] {opt['text']}")

                story.append(Paragraph(
                    "<br/>".join(options_text),
                    options_style
                ))
                story.append(Spacer(1, 5))

        # Sección de observaciones adicionales
        story.append(Spacer(1, 15))
        story.append(Paragraph("-----------------------------------------------------------------------------------------------", self.normal_style))
        story.append(Paragraph("-----------------------------------------------------------------------------------------------", self.normal_style))

        story.append(Paragraph("Observaciones Adicionales", self.subtitle_style))

        # Cantidad de movimientos
        story.append(Paragraph("Cantidad de movimientos:", self.normal_style))
        story.append(Paragraph("□ + □ ++ □ +++", options_style))
        story.append(Paragraph("                             ", options_style))


        # Estado conductual
        story.append(Paragraph("Estado conductual:", self.normal_style))
        story.append(Paragraph("_" * 50, self.normal_style))
        story.append(Paragraph("_" * 50, self.normal_style))


        # Estado de salud
        story.append(Paragraph("Estado de salud:", self.normal_style))
        story.append(Paragraph("_" * 50, self.normal_style))
        story.append(Paragraph("_" * 50, self.normal_style))


        # Otras observaciones
        story.append(Paragraph("Otras observaciones:", self.normal_style))
        story.append(Paragraph("_" * 50, self.normal_style))
        story.append(Paragraph("_" * 50, self.normal_style))
        story.append(Paragraph("_" * 50, self.normal_style))


        doc.build(story)
        return buffer.getvalue()

    def generate_results_report(self, data: Dict[str, Any], scores: Dict[str, int],
                                interpretation: str, detailed_analysis: Dict[str, Any]) -> bytes:
        buffer = io.BytesIO()
        try:
            doc = SimpleDocTemplate(
                buffer,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )

            def add_header_footer(canvas, doc):
                canvas.saveState()
                canvas.setFont('Helvetica', 8)
                canvas.setFillColor(COLORS['highlight'])  # Azul oscuro en vez de gris
                canvas.drawString(72, A4[1] - 40, "Evaluación del Rendimiento Motor Infantil (IMP)")
                page_num = canvas.getPageNumber()
                canvas.drawString(A4[0] - 85, 30, f"Página {page_num}")
                canvas.restoreState()

            story = []



            # Encabezado
            self._create_header(story, "Informe de Resultados IMP")
            self._create_basic_info_section(story, False, data)

            # Puntuaciones por tipo de habilidad
            story.append(Paragraph("Resultados por Tipo de Habilidad", self.subtitle_style))

            type_scores = self._calculate_type_scores(data)
            type_labels = {
                'P': 'Rendimiento',
                'V': 'Variedad',
                'A': 'Adaptabilidad',
                'S': 'Simetría',
                'F': 'Fluidez'
            }

            type_data = [["Habilidad", "Puntuación", "Porcentaje", "Puntuación máxima"]]
            total_score = 0
            total_max = 0

            for type_key, label in type_labels.items():
                score = type_scores[type_key]
                total_score += score['total']
                total_max += score['max']
                type_data.append([
                    label,
                    str(score['total']),
                    f"{score['percentage']}%",
                    str(score['max'])
                ])

            # Añadir total general
            total_percentage = round((total_score / total_max * 100), 1) if total_max > 0 else 0
            type_data.append([
                "TOTAL",
                str(total_score),
                f"{total_percentage}%",
                str(total_max)
            ])

            type_table = Table(type_data, colWidths=[2 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch])
            type_table.setStyle(TableStyle([
                ('GRID', (0, 0), (-1, -1), 0.5, COLORS['grid']),  # Azul grisáceo en lugar de gris
                ('PADDING', (0, 0), (-1, -1), 4),
                ('BACKGROUND', (0, 0), (-1, 0), COLORS['fill']),  # Azul claro en lugar de lightgrey
                ('TEXTCOLOR', (0, 0), (-1, -1), COLORS['text'])  # Texto en gris oscuro
            ]))

            story.append(type_table)
            story.append(Spacer(1, 20))

            # Añadir visualizaciones
            try:
                logger.info("Iniciando generación de visualizaciones")
                visualizer = IMPVisualizer()

                # Gráfico de puntuaciones por tipo
                story.append(Paragraph("Visualización de Puntuaciones por Tipo", self.subtitle_style))
                type_chart = visualizer.create_type_scores_chart(type_scores)
                story.append(type_chart)

                # Gráfico de secciones
                story.append(Spacer(1, 20))
                story.append(Paragraph("Visualización de Puntuaciones por Sección", self.subtitle_style))
                section_data = {section_info['title']: scores.get(section_name, 0)
                                for section_name, section_info in TEST_SECTIONS.items()}
                section_chart = visualizer.create_section_scores_chart(section_data)
                story.append(section_chart)

                logger.info("Visualizaciones generadas exitosamente")
            except Exception as e:
                logger.error(f"Error al generar visualizaciones: {str(e)}")
                # Continuamos con el resto del informe aunque fallen los gráficos

            # Añadir espacio después de los gráficos
            story.append(Spacer(1, 20))

            # Resultados por Sección
            story.append(Paragraph("Resultados por Sección", self.subtitle_style))
            section_data = [["Sección", "Puntuación Total"]]
            for section_name, section_info in TEST_SECTIONS.items():
                section_score = sum(int(data.get(item_name, 0))
                                    for item_name, item_info in ALL_ITEMS.items()
                                    if item_info['section'] == section_name and item_name in data)
                section_data.append([section_info['title'], str(section_score)])

            section_table = Table(section_data, colWidths=[5 * inch, 1.5 * inch])
            section_table.setStyle(TableStyle([
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                ('PADDING', (0, 0), (-1, -1), 6),
                ('ALIGN', (-1, 0), (-1, -1), 'CENTER'),
            ]))
            story.append(section_table)
            story.append(Spacer(1, 20))

            # Detalle de Respuestas por Sección
            story.append(Paragraph("Detalle de Respuestas", self.subtitle_style))

            for section_name, section_info in TEST_SECTIONS.items():
                story.append(Spacer(1, 10))
                story.append(Paragraph(section_info['title'], self.subtitle_style))

                section_items = []
                for item_name, item_info in ALL_ITEMS.items():
                    if (item_info['section'] == section_name and
                            item_name in data and
                            data[item_name]):

                        selected_value = int(data[item_name])
                        selected_text = ""
                        for opt in item_info['options']:
                            if opt['value'] == selected_value:
                                selected_text = opt['text']
                                break

                        section_items.append((
                            item_info['number'],
                            item_info['title'],
                            f"{selected_value} - {selected_text}",
                            item_info['type']
                        ))

                section_items.sort(key=lambda x: x[0])

                for num, title, response, item_type in section_items:
                    story.append(Paragraph(
                        f"{num}. {title} [{item_type}]:",
                        self.normal_style
                    ))
                    story.append(Paragraph(
                        f"    Respuesta: {response}",
                        self.normal_style
                    ))
                    story.append(Spacer(1, 5))

            # Observaciones adicionales si existen
            if any(key in data for key in
                   ['estado_conductual', 'estado_salud', 'otras_observaciones', 'cantidad_movimientos']):
                story.append(Spacer(1, 15))
                story.append(Paragraph("Observaciones", self.subtitle_style))

                if 'cantidad_movimientos' in data and data['cantidad_movimientos']:
                    story.append(Paragraph(f"Cantidad de movimientos: {data['cantidad_movimientos']}", self.normal_style))

                if 'estado_conductual' in data and data['estado_conductual']:
                    story.append(Paragraph(f"Estado conductual: {data['estado_conductual']}", self.normal_style))

                if 'estado_salud' in data and data['estado_salud']:
                    story.append(Paragraph(f"Estado de salud: {data['estado_salud']}", self.normal_style))

                if 'otras_observaciones' in data and data['otras_observaciones']:
                    story.append(Paragraph(f"Otras observaciones: {data['otras_observaciones']}", self.normal_style))

            # Fecha y firma
            story.append(Spacer(1, 40))
            story.append(Paragraph(
                f"Fecha del informe: {datetime.now().strftime('%d/%m/%Y')}",
                self.normal_style
            ))
            story.append(Spacer(1, 20))
            story.append(Paragraph("Firma del evaluador:", self.normal_style))
            story.append(Paragraph("_" * 30, self.normal_style))

            doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
            return buffer.getvalue()

        except Exception as e:
            logger.error(f"Error al generar el informe PDF: {str(e)}")
            raise

        finally:
            buffer.close()



