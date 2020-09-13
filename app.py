from bs4 import BeautifulSoup
import pandas
import requests
import urllib.request
import time
from utils import *


def get_data(parsed_doc, span_tags):
    submission_num = get_submission_num(parsed_doc)
    received = get_received_time(parsed_doc)
    commenter = get_commenter(parsed_doc, span_tags)
    organization = get_organization(parsed_doc, span_tags)
    state = get_state(parsed_doc, span_tags)
    agency = get_agency(parsed_doc, span_tags)
    initiative = get_initiative(parsed_doc, span_tags)
    attachments = get_attachments(parsed_doc)
    submission_text = get_submission_text(parsed_doc, span_tags)

    return [[submission_num, received, commenter, organization, state,
             agency, initiative, attachments, submission_text]]


output_path = 'output/nepa-comments.csv'
base_url = 'https://www.millenniumbulkeiswa.gov/'
source_url = 'https://www.millenniumbulkeiswa.gov/nepa-comment-archive.html'
response = requests.get(source_url)
html_doc = response.text

"Parse html_doc"
parser = BeautifulSoup(html_doc, "html.parser")

"Collect all <a> tags with attr 'class = bodyTextLinks'"
a_tags = parser.find_all('a', {"class": "bodyTextLinks"})

columns = ['Submission Num', 'Received', 'Commenter', 'Organization',
           'State', 'Agency', 'Initiative', 'Attachments', 'Submission Text']
df = pandas.read_csv(output_path, names=columns)
output = pandas.DataFrame(data=None)

# Use this to continue if the loop break.
# obj_slice = slice(435, 3048)
# a_tags = a_tags[obj_slice]

"Parse each html file, then save parsed data to csv file"
for tag in a_tags:
    time.sleep(1)
    link = tag['href'].replace("\\", '/')
    parsed_doc = BeautifulSoup(urllib.request.urlopen(base_url + link)
                               , "html.parser")
    span_tags = parsed_doc.findAll('span')
    data = get_data(parsed_doc, span_tags)
    output = output.append(data)
    output.to_csv(output_path)
    print("Finished tag:\t" + tag['href'])

# TESTING
# tag = a_tags[3000]
#
# link = tag['href'].replace("\\", '/')
#
# linkmultipleattachments = 'https://www.millenniumbulkeiswa.gov/Comments/MBTL-NEPA-DEIS-0003330.html'
# normalLink = 'https://www.millenniumbulkeiswa.gov/Comments/MBTL-NEPA-DEIS-0001706.html'
# parsed_doc = BeautifulSoup(urllib.request.urlopen(normalLink), "html.parser")
#
# "Init csv columns"
# output = pandas.DataFrame(data=None, columns=columns)
