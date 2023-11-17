import mysql.connector


class examSolver:

    def __init__(self, user_id, exam_id):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="brainbox"
        )
        self.cursor = self.db.cursor(buffered=True)
        self.user_id=user_id
        self.exam_id=exam_id


    #metodo start_exam debe ser creado en misty
    """def start_exam(self):

            # Obtener preguntas del examen
            preguntas = self.get_exam_questions()

            # Mostrar preguntas al estudiante y obtener respuestas
            respuestas_estudiante = self.take_exam(preguntas)

            # Almacenar respuestas en la base de datos
            self.store_answers(respuestas_estudiante)

            print("Examen completado. Gracias por responder.")"""

    def get_exam_questions(self):
        # Obtener las preguntas del examen desde la base de datos
        query_preguntas = (
            "SELECT id_pregunta, pregunta, opciones "
            "FROM pregunta "
            "WHERE id_bancoPregunta IS NULL OR id_bancoPregunta = 0"  # Preguntas sin banco específico
        )
        self.cursor.execute(query_preguntas)
        preguntas = self.cursor.fetchall()
        return preguntas

    def grade_exam(self, id_examen, id_estudiante, respuestas_estudiante):
        # Obtener las respuestas correctas de la base de datos
        query_respuestas_correctas = (
            "SELECT r.id_pregunta, p.correcta "
            "FROM respuesta_estudiante r "
            "JOIN pregunta p ON r.id_pregunta = p.id_pregunta "
            "WHERE r.id_examen = %s AND r.id_estudiante = %s"
        )
        self.cursor.execute(query_respuestas_correctas, (id_examen, id_estudiante))
        respuestas_correctas = dict(self.cursor.fetchall())

        # Comparar respuestas del estudiante con las respuestas correctas
        calificacion = 0
        preguntas_correctas = []

        for id_pregunta, respuesta_estudiante in respuestas_estudiante.items():
            respuesta_correcta = respuestas_correctas.get(id_pregunta)
            if respuesta_correcta is not None and respuesta_estudiante == respuesta_correcta:
                calificacion += 1
                preguntas_correctas.append(id_pregunta)

        # Guardar la calificación en la tabla estudiante_examen
        query_insert_calificacion = (
            "INSERT INTO estudiante_examen (id_estudiante, id_examen, calificacion) "
            "VALUES (%s, %s, %s) "
            "ON DUPLICATE KEY UPDATE calificacion = %s"
        )
        self.cursor.execute(query_insert_calificacion, (id_estudiante, id_examen, calificacion, calificacion))
        self.db.commit()

        # Retornar la calificación y las preguntas correctas
        return calificacion, preguntas_correctas


    def get_exam(self, nombre_examen):

        query_get_exam = "select ID_EX from examen where nombre =%s"
        self.cursor.execute(query_get_exam,nombre_examen)
        id_examen = self.cursor.fetchone()
        return id_examen

    def store_answers(self, respuestas_estudiante, nombre_examen, user_id, id_pregunta):
        # Almacenar las respuestas del estudiante en la base de datos
        exam_id = self.get_exam(nombre_examen)
        query_insert_respuesta = (
            "INSERT INTO respuesta_estudiante (id_estudiante, id_examen, id_pregunta, respuesta_correcta) "
            "VALUES (%s, %s, %s, %s)"
        )

        self.cursor.execute(query_insert_respuesta, (user_id, exam_id, id_pregunta, respuestas_estudiante))
        self.db.commit()
