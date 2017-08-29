import textract

text = textract.process("frmVisualizarBula.pdf")
print(text)