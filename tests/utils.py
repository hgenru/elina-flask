from lxml import etree

def parse_dom(text):
    parser = etree.HTMLParser()
    return etree.fromstring(text, parser)

def get_element_by_xpath(dom, xpath):
    elements = dom.xpath(xpath)
    try:
        return elements[0]
    except IndexError:
        return None
