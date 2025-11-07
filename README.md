# Codus 🚀

Codus — Code with Focus. A lightweight Python IDE designed for productivity.

Write, run, and test code efficiently in a clean, distraction-free environment.

![License](https://img.shields.io/github/license/VxidDev/Codus)
![GitHub stars](https://img.shields.io/github/stars/VxidDev/Codus?style=social)
![GitHub forks](https://img.shields.io/github/forks/VxidDev/Codus?style=social)
![GitHub issues](https://img.shields.io/github/issues/VxidDev/Codus)
![GitHub pull requests](https://img.shields.io/github/issues-pr/VxidDev/Codus)
![GitHub last commit](https://img.shields.io/github/last-commit/VxidDev/Codus)

<img src="https://img.shields.io/badge/language-Python-blue" alt="Python badge">
<img src="https://img.shields.io/badge/platform-Desktop-lightgrey" alt="Desktop badge">
<img src="https://img.shields.io/badge/ui-Customizable-yellowgreen" alt="Customizable badge">

## 📋 Table of Contents

- [About](#about)
- [Testing](#testing)
- [Deployment](#deployment)
- [FAQ](#faq)

## About

Codus is a lightweight, customizable Python IDE designed to enhance developer productivity. It addresses the common problem of cluttered and resource-intensive IDEs that can distract developers from their core task: writing code. Codus offers a clean, distraction-free environment with essential features like syntax highlighting, an integrated terminal, and quick-run capabilities.

This IDE is targeted towards Python developers who value simplicity, speed, and customization. Whether you're a beginner learning Python or an experienced developer working on complex projects, Codus provides a focused coding experience. The key technologies used in Codus include Python for the core logic and PyQt for the user interface.

Codus distinguishes itself through its lightweight design, focus on productivity, and extensive customization options. It aims to provide a coding environment tailored to individual preferences, allowing developers to maximize their efficiency and enjoyment.

## ✨ Features

- 🎯 **Syntax Highlighting**: Supports Python syntax highlighting for improved code readability.
- ⚡ **Quick-Run Capability**: Allows users to quickly execute Python scripts directly from the IDE.
- 💻 **Integrated Terminal**: Provides a built-in terminal for executing commands and managing projects.
- 🎨 **Customizable Interface**: Offers options to customize the appearance and behavior of the IDE.
- 🛠️ **Extensible**: Designed to be easily extended with plugins or custom modules.
- 📱 **Cross-Platform**: Compatible with Windows, macOS, and Linux.

### Screenshots
![Main Interface](sc.png)
*Main application interface showing the code editor and integrated terminal*

## 🚀 Quick Start

Clone and run in 3 steps:

```bash
git clone https://github.com/VxidDev/Codus.git
cd Codus
python main.py
```

Open the Codus application to start coding.

## 📦 Installation

### Prerequisites
- Python 3.8+
- Git
- PyQt5

### Option 1: From Source

```bash
# Clone repository
git clone https://github.com/VxidDev/Codus.git
cd Codus

# Run the application
python main.py
```

## 💻 Usage

### Basic Usage

```python
# Example Python code
def hello_world():
    print("Hello, Codus!")

hello_world()
```

### Running Scripts

1.  Open a Python file in Codus.
2.  Click the "Run" button or use the keyboard shortcut to execute the script.
3.  The output will be displayed in the integrated terminal.

## ⚙️ Configuration

### Configuration File

Codus supports configuration through a `style.qss` in the Codus's folder.

## 📁 Project Structure

```
Codus/
├── main.py              # Main application entry point           
├── plugins/             # Plugin directory
│   └── ...
├── README.md            # Project documentation
└── LICENSE              # License file
```

## 🤝 Contributing

We welcome contributions!

### Quick Contribution Steps

1.  🍴 Fork the repository
2.  🌟 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  ✅ Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  📤 Push to the branch (`git push origin feature/AmazingFeature`)
5.  🔃 Open a Pull Request

### Development Setup

```bash
# Fork and clone the repo
git clone https://github.com/yourusername/Codus.git

# Create a new branch
git checkout -b feature/your-feature-name

# Make your changes and test
python main.py  # Run the application

# Commit and push
git commit -m "Description of changes"
git push origin feature/your-feature-name
```

### Code Style

-   Follow PEP 8 guidelines.
-   Use descriptive variable names.
-   Write clear and concise comments.

## Testing

To run tests, execute the following command:

```bash
python -m unittest discover tests
```

(Note: Create a `tests` directory and relevant test files)

## Deployment

Codus can be deployed as a standalone application using tools like PyInstaller or cx_Freeze.

```bash
# Example using PyInstaller
pyinstaller --onefile main.py
```

This will create a single executable file that can be distributed to users.

## FAQ

**Q: How do I change the theme?**

A: You can change the theme by editing the `style.qss` file.

**Q: How do I install plugins?**

A: Copy the plugin files to the `plugins` directory. Codus will automatically load them on startup.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### License Summary

-   ✅ Commercial use
-   ✅ Modification
-   ✅ Distribution
-   ✅ Private use
-   ❌ Liability
-   ❌ Warranty

## 💬 Support

-   📧 **Email**: stas050595@gmail.com
-   🐛 **Issues**: [GitHub Issues](https://github.com/VxidDev/Codus/issues)

## 🙏 Acknowledgments

-   🎨 **Design inspiration**: VS Code, Sublime Text
-   📚 **Libraries used**:
    -   PyQt6 - GUI library
