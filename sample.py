import regex as re


"""A more powerful kind of zero-width assertion is look around, a mechanism
with which it is possible to match a certain previous (look behind) or ulterior
(look ahead) value to the current position."""

# Look Ahead : The zero-width nature of the two look around operations render them complex and
#difficult to understand. The Syntax is (?=regex)

pattern=re.compile(r'fox')
res=pattern.search("The quick brown fox jumps over the lazy dog")
#print(res.start(),res.end())            # 16 and 19

# As Lookhead does not consumes the charcters  so we will only get the position of the string.

reg_pattern=re.compile(r'(?=fox)')
res=reg_pattern.search("The quick brown fox jumps over the lazy dog") 
#print(res.start(),res.end())        #16 16


""" The result has been
just a position at the index 16 (both the start and end point to the same index). This
is because look around does not consume characters, and therefore, it can be used to
filter where the expression should match. However, it will not define the contents of
the result. We can visually compare these two expressions in the following figure """


reg_pattern=re.compile(r"\w+(?=,)")
res=reg_pattern.findall("There were three friends Aryan, aman and Awasthi")
#print(res)  # ['Aryan,']  Here we can see that we are only getting string as output 


# Without the Regex_Pattern 
reg_pattern=re.compile("\w+,")
res=reg_pattern.findall("There are 3 friends : Aryan, Aman and Vimlesh")
#print(res)      #['Aryan,']   Here we can see that we are getting the string with , as the ouput

# With the procedding example w

pattern=re.compile(f"\w+(?=,|\.)")
res=pattern.findall("There are 3 friends: Aryan, Aman, and Vimlesh.")
#print(res)          #['Aryan', 'Aman', 'Vimlesh'] , Here we can find the values here.

# Negative Look Ahead: It behaves very similar to Positive Look Ahead but it will work only when we dont have a match,

pattern=re.compile(r'John(?!\sSmith)')
res=pattern.finditer("I would rather go out with John Maclane than with John Smith or John Bon Jovi")
#for i in res:
 #   print(i.start(),i.end())

#  <regex.Match object; span=(27, 31), match='John'>
#<regex.Match object; span=(64, 68),

pattern=re.compile(r'\d{1,3}')
res=pattern.findall("The number is 12345567890")
#print(res)

# Pyton Program to convert the string into two characters

pattern=re.compile(r"^\d{1,3}")
res=pattern.findall("13456789798")
#print(res)


# Finding 
pattern=re.compile(r'\d{1,3}(?=(\d{3})+(?!\d))')
res=pattern.finditer('134567890')



pattern = re.compile(r'\d{1,3}(?=(\d{3})+(?!\d))')
results=pattern.findall('1234567890')
#res=pattern.sub(r'\g<0>,', "1234567890")
#print(results)

# Look Behind Syntax: (?<=regex)
pattern=re.compile(r'(?<=John\s)McLane')
results=pattern.finditer("I would rather go out with John McLane than with John Smith or John Bon Jovi")
#for i in results:
#    print(i)


# Use the Not Operators 
pattern=re.compile(r'(?<=John\s)McLane')
results=pattern.finditer("I would rather go out with John McLane than with John Smith or John Bon Jovi")
#for i in results:
#    print(i)

# Look Around & Groups :

#INFO 2013-09-17 12:13:44,487 authentication failed
pattern=re.compile(r"\w+\s[\d-]+\s[\d:]+,[\d]+\s(.*\sfailed)")
res=pattern.match("INFO 2013-09-17 12:13:44,487 authentication failed")
print(res)      #<regex.Match object; span=(0, 50), match='INFO 2013-09-17 12:13:44,487 authentication failed'>

# However, we want only to match when the failure is not an authentication error otherwise dont check for the string we have.
new_pattern=re.compile(r"\w+\s[\d-]+\s[\d:]+,[\d]+\s(.*(?<!authentication\s)failed)")
res=new_pattern.match("INFO 2013-09-17 12:13:44,487 authentication failed")
print(res)      # None 


# As we can see that during the matching pattern, and we will search only search if the error is Autentication.



