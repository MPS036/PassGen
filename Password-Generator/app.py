"""
Password Generator GUI application (PySide6).

Generates passwords from selected character groups and shows:
- Estimated entropy (bits)
- Strength level based on entropy thresholds
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit

import buttons
import password
from ui.ui_main import Ui_MainWindow
import ui.resources

class PasswordGenerator(QMainWindow):
    """
    Main window for the password generator app.
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect_slider_to_spinbox()
        self.set_password()
        self.when_self_edit()

        for btn in buttons.GENERATE_PASSWORD:
            getattr(self.ui, btn).clicked.connect(self.set_password)

        self.ui.btn_visibility.clicked.connect(self.change_visibility)
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)

    def connect_slider_to_spinbox(self) -> None:
        """
        Keep length slider and spinbox synchronized.
        """
        self.ui.slider_length.valueChanged.connect(self.ui.spiner_length.setValue)
        self.ui.spiner_length.valueChanged.connect(self.ui.slider_length.setValue)
        self.ui.spiner_length.valueChanged.connect(self.set_password)

    def when_self_edit(self) -> None:
        """
        Recalculate entropy/strength when the user edits the password manually.
        """
        self.ui.line_password.textEdited.connect(self.set_entropy)
        self.ui.line_password.textEdited.connect(self.set_strength)

    def get_characters(self) -> str:
        """
        Build allowed character set based on selected checkboxes.

        Returns:
            Concatenated string of allowed characters.
        """
        chars = ""
        for btn in buttons.Characters:
            if getattr(self.ui, btn.name).isChecked():
                chars += btn.value
        return chars

    def set_password(self) -> None:
        """
        Generate and set a new password based on UI settings.
        """
        try:
            self.ui.line_password.setText(
                password.create_new(
                    length=self.ui.slider_length.value(),
                    characters=self.get_characters(),
                )
            )
        except ValueError:
            self.ui.line_password.clear()

        self.set_entropy()
        self.set_strength()

    def get_character_number(self) -> int:
        """
        Calculate the size of selected character set.

        Returns:
            Total number of allowed characters.
        """
        total = 0
        for name, size in buttons.CHARACTER_NUMBER.items():
            if getattr(self.ui, name).isChecked():
                total += size
        return total

    def set_entropy(self) -> None:
        """
        Update entropy label based on current password and character set size.
        """
        length = len(self.ui.line_password.text())
        char_num = self.get_character_number()
        self.ui.label_entropy.setText(f"Entropy: {password.get_entropy(length, char_num)} bit")

    def set_strength(self) -> None:
        """
        Update strength label based on entropy thresholds.
        """
        length = len(self.ui.line_password.text())
        char_num = self.get_character_number()
        entropy = password.get_entropy(length, char_num)

        # pick the strongest matching category
        best = max((s for s in password.StrengthToEntropy if entropy >= s.value), default=password.StrengthToEntropy.Pathetic)
        self.ui.label_strength.setText(f"Strength: {best.name}")

    def change_visibility(self) -> None:
        """
        Toggle password field visibility (masked/unmasked).
        """
        if self.ui.btn_visibility.isChecked():
            self.ui.line_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.line_password.setEchoMode(QLineEdit.Password)

    def copy_to_clipboard(self) -> None:
        """
        Copy generated password to the system clipboard.
        """
        QApplication.clipboard().setText(self.ui.line_password.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
