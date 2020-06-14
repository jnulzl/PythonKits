# encoding:utf-8
import os
# import shutil
import copy
import argparse

from PyPDF4 import PdfFileReader, PdfFileWriter


def parseArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument(
        '--input_pdf',
        help='input pdf file path. Must input!',
        type=str,
        default='')
    parse.add_argument(
        '--input_txt',
        help='input txt file path.  Must input!',
        type=str,
        default='')
    parse.add_argument(
        '--mode',
        help='output mode. Default value is 1',
        type=int,
        default=1)
    parse.add_argument(
        '--output',
        help='output file directory. Default value is output_jnulzl_',
        type=str,
        default="output_jnulzl_")

    return parse.parse_args()


def parseTxt(txtPath):
    if not os.path.exists(txtPath):
        print("There is no %s" % (txtPath))
        return None

    tmp = []
    line_count = 1
    with open(txtPath, "rb") as fpR:
        while True:
            line = fpR.readline()
            line = line.decode().strip()
            if line is None or '' == line or '\n' == line:
                break
            if line.startswith('#'):
                continue
            print(line)
            line = line.strip().split()
            page_begin = -1
            page_end = -1
            page_num = line[0].split('-')
            if 2 == len(page_num):
                page_begin = int(page_num[0]) - 1
                page_end = int(page_num[1])
                if page_begin > page_end:
                    print("In %dth line, page num begin must <= page num end!" % (line_count))
                    return None
            elif 1 == len(page_num):
                page_begin = int(page_num[0]) - 1
                page_end = page_begin + 1

            line_count += 1
            tmp.append([page_begin, page_end, line[1]])

    return tmp


def extractPdf(pdf_file_reader, page_begin, page_end, pdf_file_writer):
    for page_num in range(page_begin, page_end, 1):
        pdf_file_writer.addPage(pdf_file_reader.getPage(page_num))

    return pdf_file_writer


def modeOne(args, txtRes):
    outPutName = os.path.join(args.output, "all_jnulzl.pdf")
    if os.path.exists(outPutName):
        print('There is exists %s' % outPutName)
        return True

    pdf = PdfFileReader(args.input_pdf)
    writer = PdfFileWriter()
    for item in txtRes:
        page_begin = item[0]
        page_end = item[1]
        writer = extractPdf(pdf, page_begin, page_end, writer)

    with open(outPutName, "wb") as fileOut:
        writer.write(fileOut)

    return True


def modeTwo(args, txtRes):
    titlePageDict = {}
    for item in txtRes:
        key = item[2]
        if key not in titlePageDict:
            titlePageDict[key] = []
        page_begin = item[0]
        page_end = item[1]
        titlePageDict[key].append([page_begin, page_end])

    for title in titlePageDict:
        outPutName = os.path.join(args.output, title + ".pdf")
        if os.path.exists(outPutName):
            print('There is exists %s' % outPutName)
            continue
        print("Save " + title)
        pdf = PdfFileReader(args.input_pdf)
        writer = PdfFileWriter()
        pageBeginEnds = titlePageDict[title]
        for item in pageBeginEnds:
            page_begin = item[0]
            page_end = item[1]
            writer = extractPdf(pdf, page_begin, page_end, writer)

        with open(outPutName, "wb") as fileOut:
            writer.write(fileOut)

        del writer

    return True


def main():
    args = parseArgs()
    if not os.path.exists(args.input_pdf):
        print("Thers is no input pdf file %s!" % (args.input_pdf))
        print(args)
        return None

    if not os.path.exists(args.input_txt):
        print("Thers is no input txt file %s!" % (args.input_txt))
        print(args)
        return None

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    txtRes = parseTxt(args.input_txt)
    if txtRes is None:
        return None

    if 1 == args.mode:
        modeOne(args, txtRes)
    elif 2 == args.mode:
        modeOne(args, txtRes)
        modeTwo(args, txtRes)


if __name__ == '__main__':
    main()
