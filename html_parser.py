import re
from BeautifulSoup import BeautifulSoup
from html2text import html2text


__author__ = 'josebermudez'


def html_parser(html_string):
    """
    Parse html content, extracting address, suite and postcode
    As a bonus try to extract description as well!
    :param html_string:
    :return: address, suite, postcode, description and images
    """
    if not html_string:
        raise ValueError('error in parameters.')

    suite = None
    postcode = None

    # address field
    parsed_html = BeautifulSoup(html_string)
    address_line = str(parsed_html.body.find('div', attrs={'class': 'display_address'}).text)

    # postcode
    postcodes = re.findall(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b', address_line)
    if postcodes:
        postcode = postcodes[0]
        # delete postcode from address_line
        index = address_line[:address_line.find(postcode)].rfind(',')
        address_line = address_line[:index]

    # suite
    suites = re.findall(r"Suite [0-9]* ", address_line)
    if suites:
        suite = str(suites[0]).strip()
        # delete suite from address_line
        index = len(suite)+1
        address_line = address_line[index:].strip()

    address = address_line

    # get html
    description_field = str(parsed_html.body.find(id='details_description_wrapper'))
    # wrapper
    text = re.findall(r'<strong>Description</strong>(.*?)<strong>', description_field, re.DOTALL)[0]
    # clean
    description = html2text(text)
    description = description.replace('_', '')
    description = ''.join(description.splitlines())
    description = description.replace('  ', ' ')
    description = description.strip()

    # images
    images_text = parsed_html.body.find(id='carousel')
    images = []
    for li in images_text.findAll('li'):
        li = str(li)
        index_start = li.rfind('http://')
        index_end = li[index_start:].find('.jpg') + 4
        link = li[index_start:index_start+index_end]
        if link:
            images.append(link)

    return address, suite, postcode, description, images
