import pdfquery
from pdfquery.cache import FileCache

part_1_1 = './resources/part1/removed-pics-attachments/1-200_removed.pdf'
part_1_2 = './resources/part1/removed-pics-attachments/401-600_removed.pdf'
part_1_3 = './resources/part1/removed-pics-attachments/601-800_removed.pdf'
part_1_4 = './resources/part1/removed-pics-attachments/801-1000_removed.pdf'
part_1_5 = './resources/part1/removed-pics-attachments/1001-1151_removed.pdf'

part_1 = [part_1_1, part_1_2, part_1_3, part_1_4, part_1_5]

part_2_1 = './resources/part2/removed-pics-attachments/1-200_removed.pdf'
part_2_2 = './resources/part2/removed-pics-attachments/201-400_removed.pdf'
part_2_3 = './resources/part2/removed-pics-attachments/401-600_removed.pdf'
part_2_4 = './resources/part2/removed-pics-attachments/601-800_removed.pdf'
part_2_5 = './resources/part2/removed-pics-attachments/801-1000_removed.pdf'
part_2_6 = './resources/part2/removed-pics-attachments/1001-1200_removed.pdf'
part_2_7 = './resources/part2/removed-pics-attachments/1201-1400_removed.pdf'
part_2_8 = './resources/part2/removed-pics-attachments/1401-1600_removed.pdf'
part_2_9 = './resources/part2/removed-pics-attachments/1601-1800_removed.pdf'
part_2_10 = './resources/part2/removed-pics-attachments/1801-2000_removed.pdf'
part_2_11 = './resources/part2/removed-pics-attachments/2001-2200_removed.pdf'
part_2_12 = './resources/part2/removed-pics-attachments/2201-2345_removed.pdf'

part_2 = [part_2_1, part_2_2, part_2_3, part_2_4, part_2_5, part_2_6, part_2_7,
          part_2_8, part_2_9, part_2_10, part_2_11, part_2_12]

part_3_1 = './resources/part3/removed-pics-attachments/1-200_removed.pdf'
part_3_2 = './resources/part3/removed-pics-attachments/201-400_removed.pdf'
part_3_3 = './resources/part3/removed-pics-attachments/401-600_removed.pdf'
part_3_4 = './resources/part3/removed-pics-attachments/601-800_removed.pdf'
part_3_5 = './resources/part3/removed-pics-attachments/801-1000_removed.pdf'
part_3_6 = './resources/part3/removed-pics-attachments/1001-1200_removed.pdf'
part_3_7 = './resources/part3/removed-pics-attachments/1201-1400_removed.pdf'
part_3_8 = './resources/part3/removed-pics-attachments/1401-1600_removed.pdf'
part_3_9 = './resources/part3/removed-pics-attachments/1601-1800_removed.pdf'
part_3_10 = './resources/part3/removed-pics-attachments/1801-2000_removed.pdf'
part_3_11 = './resources/part3/removed-pics-attachments/2001-2264_removed.pdf'

part_3 = [part_3_1, part_3_2, part_3_3, part_3_4, part_3_5, part_3_6, part_3_7,
          part_3_8, part_3_9, part_3_10, part_3_11]


def get_part_1():
    list_1 = []
    for pdf_path in part_1:
        pdf = pdfquery.PDFQuery(pdf_path, parse_tree_cacher=FileCache("./tmp/"))
        pdf.load()
        list_1.append(pdf)
    print("Finished getting part 1")
    return list_1


def get_part_2():
    list_2 = []
    for pdf_path in part_2:
        pdf = pdfquery.PDFQuery(pdf_path, parse_tree_cacher=FileCache("./tmp/"))
        pdf.load()
        list_2.append(pdf)
    print("Finished getting part 2")
    return list_2


def get_part_3():
    list_3 = []
    for pdf_path in part_3:
        pdf = pdfquery.PDFQuery(pdf_path, parse_tree_cacher=FileCache("./tmp/"))
        pdf.load()
        list_3.append(pdf)
    print("Finished getting part 3")
    return list_3


def get_pdf(path):
    pdf = pdfquery.PDFQuery(path, parse_tree_cacher=FileCache("./tmp/"))
    pdf.load()
    return pdf
