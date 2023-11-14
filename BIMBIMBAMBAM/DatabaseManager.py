import mysql.connector
import hashlib


class DatabaseManager:


#    def getInstance(self):
 #       return self.db

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()


    def create_grade_table(self):
        # Este método crea la tabla 'grados' en la base de datos.
        create_table_query = """
            CREATE TABLE IF NOT EXISTS grados (
                   GradoCode INT(15) AUTO_INCREMENT PRIMARY KEY,
                   GradoName VARCHAR(255)
            )
            """
        self.cursor.execute(create_table_query)
        self.db.commit()

    def create_student_table(self):
        # Este método crea la tabla 'estudiantes' en la base de datos.
        create_table_query = """
        CREATE TABLE IF NOT EXISTS estudiantes (
            ID_student INT(10) AUTO_INCREMENT PRIMARY KEY,
            StudentName VARCHAR(255),
            StudentLastName VARCHAR(255),
            GradeID INT,
            FOREIGN KEY (GradeID) REFERENCES grados(GradoCode)
        )
        """
        self.cursor.execute(create_table_query)
        self.db.commit()



    def create_users_table(self):
        # Crea una tabla de usuarios en la base de datos si no existe
        query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """
        self.cursor.execute(query)
        self.db.commit()
        print("Tabla de usuarios creada exitosamente")

    def insert_user(self, username, password):
        # Inserta un nuevo usuario en la base de datos
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        hashed_password = self._hash_password(password)
        self.cursor.execute(query, (username, hashed_password))
        self.db.commit()

    def update_password(self, username, new_password):
        # Actualiza la contraseña de un usuario en la base de datos
        query = "UPDATE users SET password = %s WHERE username = %s"
        hashed_password = self._hash_password(new_password)
        self.cursor.execute(query, (hashed_password, username))
        self.db.commit()


    def _hash_password(self, password):
        # Función para generar un hash de contraseña
        salt = "un_salt_aleatorio"  # Debes usar un valor único y aleatorio como salt
        password_with_salt = password + salt
        hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()
        return hashed_password
