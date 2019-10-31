# -*- coding:utf-8*-
__author__ = '99k'

# 利用PyPDF2模块对文件夹内的PDF进行旋转操作，旋转后的文件保存于同目录的rotated文件夹内，文件名不变
# 只需修改存放PDF文件的文件夹变量：file_dir， 和需要旋转的度数变量 degrees

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from merge import getFileName


# fileList为需要旋转的文件列表
# rotateDegrees 为每个文件对应的顺时针旋转度数
def rotatePDF(fileList, rotateDegrees):
    if not os.path.exists(os.path.join(os.path.split(fileList[0])[0], "rotated/")):
        os.mkdir(os.path.join(os.path.split(fileList[0])[0], "rotated/"))
    for pdf_file, degree in zip(fileList, rotateDegrees):
        pdf = PdfFileReader(open(pdf_file, "rb"))
        page = pdf.getPage(0)
        page.rotateClockwise(180)
        pdfWriter = PdfFileWriter()
        pdfWriter.addPage(page)
        print(os.path.join(os.path.split(pdf_file)[0], "rotated"), os.path.split(pdf_file)[1])
        outFile = open(os.path.join(os.path.join(os.path.split(pdf_file)[0], "rotated"), os.path.split(pdf_file)[1]), 'wb')
        pdfWriter.write(outFile)
        outFile.close()
    
    
if __name__ == '__main__':
    file_dir = r"E:\HPSCANS\plan\need_rotate"
    fileList = getFileName(file_dir)
    degrees = [180] * len(fileList)
    rotatePDF(fileList, degrees)