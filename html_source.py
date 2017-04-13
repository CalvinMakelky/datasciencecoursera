from urllib import urlopen, urlretrieve

urladdr = 'https://docs.python.org/3/'

def print_html(urladdr):
    webpage = urlopen(urladdr)
    html = webpage.read()
    print html

print_html(urladdr)

def save_html(urladdr, localfile):
    urlretrieve(urladdr, localfile)

save_html(urladdr, r'E:\PythonPerl_Sp16\Lectures\lecture_11\index.html')
    
