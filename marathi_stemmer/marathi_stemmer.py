import codecs
import re

filename='marathi_text.txt'
file=codecs.open(filename,encoding='utf-8')
doc=file.read()



doc=re.sub(r'(\d+)',r'',doc)
doc=doc.replace(u',','')
doc=doc.replace(u'"','')
doc=doc.replace(u'(','')
doc=doc.replace(u')','')
doc=doc.replace(u'"','')
doc=doc.replace(u':','')
doc=doc.replace(u"'",'')
doc=doc.replace(u"‘‘",'')
doc=doc.replace(u"’’",'')
doc=doc.replace(u"''",'')
doc=doc.replace(u".",'')
doc=doc.replace(u"*",'')
doc=doc.replace(u"#",'')


doc=doc.split(u".")

tokens=[]
for each in doc:
        word_list=each.split(' ')
        tokens=tokens+word_list

for tok in tokens:
    tok=tok.strip()

for each in tokens:
     if '-' in each:
            tok=each.split('-')
            tokens.remove(each)
            tokens.append(tok[0])
            tokens.append(tok[1])



suffixes = {
    1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा",u"च"],
    2: [u"चा",u"चे",u"ने",u"नी",u"ना",u"ते",u"ीं",u"तील",u"ात",u"ाँ",u"ां",u"ों",u"ें",u"तच",u"ता",u"ही",u"ले"],
    3: [u"ाचा",u"ाचे",u"तील",u"ानी",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"तून",u"तील",u"तही",u"तपण",u"कडे",u"ातच",u"हून",u"पणे",u"ाही",u"ाले"],
    4: [u"मधले",u"ातील",u"च्या",u"न्या",u"ऱ्या",u"ख्या",u"वर",u"साठी",u"ातून",u"कडून",u"मुळे",u"वरून",u"ातील",u"नीही",u"ातही",u"ातपण",u"ाकडे",u"पाशी",u"ाहून",u"ापणे",u"मधला"],
    5: [u"ामधले",u"ाच्या",u"ान्या",u"ाऱ्या",u"ाख्या",u"ावर",u"ासाठी",u"पासून",u"ाकडून",u"ामुळे",u"ावरून",u"कडेही",u"ानीही",u"ापाशी",u"ामधला",u"मध्ये"],
    6: [u"पर्यंत",u"ापासून",u"ाकडेही",u"पूर्वक",u"लेल्या",u"ामध्ये"],
    7: [u"ापर्यंत",u"प्रमाणे",u"तसुद्धा",u"ापूर्वक",u"ालेल्या"],
    8: [u"ाप्रमाणे",u"ातसुद्धा"],
}


stems=[]
for word in tokens:
    for i in range(8,0,-1):
        if len(word) > i + 1:
             for suf in suffixes[i]:
                        if word.endswith(suf):
                            word=word[:-i]
    if word:
         stems.append(word)




#Write the stems in a file, change path accordingly.
filename=filename='output_stem.txt'
f=codecs.open(filename,"w",encoding='utf-8')
for stem in stems:
        f.write(str(stem))
        f.write(u"\u0020")
f.close()












