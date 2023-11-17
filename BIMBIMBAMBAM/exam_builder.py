import hashlib
import mysql.connector


class exam_builder:

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="brainbox"
        )
        self.cursor = self.db.cursor(buffered=True)

    def create_question(self, id_pregunta, pregunta_text, opciones, correcta, publico, tema, id_banco_preguntas, nombre,
                        descripcion, creator_id):
        # Insertar la pregunta en la tabla pregunta

        query_insert_preg_to_bancopreg = (
            "INSERT INTO bancopreg (banco_id,pregunta,nombre,descripcion,creator_id) values (%s,%s,%s,%s,%s)")
        self.cursor.execute(query_insert_preg_to_bancopreg, (id_banco_preguntas, pregunta_text, nombre,
                                                             descripcion, creator_id))

        query_insert_pregunta = (
            "INSERT INTO pregunta (id_pregunta, pregunta, opciones, correcta, publico, tema, id_bancoPregunta) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        self.cursor.execute(query_insert_pregunta,
                            (id_pregunta, pregunta_text, opciones, correcta, publico, tema, id_banco_preguntas))

        # Insertar la relación en la tabla pregunta_banco_relacion
        query_insert_relacion = "INSERT INTO pregunta_banco_relacion (id_pregunta, id_bancoPreguntas) VALUES (%s, %s)"
        self.cursor.execute(query_insert_relacion, (id_pregunta, id_banco_preguntas))

        # Hacer commit para guardar los cambios en la base de datos
        self.db.commit()

        print(f"Pregunta '{pregunta_text}' creada con éxito.")

    def create_exam(self, id_examen, nombre_examen):
        # Insertar el examen en la tabla examen
        query_insert_examen = "INSERT INTO examen (ID_EX,nombre) VALUES (%s,%s)"
        self.cursor.execute(query_insert_examen, (id_examen, nombre_examen))

        # Seleccionar preguntas para el examen (aquí deberías tener lógica para seleccionar preguntas)
        # En este ejemplo, seleccionamos preguntas de un banco específico
        id_banco_preguntas = 1  # Reemplaza con el ID del banco de preguntas deseado
        num_preguntas = 5
        preguntas = self.get_random_questions(id_banco_preguntas, num_preguntas)

        # Insertar la relación en la tabla examen_pregunta
        query_insert_relacion = "INSERT INTO examen_pregunta (id_examen, id_pregunta) VALUES (%s, %s)"
        for pregunta in preguntas:
            self.cursor.execute(query_insert_relacion, (id_examen, pregunta[0]))

        # Hacer commit para guardar los cambios en la base de datos
        self.db.commit()

        print(f"Examen creado con éxito. ID del examen: {id_examen}")


    def get_random_questions(self, id_banco_preguntas, cantidad):
        query = (
            "SELECT id_pregunta FROM pregunta "
            "WHERE id_bancoPregunta = %s AND publico = true "
         "ORDER BY RAND() "
            "LIMIT %s;"
        )

        self.cursor.execute(query, (id_banco_preguntas, cantidad))
        result = self.cursor.fetchall()
        return result