from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", size=45)
        self.cell(0, 60, txt="CS50 Shirtificate",align="C")
        self.image("shirtificate.png", x=0, y=60)

def main():
    name = input("Name: ")
    get_shirt(name)

def get_shirt(name):
    shirt = PDF()
    shirt.add_page()
    shirt.set_font("Helvetica", "B", size=27)
    shirt.set_text_color(255, 255, 255)
    shirt.text(x=36, y=144, txt=f"{name} took CS50")
    shirt.output("shirtificate.pdf")
if __name__ == "__main__":
    main()