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

    def create_statistics_table(self):
        # Este método crea la tabla 'estadisticas' en la base de datos.
        create_table_query = """
        CREATE TABLE IF NOT EXISTS estadisticas (
            ID_results INT AUTO_INCREMENT PRIMARY KEY,
            ID_ex INT,
            ID_student INT,
            student_performance VARCHAR(255),
            FOREIGN KEY (ID_ex) REFERENCES exams(ID),
            FOREIGN KEY (ID_student) REFERENCES students(ID)
        )
        """
        self.cursor.execute(create_table_query)
        self.db.commit()

    def save_student_performance(self, exam_id, student_id, performance):
        # Este método guarda el rendimiento del estudiante en la tabla 'estadisticas'.
        insert_query = """
        INSERT INTO estadisticas (ID_ex, ID_student, student_performance)
        VALUES (%s, %s, %s)
        """
        values = (exam_id, student_id, performance)
        self.cursor.execute(insert_query, values)
        self.db.commit()

    def get_student_performance(self, exam_id, student_id):
        # Este método obtiene el rendimiento del estudiante desde la tabla 'estadisticas'.
        select_query = """
        SELECT student_performance FROM estadisticas
        WHERE ID_ex = %s AND ID_student = %s
        """
        values = (exam_id, student_id)
        self.cursor.execute(select_query, values)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
