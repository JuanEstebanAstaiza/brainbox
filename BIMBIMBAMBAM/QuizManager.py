from DatabaseManager import DatabaseManager
class QuizManager:
    def __init__(self, database_manager):
        self.db = database_manager
        # Puedes inyectar una instancia de DatabaseManager para gestionar las operaciones de la base de datos.

    def create_question(self, question_text, options, correct_option):
        # Crea una nueva pregunta y almacénala en la base de datos
        question_id = self.db.insert_question(question_text)
        for option in options:
            self.db.insert_option(question_id, option)
        self.db.set_correct_option(question_id, correct_option)
        return question_id

    def create_exam(self, exam_name, questions):
        # Crea un nuevo examen y asocia preguntas existentes
        exam_id = self.db.insert_exam(exam_name)
        for question_id in questions:
            self.db.associate_question_with_exam(exam_id, question_id)
        return exam_id

    def get_question(self, question_id):
        # Obtiene una pregunta específica por su ID
        return self.db.get_question(question_id)

    def get_exam(self, exam_id):
        # Obtiene un examen específico por su ID
        return self.db.get_exam(exam_id)

    def get_exam_questions(self, exam_id):
        # Obtiene la lista de preguntas asociadas a un examen
        return self.db.get_exam_questions(exam_id)

    def delete_question(self, question_id):
        # Elimina una pregunta específica por su ID
        return self.db.delete_question(question_id)

    def delete_exam(self, exam_id):
        # Elimina un examen específico por su ID
        return self.db.delete_exam(exam_id)

    #def connect_to_database(self, db_host, db_user, db_password, db_database):
     #   pass

