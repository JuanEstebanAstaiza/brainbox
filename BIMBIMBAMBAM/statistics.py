# statistics.py
import mysql.connector

class Statistics:
    def __init__(self, quiz_manager, host, user, password, database):
        self.quiz_manager = quiz_manager
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor(buffered=True)



    def save_student_performance(self, exam_id, student_id, performance):
        # Este método guarda el rendimiento del estudiante en la tabla 'estadisticas'.
        insert_query = """
        INSERT INTO statistics (ID_ex, ID_student, student_performance)
        VALUES (%s, %s, %s)
        """
        values = (exam_id, student_id, performance)
        self.cursor.execute(insert_query, values)
        self.db.commit()

    def get_student_performance(self, exam_id, student_id):
        # Este método obtiene el rendimiento del estudiante desde la tabla 'estadisticas'.
        select_query = """
        SELECT student_performance FROM statistics
        WHERE ID_ex = %s AND ID_student = %s
        """
        values = (exam_id, student_id)
        self.cursor.execute(select_query, values)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
