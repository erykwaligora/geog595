# created on Dec 24, 2020
# @authors:          Bo Zhao (zhaobo@uw.edu), Jou Ho ()
# @website:         https://www.github.com/jakobzhao/geog595
# @organization:    Department of Geography, University of Washington, Seattle
# @description:     XXXXX

from os import listdir
from os.path import isfile, join
from fitz import open as fitzOpen
from tika import parser

bookPath = "assets/gay-seattle"
delFrontPagePath = "assets/delFrontPage"
txtPath = "assets/gay-seattle.txt"
pdfs = [f for f in listdir(bookPath) if isfile(join(bookPath, f))]

for pdf in pdfs:
    # delete the front page of each pdf file
    pdfHandle = fitzOpen(bookPath + '/' + pdf)
    pages = list(range(pdfHandle.pageCount))
    pages.pop(0)
    pdfHandle.select(pages)
    pdfHandle.save(delFrontPagePath + '/' + pdf)
    pdfHandle.close()

    # read the content of each pdf and make a text file contains the entire book content.
    content = parser.from_file(delFrontPagePath + '/' + pdf)['content']
    try:
        print(content)
        with open(txtPath, 'a', encoding='utf8') as output:
            if content is not None:
                output.write(content)
    except AttributeError as error:
        print(error)
print("finished!")