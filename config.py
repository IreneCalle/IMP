# config.py

"""
Configuración completa para la evaluación IMP (Infant Motor Performance).
Incluye todos los ítems de evaluación con sus valores y descripciones según la traducción oficial.
"""

from typing import Dict, List, Any

# =========================================================
# CONFIGURACIÓN DE ÍTEMS Y VALORES
# =========================================================

ALL_ITEMS: Dict[str, Dict[str, Any]] = {
    'control_cabeza': {
        'title': 'Control de movimientos de la cabeza',
        'section': 'supine',
        'number': 1,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No controla los movimientos de la cabeza'},
            {'value': 2, 'text': 'Controla los movimientos de la cabeza de forma limitada'},
            {'value': 3, 'text': 'Controla los movimientos de la cabeza'}
        ]
    },
    'variedad_movimientos_cabeza': {
        'title': 'Variedad de movimientos de la cabeza',
        'section': 'supine',
        'number': 2,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_movimientos_cabeza': {
        'title': 'Capacidad de adaptar los movimientos de la cabeza',
        'section': 'supine',
        'number': 3,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'posicion_cabeza_lado': {
        'title': 'Posición de la cabeza, tendencia hacia un lado',
        'section': 'supine',
        'number': 4,
        'type': 'S',  # Symmetry
        'options': [
            {'value': 1, 'text': 'Posición muy marcada hacia derecha/izquierda'},
            {'value': 2, 'text': 'Posición moderadamente marcada hacia derecha/izquierda'},
            {'value': 3, 'text': 'Sin posición predominante o ligera tendencia hacia un lado'}
        ]
    },
    'rtca_presencia': {
        'title': 'Postura, presencia de reflejo tónico del cuello (RTCA)',
        'section': 'supine',
        'number': 5,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Reflejo frecuente u obligatorio'},
            {'value': 2, 'text': 'Sin reflejo o reflejo ocasional no obligatorio'}
        ]
    },
    'hiperextension_presencia': {
        'title': 'Postura, presencia de hiperextensión de cuello y tronco',
        'section': 'supine',
        'number': 6,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Extensión excesiva frecuente o persistente'},
            {'value': 2, 'text': 'Sin extensión excesiva o raramente presente'}
        ]
    },
    'manipulacion_manos': {
        'title': 'Manipulación con manos y dedos',
        'section': 'supine',
        'number': 7,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No manipula'},
            {'value': 2, 'text': 'Manipula ropa; con manos en línea media, sobre rodillas o pies; juega con manos en boca'}
        ]
    },
    'variedad_movimientos_brazos': {
        'title': 'Variedad de movimientos de brazos',
        'section': 'supine',
        'number': 8,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'variedad_movimientos_dedos': {
        'title': 'Variedad de movimientos de dedos',
        'section': 'supine',
        'number': 9,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'basculacion_pelvis': {
        'title': 'Movimiento de la pelvis (basculación pélvica)',
        'section': 'supine',
        'number': 10,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'Sin movimiento de pelvis'},
            {'value': 2, 'text': 'Mueve la pelvis, pero no lo suficiente para que las manos toquen las rodillas'},
            {'value': 3, 'text': 'Mueve la pelvis permitiendo que las manos toquen las rodillas'},
            {'value': 4, 'text': 'Las manos juegan con los pies'}
        ]
    },
    'variedad_movimientos_piernas': {
        'title': 'Variedad de movimientos de piernas',
        'section': 'supine',
        'number': 11,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'variedad_movimientos_dedos_pie': {
        'title': 'Variedad de movimientos de dedos del pie',
        'section': 'supine',
        'number': 12,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'giro_supino_prono': {
        'title': 'Giro (volteo) de boca arriba a boca abajo',
        'section': 'supine',
        'number': 13,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'Sin intentos de giro'},
            {'value': 2, 'text': 'Hace movimientos serpenteantes con la pelvis, pero no gira hacia el lado'},
            {'value': 3, 'text': 'Gira hacia un lado, unilateral'},
            {'value': 4, 'text': 'Gira hacia ambos lados'},
            {'value': 5, 'text': 'Se voltea completamente hacia un lado'},
            {'value': 6, 'text': 'Se voltea completamente hacia ambos lados'}
        ]
    },
    'alcance_manipulacion': {
        'title': 'Alcance, agarre y manipulación de objetos',
        'section': 'supine',
        'number': 14,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No intenta alcanzar, no muestra movimientos de intento'},
            {'value': 2, 'text': 'No alcanza, pero muestra intentos de movimiento'},
            {'value': 3, 'text': 'Intenta alcanzar el objeto pero no lo agarra'},
            {'value': 4, 'text': 'Alcanza, agarra y sostiene el objeto, pero no lo manipula'},
            {'value': 5, 'text': 'Alcanza, sostiene y manipula 1 objeto'},
            {'value': 6, 'text': 'Alcanza, sostiene y manipula 2 objetos'},
            {'value': 7, 'text': 'Alcanza y sostiene ≥3 objetos'}
        ]
    },
    'asimetria_alcance_supino': {
        'title': 'Alcance, agarre y manipulación: presencia de asimetría',
        'section': 'supine',
        'number': 15,
        'type': 'S',  # Symmetry
        'options': [
            {'value': 0, 'text': 'Sin movimientos de alcance o intento'},
            {'value': 1, 'text': 'Asimetría marcada, lado derecho/izquierdo peor'},
            {'value': 2, 'text': 'Asimetría moderada, lado derecho/izquierdo peor'},
            {'value': 3, 'text': 'Sin asimetría o asimetría leve'}
        ]
    },
    'variedad_alcance_supino': {
        'title': 'Variedad en movimientos de alcance de los brazos',
        'section': 'supine',
        'number': 16,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'Sin movimientos de alcance'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_alcance_supino': {
        'title': 'Adaptabilidad de movimientos de alcance de los brazos',
        'section': 'supine',
        'number': 17,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'Sin movimientos de alcance'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'variedad_mano_alcance_supino': {
        'title': 'Variedad en movimientos de la mano durante alcance, agarre y manipulación',
        'section': 'supine',
        'number': 18,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'Sin movimientos de alcance'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_mano_supino': {
        'title': 'Adaptabilidad de movimientos de la mano durante alcance, agarre y manipulación',
        'section': 'supine',
        'number': 19,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'Sin movimientos de alcance'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'temblor_alcance_supino': {
        'title': 'Temblor durante intentos de alcance',
        'section': 'supine',
        'number': 20,
        'type': 'F',  # Fluency
        'options': [
            {'value': 0, 'text': 'Sin movimientos de alcance o intento'},
            {'value': 1, 'text': 'Temblor frecuente'},
            {'value': 2, 'text': 'Sin temblor o temblor ocasional'}
        ]
    },
    'fluidez_movimiento_supino': {
        'title': 'Fluidez de movimiento en posición boca arriba',
        'section': 'supine',
        'number': 21,
        'type': 'F',  # Fluency
        'options': [
            {'value': 1, 'text': 'No fluido: rígido, brusco, flácido/lento'},
            {'value': 2, 'text': 'Fluido'}
        ]
    },
    'elevacion_cabeza_prono': {
        'title': 'Elevación de la cabeza en prono',
        'section': 'prone',
        'number': 22,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No levanta ni gira la cabeza'},
            {'value': 2, 'text': 'Gira la cabeza hacia un lado con mínima elevación'},
            {'value': 3, 'text': 'Levanta la cabeza durante unos segundos'},
            {'value': 4, 'text': 'Mantiene la cabeza levantada al menos 10 segundos, con alguna dificultad para mirar alrededor'},
            {'value': 5, 'text': 'Mantiene la cabeza levantada y mira alrededor'}
        ]
    },
    'posicion_cabeza_prono': {
        'title': 'Posición de la cabeza, presencia de tendencia hacia un lado',
        'section': 'prone',
        'number': 23,
        'type': 'S',  # Symmetry
        'options': [
            {'value': 0, 'text': 'No levanta ni gira la cabeza'},
            {'value': 1, 'text': 'Posición muy marcada hacia derecha/izquierda'},
            {'value': 2, 'text': 'Posición moderadamente marcada hacia derecha/izquierda'},
            {'value': 3, 'text': 'Sin posición predominante o ligera tendencia hacia un lado'}
        ]
    },
    'variedad_movimientos_cabeza_prono': {
        'title': 'Variedad de movimientos de la cabeza',
        'section': 'prone',
        'number': 24,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_movimientos_cabeza_prono': {
        'title': 'Adaptabilidad de movimientos de la cabeza',
        'section': 'prone',
        'number': 25,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'capacidad_funcional_hombros': {
        'title': 'Capacidad funcional de la cintura escapular mientras está en prono',
        'section': 'prone',
        'number': 26,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No usa brazos ni manos para elevar cabeza y tórax'},
            {'value': 2, 'text': 'Usa brazos y manos para elevar cabeza y tórax, pero no logra apoyo activo en codos y antebrazos'},
            {'value': 3, 'text': 'Se apoya en codos y antebrazos'},
            {'value': 4, 'text': 'Eleva la parte superior del tórax apoyándose en manos con brazos extendidos'}
        ]
    },
    'capacidad_funcional_brazos': {
        'title': 'Capacidad funcional de brazos y manos mientras está en prono',
        'section': 'prone',
        'number': 27,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'Tiene dificultades para usar brazos y manos en control postural y no los usa para otras actividades'},
            {'value': 2, 'text': 'Usa uno o dos brazos y manos para control postural, sin usarlos para otras actividades'},
            {'value': 3, 'text': 'Usa uno o dos brazos para control postural mientras las manos muestran algo de juego'},
            {'value': 4, 'text': 'Usa un brazo para apoyo postural y usa el otro brazo y mano para alcance y manipulación'}
        ]
    },
    'asimetria_postura_prono': {
        'title': 'Postura y movimientos de brazos y manos durante actividad: presencia de asimetría',
        'section': 'prone',
        'number': 28,
        'type': 'S',  # Symmetry
        'options': [
            {'value': 0, 'text': 'Ambos brazos permanecen en posición impuesta por examinador'},
            {'value': 1, 'text': 'Asimetría marcada, lado derecho/izquierdo peor'},
            {'value': 2, 'text': 'Asimetría moderada, lado derecho/izquierdo peor'},
            {'value': 3, 'text': 'Sin asimetría o asimetría leve'}
        ]
    },
    'progresion_prono': {
        'title': 'Progresión mientras está en prono: desarrollo del gateo',
        'section': 'prone',
        'number': 29,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No muestra giro sobre sí mismo (pivote) ni gateo'},
            {'value': 2, 'text': 'Gira sobre sí mismo (pivote)'},
            {'value': 3, 'text': 'Gateo sobre abdomen, usa brazos y/o piernas'},
            {'value': 4, 'text': 'Gatea sobre manos y rodillas, abdomen separado de la superficie'}
        ]
    },
    'variedad_pregateo': {
        'title': 'Variedad en movimientos pre-gateo de las piernas',
        'section': 'prone',
        'number': 30,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'Muestra progresión en prono (gateo)'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'giro_prono_supino': {
        'title': 'Giro (volteo) de boca abajo a boca arriba',
        'section': 'prone',
        'number': 31,
        'type': 'P',  # Performance
        'options': [
            {'value': 0, 'text': 'No muestra giro ya que prefiere cambiar de posición mediante gateo'},
            {'value': 1, 'text': 'Sin intentos de giro, no puede cambiar posición con ayuda de sentado o gateo'},
            {'value': 2, 'text': 'Gira hacia un lado, unilateral'},
            {'value': 3, 'text': 'Gira hacia ambos lados'},
            {'value': 4, 'text': 'Voltea completamente hacia un lado'},
            {'value': 5, 'text': 'Voltea completamente hacia ambos lados'}
        ]
    },
    'variedad_gateo': {
        'title': 'Variedad en el gateo',
        'section': 'prone',
        'number': 32,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'No muestra progresión en prono'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_gateo': {
        'title': 'Adaptabilidad del gateo',
        'section': 'prone',
        'number': 33,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'No muestra progresión en prono'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'control_cabeza_sedestacion': {
        'title': 'Control de movimientos de la cabeza',
        'section': 'sitting',
        'number': 34,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No controla los movimientos de la cabeza'},
            {'value': 2, 'text': 'Controla los movimientos de la cabeza de forma limitada'},
            {'value': 3, 'text': 'Controla los movimientos de la cabeza'}
        ]
    },
    'posicion_cabeza_sedestacion': {
        'title': 'Posición de la cabeza mientras está sentado: tendencia hacia un lado',
        'section': 'sitting',
        'number': 35,
        'type': 'S',  # Symmetry
        'options': [
            {'value': 1, 'text': 'Posición muy marcada hacia derecha/izquierda'},
            {'value': 2, 'text': 'Posición moderadamente marcada hacia derecha/izquierda'},
            {'value': 3, 'text': 'Sin posición predominante o ligera tendencia hacia un lado'}
        ]
    },
    'capacidad_sentarse': {
        'title': 'Capacidad de mantenerse sentado',
        'section': 'sitting',
        'number': 36,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No puede sentarse independientemente'},
            {'value': 2, 'text': 'Se sienta con flexión extrema de pelvis (abdomen tocando muslos), brazos apoyados; no puede sentarse erguido'},
            {'value': 3, 'text': 'Se sienta independientemente más de 5 segundos; no puede desplazar peso'},
            {'value': 4, 'text': 'Se sienta independientemente, puede desplazar peso, pero muestra poca o ninguna rotación de tronco'},
            {'value': 5, 'text': 'Se sienta independientemente y puede desplazar peso y rotar el tronco'}
        ]
    },
    'postura_tronco_sedestacion': {
        'title': 'Postura del tronco en sedestación independiente',
        'section': 'sitting',
        'number': 37,
        'type': 'P',  # Performance
        'options': [
            {'value': 0, 'text': 'No puede sentarse independientemente'},
            {'value': 1, 'text': 'Espalda redondeada'},
            {'value': 2, 'text': 'Espalda recta'}
        ]
    },
    'asimetria_tronco_piernas': {
        'title': 'Postura de tronco y piernas mientras está sentado: presencia de asimetría',
        'section': 'sitting',
        'number': 38,
        'type': 'S',  # Symmetry
        'options': [
            {'value': 0, 'text': 'No puede sentarse independientemente'},
            {'value': 1, 'text': 'Asimetría marcada, se cae hacia derecha/izquierda'},
            {'value': 2, 'text': 'Asimetría moderada, se inclina hacia derecha/izquierda'},
            {'value': 3, 'text': 'Sin asimetría o asimetría leve'}
        ]
    },
    'asimetria_extremidades_superiores': {
        'title': 'Postura y movimientos de extremidades superiores durante sedestación: presencia de asimetría',
        'section': 'sitting',
        'number': 39,
        'type': 'S',  # Symmetry
        'options': [
            {'value': 0, 'text': 'Puede sentarse independientemente de forma limitada'},
            {'value': 1, 'text': 'Asimetría marcada, lado derecho/izquierdo peor'},
            {'value': 2, 'text': 'Asimetría moderada, lado derecho/izquierdo peor'},
            {'value': 3, 'text': 'Sin asimetría o asimetría leve'}
        ]
    },
    'uso_brazos': {
        'title': 'Uso de brazos para actividades voluntarias',
        'section': 'sitting',
        'number': 40,
        'type': 'P',  # Performance
        'options': [
            {'value': 0, 'text': 'No puede sentarse independientemente'},
            {'value': 1, 'text': 'Usa uno o dos brazos para apoyo postural, no los usa para actividad voluntaria'},
            {'value': 2, 'text': 'Usa un brazo para apoyo postural, usa el otro para actividad voluntaria'},
            {'value': 3, 'text': 'Usa ambos brazos para actividad voluntaria, no los usa para apoyo postural'}
        ]
    },
    'variedad_sedestacion': {
        'title': 'Variedad en los movimientos durante sedestación',
        'section': 'sitting',
        'number': 41,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'No puede sentarse independientemente'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_sedestacion': {
        'title': 'Adaptabilidad de movimientos durante sedestación',
        'section': 'sitting',
        'number': 42,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'No puede sentarse independientemente'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'pasar_sentado': {
        'title': 'Pasar a posición sentada',
        'section': 'sitting',
        'number': 43,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No se sienta o se levanta independientemente'},
            {'value': 2, 'text': 'Se sienta o se levanta independientemente'}
        ]
    },
    'variedad_sentarse': {
        'title': 'Variedad al pasar a posición sentada',
        'section': 'sitting',
        'number': 44,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'No mostró o solo mostró una vez movimientos para sentarse o levantarse'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_sentarse': {
        'title': 'Adaptabilidad al pasar a posición sentada',
        'section': 'sitting',
        'number': 45,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'No mostró o solo mostró una vez movimientos para sentarse o levantarse'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'desplazamiento_sentado': {
        'title': 'Desplazamiento sentado',
        'section': 'sitting',
        'number': 46,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'No puede sentarse independientemente'},
            {'value': 1, 'text': 'El desplazamiento sentado es, aparte de la marcha, la única estrategia para moverse'},
            {'value': 2, 'text': 'Sin desplazamiento sentado o presente como una de las estrategias para moverse'}
        ]
    },
    'capacidad_bipedestacion': {
        'title': 'Capacidad de mantenerse de pie',
        'section': 'standing',
        'number': 47,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No puede ponerse de pie'},
            {'value': 2, 'text': 'Se mantiene de pie con ayuda'},
            {'value': 3, 'text': 'Se mantiene de pie independientemente durante unos segundos'},
            {'value': 4, 'text': 'Se mantiene de pie independientemente más de 10 segundos, pero rota el tronco mínimamente'},
            {'value': 5, 'text': 'Se mantiene de pie independientemente y puede rotar el tronco'}
        ]
    },
    'ponerse_pie': {
        'title': 'Ponerse de pie',
        'section': 'standing',
        'number': 48,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No puede ponerse de pie'},
            {'value': 2, 'text': 'Se pone de rodillas'},
            {'value': 3, 'text': 'Se pone de pie independientemente con ayuda de muebles'},
            {'value': 4, 'text': 'Se pone de pie independientemente sin usar muebles'}
        ]
    },
    'variedad_ponerse_pie': {
        'title': 'Variedad en ponerse de pie',
        'section': 'standing',
        'number': 49,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'No se puso de pie o solo lo hizo una vez'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_ponerse_pie': {
        'title': 'Adaptabilidad al ponerse de pie',
        'section': 'standing',
        'number': 50,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'No se puso de pie o solo lo hizo una vez'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'marcha': {
        'title': 'Marcha',
        'section': 'standing',
        'number': 51,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No puede caminar'},
            {'value': 2, 'text': 'Camina cuando recibe apoyo con dos manos'},
            {'value': 3, 'text': 'Camina cuando recibe apoyo con una mano'},
            {'value': 4, 'text': 'Camina independientemente'}
        ]
    },
    'equilibrio_marcha': {
        'title': 'Equilibrio mientras camina independientemente',
        'section': 'standing',
        'number': 52,
        'type': 'P',  # Performance
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Pobre capacidad de equilibrio'},
            {'value': 2, 'text': 'Moderada capacidad de equilibrio'},
            {'value': 3, 'text': 'Buena capacidad de equilibrio'}
        ]
    },
    'postura_brazos_marcha': {
        'title': 'Postura de brazos mientras camina independientemente',
        'section': 'standing',
        'number': 53,
        'type': 'P',  # Performance
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Guardia alta o semi-alta'},
            {'value': 2, 'text': 'Postura de brazos arbitraria'}
        ]
    },
    'asimetria_extremidades_superiores_marcha': {
        'title': 'Postura y movimientos de extremidades superiores mientras camina independientemente: presencia de asimetría',
        'section': 'standing',
        'number': 54,
        'type': 'S',  # Symmetry
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Asimetría marcada, lado derecho/izquierdo peor'},
            {'value': 2, 'text': 'Asimetría moderada, lado derecho/izquierdo peor'},
            {'value': 3, 'text': 'Sin asimetría o asimetría leve'}
        ]
    },
    'variedad_brazos_marcha': {
        'title': 'Variedad en movimientos de brazos y manos mientras camina independientemente',
        'section': 'standing',
        'number': 55,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente o camina con guardia alta/semi-alta'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_brazos_marcha': {
        'title': 'Adaptabilidad de movimientos de brazos y manos mientras camina independientemente',
        'section': 'standing',
        'number': 56,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente o camina con guardia alta/semi-alta'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'variedad_tronco_marcha': {
        'title': 'Variedad en movimientos del tronco mientras está de pie y camina independientemente',
        'section': 'standing',
        'number': 57,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_tronco_marcha': {
        'title': 'Adaptabilidad de movimientos del tronco mientras está de pie y camina independientemente',
        'section': 'standing',
        'number': 58,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'asimetria_piernas_marcha': {
        'title': 'Postura y movimientos de piernas mientras camina independientemente: presencia de asimetría',
        'section': 'standing',
        'number': 59,
        'type': 'S',  # Symmetry
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Asimetría marcada, lado derecho/izquierdo peor'},
            {'value': 2, 'text': 'Asimetría moderada, lado derecho/izquierdo peor'},
            {'value': 3, 'text': 'Sin asimetría o asimetría leve'}
        ]
    },
    'variedad_piernas_marcha': {
        'title': 'Variedad en movimientos de piernas mientras camina independientemente',
        'section': 'standing',
        'number': 60,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_piernas_marcha': {
        'title': 'Adaptabilidad de movimientos de piernas mientras camina independientemente',
        'section': 'standing',
        'number': 61,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'marcha_talon_punta': {
        'title': 'Marcha talón-punta mientras camina independientemente',
        'section': 'standing',
        'number': 62,
        'type': 'P',  # Performance
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Sin marcha talón-punta o solo ocasionalmente'},
            {'value': 2, 'text': 'Predominantemente marcha talón-punta'}
        ]
    },
    'variedad_pie_marcha': {
        'title': 'Variedad en movimientos del pie mientras camina independientemente',
        'section': 'standing',
        'number': 63,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_pie_marcha': {
        'title': 'Adaptabilidad de movimientos del pie mientras camina independientemente',
        'section': 'standing',
        'number': 64,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'No puede caminar independientemente'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'fluidez_marcha': {
        'title': 'Fluidez de movimientos mientras camina independientemente',
        'section': 'standing',
        'number': 65,
        'type': 'F',  # Fluency
        'options': [
            {'value': 1, 'text': 'No fluido: rígido, brusco, flácido/lento, otro'},
            {'value': 2, 'text': 'La mayoría de movimientos fluidos'}
        ]
    },
    'alcance_manipulacion_sedestacion': {
        'title': 'Alcance, agarre y manipulación de objetos',
        'section': 'manipulation',
        'number': 66,
        'type': 'P',  # Performance
        'options': [
            {'value': 1, 'text': 'No intenta alcanzar, no muestra movimientos de intento'},
            {'value': 2, 'text': 'No alcanza, pero muestra intentos de movimiento'},
            {'value': 3, 'text': 'Intenta alcanzar el objeto pero no lo agarra'},
            {'value': 4, 'text': 'Alcanza, agarra y sostiene el objeto, pero no lo manipula'},
            {'value': 5, 'text': 'Alcanza, sostiene y manipula 1 objeto'},
            {'value': 6, 'text': 'Alcanza, sostiene y manipula 2 objetos'},
            {'value': 7, 'text': 'Alcanza y sostiene ≥3 objetos'}
        ]
    },
    'asimetria_alcance_sedestacion': {
        'title': 'Alcance, agarre y manipulación: presencia de asimetría',
        'section': 'manipulation',
        'number': 67,
        'type': 'S',  # Symmetry
        'options': [
            {'value': 0, 'text': 'No muestra movimientos de alcance o intento'},
            {'value': 1, 'text': 'Asimetría marcada, lado derecho/izquierdo peor'},
            {'value': 2, 'text': 'Asimetría moderada, lado derecho/izquierdo peor'},
            {'value': 3, 'text': 'Sin asimetría o asimetría leve'}
        ]
    },
    'variedad_alcance_sedestacion': {
        'title': 'Variedad en movimientos de alcance de los brazos',
        'section': 'manipulation',
        'number': 68,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'Sin movimientos de alcance'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_alcance_sedestacion': {
        'title': 'Adaptabilidad de movimientos de alcance',
        'section': 'manipulation',
        'number': 69,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'Sin movimientos de alcance'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'tipo_agarre': {
        'title': 'Tipo de agarre durante sedestación',
        'section': 'manipulation',
        'number': 70,
        'type': 'P',  # Performance
        'options': [
            {'value': 0, 'text': 'No agarra el objeto'},
            {'value': 1, 'text': 'Agarre palmar'},
            {'value': 2, 'text': 'Agarre radio-palmar o en tijera'},
            {'value': 3, 'text': 'Pinza inferior'},
            {'value': 4, 'text': 'Pinza'}
        ]
    },
    'variedad_mano_sedestacion': {
        'title': 'Variedad en movimientos de la mano durante alcance, agarre y manipulación',
        'section': 'manipulation',
        'number': 71,
        'type': 'V',  # Variation
        'options': [
            {'value': 0, 'text': 'Sin movimientos de alcance'},
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_mano_sedestacion': {
        'title': 'Adaptabilidad de movimientos de la mano durante alcance, agarre y manipulación',
        'section': 'manipulation',
        'number': 72,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 0, 'text': 'Sin movimientos de alcance'},
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'temblor_alcance_sedestacion': {
        'title': 'Temblor durante intentos de alcance',
        'section': 'manipulation',
        'number': 73,
        'type': 'F',  # Fluency
        'options': [
            {'value': 0, 'text': 'No muestra movimientos de alcance o intento'},
            {'value': 1, 'text': 'Temblor frecuente'},
            {'value': 2, 'text': 'Sin temblor o temblor ocasional'}
        ]
    },
    'fluidez_alcance_sedestacion': {
        'title': 'Fluidez de movimientos durante intentos de alcance',
        'section': 'manipulation',
        'number': 74,
        'type': 'F',  # Fluency
        'options': [
            {'value': 0, 'text': 'No muestra movimientos de alcance o intento'},
            {'value': 1, 'text': 'No fluido: rígido, brusco, flácido/lento, otro'},
            {'value': 2, 'text': 'La mayoría de movimientos fluidos'}
        ]
    },
    'variedad_expresion_facial': {
        'title': 'Variedad en expresión facial',
        'section': 'general',
        'number': 75,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Variedad insuficiente'},
            {'value': 2, 'text': 'Variedad suficiente'}
        ]
    },
    'adaptabilidad_expresion_facial': {
        'title': 'Adaptabilidad de expresión facial',
        'section': 'general',
        'number': 76,
        'type': 'A',  # Adaptability
        'options': [
            {'value': 1, 'text': 'Sin capacidad de adaptar el movimiento'},
            {'value': 2, 'text': 'Con capacidad de adaptar el movimiento'}
        ]
    },
    'babeo': {
        'title': 'Babeo',
        'section': 'general',
        'number': 77,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Babeo marcado'},
            {'value': 2, 'text': 'Sin babeo o babeo escaso'}
        ]
    },
    'protrusion_lengua': {
        'title': 'Presencia de protrusión estereotipada de lengua',
        'section': 'general',
        'number': 78,
        'type': 'V',  # Variation
        'options': [
            {'value': 1, 'text': 'Sí'},
            {'value': 2, 'text': 'No'}
        ]
    },
    'temblor_general': {
        'title': 'Temblor',
        'section': 'general',
        'number': 79,
        'type': 'F',  # Fluency
        'options': [
            {'value': 1, 'text': 'Frecuentemente presente'},
            {'value': 2, 'text': 'No presente o presente ocasionalmente'}
        ]
    },
    'fluidez_comportamiento_motor': {
        'title': 'Fluidez del comportamiento motor',
        'section': 'general',
        'number': 80,
        'type': 'F',  # Fluency
        'options': [
            {'value': 1, 'text': 'No fluido: rígido, brusco, flácido/lento, otro'},
            {'value': 2, 'text': 'Fluido'}
        ]
    }
}

# Configuración de observaciones adicionales
ADDITIONAL_OBSERVATIONS = {
    'cantidad_movimientos': {
        'title': 'Cantidad de movimientos',
        'options': ['+', '++', '+++']
    },
    'estado_conductual': {
        'title': 'Estado conductual',
        'type': 'text'
    },
    'estado_salud': {
        'title': 'Estado de salud',
        'type': 'textarea'
    },
    'otras_observaciones': {
        'title': 'Otras observaciones',
        'type': 'textarea'
    }
}

# Rangos de edad y percentiles para interpretación
AGE_RANGES = {
    '32-34': {  # Semanas postmenstruales
        'p5': 20,
        'p16': 30,
        'p25': 35,
        'p50': 45,
        'p75': 55,
        'p95': 65
    },
    '35-37': {
        'p5': 25,
        'p16': 35,
        'p25': 40,
        'p50': 50,
        'p75': 60,
        'p95': 70
    },
    '38-40': {
        'p5': 30,
        'p16': 40,
        'p25': 45,
        'p50': 55,
        'p75': 65,
        'p95': 75
    },
    '41-43': {  # 1-3 semanas postérmino
        'p5': 35,
        'p16': 45,
        'p25': 50,
        'p50': 60,
        'p75': 70,
        'p95': 80
    },
    '44-47': {  # 4-7 semanas postérmino
        'p5': 40,
        'p16': 50,
        'p25': 55,
        'p50': 65,
        'p75': 75,
        'p95': 85
    },
    '48-51': {  # 8-11 semanas postérmino
        'p5': 45,
        'p16': 55,
        'p25': 60,
        'p50': 70,
        'p75': 80,
        'p95': 90
    },
    '52-55': {  # 12-15 semanas postérmino
        'p5': 50,
        'p16': 60,
        'p25': 65,
        'p50': 75,
        'p75': 85,
        'p95': 95
    },
    '56-64': {  # 16 semanas postérmino
        'p5': 55,
        'p16': 65,
        'p25': 70,
        'p50': 80,
        'p75': 90,
        'p95': 100
    }
}

# Mensajes de interpretación basados en percentiles
INTERPRETATION_MESSAGES = {
    'below_p5': 'Puntuación por debajo del percentil 5. Se recomienda evaluación detallada e intervención temprana.',
    'p5_p16': 'Puntuación entre percentil 5-16. Se recomienda seguimiento cercano.',
    'p16_p25': 'Puntuación entre percentil 16-25. Se recomienda monitorización.',
    'p25_p75': 'Puntuación entre percentil 25-75. Desarrollo dentro de rangos típicos.',
    'above_p75': 'Puntuación por encima del percentil 75. Desarrollo avanzado.'
}

# Valores máximos y mínimos para validación
VALIDATION_RANGES = {
    'age_weeks': {
        'min': 32,  # 32 semanas postmenstruales
        'max': 64   # 16 semanas postérmino
    },
    'total_score': {
        'min': 0,
        'max': 142  # Puntuación máxima teórica
    }
}

# Secciones del test para organización y cálculo de subtotales
TEST_SECTIONS = {
    'supine': {
        'start': 1,
        'end': 21,
        'title': 'Posición Boca Arriba (Decúbito Supino)'
    },
    'prone': {
        'start': 22,
        'end': 33,
        'title': 'Posición Boca Abajo (Decúbito Prono)'
    },
    'sitting': {
        'start': 34,
        'end': 46,
        'title': 'Posición Sentada (Sedestación)'
    },
    'standing': {
        'start': 47,
        'end': 65,
        'title': 'Posición de Pie (Bipedestación) y Marcha'
    },
    'manipulation': {
        'start': 66,
        'end': 74,
        'title': 'Alcance, agarre y manipulación de objetos durante sedestación'
    },
    'general': {
        'start': 75,
        'end': 80,
        'title': 'General: Ítems observados durante la evaluación'
    }
}

# Ponderaciones para el cálculo de la puntuación total
SECTION_WEIGHTS = {
    'supine': 1.0,
    'prone': 1.0,
    'sitting': 1.0,
    'standing': 1.0,
    'manipulation': 1.0,
    'general': 1.0
}

# Items que son observados durante la evaluación
OBSERVED_ITEMS = {
    'control_cabeza',
    'variedad_movimientos_cabeza',
    'adaptabilidad_movimientos_cabeza',
    'posicion_cabeza_lado',
    'rtca_presencia',
    'hiperextension_presencia',
    'manipulacion_manos',
    'variedad_movimientos_brazos',
    'variedad_movimientos_dedos',
    'basculacion_pelvis',
    'variedad_movimientos_piernas',
    'variedad_movimientos_dedos_pie',
    'giro_supino_prono',
    'alcance_manipulacion',
    'asimetria_alcance_supino',
    'variedad_alcance_supino',
    'adaptabilidad_alcance_supino',
    'variedad_mano_alcance_supino',
    'adaptabilidad_mano_supino',
    'temblor_alcance_supino',
    'fluidez_movimiento_supino',
    'elevacion_cabeza_prono',
    'posicion_cabeza_prono',
    'variedad_movimientos_cabeza_prono',
    'adaptabilidad_movimientos_cabeza_prono',
    'capacidad_funcional_hombros',
    'capacidad_funcional_brazos',
    'asimetria_postura_prono',
    'progresion_prono',
    'variedad_pregateo',
    'giro_prono_supino',
    'variedad_gateo',
    'adaptabilidad_gateo',
    'control_cabeza_sedestacion',
    'posicion_cabeza_sedestacion',
    'capacidad_sentarse',
    'postura_tronco_sedestacion',
    'asimetria_tronco_piernas',
    'asimetria_extremidades_superiores',
    'uso_brazos',
    'variedad_sedestacion',
    'adaptabilidad_sedestacion',
    'pasar_sentado',
    'variedad_sentarse',
    'adaptabilidad_sentarse',
    'desplazamiento_sentado',
    'capacidad_bipedestacion',
    'ponerse_pie',
    'variedad_ponerse_pie',
    'adaptabilidad_ponerse_pie',
    'marcha',
    'equilibrio_marcha',
    'postura_brazos_marcha',
    'asimetria_extremidades_superiores_marcha',
    'variedad_brazos_marcha',
    'adaptabilidad_brazos_marcha',
    'variedad_tronco_marcha',
    'adaptabilidad_tronco_marcha',
    'asimetria_piernas_marcha',
    'variedad_piernas_marcha',
    'adaptabilidad_piernas_marcha',
    'marcha_talon_punta',
    'variedad_pie_marcha',
    'adaptabilidad_pie_marcha',
    'fluidez_marcha',
    'alcance_manipulacion_sedestacion',
    'asimetria_alcance_sedestacion',
    'variedad_alcance_sedestacion',
    'adaptabilidad_alcance_sedestacion',
    'tipo_agarre',
    'variedad_mano_sedestacion',
    'adaptabilidad_mano_sedestacion',
    'temblor_alcance_sedestacion',
    'fluidez_alcance_sedestacion',
    'variedad_expresion_facial',
    'adaptabilidad_expresion_facial',
    'babeo',
    'protrusion_lengua',
    'temblor_general',
    'fluidez_comportamiento_motor'
}
# Añadir después de OBSERVED_ITEMS

# Items que requieren provocación específica durante la evaluación
PROVOKED_ITEMS = {
    'adaptabilidad_movimientos_cabeza',
    'adaptabilidad_alcance_supino',
    'adaptabilidad_mano_supino',
    'adaptabilidad_movimientos_cabeza_prono',
    'adaptabilidad_gateo',
    'adaptabilidad_sedestacion',
    'adaptabilidad_sentarse',
    'adaptabilidad_ponerse_pie',
    'adaptabilidad_brazos_marcha',
    'adaptabilidad_tronco_marcha',
    'adaptabilidad_piernas_marcha',
    'adaptabilidad_pie_marcha',
    'adaptabilidad_alcance_sedestacion',
    'adaptabilidad_mano_sedestacion',
    'adaptabilidad_expresion_facial'
}