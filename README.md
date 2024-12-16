# Password Manager

A simple and secure **Password Manager** built with Python and Tkinter. This application helps you generate strong passwords and store them locally for easy access.

---

## Features

- **Password Generator**: Generate random, secure passwords with a mix of letters, numbers, and symbols.
- **Clipboard Copy**: Automatically copies the generated password to the clipboard.
- **Save Passwords**: Store passwords securely in a local file (`data.txt`).
- **User-Friendly GUI**: Intuitive graphical interface built with Tkinter.

---

## Requirements

- Python 3.x
- Required Libraries:
  - `tkinter` (for GUI)
  - `pyperclip` (for clipboard functionality)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-manager
   ```
3. Install the required library:
   ```bash
   pip install pyperclip
   ```
4. Place a `logo.png` file in the project directory for the app logo.

---

## Usage

1. Run the application:
   ```bash
   python password_manager.py
   ```
2. Fill in the `Website` and `Email/Username` fields.
3. Click **Generate Password** to create a secure password.
4. Click **Add** to save the website, username, and password to `data.txt`.

---

## File Structure

```
password-manager/
├── password_manager.py  # Main application script
├── data.txt             # File to store saved passwords (auto-generated)
├── logo.png             # Logo image for the app
└── README.md            # Project documentation
```

---

## Example

![App Screenshot](![Screenshot 2024-12-16 153728](https://github.com/user-attachments/assets/8da47588-a4b7-4ae1-973c-b58dd539b479)
)  



---

## Future Enhancements

- Add encryption for the `data.txt` file for improved security.
- Implement a search functionality to retrieve saved passwords.
- Provide multi-platform support.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Acknowledgments

- Tkinter for the GUI framework.
- Pyperclip for the clipboard integration.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and bug reports.
