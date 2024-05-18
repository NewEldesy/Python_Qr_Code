# Importation des librairies
import sys
import cv2
import qrcode
import datetime
# Importation des options de PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui

class MyGUI(QMainWindow):

    def __init__(self):
        # Initialise la classe parente QMainWindow
        super(MyGUI, self).__init__()
        # Charge l'interface utilisateur à partir du fichier UI spécifié et la lie à cette instance de classe
        uic.loadUi("qr_code_UI.ui", self)
        # Affiche la fenêtre principale de l'application
        self.show()

        self.current_file = ""
        # Connecte l'action de charger une image à la méthode load_image
        self.actionLoad.triggered.connect(self.load_image)
        # Connecte l'action de sauvegarder une image à la méthode save_image
        self.actionSave.triggered.connect(self.save_image)
        # Connecte l'action de quitter l'application à la méthode exit
        self.actionQuitter.triggered.connect(self.exit)
        # Connecte l'action de rafraîchir les champs de texte à la méthode clear_fields
        self.actionActualiser.triggered.connect(self.clear_fields)
        # Connecte le clic sur le premier bouton à la méthode generate_code
        self.btn1.clicked.connect(self.generate_code)
        # Connecte le clic sur le deuxième bouton à la méthode read_code
        self.btn2.clicked.connect(self.read_code)

    def load_image(self):
        # Crée une boîte de dialogue de sélection de fichier avec les options par défaut
        options = QFileDialog.Options()
        # Ouvre une boîte de dialogue pour sélectionner un fichier et récupère le nom du fichier sélectionné
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)",
                                                  options=options)
        
        # Vérifie si un fichier a été sélectionné
        if filename != "":
            # Met à jour le chemin du fichier courant avec le fichier sélectionné
            self.current_file = filename
            # Charge l'image sélectionnée dans un pixmap
            pixmap = QtGui.QPixmap(self.current_file)
            # Redimensionne le pixmap pour l'affichage dans une taille de 300x300 pixels
            pixmap = pixmap.scaled(300, 300)
            # Configure le pixmap pour être mis à l'échelle selon le contenu de l'étiquette
            self.label.setScaledContents(True)
            # Affiche le pixmap dans l'étiquette
            self.label.setPixmap(pixmap)

    def save_image(self):
        # Crée une boîte de dialogue de sauvegarde de fichier avec les options par défaut
        options = QFileDialog.Options()
        # Ouvre une boîte de dialogue pour sélectionner le chemin et le nom du fichier de sauvegarde
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "PNG (*.PNG)",
                                                  options=options)
        
        # Vérifie si un nom de fichier a été spécifié pour la sauvegarde
        if filename != "":
            # Récupère le pixmap de l'étiquette contenant l'image à sauvegarder
            img = self.label.pixmap()
            # Sauvegarde le pixmap dans le fichier spécifié au format PNG
            img.save(filename, "PNG")

    def generate_code(self):
        # Crée un objet QRCode avec les paramètres spécifiés
        qr = qrcode.QRCode(version=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=20,
                           border=2)

        # Ajoute les données du texte de l'éditeur de texte au QRCode
        qr.add_data(self.textEdit.toPlainText())
        # Génère le QR code
        qr.make(fit=True)

        # Obtient la date et l'heure actuelles et les formate en chaîne de caractères
        current_datetime = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        # Construit le nom de fichier pour le QR code avec la date et l'heure actuelles
        filename = f"qrcode_{current_datetime}.png"

        # Génère une image du QR code avec les données fournies, un remplissage noir et un fond blanc
        img = qr.make_image(fill_color="black", back_color="white")
        # Enregistre l'image dans le fichier spécifié
        img.save(filename)
        # Charge l'image du QR code dans un pixmap
        pixmap = QtGui.QPixmap(filename)
        # Redimensionne le pixmap pour l'affichage dans une taille de 300x300 pixels
        pixmap = pixmap.scaled(300, 300)
        # Configure le pixmap pour être mis à l'échelle selon le contenu de l'étiquette
        self.label.setScaledContents(True)
        # Affiche le pixmap dans l'étiquette
        self.label.setPixmap(pixmap)


    def read_code(self):
        # Charge l'image du fichier actuellement sélectionné
        img = cv2.imread(self.current_file)
        # Initialise un détecteur de QR code
        detector = cv2.QRCodeDetector()
        # Utilise le détecteur pour extraire les données du QR code à partir de l'image
        data, _, _ = detector.detectAndDecode(img)
        # Affiche les données extraites dans l'éditeur de texte
        self.textEdit.setText(data)

    def clear_fields(self):
        # Efface le contenu de l'éditeur de texte
        self.textEdit.clear()
        # Efface le contenu de la zone ou se trouve le QR code (label)
        self.label.clear()
    
    def exit(self):
        # Quitte l'application
        QApplication.quit()

def main():
    # Crée une instance de QApplication pour gérer l'application
    app = QApplication(sys.argv)
    # Crée une instance de la classe MyGUI, qui représente la fenêtre principale de l'application
    window = MyGUI()
    # Lance l'exécution de l'application
    app.exec_()

# Point d'entrée de l'application
if __name__ == "__main__":
    main()