#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys, getopt, re

#function เสริมเอาไว้สำหรับการทำ Text Sanitization
def text_sanitization(sourcetext):
    targettext = sourcetext.lower().replace('\t','_').replace('\n','')
    return targettext

#function เสริมเอาไว้สำหรับการทำ Simple Statistic
def simple_statistic(targettext):
    targettext_onlyalphabet = targettext.replace('_','').replace(' ','').replace('\n','')
    r = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    targettext_onlyalphabet = r.sub('', targettext_onlyalphabet)
    alphabet_frequency_dictionary = {}
    for alphabet in set(targettext_onlyalphabet):
        alphabet_frequency_dictionary[alphabet] = targettext_onlyalphabet.count(alphabet)
    alphabet_frequency_dictionary = dict(sorted(alphabet_frequency_dictionary.items(), key=lambda item: item[1]))
    return alphabet_frequency_dictionary

#function หลักของ application program
def main(argv):
    # เริ่มการอ่าน Arguments จาก CLI แล้วจากนั้นจึงเก็บเข้ามาที่ตัวแปร sourcefile และ targetfile เพื่อนำไปใช้อ่านไฟล์ต่อ
    sourcefile = ''
    
    targetfile = ''
    
    try:
        opts, args = getopt.getopt(argv, "h:s:t:",["sfile=","tfile="])
        
    except getopt.GetoptError:
        print('GetoptError textsanitizer.py -s <sourcefile> -t <targetfile>')
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print('textsanitizer.py -s <sourcefile> -t <targetfile>')
            sys.exit()
        elif opt in ('-s', '--sfile'):
            sourcefile = arg
        elif opt in ('-t', '--tfile'):
            targetfile = arg
    # จบการอ่าน Arguments จาก CLI แล้วจากนั้นจึงเก็บเข้ามาที่ตัวแปร sourcefile และ targetfile เพื่อนำไปใช้อ่านไฟล์ต่อ
    
    # เริ่มการอ่าน Text ที่อยู่ใน sourcefile แล้วเก็บไว้ที่ตัวแปร sourcetext จากนั้นทำ text sanitization และ simple statistic
    with open(sourcefile, 'r', encoding='utf-8') as source_file:
        
        sourcetext = source_file.readlines()
        
        for text in sourcetext:
            targettext = text_sanitization(text)
            alphabet_frequency_dictionary = simple_statistic(targettext)
            print("This is a text from source file =",text.replace('\n',''))
            print("This is a text after sanitization =",targettext)
            print("This is a number of occurrence for each alphabet not include space & tab =",alphabet_frequency_dictionary)
            for alphabet,occurrence in alphabet_frequency_dictionary.items():
                print(f'Alphabet : {alphabet} , Occurrence : {occurrence}')
                
            # เริ่มการ Save sanitized text ลงบน targetfile
            with open(targetfile, 'a+', encoding='utf-8') as target_file:
                target_file.seek(0,2)
                target_file.write('\n')
                target_file.write(targettext)
            # จบการ Save sanitized text ลงบน target file
    # จบการอ่าน Text ที่อยู่ใน sourcefile แล้วเก็บไว้ที่ตัวแปร sourcetext จากนั้นทำ text sanitization และ simple statistic และ save ลง file
            
if __name__ == "__main__":
    main(sys.argv[1:])

