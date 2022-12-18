from fpdf import FPDF
import pandas as pd
import webbrowser
import types


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


def footer_decorator(topic):                    # saves topic of current loop
    def decorator(func):                        # decorates footer
        def wrapper(self):                      # wraps func, passes on self
            func(self, topic)                   # call func with self, topic
        return wrapper
    return decorator


for index, row in df.iterrows():

    @footer_decorator(row.Topic)                # parametric decorator with current topic
    def footer(self, topic):                    # method to monkey patch
        print("footer", self, topic)
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Print centered page number
        self.cell(0, 10, f'Page {self.page_no()}, {topic}', 0, 0, 'C')

    pdf.footer = types.MethodType(footer, pdf)  # monkey patch method

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