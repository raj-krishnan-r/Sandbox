from fpdf import FPDF
pdf = FPDF('P',"in",(4,6))
pdf.add_page()
pdf.image("icon.png",x=0,y=0,w=1.5,h=.5,type='PNG')
pdf.image("qr.png",x=1.5,y=.5,h=1,w=1,type='PNG')
pdf.set_font('Times','B',14)
pdf.cell(w=4,h=1,txt="Hello Wolf")
pdf.output('tuto1.pdf', 'F')
