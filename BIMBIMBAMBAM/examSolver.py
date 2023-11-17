import mysql.connector


class examSolver:

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="brainbox"
        )
        self.cursor = self.db.cursor(buffered=True)


    #metodo start_exam debe ser creado en misty
    """def start_exam(self):

            # Obtener preguntas del examen
            preguntas = self.get_exam_questions()

            # Mostrar preguntas al estudiante y obtener respuestas
            respuestas_estudiante = self.take_exam(preguntas)

            # Almacenar respuestas en la base de datos
            self.store_answers(respuestas_estudiante)

            print("Examen completado. Gracias por responder.")"""

    def getSustentacionId(self):
        query_preguntas = "SELECT COUNT(*) FROM estudiante_examen"
        self.cursor.execute(query_preguntas)
        count_tuple = self.cursor.fetchall()

        # Extract the count value from the tuple
        count = (count_tuple[0][0] if count_tuple and count_tuple[0] else 0)+1

        return count

    def newSustentacion(self, id_estudiante, id_examen):
        sustentacion_id = self.getSustentacionId()
        query_preguntas = ("INSERT INTO estudiante_examen(sustentacion_id, id_estudiante,id_examen) VALUES (%s,%s,%s)")
        self.cursor.execute(query_preguntas, (sustentacion_id, id_estudiante, id_examen))
        self.db.commit()
        return sustentacion_id

    def get_exam_questions(self, id_examen):
        # Obtener las preguntas del examen desde la base de datos
        query_preguntas = (
            "SELECT p.id_pregunta, p.pregunta as text_pregunta, p.opciones "
            "FROM pregunta p "
            "JOIN examen_pregunta ep ON p.id_pregunta = ep.id_pregunta "
            "WHERE ep.id_examen = %s"
        )
        self.cursor.execute(query_preguntas, (id_examen,))
        preguntas = self.cursor.fetchall()
        return preguntas

    def grade_exam(self, id_sustentacion):
        query = "SELECT id_pregunta FROM respuesta_estudiante WHERE sustentacion_id = %s"
        self.cursor.execute(query, (id_sustentacion,))
        id_preguntas = self.cursor.fetchall()  # Usar fetchall en lugar de fetchone

        count = 0
        tot = 0

        for id_pregunta in id_preguntas:
            # Corregir la llamada a grade_question y sumar count y tot adecuadamente
            if self.grade_question(id_pregunta[0], id_sustentacion):
                count += 1
            tot += 1

        # Verificar para evitar división por cero
        return count / tot if tot > 0 else 0

    def grade_question(self, id_pregunta, id_sustentacion):
        # Obtener las respuestas correctas de la base de datos
        query_respuestas_correctas = (
            "SELECT (r.respuesta_correcta = p.correcta) as correct "
            "FROM respuesta_estudiante r "
            "JOIN pregunta p ON r.id_pregunta = p.id_pregunta "
            "WHERE r.sustentacion_id = %s AND r.id_pregunta= %s"
        )
        self.cursor.execute(query_respuestas_correctas, (id_sustentacion, id_pregunta))
        correcto = self.cursor.fetchone()  # Usar fetchone ya que esperas un solo valor
        return correcto[0] if correcto else False  # Devolver False si no hay respuesta

    def get_exam(self, nombre_examen):

        query_get_exam = "select ID_EX from examen where nombre =%s"
        self.cursor.execute(query_get_exam, (nombre_examen, ))
        id_examen = self.cursor.fetchone()
        return id_examen

    def store_answers(self, respuestas_estudiante, exam_id, user_id, id_pregunta, id_sustentacion):
        # Almacenar las respuestas del estudiante en la base de datos
        query_insert_respuesta = (
            "INSERT INTO respuesta_estudiante (id_estudiante, id_examen, id_pregunta, respuesta_correcta, sustentacion_id) "
            "VALUES (%s, %s, %s, %s, %s)"
        )

        self.cursor.execute(query_insert_respuesta, (user_id, exam_id, id_pregunta, respuestas_estudiante, id_sustentacion))
        self.db.commit()
