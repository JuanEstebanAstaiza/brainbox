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

    def register_user(self, username, pwd,type):
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

    def delete_user(self, username):
        def delete_user(self, username):
            # Comprobar si el usuario existe en la base de datos
            if not self.user_exists(username):
                print("El usuario no existe. No se puede eliminar.")
                return

            # Eliminar el usuario de la base de datos
            query = "DELETE FROM users WHERE username = %s"
            self.cursor.execute(query, (username,))
            self.db.commit()
            print(f"Usuario {username} eliminado con éxito")

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



