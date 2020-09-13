import pdfquery


def pdf_file_query(page, pdf_file):
    return pdf_file.extract([
        ('with_parent', 'LTPage[pageid="{}"]'.format(page + 1)),
        ('with_formatter', None),
        ('submission_num', 'LTTextLineHorizontal:in_bbox("16, 745.314, 612, 770")'),
        ('received', 'LTTextLineHorizontal:in_bbox("16, 718.314, 612, 730.566")'),
        ('commenter', 'LTTextLineHorizontal:in_bbox("16, 704.814, 612, 717.566")'),
        ('organization', 'LTTextLineHorizontal:in_bbox("16, 691.314, 612, 703.566")'),
        ('state', 'LTTextLineHorizontal:in_bbox("16, 677.814, 612, 690.066")'),
        ('agency', 'LTTextLineHorizontal:in_bbox("16, 650.814, 612, 663.066")'),
        ('initiative', 'LTTextLineHorizontal:in_bbox("16, 637.314, 612, 649.566")'),
        ('attachments', 'LTTextLineHorizontal:in_bbox("16, 623.814, 612, 636.066")'),
        ('submission_text', 'LTTextLineHorizontal:in_bbox("16, 0, 612, 616.066")')
    ])


error_history_path = 'output/error.txt'


def append_row_to_text_file(string, error_history):
    with open(error_history, "a") as file_object:
        file_object.write("\n" + string)


def check_error(string, page, filename):
    if '(cid:' in string:
        error_report = "Error at page %i in %s" % (page, filename)
        print(error_report)
        append_row_to_text_file(error_report, error_history_path)
    if 'No attachments' in string:
        error_report = "Attachment at page %i in %s" % (page, filename)
        print(error_report)
        append_row_to_text_file(error_report, error_history_path)


def get_string_after_colons(string, page, filename):
    if string == "":
        return string
    rs = string.split(':', 1)[1].strip()
    check_error(rs, page + 1, filename)
    return rs


def parse_query(query, page, filename):
    submission_num = get_string_after_colons(query.get('submission_num').text(), page, filename)
    received = get_string_after_colons(query.get('received').text(), page, filename)
    commenter = get_string_after_colons(query.get('commenter').text(), page, filename)
    organization = get_string_after_colons(query.get('organization').text(), page, filename)
    state = get_string_after_colons(query.get('state').text(), page, filename)
    agency = get_string_after_colons(query.get('agency').text(), page, filename)
    initiative = get_string_after_colons(query.get('initiative').text(), page, filename)
    attachments = get_string_after_colons(query.get('attachments').text(), page, filename)
    submission_text = query.get('submission_text').text()

    data = [submission_num, received, commenter, organization, state,
            agency, initiative, attachments, submission_text]
    return data


def test_submission_number(num_of_pages, pdf_file):
    print("\nGETTING SUB_NUM")
    count = 0
    for pg in range(num_of_pages):
        data = pdf_file.extract([
            ('with_parent', 'LTPage[pageid="{}"]'.format(pg + 1)),
            ('with_formatter', None),
            ('sub_num', 'LTTextLineHorizontal:in_bbox("16, 745.314, 612, 770")')
        ])
        getter = data.get('sub_num').text()
        print(getter)
        print(str(count))
        count = count + 1


# Get Received, x0 = 16, y0 = 718.314, x1 = 179.096, y1 = 730.566 """
def test_received(num_of_pages, pdf_file):
    print("\nGETTING received")
    count = 0
    for pg in range(num_of_pages):
        data = pdf_file.extract([
            ('with_parent', 'LTPage[pageid="{}"]'.format(pg + 1)),
            ('with_formatter', None),
            ('received', 'LTTextLineHorizontal:in_bbox("16, 718.314, 612, 730.566")')
        ])
        getter = data.get('received').text()
        if getter is "":
            print("Empty")
        else:
            print(getter)
        print(str(count))
        count = count + 1


# Get Commenter, x0 = 16, y0 = 704.814, x1 = 159,9, al = 220, y1 = 717.066
def test_commenter(num_of_pages, pdf_file):
    print("\nGETTING Commenter")
    count = 0
    for pg in range(num_of_pages):
        data = pdf_file.extract([
            ('with_parent', 'LTPage[pageid="{}"]'.format(pg + 1)),
            ('with_formatter', None),
            ('commenter', 'LTTextLineHorizontal:in_bbox("16, 704.814, 612, 717.566")')
        ])
        getter = data.get('commenter').text()
        if getter is "":
            print("Empty")
        else:
            print(getter)
        print(str(count))
        count = count + 1


# Get Organization, x0 = 16, y0 = 691.314, x1 = 144.664, y1 = 703.566
def test_organization(num_of_pages, pdf_file):
    print("\nGETTING Organization")
    count = 0
    for pg in range(num_of_pages):
        data = pdf_file.extract([
            ('with_parent', 'LTPage[pageid="{}"]'.format(pg + 1)),
            ('with_formatter', None),
            ('organization', 'LTTextLineHorizontal:in_bbox("16, 691.314, 612, 703.566")')
        ])
        getter = data.get('organization').text()
        if getter is "":
            print("Empty")
        else:
            print(getter)
        print(str(count))
        count = count + 1


# Get State, x0 = 16, y0 = 677.814, x1 = 106.996, y1 = 690.066
def test_state(num_of_pages, pdf_file):
    print("\nGETTING State")
    count = 0
    for pg in range(num_of_pages):
        data = pdf_file.extract([
            ('with_parent', 'LTPage[pageid="{}"]'.format(pg + 1)),
            ('with_formatter', None),
            ('state', 'LTTextLineHorizontal:in_bbox("16, 677.814, 612, 690.066")')
        ])
        getter = data.get('state').text()
        if getter is "":
            print("Empty")
        else:
            print(getter)
        print(str(count))
        count = count + 1


# Get Agency, x0 = 16, y0 = 650.814, x1 = 355.24, y1 = 663.066
def test_state(num_of_pages, pdf_file):
    print("\nGETTING Agency")
    count = 0
    for pg in range(num_of_pages):
        data = pdf_file.extract([
            ('with_parent', 'LTPage[pageid="{}"]'.format(pg + 1)),
            ('with_formatter', None),
            ('agency', 'LTTextLineHorizontal:in_bbox("16, 650.814, 612, 663.066")')
        ])
        getter = data.get('agency').text()
        if getter is "":
            print("Empty")
        else:
            print(getter)
        print(str(count))
        count = count + 1


# Get Initiative, x0 = 16, y0 = 637.314, x1 = 321.664, y1 = 649.566
def test_initiative(num_of_pages, pdf_file):
    print("\nGETTING Initiative")
    count = 0
    for pg in range(num_of_pages):
        data = pdf_file.extract([
            ('with_parent', 'LTPage[pageid="{}"]'.format(pg + 1)),
            ('with_formatter', None),
            ('initiative', 'LTTextLineHorizontal:in_bbox("16, 637.314, 612, 649.566")')
        ])
        getter = data.get('initiative').text()
        if getter is "":
            print("Empty")
        else:
            print(getter)
        print(str(count))
        count = count + 1


# Get Attachments, x0 = 16, y0 = 623.814, x1 = 167.41, y1 = 636.066
def test_attachments(num_of_pages, pdf_file):
    print("\nGETTING attachments")
    count = 0
    for pg in range(num_of_pages):
        data = pdf_file.extract([
            ('with_parent', 'LTPage[pageid="{}"]'.format(pg + 1)),
            ('with_formatter', None),
            ('attachments', 'LTTextLineHorizontal:in_bbox("16, 623.814, 612, 636.066")')
        ])
        getter = data.get('attachments').text()
        if getter is "":
            print("Empty")
        else:
            print(getter)
        print(str(count))
        count = count + 1


# Get Submission Text, x0 = 16, y0 = 597.066, x1 = 588.664 -> 612, y1 = 609.066 -> 55.566
def test_submission_text(num_of_pages, pdf_file):
    print("\n Getting Submission Text")
    count = 0
    for pg in range(num_of_pages):
        data = pdf_file.extract([
            ('with_parent', 'LTPage[pageid="{}"]'.format(pg + 1)),
            ('with_formatter', None),
            ('submission_text', 'LTTextLineHorizontal:in_bbox("16, 0, 612, 616.066")')
        ])
        getter = data.get('submission_text').text()
        if getter is "":
            print("Empty")
        else:
            print(getter)
        print(str(count))
        count = count + 1


""" Use this to get coordinate """
# for pg in range(num_of_pages):
#     test_string = "goals, this project will increase emissions equal to 7 coal fired plants? Really? This is an oxymoron in my opinion."
#     label = pdf_file.pq('LTTextLineHorizontal:contains("%s")' % test_string)
#     left_corner = float(label.attr('x0'))
#     bottom_corner = float(label.attr('y0'))
#     sub_num = pdf_file.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")'
#                           % (16, 677.814, 612, 690.066)).text()
#     print("Hehe")
