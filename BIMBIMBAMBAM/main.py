from user_management import UserManager
from QuizManager import QuizManager
from gui import GUI  # Importa la clase GUI que contiene la interfaz gráfica


def main():
    user_manager = UserManager()
    quiz_manager = QuizManager()

    # Inicializa la interfaz gráfica y pasa las instancias de user_manager y quiz_manager
    gui = GUI(user_manager, quiz_manager)
    gui.run()  # Inicia la interfaz gráfica


if __name__ == "__main__":
    main()
