class Admin:
    def __init__(self, user_manager, quiz_manager, console_interface, statistics):
        self.user_manager = user_manager
        self.quiz_manager = quiz_manager
        self.console_interface = console_interface
        self.statistics = statistics

    def view_student_performance(self):
        # Implementa la lógica para ver el rendimiento de los estudiantes.
        student_performance = self.statistics.get_student_performance()
        self.console_interface.display_student_performance(student_performance)


    def manage_users(self):
        while True:
            self.console_interface.print_admin_menu()
            choice = self.console_interface.get_user_choice()

            if choice == "1":
                # Ver el rendimiento de los estudiantes
                self.view_student_performance()
            elif choice == "2":
                # Crear un usuario (por si también los administradores pueden crear usuarios)
                self.user_manager.create_user()
            elif choice == "3":
                # Volver al menú principal
                break

    def run_admin_menu(self):
        # Menú principal de administrador
        while True:
            self.console_interface.print_admin_main_menu()
            choice = self.console_interface.get_user_choice()

            if choice == "1":
                # Gestionar usuarios
                self.manage_users()
            elif choice == "2":
                # Realizar otras tareas administrativas
                pass  # Agrega la lógica necesaria para otras tareas administrativas
            elif choice == "3":
                # Salir del modo administrador
                break

    def login_as_admin(self):
        # Implementa la lógica para iniciar sesión como administrador.
        admin_username = input("Ingrese el nombre de usuario del administrador: ")
        admin_password = input("Ingrese la contraseña del administrador: ")

        # Verifica las credenciales del administrador
        if self.user_manager.login_admin(admin_username, admin_password):
            print("Iniciaste sesión como administrador.")
        else:
            print("Credenciales incorrectas. No se pudo iniciar sesión como administrador.")

    def logout_admin(self):
        # Implementa la lógica para cerrar sesión como administrador.
        self.user_manager.logout_admin()
        print("Cerraste sesión como administrador.")

    def start(self):
        # Implementa la lógica principal para el administrador.
        self.console_interface.print_welcome_admin()
        self.login_as_admin()  # Iniciar sesión como administrador

        if self.user_manager.is_admin_logged_in:
            self.run_admin_menu()  # Ejecutar el menú principal de administrador

        self.logout_admin()  # Cerrar sesión como administrador
