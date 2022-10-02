letters={'A':'G','B':'H','C':'I','D':'J','E':'K','F':'L','G':'M','H':'N','I':'O',
         'J':'P','K':'Q','L':'R','M':'S','N':'T','O':'U','P':'V','Q':'W','R':'X',
         'S':'Y','T':'Z','U':'A','V':'B','W':'C','X':'D','Y':'E','Z':'F','a':'g',
         'b':'h','c':'i','d':'j','e':'k','f':'l','g':'m','h':'n','i':'o','j':'p',
         'k':'q','l':'r','m':'s','n':'t','o':'u','p':'v','q':'w','r':'x','s':'y',
         't':'z','u':'a','v':'b','w':'c','x':'d','y':'e','z':'f',' ':' '}

def encrypt(string):
    str1=""
    for i in string:
        m=ord(letters[i])-65
        n=chr(m+65)
        str1=str1+n
    print("Encrypted text:",str1)
    return str1
    
def decrypt(c):
    str2=""
    for j in c:
        value=[i for i in letters if letters[i]==j]
        str2=str2+value[0]
    print("Decrypted text:",str2)

string=input("Enter string:")
c=encrypt(string)
decrypt(c)

    





