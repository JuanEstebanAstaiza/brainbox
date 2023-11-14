
from user_management import UserManager
from QuizManager import QuizManager

class ExamTaking:
    def __init__(self, user_manager, quiz_manager):
        self.user_manager = user_manager
        self.quiz_manager = quiz_manager

    def take_exam(self, student_id, ID_EX):
        # Verificar si el estudiante existe
        student = self.user_manager.get_user_by_id(student_id)
        if not student:
            print("El estudiante no existe.")
            return

        # Verificar si el examen existe
        exam = self.quiz_manager.get_exam_by_id(ID_EX)
        if not exam:
            print("El examen no existe.")
            return

        # Obtener preguntas del examen
        questions = self.quiz_manager.get_exam_questions(ID_EX)

        if not questions:
            print("El examen no tiene preguntas.")
            return

        # Tomar el examen
        answers = {}
        for question in questions:
            print(f"Pregunta: {question['question']}")
            answer = input("Tu respuesta: ")
            answers[question['question_id']] = answer

        # Evaluar el rendimiento del estudiante
        score = self.quiz_manager.evaluate_exam(ID_EX, answers)

        # Guardar los resultados en la base de datos
        self.quiz_manager.save_exam_results(student_id, ID_EX, score)

        print(f"¡Examen completado! Tu puntuación es: {score}")


    def view_exam_results(self, student_id, ID_EX):
        # Verificar si el estudiante existe
        student = self.user_manager.get_user_by_id(student_id)
        if not student:
            print("El estudiante no existe.")
            return

        # Verificar si el examen existe
        exam = self.quiz_manager.get_exam_by_id(ID_EX)
        if not exam:
            print("El examen no existe.")
            return

        # Obtener los resultados del examen para el estudiante
        results = self.quiz_manager.get_student_exam_results(student_id, ID_EX)

        if results is not None:
            print(f"Resultados del estudiante {student_id} en el examen {ID_EX}: {results}")
        else:
            print(f"El estudiante {student_id} no ha tomado el examen {ID_EX}.")
