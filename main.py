from PyQt6.QtCore import QRegularExpression , Qt
from PyQt6.QtGui import QColor, QTextCharFormat, QSyntaxHighlighter , QFontMetrics
from PyQt6.QtWidgets import QApplication, QPlainTextEdit , QWidget , QVBoxLayout , QPushButton , QFileDialog , QHBoxLayout
from QTermWidget import QTermWidget
import sys , subprocess , pathlib

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self , document):
        super().__init__(document)

        keywordHighlightBasic = QTextCharFormat()
        keywordHighlightBasic.setForeground(QColor("blue"))

        keywordHighlightStatements = QTextCharFormat()
        keywordHighlightStatements.setForeground(QColor("orange"))

        importHighlight = QTextCharFormat()
        importHighlight.setForeground(QColor("purple"))

        libHighlight = QTextCharFormat()
        libHighlight.setForeground(QColor("pink"))

        parenthesisHighlight = QTextCharFormat()
        parenthesisHighlight.setForeground(QColor("yellow"))

        stringHighlight = QTextCharFormat()
        stringHighlight.setForeground(QColor("green"))

        createHighlight = QTextCharFormat()
        createHighlight.setForeground(QColor("magenta"))

        decoratorHighlight = QTextCharFormat()
        decoratorHighlight.setForeground(QColor("lightblue"))

        commentHighlight = QTextCharFormat()
        commentHighlight.setForeground(QColor("gray"))

        self.rules = [
            (QRegularExpression(r"\b(print)\b") , keywordHighlightBasic),
            (QRegularExpression(r"\b(import|from)\b") , importHighlight),
            (QRegularExpression(r'\bimport\s+(\w+)') , libHighlight),
            (QRegularExpression(r'\bfrom\s+(\w+)') , libHighlight),
            (QRegularExpression(r"[()\[\]]") , parenthesisHighlight),
            (QRegularExpression(r"(\".*?\"|\'.*?\')") , stringHighlight),
            (QRegularExpression(r"\b(if|elif|else|while|for|in|not|is|return|as)\b") , keywordHighlightStatements),
            (QRegularExpression(r"\b(def|class)\b") , createHighlight),
            (QRegularExpression(r"@\w+") , decoratorHighlight),
            (QRegularExpression(r"#.*") , commentHighlight)
        ]

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

def runCode():
    with open(f"{pathlib.Path(__file__).resolve().parent / 'temp.py' if not selectedFile else selectedFile}" , "w") as file:
        file.write(codeEditor.toPlainText())
    
    console.sendText(f"python '{pathlib.Path(__file__).resolve().parent / 'temp.py' if not selectedFile else selectedFile}'\n")


def saveCode():
    global selectedFile
    path, _ = QFileDialog.getSaveFileName(
        None,                      
        "Select Save Path",          
        "/",                        
        "Python Files (*.py);;All Files (*)" 
    )

    if path:
        with open(path, "w", encoding="utf-8") as file:
            file.write(codeEditor.toPlainText())
            selectedFile = path

def loadCode():
    global selectedFile
    path , _ = QFileDialog.getOpenFileName(
        None,
        "Select Load Path",
        "/",
        "Python Files (*.py);;All Files(*)"
    )

    if path:
        with open(path , "r" , encoding="utf-8") as file:
            codeEditor.setPlainText(file.read())
            selectedFile = path

def resizeLineNumbers():
    fontmetrics = QFontMetrics(lineCounter.font())
    charSize = fontmetrics.horizontalAdvance("9")
    text = lineCounter.toPlainText()
    padding = 11
    lineCounter.setFixedWidth((len(text.split()[len(text.split()) - 1]) * charSize) + padding)

def updateLineNumbers():
    lines = [f"{i}\n" for i in range(1, codeEditor.blockCount() + 1)]
    lineCounter.setPlainText("".join(lines))
    resizeLineNumbers()

app = QApplication(sys.argv)
try:
    with open(f"{pathlib.Path(__file__).resolve().parent}/style.qss" , "r") as file:
        app.setStyleSheet(file.read())
except FileNotFoundError:
    print("QSS file not found. Skipping...")

window = QWidget()
window.show()

vlayout = QVBoxLayout(window)
vlayout.setContentsMargins(0 , 0 , 0 , 0)
vlayout.setSpacing(0)

hLayout = QHBoxLayout()
vlayout.addLayout(hLayout)

editorContainer = QHBoxLayout()
vlayout.addLayout(editorContainer)

lineCounter = QPlainTextEdit("1")
lineCounter.setReadOnly(True)
lineCounter.setFixedWidth(25)
lineCounter.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
lineCounter.setObjectName("lineCounter")
editorContainer.addWidget(lineCounter)

codeEditor = QPlainTextEdit()
codeEditor.textChanged.connect(updateLineNumbers)
codeEditor.verticalScrollBar().valueChanged.connect(
    lambda value=codeEditor.verticalScrollBar().value: lineCounter.verticalScrollBar().setValue(value)
)
editorContainer.addWidget(codeEditor)

console = QTermWidget()
console.setColorScheme("BreezeModified")
vlayout.addWidget(console)

saveButton = QPushButton("Save")
saveButton.clicked.connect(lambda e: saveCode())
hLayout.addWidget(saveButton)

runButton = QPushButton("Run")
runButton.clicked.connect(lambda e: runCode())
hLayout.addWidget(runButton)

loadButton = QPushButton("Load")
loadButton.clicked.connect(lambda e: loadCode())
hLayout.addWidget(loadButton)

syntaxHighlighter = SyntaxHighlighter(codeEditor.document())

selectedFile = None

sys.exit(app.exec())
