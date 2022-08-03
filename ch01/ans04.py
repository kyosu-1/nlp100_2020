import re


one_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine.\
 New Nations Might Also Sign Peace Security Clause. Arthur King Can."

s = re.sub(r'[,\.]', '', s)
s = s.split()

ans = {
    word[0] if i+1 in one_list else word[:2]: i+1
    for i, word in enumerate(s)
}
print(ans)
