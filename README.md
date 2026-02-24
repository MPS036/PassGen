🔐 Password Generator (PySide6)

A desktop password generator built with **PySide6 (Qt)**.

The app generates passwords based on selected character groups and shows:
(i) Entropy (bits) estimation;
(ii) Strength level based on entropy thresholds;
(iii) Copy-to-clipboard and password visibility toggle.

✨ Features:
(i) Secure password generation using Python `secrets`;
(ii) Configurable character sets (lower/upper/digits/special);
(iii) Adjustable length (slider + spinbox);
(iv) Entropy and strength indicators;
(v) Copy button + show/hide password.

🛠 Requirements:
(i) Python 3.x;
(ii) PySide6.

📦 Packaging (optional)

The application can be bundled into a standalone executable using tools like Nuitka or PyInstaller.
Example (Nuitka):

```bash
nuitka --onefile --follow-imports --enable-plugin=pyside6 app.py
