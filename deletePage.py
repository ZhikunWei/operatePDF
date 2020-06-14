#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

# 安装PyPDF2： pip3 install PyPDF2

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def deletePage(filename, pages=()):
    input = PdfFileReader(open(filename, "rb"))
    output = PdfFileWriter()
    for i in range(input.getNumPages()):
        if i+1 in pages:
            continue
        output.addPage(input.getPage(i))
        
    outputStream = open('output.pdf', "wb")
    output.write(outputStream)
    outputStream.close()


if __name__ == '__main__':
    deletePage('1.pdf', [2, 38])