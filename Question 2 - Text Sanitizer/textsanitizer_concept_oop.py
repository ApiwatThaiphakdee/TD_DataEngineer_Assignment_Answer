#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys, getopt, re

#Define Class สำหรับการทำ Text Sanitization
class TD_DataEngineer():
    
    def __init__(self,argv):
        
        #1.เรียกใช้ Method define_source_target เพื่อกำหนดแหล่งข้อมูลต้นทางและปลายทาง
        self.sourcetype = self.define_source_target(argv)[0]
        self.sourcename = self.define_source_target(argv)[1]
        self.targettype = self.define_source_target(argv)[2]
        self.targetname = self.define_source_target(argv)[3]
        
        #2.เรียกใช้ Method read_data_from_source เพื่ออ่านข้อมูลที่อยู่ใน source แล้วเก็บไว้ที่ตัวแปร sourcedata
        self.sourcedata = self.read_data_from_source(self.sourcetype,self.sourcename)
        
        #Run Loop เพื่อไล่ปรับปรุง Text และ Save ลง Target File ทีละบรรทัด
        for rawtext in self.sourcedata:
            
            #3.เรียกใช้ Method text_sanitization เพื่อเอาไว้ปรับปรุง format ของ text ตามที่ต้องการ
            self.sanitizedtext = self.text_sanitization(rawtext)
            
            #4.เรียกใช้ Method simple_statistic เพื่อเอาไว้นับความถี่ของตัวอักษรแต่ละตัวที่อยู่ใน text
            self.alphabetfrequencydictionary = self.simple_statistic(self.sanitizedtext)
            
            #5.เรียกใช้ Method save_sanitized_text_to_target เพื่อบันทึก text ที่ถูกปรับปรุงแล้วลงบนแหล่งข้อมูลปลายทาง
            self.save_sanitized_text_to_target(self.targettype,self.targetname,self.sanitizedtext)
            
            #6.แสดงข้อมูล Text ก่อน Sanitize / Text หลัง Sanitize / ความถี่ของตัวอักษรแต่ละตัวใน Text
            print("This is a text from source file =",rawtext.replace('\n',''))
            print("This is a text after sanitization =",self.sanitizedtext)
            print("This is a number of occurrence for each alphabet =",self.alphabetfrequencydictionary)
            for alphabet,occurrence in self.alphabetfrequencydictionary.items():
                print(f'Alphabet : {alphabet} , Occurrence : {occurrence}')
        
        return None
    
    # Define Method 1
    def define_source_target(self,argv):
        
        sourcetype = ''
        sourcename = ''
        targettype = ''
        targetname = ''
        
        try:
            opts, args = getopt.getopt(argv,"h:a:b:c:d:",["sfile=","sdatabase=","tfile=","tdatabase="])
        except getopt.GetoptError:
            print('Please Type : textsanitizer_concept_oop.py -a <sourcefile> -c <targetfile>')
            print('OR')
            print('Please Type : textsanitizer_concept_oop.py -a <sourcefile> -d <targetdatabase>')
            print('OR')
            print('Please Type : textsanitizer_concept_oop.py -b <sourcedatabase> -c <targetfile>')
            print('OR')
            print('Please Type : textsanitizer_concept_oop.py -b <sourcedatabase> -d <targetdatabase>')
            sys.exit(2)
            
        for opt, arg in opts:
            if opt == '-h':
                print('Please Type : textsanitizer_concept_oop.py -a <sourcefile> -c <targetfile>')
                print('OR')
                print('Please Type : textsanitizer_concept_oop.py -a <sourcefile> -d <targetdatabase>')
                print('OR')
                print('Please Type : textsanitizer_concept_oop.py -b <sourcedatabase> -c <targetfile>')
                print('OR')
                print('Please Type : textsanitizer_concept_oop.py -b <sourcedatabase> -d <targetdatabase>')
                sys.exit()
            elif opt in ('-a', '--sfile'):
                sourcetype = "textfile"
                sourcename = arg
            elif opt in ('-b', '--sdatabase'):
                sourcetype = "database"
                sourcename = arg
            elif opt in ('-c', '--tfile'):
                targettype = "textfile"
                targetname = arg
            elif opt in ('-d', '--tdatabase'):
                targettype = "database"
                targetname = arg
                
        return sourcetype,sourcename,targettype,targetname
    
    # Define Method 2
    def read_data_from_source(self,sourcetype,sourcename):
        
        if sourcetype == "textfile":
            print("Open Text File",sourcename)
            with open(sourcename, 'r', encoding='utf-8') as sourcefile:
                sourcedata = sourcefile.readlines()
            
        elif sourcetype == "database":
            print("Open Database",sourcename)
            print("This Feature Will Available For Future - Please Add Code Here")
            sourcedata = "Database Data"
            
        else:
            print("Open Both Text File And Database")
            print("This Feature Will Available For Future - Please Add Code Here")
            sourcedata = "Text & Database Data"
            
        return sourcedata
    
    # Define Method 3
    def text_sanitization(self,sourcedata):
        
        sanitizedtext = sourcedata.lower().replace('\t','_').replace('\n','')
        
        return sanitizedtext
    
    # Define Method 4
    def simple_statistic(self,sanitizedtext):
        
        r = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        
        sanitizedtextonlyalphabet = sanitizedtext.replace('_','').replace(' ','').replace('\n','')
        sanitizedtextonlyalphabet = r.sub('', sanitizedtextonlyalphabet)
        
        alphabetfrequencydictionary = {}
        
        for alphabet in set(sanitizedtextonlyalphabet):
            alphabetfrequencydictionary[alphabet] = sanitizedtextonlyalphabet.count(alphabet)
        
        alphabetfrequencydictionary = dict(sorted(alphabetfrequencydictionary.items(), key=lambda item: item[1]))
        
        return alphabetfrequencydictionary
    
    # Define Method 5
    def save_sanitized_text_to_target(self,targettype,targetname,sanitizedtext):
        
        if targettype == "textfile":
            print("Save Text File",targetname)
            with open(targetname, 'a+', encoding='utf-8') as targetfile:
                targetfile.seek(0,2)
                targetfile.write('\n')
                targetfile.write(sanitizedtext)
                
        elif targettype == "database":
            print("Save Database",targetname)
            print("This Feature Will Available For Future - Please Add Code Here")
            
        else:
            print("Save Both Text File And Database")
            print("This Feature Will Available For Future - Please Add Code Here")
            
        return None
    
#--------------------------------------------------------End Of Define Class----------------------------------------------------

TD_DataEngineer(sys.argv[1:])

# Define Constructor 
# 1.เรียกใช้ Method define_source_target เพื่อกำหนดแหล่งข้อมูลต้นทางและปลายทาง
# 2.เรียกใช้ Method read_data_from_source เพื่ออ่านข้อมูลที่อยู่ใน source แล้วเก็บไว้ที่ตัวแปร sourcedata
# 3.เรียกใช้ Method text_sanitization เพื่อเอาไว้ปรับปรุง format ของ text ตามที่ต้องการ
# 4.เรียกใช้ Method simple_statistic เพื่อเอาไว้นับความถี่ของตัวอักษรแต่ละตัวที่อยู่ใน text
# 5.เรียกใช้ Method save_sanitized_text_to_target เพื่อบันทึก text ที่ถูกปรับปรุงแล้วลงบนแหล่งข้อมูลปลายทาง
    
# Method 1.เก็บ Arguments จาก CLI เข้ามาที่ตัวแปร source และ target (สามารถระบุชื่อและประเภทของแหล่งต้นทาง / ชื่อและประเภทของแหล่งปลายทาง)
# Method 2.เริ่มการอ่านข้อมูลที่อยู่ใน source แล้วเก็บไว้ที่ตัวแปร sourcedata (สามารถอ่านข้อมูลจากแหล่งต้นทางแต่ละประเภทที่มีอยู่ใน Method 1 ได้)
# Method 3.เริ่มปรับปรุง data โดยการเปลี่ยนเป็นตัวพิมพ์เล็กทั้งหมดจากนั้นแทนที่ Tab ด้วย "__" จากนั้นลบการขั้นบรรทัดใหม่
# Method 4.เริ่มปรับนับความถี่เฉพาะตัวอักษรแต่ละตัวที่อยู่ใน data โดยไม่นับช่องว่างและอักขระพิเศษต่างๆพร้อมทั้งเรียงลำดับจากตัวที่มีความถี่น้อยไปมาก
# Method 5.เริ่มบันทึก data ที่ถูกปรับปรุงแล้วลงบน target (สามารถบันทึกข้อมูลลงแหล่งปลายทางแต่ละประเภทที่มีอยู่ใน Method 1 ได้)

