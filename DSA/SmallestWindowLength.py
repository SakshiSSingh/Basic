s = 'lcpsklryvmcpjnbpbwllsrehfmxrkecwitrsglrexvtjmxypunbqfgxmuvgfajclfvenhyuhuorjosamibdn'
s1=''
for i in s:
    s1+=i
    print(i, len(set(s1)), len(set(s)))
    if len(set(s1))==len(set(s)):
        print(len(s1))
        break
