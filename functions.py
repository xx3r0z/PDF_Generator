from fpdf import FPDF


def create_pdf(topic, pages):
    pdf = FPDF(orientation="P", unit="mm", format="A4")