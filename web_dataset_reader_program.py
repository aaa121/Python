#Define a function for reading a dataset from a webpage

def web_dataset_reader(url):
    '''
    :param url: Input a web address.
    :return: This algorithm returns a dataseet and its descriptive statistics.
    Example:
    >>> url='http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
    >>> import web_dataset_reader_program as wbd
    >>> print(wbd.web_dataset_reader(url))
    >>> .
        .
        .
    '''
    from urllib import request as ur
    import web_skip_header_program as wh
    import statistics as st
    highvalue=0
    count=0
    with ur.urlopen(url) as webpage:
        first_data=wh.webpage_skip_head(webpage)
        first_data=first_data.split()
        dataset=first_data
        for data in webpage: # This reads the remaining lines of the webpage
            data=data.decode('utf-8')
            data=data.split()
            dataset+=data # For each iteration, the data transformed into
            # list append to dataset with first_data as its first list
            # #print(dataset)
            data_float=dataset
        for i in range(len(dataset)):
            data=float(dataset[i])
            data_float[i]=float(dataset[i]) # Elements in the list 'dataset' are transformed to
            #  float for additional operations such as min, max, range, sum
            count+= 1 # This counts the number of elements in the list
            highvalue =max(highvalue,data) # Zero is assigned to highvalue for its start value.
            #  The data changes for each loop and compared with each element in the list
        lowvalue = min(data_float)
        totalvalue =sum(data_float)
        rangevalue = highvalue - lowvalue
        #print(count)
        observation=len(dataset)
        average=totalvalue/observation
        mean=st.mean(data_float)
        median=st.median(data_float)
        median_high=st.median_high(data_float)
        median_low=st.median_low(data_float)
        #mode=st.mode(data_float)# If there is more than one mode, it will return Stat Error
        stdev=st.pstdev(data_float)
        variance=st.pvariance(data_float)
    return print('The Dataset in List form is:\n',data_float,'\n',
              '=============================================\n','            DIAGNOSTIC ANALYTICS             \n',
                 '=============================================\n','The Descriptive Statistics of the Dataset are:',
                 '\nTotal:\t\t{3}\nMaximum:\t{0}\nMinimum:\t{1}\nRange:\t\t{2}\nAverage:\t{5:.2f}\nMedian:\t\t{6}'
              '\nMedianHigh:\t{7}\nMedian Low:\t{8}\nVariance:\t{10:.2f}\nStd.Dev:\t{9:.2f}\nCounts:\t\t{4}'
              .format(highvalue,lowvalue,rangevalue,totalvalue,observation,mean,median,median_high,
                      median_low,stdev,variance),'\n','=============================================')
