from PyQt6.QtCore import QRegularExpression , Qt
from PyQt6.QtGui import QColor, QTextCharFormat, QSyntaxHighlighter , QFontMetrics
from PyQt6.QtWidgets import QApplication, QPlainTextEdit , QWidget , QVBoxLayout , QPushButton , QFileDialog , QHBoxLayout
from QTermWidget import QTermWidget
import sys , subprocess , pathlib

class SyntaxHighlight(QTextCharFormat):
    def __init__(self , fgColor: QColor):
        super().__init__()

        self.setForeground(fgColor)

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self , document , rules: dict):
        super().__init__(document)
        
        self.rules = rules

    def highlightBlock(self, text):
        for pattern, rule in self.rules:
            it = pattern.globalMatch(text)
            while it.hasNext():
                match = it.next()

                if pattern.pattern().startswith(r'\bimport\s+') or pattern.pattern().startswith(r'\bfrom\s+'):
                    start = match.capturedStart(1)
                    length = match.capturedLength(1)
                    self.setFormat(start, length, rule)
                else:
                    self.setFormat(match.capturedStart(), match.capturedLength(), rule)

class App(QWidget):
    def __init__(self):
        super().__init__() # initialize QWidget
        self.show()
        
        self.vlayout = QVBoxLayout(self) # vertical layout for rows
        self.vlayout.setContentsMargins(0 , 0 , 0 , 0)
        self.vlayout.setSpacing(0)

        self.setLayout(self.vlayout)

        self.hlayout = QHBoxLayout() # horizontal layout for columns
        self.vlayout.addLayout(self.hlayout) # adding horizontal layout to vertical layout because QWidget cant have 2 layouts by itself.

        self.editorContainer = QHBoxLayout() # another horizontal layout for add lineCounter.
        self.vlayout.addLayout(self.editorContainer)

        self.lineCounter = QPlainTextEdit("1")
        self.lineCounter.setReadOnly(True)
        self.lineCounter.setFixedWidth(25)
        self.lineCounter.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.lineCounter.setObjectName("lineCounter")
        self.editorContainer.addWidget(self.lineCounter)

        self.codeEditor = QPlainTextEdit()
        self.codeEditor.textChanged.connect(self.updateLineNumbers)
        self.codeEditor.verticalScrollBar().valueChanged.connect(
            lambda value=self.codeEditor.verticalScrollBar().value: self.lineCounter.verticalScrollBar().setValue(value)
)

        self.editorContainer.addWidget(self.codeEditor)

        self.console = QTermWidget()
        self.console.setColorScheme("BreezeModified")
        self.vlayout.addWidget(self.console)

        self.saveButton = QPushButton("Save")
        self.saveButton.clicked.connect(lambda e: self.saveCode())
        self.hlayout.addWidget(self.saveButton)

        self.runButton = QPushButton("Run")
        self.runButton.clicked.connect(lambda e: self.runCode())
        self.hlayout.addWidget(self.runButton)

        self.loadButton = QPushButton("Load")
        self.loadButton.clicked.connect(lambda e: self.loadCode())
        self.hlayout.addWidget(self.loadButton)
        
        self.formats = {
            "keywordBasic": SyntaxHighlight(QColor("blue")),
            "keywordStatements": SyntaxHighlight(QColor("orange")),
            "import": SyntaxHighlight(QColor("purple")),
            "lib": SyntaxHighlight(QColor("pink")),
            "parenthesis": SyntaxHighlight(QColor("yellow")),
            "string": SyntaxHighlight(QColor("green")),
            "create": SyntaxHighlight(QColor("magenta")),
            "decorator": SyntaxHighlight(QColor("lightblue")),
            "comment": SyntaxHighlight(QColor("gray"))
        }

        self.syntaxRules = [
            (QRegularExpression(r"\b(print)\b"), self.formats["keywordBasic"]),
            (QRegularExpression(r"\b(import|from)\b"), self.formats["import"]),
            (QRegularExpression(r'\bimport\s+(\w+)'), self.formats["lib"]),
            (QRegularExpression(r'\bfrom\s+(\w+)'), self.formats["lib"]),
            (QRegularExpression(r"[()\[\]]"), self.formats["parenthesis"]),
            (QRegularExpression(r"(\".*?\"|\'.*?\')"), self.formats["string"]),
            (QRegularExpression(r"\b(if|elif|else|while|for|in|not|is|return|as)\b"), self.formats["keywordStatements"]),
            (QRegularExpression(r"\b(def|class)\b"), self.formats["create"]),
            (QRegularExpression(r"@\w+"), self.formats["decorator"]),
            (QRegularExpression(r"#.*"), self.formats["comment"])
        ]

        self.syntaxHighlighter = SyntaxHighlighter(self.codeEditor.document() , self.syntaxRules)

        self.selectedFile = None
    
    def updateLineNumbers(self):
        lines = [f"{i}\n" for i in range(1, self.codeEditor.blockCount() + 1)]
        self.lineCounter.setPlainText("".join(lines))
        self.resizeLineNumbers()

    def resizeLineNumbers(self):
        fontmetrics = QFontMetrics(self.lineCounter.font())
        charSize = fontmetrics.horizontalAdvance("9")
        text = self.lineCounter.toPlainText()
        padding = 11
        self.lineCounter.setFixedWidth((len(text.split()[len(text.split()) - 1]) * charSize) + padding)

    def runCode(self):
        with open(f"{pathlib.Path(__file__).resolve().parent / 'temp.py' if not self.selectedFile else self.selectedFile}" , "w") as file:
            file.write(self.codeEditor.toPlainText())
        
        self.console.sendText(f"python '{pathlib.Path(__file__).resolve().parent / 'temp.py' if not self.selectedFile else self.selectedFile}'\n")


    def saveCode(self):
        path, _ = QFileDialog.getSaveFileName(
            None,                      
            "Select Save Path",          
            "/",                        
            "Python Files (*.py);;All Files (*)" 
        )

        if path:
            with open(path, "w", encoding="utf-8") as file:
                file.write(self.codeEditor.toPlainText())
                self.selectedFile = path

    def loadCode(self):
        path , _ = QFileDialog.getOpenFileName(
            None,
            "Select Load Path",
            "/",
            "Python Files (*.py);;All Files(*)"
        )

        if path:
            with open(path , "r" , encoding="utf-8") as file:
                self.codeEditor.setPlainText(file.read())
                self.selectedFile = path

app = QApplication(sys.argv) # Instance of QApplication to allow adding QWidgets

try:
    with open(f"{pathlib.Path(__file__).resolve().parent}/style.qss" , "r") as file:
        app.setStyleSheet(file.read())
except FileNotFoundError:
    print("QSS file not found. Skipping...")

window = App()

sys.exit(app.exec())
