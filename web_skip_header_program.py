def webpage_skip_head(WebPageName):
    ''' Notype -> Notype
    It reads the line that first contain numberic data or that didn't not start with #
    :param filename: The name of the datafile e.g web address
    :return: Returns the first data. Ensure to name the function as first_data or something convenient.
     Example:
     >>> from urllib import request as ur
     >>> import web_skip_header_program as wh
     >>> url='http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
     >>> with ur.urlopen(url) as webpage:
     >>> first_data=wh.webpage_skip_head(webpage)
     >>> print(first_data)
     22
     >>> for data in webpage
     >>> data=data.strip().decode('utf-8')
     >>> print(data)
    '''
    WebPageName.readline().strip().decode('utf')
    first_data=WebPageName.readline().strip().decode('utf')
    while first_data.startswith('#'):
        first_data=WebPageName.readline().strip().decode('utf')
    return first_data