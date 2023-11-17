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

    def take_exam(self, preguntas):
        # Mostrar preguntas al estudiante y obtener respuestas
        respuestas_estudiante = {}
        for pregunta in preguntas:
            id_pregunta, texto_pregunta, opciones = pregunta
            print(f"{texto_pregunta}\nOpciones: {opciones}")
            respuesta = input("Tu respuesta: ")
            respuestas_estudiante[id_pregunta] = respuesta

        return respuestas_estudiante



    def get_exam(self, id_examen):

        query_get_exam = "select nombre from examen where ID_EX =%s"
        self.cursor.execute(query_get_exam,id_examen)
        id_examen = self.cursor.fetchone()
        return id_examen

    def store_answers(self, respuestas_estudiante, exam_id, user_id, id_pregunta):
        # Almacenar las respuestas del estudiante en la base de datos
        query_insert_respuesta = (
            "INSERT INTO respuesta_estudiante (id_estudiante, id_examen, id_pregunta, respuesta_correcta) "
            "VALUES (%s, %s, %s, %s)"
        )

        self.cursor.execute(query_insert_respuesta, (user_id, exam_id, id_pregunta, respuestas_estudiante))
        self.db.commit()
