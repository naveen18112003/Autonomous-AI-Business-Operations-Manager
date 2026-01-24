from fpdf import FPDF
import logging

logger = logging.getLogger(__name__)

class PDFService(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Autonomous AI Business Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        safe_body = body.encode('latin-1', 'replace').decode('latin-1')
        self.multi_cell(0, 7, safe_body)
        self.ln()

    def generate_report(self, content: dict, filename: str):
        self.add_page()
        for section, text in content.items():
            self.chapter_title(section)
            self.chapter_body(text)

        self.output(filename)

pdf_service = PDFService()
