from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()
pdf.set_font("Times", style="B", size=12)
pdf.cell(w=0, txt="Test", h=12, align="L", border=0, ln=1)
pdf.cell(w=0, txt="Test", h=12, align="L", border=0)
pdf.ln()
pdf.cell(w=0, txt="Test", h=12, align="L", border=0)
pdf.output("test.pdf")
