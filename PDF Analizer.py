import sys
import spacy
import regex as re
import pymupdf
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit

MODEL_PATH = "model/NER_CComp"

class PDFAnalyzerApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.nlp = spacy.load(MODEL_PATH)
        
        if self.nlp is None:
            print("Error: Model not found or failed to load.")
            sys.exit(1)
        else:
            print("NER model loaded successfully.")
        
        self.pdf_text = ""

    def initUI(self):
        self.setWindowTitle("PDF Analyzer")
        self.setGeometry(100, 100, 500, 400)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Select a PDF to analyze:")
        layout.addWidget(self.label)
        
        self.selectButton = QPushButton("Select PDF")
        self.selectButton.clicked.connect(self.load_pdf)
        layout.addWidget(self.selectButton)
        
        self.analyzeButton = QPushButton("Analyze PDF")
        self.analyzeButton.setEnabled(False)
        self.analyzeButton.clicked.connect(self.analyze_text)
        layout.addWidget(self.analyzeButton)
        
        self.resultText = QTextEdit()
        self.resultText.setReadOnly(True)
        layout.addWidget(self.resultText)
        
        self.setLayout(layout)

    def load_pdf(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "/home", "PDF Files (*.pdf)")
        
        if file_name:
            self.extract_text_from_pdf(file_name)
            self.analyzeButton.setEnabled(True)
            self.label.setText(f"Loaded: {file_name}")
    
    def extract_text_from_pdf(self, file_path):
        doc = pymupdf.open(file_path)
        text = "\n".join(page.get_text("text", flags=pymupdf.TEXTFLAGS_TEXT) for page in doc)
        self.pdf_text = text
    
    def analyze_text(self):
        if self.pdf_text:
            self.__pre_process_text()
            doc = self.nlp(self.pdf_text)
            entities = "\n".join([f"{ent.text} ({ent.label_})" for ent in doc.ents])
            self.resultText.setPlainText(entities if entities else "No named entities found.")
    
    def __pre_process_text(self):
        # This will remove special characters, hyphens and extra spaces
        def clean_text(text):
            text = re.sub(r'[^\w\d\s\-\*]', ' ', text, flags=re.UNICODE)  # Removes everything except letters, numbers, spaces, hyphens and asterisks
            text = re.sub(r'-+', ' ', text)  # Removes hyphens
            text = re.sub(r'\s+', ' ', text).strip()  # Cleans up extra spaces
            return text
        
        self.pdf_text = clean_text(self.pdf_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFAnalyzerApp()
    window.show()
    sys.exit(app.exec())
