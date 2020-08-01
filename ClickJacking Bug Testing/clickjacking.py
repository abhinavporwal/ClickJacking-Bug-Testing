from urllib.request import urlopen
from sys import argv,exit

__author__="Cyber Asset - Abhinav Porwal"

def checking(url):
    "to check if url is vulnerable or not"

    try:
        if "http" not in url:
            url="http://"+url
        data=urlopen(url)
        headers=data.info()
        if "X-Frame-Options" not in headers:
            return True
    except:
        return False


def proof(url):
    payload="""
    <html>
      <head>
        <title>Click Jacking Test Page</title>
      </head>
      <body>
        <p>Website is Vulerable to clickjacking...</p>
        <iframe src="http://{}" width="500" height="500"></iframe>

      </body>
    </html> """.format(url)
    with open(url +".html" ,"w") as file:
        file.write(payload)
        file.close()

def main():
    try:
        sites=open(argv[1] , 'r').readlines()
    except:
        print("[*] Usage: python(3) clickjacking.py <file_name>");exit(0)

    for site in sites[0:]:
        print("[*] Checking " + site)
        status=checking(site)

        if(status):
            print("  [+] Website is Vulnerable!!")
            proof(site.split('\n')[0])

            print("  [+] Proof Created and Saved as <URL>.html\n")
        elif not status:
            print("  [-] Website is not Vulnerable!\n")

        else:
            print("Python Crashed please Re-Launch")

if __name__=='__main__':main()
