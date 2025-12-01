from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")

# the df variable contains an object data frame
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    # Set text color in (R,G,B)
    pdf.set_text_color(100,100,100)
    # to access the topics in each row
    topic = row["Topic"]
    # w-width (set to zero means it will cover the whole width. H: Height, align: Align text to the left, Border: Set border,
    # ln: to make the next cell start in a new line
    pdf.cell(w=0, h=24, txt=f"{topic}", align="L", ln=1, border=1)

    # pdf line is to draw a line in the pdf page, x1&x2 is the distance from the left hand edge of the page y1&y2 is
    # the distance from the top all measurement in mm as stated in the unit from above
    pdf.line(10, 40, 200, 40)

    # to create footer, .ln(278) is breakline method, 230mm
    pdf.ln(230)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=f"{topic}", align="R", ln=1, border=1)

    #Add lines to the page
    for i in range(50, 260, 10):
        x1 = 10
        x2 = 200
        y1 = i
        y2 = i
        pdf.line(x1, y1, x2, y2)

    # range(5) creates a list [0,1,2,3,4], but you have to cover it in list() to view the list
    # print(list(range(row["Pages"])))
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(240)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=f"{topic}", align="R", ln=1, border=1)

        # Add lines to the page
        for i in range(50, 240, 10):
            x1 = 10
            x2 = 200
            y1 = i
            y2 = i
            pdf.line(x1, y1, x2, y2)


pdf.output("output.pdf")

