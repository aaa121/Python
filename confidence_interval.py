#Confidence Interval for test of Hypothesis at 95% CI
def coverage_rate_95(zscore):
    '''
    ... num -> num, str
    :param zscore: Input is numeric. The calculated Zscore
    :return: Numeric and Decision iff (if and only if) is within or outside the interval

    Examnples:
    >>> coverage_rate_95(1.23)
    1.23  is within the coverage range. Reject Null Hypothesis.

    >>> coverage_rate_95(-2.13)
    -2.13  is not within the coverage range. Accept Null Hypothesis.
    '''
    x= -1.96 <= zscore <= 1.96
    if x == True:
        print(zscore, " is within the coverage range. Reject Null Hypothesis.")
    else:
        print(zscore, " is not within the coverage range. Accept Null Hypothesis.")
    return