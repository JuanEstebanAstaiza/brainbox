import hashlib
import mysql.connector


class statsController:

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="brainbox"
        )
        self.cursor = self.db.cursor(buffered=True)

        def get_exam_statistics(self, id_examen):
            # Obtener la calificación de todos los estudiantes para un examen específico
            query_calificaciones = (
                "SELECT e.id_estudiante, e.calificacion "
                "FROM estudiante_examen e "
                "WHERE e.id_examen = %s"
            )
            self.cursor.execute(query_calificaciones, (id_examen,))
            calificaciones = self.cursor.fetchall()

            # Calcular el promedio de calificaciones y otros estadísticas si es necesario
            promedio = sum(calificacion[1] for calificacion in calificaciones) / len(
                calificaciones) if calificaciones else 0
            print(f"Promedio de calificaciones: {promedio}")

        def get_question_statistics(self, id_examen, id_pregunta):
            # Obtener el porcentaje de aciertos y errores por pregunta para un examen específico
            query_preguntas = (
                "SELECT p.id_pregunta, COUNT(*) AS total, "
                "SUM(CASE WHEN r.respuesta_correcta = p.correcta THEN 1 ELSE 0 END) AS aciertos "
                "FROM pregunta p "
                "JOIN respuesta_estudiante r ON p.id_pregunta = r.id_pregunta "
                "WHERE r.id_examen = %s AND r.id_pregunta = %s "
                "GROUP BY p.id_pregunta"
            )
            self.cursor.execute(query_preguntas, (id_examen, id_pregunta))
            resultados_preguntas = self.cursor.fetchall()

            for resultado in resultados_preguntas:
                id_pregunta, total, aciertos = resultado
                porcentaje_aciertos = (aciertos / total) * 100 if total > 0 else 0
                porcentaje_errores = 100 - porcentaje_aciertos
                print(f"Pregunta {id_pregunta}:")
                print(f"Porcentaje de aciertos: {porcentaje_aciertos}%")
                print(f"Porcentaje de errores: {porcentaje_errores}%")

        def get_student_results(self, id_examen, id_estudiante):
            # Obtener los resultados del examen por estudiante, mostrando preguntas correctas e incorrectas
            query_resultados = (
                "SELECT e.id_estudiante, e.calificacion, "
                "GROUP_CONCAT(CASE WHEN r.respuesta_correcta = p.correcta THEN p.id_pregunta END) AS preguntas_correctas, "
                "GROUP_CONCAT(CASE WHEN r.respuesta_correcta != p.correcta THEN p.id_pregunta END) AS preguntas_incorrectas "
                "FROM estudiante_examen e "
                "JOIN respuesta_estudiante r ON e.id_estudiante = r.id_estudiante AND e.id_examen = r.id_examen "
                "JOIN pregunta p ON r.id_pregunta = p.id_pregunta "
                "WHERE e.id_examen = %s AND e.id_estudiante = %s "
                "GROUP BY e.id_estudiante"
            )
            self.cursor.execute(query_resultados, (id_examen, id_estudiante))
            resultados_estudiantes = self.cursor.fetchall()

            for resultado in resultados_estudiantes:
                id_estudiante, calificacion, preguntas_correctas, preguntas_incorrectas = resultado
                print(f"Estudiante {id_estudiante}:")
                print(f"Calificación: {calificacion}")
                print(f"Preguntas correctas: {preguntas_correctas}")
                print(f"Preguntas incorrectas: {preguntas_incorrectas}")