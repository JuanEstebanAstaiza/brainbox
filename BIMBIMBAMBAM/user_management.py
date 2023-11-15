import hashlib
import mysql.connector


class UserManager:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="brainbox"
        )
        self.cursor = self.db.cursor(buffered=True)

    def register_user(self, username, pwd, type):
        # Comprobar si el usuario ya existe en la base de datos
        if self.user_exists(username):
            print("El usuario ya existe. No se puede registrar.")
            return

        # Generar un nuevo hash de contraseña
        hashed_password = self._hash_password(pwd)

        # Insertar el nuevo usuario en la base de datos
        query = "INSERT INTO users (username, pwd,type) VALUES (%s, %s,%s)"
        self.cursor.execute(query, (username, hashed_password, type))
        self.db.commit()
        print("Usuario registrado con éxito")

    def login_user(self, username, pwd):
        # Verificar si el usuario existe en la base de datos
        query = "SELECT pwd FROM users WHERE username = %s"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()

        if result:
            stored_password = result[0]
            if self._verify_password(pwd, stored_password):
                print("Inicio de sesión exitoso")
                return True
        print("Inicio de sesión fallido")
        return False

    def change_password(self, username, new_password):
        if self.user_exists(username):
            # Generar un nuevo hash de contraseña para la nueva contraseña
            hashed_password = self._hash_password(new_password)

            # Actualizar la contraseña en la base de datos
            query = "UPDATE users SET pwd= %s WHERE username = %s"
            self.cursor.execute(query, (hashed_password, username))
            self.db.commit()
            print("Contraseña actualizada con éxito")

        #def delete_user(self, username):


    def user_exists(self, username):
        # Comprobar si un usuario con el nombre de usuario especificado existe en la base de datos
        query = "SELECT username FROM users WHERE username = %s"
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone() is not None

    def _hash_password(self, password):
        # Función para generar un hash de contraseña
        salt = "un_salt_aleatorio"  # Debes usar un valor único y aleatorio como salt
        password_with_salt = password + salt
        hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()
        return hashed_password

    def _verify_password(self, password, stored_password):
        # Función para verificar una contraseña con su hash almacenado
        return self._hash_password(password) == stored_password

    def insertStudentData(self, ID_estudiante, student_name, student_lastname, grado, username):
        if self.student_exists(username):
            print("El estudiante ya existe. No se puede insertar.")
            return

        query = "INSERT INTO estudiante (ID_estudiante, student_name, student_lastname, grado, username) VALUES (%s, %s, %s, %s, %s)"
        values = (ID_estudiante, student_name, student_lastname, grado, username)

        try:
            self.cursor.execute(query, values)
            self.db.commit()
            print("Estudiante insertado exitosamente.")
        except Exception as e:
            print(f"Error al insertar estudiante: {e}")
            self.db.rollback()

    #def insertGradeData(self, gradeCode, gradeName):
        #if self.grade_exists(gradeCode):
            #print("El grado ya existe. No se puede insertar.")
            #return

        #query = "INSERT INTO grados (gradoCode, GradoName) VALUES (%s, %s)"
        #values = (gradeCode, gradeName)

        #try:
            #self.cursor.execute(query, values)
            #self.db.commit()
            #print("Grado insertado exitosamente.")
        #except Exception as e:
            #print(f"Error al insertar grado: {e}")
            #self.db.rollback()

    def student_exists(self, username):
        query = "SELECT COUNT(*) FROM estudiante WHERE username = %s"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()[0]
        return result > 0

    #def grade_exists(self, gradeCode):
        #query = "SELECT COUNT(*) FROM grados WHERE gradoCode = %s"
        #self.cursor.execute(query, (gradeCode,))
        #result = self.cursor.fetchone()[0]
        #return result > 0

    def delete_user(self, username_insert):
        # Eliminar el usuario de la base de datos
        query = "DELETE FROM users WHERE username = %s"
        self.cursor.execute(query, (username_insert,))
        self.db.commit()
        print(f"Usuario {username_insert} eliminado con éxito")

    def delete_student(self, username_insert):
        query = "DELETE FROM estudiante WHERE username = %s"
        self.cursor.execute(query, (username_insert,))
        self.db.commit()
        print(f"Usuario {username_insert} eliminado con éxito")

    def delete_professor(self, username_insert):

        query = "DELETE FROM docentes WHERE username = %s"
        self.cursor.execute(query, (username_insert,))
        self.db.commit()
        print(f"Usuario {username_insert} eliminado con éxito")


    def professor_data(self, name, id, subject, teachingID,professor_username):
        if self.professor_exists(id):
            print("El profesor ya existe. No se puede insertar.")
            return

        query = "INSERT INTO docentes (prof_name, prof_id, subject_id, teaching_id,username) VALUES (%s, %s, %s, %s,%s)"
        values = (name, id, subject, teachingID,professor_username)

        try:
            self.cursor.execute(query, values)
            self.db.commit()
            print("Profesor insertado exitosamente.")
        except Exception as e:
            print(f"Error al insertar profesor: {e}")
            self.db.rollback()

    def professor_exists(self, id):
        query = "SELECT COUNT(*) FROM docentes WHERE prof_id = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()[0]
        return result > 0

    def insert_subject_data(self, subject_id):

        query = "INSERT INTO subjects (subject_id) VALUE (%s)"
        self.cursor.execute(query, (subject_id,))
        self.db.commit()
        print("Subject inserted successfully.")


