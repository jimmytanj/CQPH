# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import paramiko
import chardet
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def getIsbnFromPDF(pdfFile):
    praser = PDFParser(pdfFile)
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)
    doc.initialize()
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
         rsrcmgr = PDFResourceManager()
         laparams = LAParams()
         device = PDFPageAggregator(rsrcmgr, laparams=laparams)
         interpreter = PDFPageInterpreter(rsrcmgr, device)
         for page in doc.get_pages():
             interpreter.process_page(page)
             layout = device.get_result()
             for x in layout:
                 if (isinstance(x, LTTextBoxHorizontal)):
                     results = x.get_text()
                     print(results)

basicPath='/opt/haishu/cqph-data/book2000/all'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="117.50.43.176", port=22, username="haishu", password="Hlw..2018")
sftp_client = ssh.open_sftp()
basicDirs=sftp_client.listdir(basicPath)
dirList=[]
pdfList=[]
for eachDir in basicDirs:
    dirList.append(basicPath+'/'+eachDir)
for dirItem in dirList:
    files=sftp_client.listdir(dirItem)
    for eachFile in files :
        if eachFile.find(".txt")>0:
            remote_file = sftp_client.open(dirItem+'/'+eachFile, 'rb')
            print("开始解%s"%(dirItem+'/'+eachFile))
            for lines in remote_file.readline():
                print(chardet.detect(lines))
            remote_file.close()