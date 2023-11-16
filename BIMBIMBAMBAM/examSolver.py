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

    def start_exam(self):

            # Obtener preguntas del examen
            preguntas = self.get_exam_questions()

            # Mostrar preguntas al estudiante y obtener respuestas
            respuestas_estudiante = self.take_exam(preguntas)

            # Almacenar respuestas en la base de datos
            self.store_answers(respuestas_estudiante)

            print("Examen completado. Gracias por responder.")

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

    def take_exam(self, preguntas):
        # Mostrar preguntas al estudiante y obtener respuestas
        respuestas_estudiante = {}
        for pregunta in preguntas:
            id_pregunta, texto_pregunta, opciones = pregunta
            print(f"{texto_pregunta}\nOpciones: {opciones}")
            respuesta = input("Tu respuesta: ")
            respuestas_estudiante[id_pregunta] = respuesta

        return respuestas_estudiante

    def store_answers(self, respuestas_estudiante):
        # Almacenar las respuestas del estudiante en la base de datos
        for id_pregunta, respuesta in respuestas_estudiante.items():
            query_insert_respuesta = (
                "INSERT INTO respuesta_estudiante (id_estudiante, id_examen, id_pregunta, respuesta_correcta) "
                "VALUES (%s, %s, %s, %s)"
            )
            self.cursor.execute(query_insert_respuesta, (self.user_id, self.exam_id, id_pregunta, respuesta))

        self.db.commit()
