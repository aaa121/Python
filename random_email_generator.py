def random_email(length,atdomain):
    '''

    :param length: The length of the email string
    :param domain: the domain identifier i.e. @gmail.com
    :return: A random letter email address.
    For example:
    print(random_email(7,"@pg.canterbury.ac.nz"))

    Example II:
    for i in range(10):
    print(random_email(7, "@pg.canterbury.ac.nz"))
    '''
    import random
    import string
    rndstring = ''
    for i in range(length):
        rndstring += random.choice(string.ascii_letters)
    return rndstring.lower() + atdomain

'''
print(random_email(7,"@pg.canterbury.ac.nz"))
for i in range(10):
    print(random_email(7, "@pg.canterbury.ac.nz"))
'''
email = {}
for i in range(10):
    email[i]= random_email(7, "@pg.canterbury.ac.nz")
print(email)