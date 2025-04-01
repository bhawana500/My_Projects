email=input("Enter your Email Here: ")
invalid=0
count_a=0
place_a=0
for i in range(len(email)):
    if email[i]=='@':
        count_a+=1
        place_a=i
email_extensions = [".co", ".io", ".ai", ".us", ".uk", ".in", ".ca", ".au", ".de", ".fr", ".jp", ".cn", ".br", ".ru",  
".ch", ".se", ".no", ".dk", ".fi", ".pl", ".it", ".es", ".mx", ".tr", ".sa", ".ae", ".pk", ".bd", ".lk", ".ng", ".gh",  
".biz", ".tv", ".me", ".cc", ".ws", ".eu", ".nz", ".za", ".sg", ".my", ".id", ".ph", ".th", ".vn",  
".gov", ".edu", ".com", ".net", ".org", ".mil", ".intl",  
".mobi", ".name", ".info", ".tech", ".xyz", ".apps"
]
extension=''
for i in email_extensions:
    if i in email:
        extension=i
temp=[]
for i in email:
    temp.append(i)
temp=temp[:-(len(extension))]
temp=''.join(temp)
username=temp[:place_a]
sld=temp[place_a+1:]
if count_a!=1 or count_a==0 or len(sld)==0 or len(username)==0 or username[0]=='.' or username[-1]=='.' or temp=='' or sld[0]=='_' or sld[-1]=='_':
    invalid+=1
if '..' in email or '__' in email:
    invalid+=1
if len(email)<6 or len(email)>320:
    invalid+=1
invalid_username_characters = [" ", ",", ":", ";", "!", "#", "$", "%", "^", "&" 
"*", "(", ")", "[", "]", "{", "}", "\"", "'",
"<", ">", "\\", "/", "|", "~", "=","+", "`"]
for i in username:
    if i in invalid_username_characters:
        invalid+=1
invalid_domain_characters = [" ", ",", ":", ";", "!", "@", "(", ")", "[", "]", "{", "}", "\"", "'", "<", ">", "\\", "/", "|", "~",'_']
for i in email[place_a+1:]:
    if i in invalid_domain_characters:
        invalid+=1
if invalid>0:
    print("Your Email is Invalid")
else:
    print("You have a Valid Email")