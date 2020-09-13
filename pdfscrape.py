import pdfquery
from pdf_loader import get_pdf, get_part_1, get_part_2, get_part_3
from pdfscrape_utils import pdf_file_query, parse_query, append_row_to_text_file
from csv import writer


def append_row_to_csv(file, row):
    with open(file, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(row)


def main_process(list_pdf):
    for pdf_file in list_pdf:
        pages = pdf_file._cached_pages()
        num_of_pages = len(pages)
        for page in range(num_of_pages):
            query = pdf_file_query(page, pdf_file)
            try:
                data = parse_query(query, page, pdf_file.file.name)
                append_row_to_csv(filename, data)
            except IndexError:
                error_report = "Cannot parse pdf at page %i in %s" % (page + 1, pdf_file.file.name)
                append_row_to_text_file(error_report, error_history)
                print(error_report)


list_1 = get_part_1()
list_2 = get_part_2()
list_3 = get_part_3()
filename = 'output/sepa-comments.csv'
error_history = 'output/error.txt'

big_list = [list_1, list_2, list_3]

for list_pdf in big_list:
    main_process(list_pdf)


""" Testing """
# path = './resources/part1/removed-pics-attachments/401-600_removed.pdf'
# pdf_file = get_pdf(path)
# pages = pdf_file._cached_pages()
# num_of_pages = len(pages)
#
# for page in range(num_of_pages):
#     query = pdf_file_query(page, pdf_file)
#     try:
#         data = parse_query(query, page, pdf_file.file.name)
#         append_row_to_csv(filename, data)
#     except IndexError:
#         error_report = "Cannot parse pdf at page %i in %s" % (page + 1, pdf_file.file.name)
#         append_row_to_text_file(error_report, error_history)
#         print(error_report)


# query = pdf_file_query(15, pdf_file)
# data = parse_query(query, 15, pdf_file.file.name)
