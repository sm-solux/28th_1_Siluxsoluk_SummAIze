# -*- coding: utf-8 -*-
"""PDF_2_TXT

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fXC1M2QoiLwcuqOtTjlL-ZoHdpkV5stN
"""

#!pip install git+https://github.com/pdftables/python-pdftables-api.git

!pip install 'PyPDF2<3.0'

from google.colab import drive
drive.mount("/content/gdrive")

!pip install tabula-py

contents="/content/수사기관의 정보수집에 관한 최신 해외 사례와 시사점.pdf"

import PyPDF2
pdfReader = PyPDF2.PdfFileReader(contents)
total = ''
for i in range(pdfReader.numPages):
    data = pdfReader.getPage(i).extractText()
    total += data
print(total[:1000])

with open('수사기관의 정보수집에 관한 최신 해외 사례와 시사점.txt','w') as f:
  f.write(total)

# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf("수사기관의 정보수집에 관한 최신 해외 사례와 시사점.pdf", pages='all')[1]
# convert PDF into CSV
#tabula.convert_into("수사기관의 정보수집에 관한 최신 해외 사례와 시사점.pdf", "iplmatch.csv", output_format="csv", pages='all')
print(df)