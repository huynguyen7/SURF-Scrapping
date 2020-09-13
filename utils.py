from bs4 import NavigableString;

base_attachment_url = 'https://www.millenniumbulkeiswa.gov/Comments/'

def get_submission_num(parsed_doc):
    return parsed_doc.find('span',
                           {'style': 'font-style:italic; font-weight:bold; '}).contents[0]


def get_received_time(parsed_doc):
    return parsed_doc.find('br').next.next.next.next.next


def get_commenter(parsed_doc, span_tags):
    if isinstance(span_tags[5].next.next, NavigableString) \
            and isinstance(span_tags[5].next.next.next.next.next, NavigableString):
        return span_tags[5].next.next + " " + span_tags[5].next.next.next.next.next
    elif isinstance(span_tags[5].next.next, NavigableString):
        return span_tags[5].next.next
    else:
        return ""


def get_organization(parsed_doc, span_tags):
    if isinstance(span_tags[8].next.next, NavigableString):
        return span_tags[8].next.next
    else:
        return ""


def get_state(parsed_doc, span_tags):
    if isinstance(span_tags[10].next.next, NavigableString):
        return span_tags[10].next.next
    else:
        return ""


def get_agency(parsed_doc, span_tags):
    if isinstance(span_tags[11].next.next, NavigableString):
        return span_tags[11].next.next
    else:
        return ""


def get_initiative(parsed_doc, span_tags):
    if isinstance(span_tags[13].next.next, NavigableString):
        return span_tags[13].next.next
    else:
        return ""


def get_attachments(parsed_doc):
    a_tags = parsed_doc.findAll('a')
    rs = ""
    for tag in a_tags:
        if ".html" not in tag['href']:
            rs += base_attachment_url + tag['href'] + "\t"
    return rs


def get_submission_text(parsed_doc, span_tags):
    if isinstance(span_tags[16].next.next.next, NavigableString):
        return span_tags[16].next.next.next
    else:
        return ""
