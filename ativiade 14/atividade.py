import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout

class MainJanela(QMainWindow):
    def _init_(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Janela')
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel('Mensagem e Nome aqui:', self)
        self.label.setGeometry(20, 20, 200, 30)

        self.show()

    def updateMensagem(self, mensagem):
        self.label.setText(mensagem)

class JanelaEntrada(QWidget):
    def _init_(self, main_janela):
        super().__init__()

        self.main_janela = main_janela

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Janela de Entrada')
        self.setGeometry(200, 200, 300, 150)

        self.label_nome = QLabel('Nome:', self)
        self.label_mensagem = QLabel('Mensagem:', self)
        self.nome_input = QLineEdit(self)
        self.mensagem_input = QLineEdit(self)
        self.enviar_button = QPushButton('Enviar', self)

        layout = QVBoxLayout()
        layout.addWidget(self.label_nome)
        layout.addWidget(self.nome_input)
        layout.addWidget(self.label_mensagem)
        layout.addWidget(self.mensagem_input)
        layout.addWidget(self.enviar_button)
        self.setLayout(layout)

        self.enviar_button.clicked.connect(self.enviarMensagem)

        self.show()

    def enviarMensagem(self):
        nome = self.nome_input.text()
        mensagem = self.mensagem_input.text()
        mensagem_completa = f'{nome}: {mensagem}'
        self.main_janela.updateMensagem(mensagem_completa)
        self.close()

def main():
    app = QApplication(sys.argv)
    main_janela = MainJanela()
    janela_entrada = JanelaEntrada(main_janela)
    sys.exit(app.exec_())

if _name_ == '__main__':
    main()