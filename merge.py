# -*- coding:utf-8*-
__author__ = '99k'

# 安装PyPDF2： pip3 install PyPDF2
# 利用PyPDF2模块合并同一文件夹下的所有PDF文件, 文件名会按照升序排列合并
# 只需修改存放PDF文件的文件夹变量：file_dir 和 输出文件名变量: outfile
# reference: \url{https://www.jianshu.com/p/82485e3e46e1}
#           \url{https://pythonhosted.org/PyPDF2/}
#           \url{https://blog.csdn.net/FairyTale__/article/details/89036889}

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


# 使用os模块的listdir函数，搜索出指定目录下的PDF文件，注意，不包含子目录文件
# 返回同一目录下的所有PDF文件的绝对路径
def getFileName(filedir):
    file_list = [os.path.join(filedir, filespath) \
                 for filespath in os.listdir(filedir) \
                 if str(filespath).endswith('pdf')
                 ]

    file_list.sort()
    print(file_list)
    return file_list if file_list else []


# 合并同一目录下的所有PDF文件
def MergePDF(filepath, outfile):
    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = getFileName(filepath)
    
    if pdf_fileName:
        for pdf_file in pdf_fileName:
            print("路径：%s" % pdf_file)
            
            # 读取源PDF文件
            input = PdfFileReader(open(pdf_file, "rb"))
            
            # 获得源PDF文件中页面总数
            pageCount = input.getNumPages()
            outputPages += pageCount
            print("页数：%d" % pageCount)
            
            # 分别将page添加到输出output中
            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))
        
        print("合并后的总页数:%d." % outputPages)
        # 写入到目标PDF文件
        outputStream = open(os.path.join(filepath, outfile), "wb")
        output.write(outputStream)
        outputStream.close()
        print("PDF文件合并完成！")
    
    else:
        print("没有可以合并的PDF文件！")


# 主函数
if __name__ == '__main__':
    file_dir = r'E:\HPSCANS\plan'  # 存放PDF的原文件夹
    outfile = "out.pdf"  # 输出的PDF文件的名称
    if os.path.exists(os.path.join(file_dir, outfile)):
        print("out file exits! delete it and rerun!")
        exit()
    MergePDF(file_dir, outfile)

