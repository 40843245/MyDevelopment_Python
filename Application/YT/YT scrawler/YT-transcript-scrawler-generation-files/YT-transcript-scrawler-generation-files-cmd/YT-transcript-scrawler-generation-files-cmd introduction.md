# Objectives
I will introduce my development tool YT-transcript-scrawler-generation-files-cmd-code1.py

# Code 

  YT-transcript-scrawler-generation-files-cmd-code1.py
  
  ORDER_class.py

# Classes
In ORDER_class.py, it only contains the enum class 
   
   class ORDER():
   
        ASCENDING="ASCENDING"
        
        ASCENDING_FROM_1="ASCENDING_FROM_1"
        
        DESCENDING="DESCENDING" 
        
        DESCENDING_BRACKET_WHEN_NEED="DESCENDING_BRACKET_WHEN_NEED"
        
        ARBIRTARY="ARBIRTARY" #Specify the name
        
        RANDOM="RANDOM"

# Methods
In YT-transcript-scrawler-generation-files-cmd-code1.py

## Content
  class YT_video():
       
       def Print_Info(self,o,msg):
       
       def __dict__(self):
       
       def Print_Dict_ElemByElem(self):
       
       def __init__(self,transcript_languages,base_channel_url
                 ,tar_channel_url
                 ,wantToOpen,document_name: str
                 ,document_ext : list 
                 ,naming_method : ORDER_class.ORDER
                 ,tar_languanges : list
                 ,lines:int
                 ,headerList:list
                 ,footerList:list
                 ,fontList1:list
                 ,fontList2:list
                 ):
                 
       def Set_DefaultValue(self,tar,defaultValue):
       
       def Set_All_DefaultValues(self):
       
       def ConcatentateListToLetter(self,otherOptions):
       
       def create_element(self,name):
       
       def create_attribute(self,element, name, value):
       
       def add_page_number(self,run,options):
       
       def GetChannel(self):
       
       def GetAllVideoUrl_List(self):
       
       def YT_handler(self):
       
       def YT_Video_Transcript(self,video_url,
                            document_name
                            ,document_ext
                            ,transcript_language
                            ,tar_languages
                            ,lines:int
                            ,headerList
                            ,footerList
                            ,fontList1
                            ,fontList2
                            ):
       def Auto_Add_Page_Number(self,options):
       
       def TryOpenUrl(self,base_channel_url,tar_channel_url,wantToOpen=1):

## Functionality

1) def __init__ 

    The constructor of the class.
    
    The __init__ is the special name in Python.
    
2) def __dict__
 
  It returns a dictionary of the class.
  
  Here, in this code, I get the attribute by the dictionary returned from __dict__() method.
  
  Thus, you don't change the code of __dict__(). Otherwise, it may cause unexpected results.
  
  
3) def ConcatentateListToLetter 
 
  My own method to concatenate all elements of list to string and help us to insert the OXMLElement with the method add_page_number.
 
  So that, we can add header and footer.

4)def create_element

  Utility method for the method add_page_number.
  
5)def create_attribute

  Utility method for the method add_page_number.
  
6) def add_page_number

  Method to add headers and footers to Microsoft word.
  
7) def GetChannel

  Method to fetch all data of the YT channel in the specified YT channel ID (string type). Then store it to an attribute.
  
8) def GetAllVideoUrl_List

  Method to get all links of all videos in the specified YT channel ID (string type). Then store it to an attribute.
  
9) def YT_handler

  Method to handle all YT vidoes. This method will call the method YT_Video_Transcript.
  
10) def YT_Video_Transcript

  Method to fetch the transcipt of a given YT video link. Then write the result to a file.
  
  

# Attribute


