from user_management import UserManager
from QuizManager import QuizManager
from interface import ConsoleInterface

def main():
    # Configuración de la base de datos
    db_host = "localhost"
    db_user = "root"
    db_password = "root"
    db_database = "brainbox"

    # Crear instancias de las clases necesarias
    user_manager = UserManager()
    quiz_manager = QuizManager()
    console_interface = ConsoleInterface()

    # Conectar a la base de datos
    quiz_manager.connect_to_database(db_host, db_user, db_password, db_database)

    # Ciclo principal de la aplicación
    while True:
        console_interface.print_menu()
        choice = console_interface.get_user_choice()

        if choice == "1":
            # Menú de gestión de usuarios
            user_management_menu(user_manager, console_interface)

        elif choice == "2":
            # Menú de gestión de preguntas y exámenes
            quiz_management_menu(quiz_manager, console_interface)

        elif choice == "3":
            # Realizar un examen
            take_exam(quiz_manager, console_interface)

        elif choice == "4":
            # Mostrar estadísticas
            show_statistics(quiz_manager, console_interface)

        elif choice == "5":
            # Salir de la aplicación
            break

def user_management_menu(user_manager, console_interface):
    while True:
        console_interface.print_user_management_menu()
        choice = console_interface.get_user_choice()

        if choice == "1":
            # Crear un usuario
            user_manager.create_user()
        elif choice == "2":
            # Iniciar sesión
            user_manager.login_user()
        elif choice == "3":
            # Cambiar contraseña
            user_manager.change_password()
        elif choice == "4":
            # Volver al menú principal
            break

def quiz_management_menu(quiz_manager, console_interface):
    while True:
        console_interface.print_quiz_management_menu()
        choice = console_interface.get_user_choice()

        if choice == "1":
            # Crear una pregunta
            quiz_manager.create_question()
        elif choice == "2":
            # Crear un examen
            quiz_manager.create_exam()
        elif choice == "3":
            # Eliminar pregunta
            quiz_manager.delete_question()
        elif choice == "4":
            # Eliminar examen
            quiz_manager.delete_exam()
        elif choice == "5":
            # Volver al menú principal
            break

def take_exam(quiz_manager, console_interface):
    # Implementa la lógica para que un estudiante tome un examen aquí
    pass

def show_statistics(quiz_manager, console_interface):
    # Implementa la lógica para mostrar estadísticas aquí
    pass

if __name__ == "__main__":
    main()
