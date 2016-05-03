# This program requires one major input: (1). The variable defined url
# It only reads a website by stripping and formating the bytes in utf-8 form
def webpage_reader(url):
    '''
    It reads the content of a website
    :param url: The web address
    :return: The content of a website. It will add additional newline at the end of the website
    Example:
    >>> import webpage_reader_program as wr
    >>> url='http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
    >>> content=wr.webpage_reader(url)
    >>> print(content)
        .
        .
        .
    '''
    from urllib import request as ur
    with ur.urlopen(url) as webpage:
        content=''
        for view in webpage:
            view=view.strip().decode('utf-8')
            content+=view+'\n'
    return content
