from fpdf import FPDF
import pandas as pd
import webbrowser


def gettcoords(pdf):
    x = round(pdf.get_x(), 2)
    y = round(pdf.get_y(), 2)
    w = round(pdf.w - (pdf.l_margin + pdf.r_margin), 2)
    h = round(pdf.h - (pdf.t_margin + pdf.b_margin), 2)
    return x, y, w, h


def printcoords(pdf):
    x, y, w, h = gettcoords(pdf)
    print(f"{x=} {y=} {w=} {h=} ")


pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    pdf.add_page()
    pdf.set_font("Times", style="B", size=24)
    # pdf.set_text_color(100, 100, 100)

    print(index, row.Order, row.Topic, row.Pages)
    printcoords(pdf)
    pdf.cell(w=0, txt=row.Topic, h=12, align="L", border=0, ln=1)
    printcoords(pdf)

    x, y, w, h = gettcoords(pdf)
    pdf.line(x, y, x + w, y)
    for page in range(row.Pages - 1):
        pdf.add_page()

pdf.output("output.pdf")
webbrowser.open("output.pdf")