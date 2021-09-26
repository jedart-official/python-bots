from docx import Document

wordDoc = Document('ТП-27 гот.docx')

for table in wordDoc.tables:
    for row in (table.rows[1],table.rows[1]):
        for cell in row.cells:
            print (cell.text)