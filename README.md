# 🔐 Password Generator (PySide6)

A desktop password generator built with **PySide6 (Qt)**.

The app generates passwords based on selected character groups and shows:
- Entropy (bits) estimation;
- Strength level based on entropy thresholds;
-) Copy-to-clipboard and password visibility toggle.

## ✨ Features:
- Secure password generation using Python `secrets`;
- Configurable character sets (lower/upper/digits/special);
- Adjustable length (slider + spinbox);
- Entropy and strength indicators;
- Copy button + show/hide password.

## 🛠 Requirements:
- Python 3.x;
- PySide6.

## 📦 Packaging (optional)

- The application can be bundled into a standalone executable using tools like Nuitka or PyInstaller.
Example (Nuitka):

```bash
nuitka --onefile --follow-imports --enable-plugin=pyside6 app.py
