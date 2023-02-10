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
  
7) Auto_Add_Page_Number

  Method to alignment the text of header and footer. Then insert the elements to headers and footer.
  
8) def GetChannel

  Method to fetch all data of the YT channel in the specified YT channel ID (string type). Then store it to an attribute.
  
9) def GetAllVideoUrl_List

  Method to get all links of all videos in the specified YT channel ID (string type). Then store it to an attribute.
  
10) def YT_handler

  Method to handle all YT vidoes. This method will call the method YT_Video_Transcript.
  
11) def YT_Video_Transcript

  Method to fetch the transcipt of a given YT video link. Then write the result to a file.
  
12) def TryOpenUrl(self,base_channel_url,tar_channel_url,wantToOpen=1):

  Method to try to open url.
  
  The default value of wantToOpen is 1.
  
  If the value of the parameter wantToOpen is 1, then the webbrowser will open the url.
  
  NOTE that url = base_channel_url + tar_channel_url
  
13) def Set_DefaultValue(self,tar,defaultValue):

  Set the default value given by the parameter if tar is None, undefined or unassigned,.
  
  This method will check the tar is either None, undefined or unassigned. 
  
  If so, assign the defaultValue to tar.
  
  If NOT, nothing happens.
  
14) def Set_All_DefaultValues
  
  Set some attributes to default values. 
  
  I set some attributes to default values for the convenience of test.
  
  If you don't want to use the default values, you can uncomment the call.
  
15) def Print_Dict_ElemByElem

  Method to print all elements of the result returned from __dict__().

16)  def Print_Info(self,o,msg):

  Method to print the information of the parameter o.

# Attributes

## Content

  dic={
  
            "self.transcript_languages=":self.transcript_languages
            
            ,"self.base_channel_url=":self.base_channel_url
            
            ,"self.tar_channel_url=":self.tar_channel_url
            
            ,"self.wantToOpen=":self.wantToOpen
            
            ,"self.document_name=":self.document_name
            
            ,"self.document_ext=":self.document_ext
            
            ,"self.naming_method=":self.naming_method
            
            ,"self.tar_languanges=":self.tar_languanges
            
            ,"self.lines=":self.lines
            
            ,"self.headerList=":self.headerList
            
            ,"self.footerList=":self.footerList
            
            ,"self.fontList1=":self.fontList1
            
            ,"self.fontList2=":self.fontList2
            
            ,"self.base_watch_video_url=":self.base_watch_video_url
            
            ,"self.base_channel_url=":self.base_channel_url
            
            ,"self.videos=":self.videos
            
            ,"self.video_url_list=":self.video_url_list
            
        }
        
## Intro

NOTE that I will get the value of an attribute by the key of the dictionary returned from __dict__() method.

To avoid exceptions at runtime and unexpected results, I will NOT get the value of an attribute by directly access of the class.

For example, if I want to get the value of fontList2. 

I should type

  self.__dict__()["self.fontList2="] 

instead 
  
  self.fontList2
    
For convenience, I defined all keys which ends with an assignment symbol (i.e. =)

Although, direct access of most attribute has same results of get the value from the specified key in the dictionary self.__dict__(),

I have tested that for few attributes (such as self.videos, self.video_url_list) will NOT have same results by direct access and access from the dictionary.

since the types are different.

For example, type of self.videos and type of self.__dict__()['self.videos='] are different.

DON'T ask me why. I don't know. It amazed me.

## Functionality

"self.transcript_languages=":self.transcript_languages
            
            the source language of transcript of the video.
            
"self.base_channel_url=":self.base_channel_url
            
            The basic part of the YT url. I observed that for every YT channel has the self.base_channel_url
            
            self.base_channel_url="https://www.youtube.com/channel/"
            
            The url
            
            "https://www.youtube.com/channel/" + <channel-ID>
            
            can find specific YT channel.
           
"self.tar_channel_url=":self.tar_channel_url
            
            The desried target url we want to fetch.
            
"self.wantToOpen=":self.wantToOpen
                       
                       Set 1 to open the webbrowser of the YT channel.
                       
                       Set 0 to NOT open.
                       
"self.document_name=":self.document_name
            
            The document name you specified.
            
"self.document_ext=":self.document_ext
            
            A list of files extensions which determines that want kind of files it will generate.
            
"self.naming_method=":self.naming_method
    
            The naming method of file.
            
"self.tar_languanges=":self.tar_languanges

            A list of desired languages, the transcript are translated to respectively.            
            
            For example, if I set it to ['en','ja'].
            
            Then first record are translated into english then japanese respectively.
            
            And so second record. And so on.
           
"self.lines=":self.lines
 
            The maximum number of records it fetches.
            
"self.headerList=":self.headerList
            
            A list which indicates the information about the header for each file.
            
 "self.footerList=":self.footerList
 
            A list which indicates the information about the footer for each file.
 
 "self.fontList1=":self.fontList1
 
             Part 1. A list which indicates the information about text font for each file.
             
             It stores the status of the font size of text, the font body of text, the color of text, and the background color of text which highlights the text.
            
 "self.fontList2=":self.fontList2
 
            Part 1. A list which indicates the information about text font for each file.
            
            It stores the status of the font bold of text, the font underline of text, the font italic of text, and the font strike of the text.
            
 "self.base_watch_video_url=":self.base_watch_video_url
 
            A basic part of an url when watching YT video. All YT videos must start with 'https://www.youtube.com/watch?v='.
            
            self.base_watch_video_url = 'https://www.youtube.com/watch?v='
                       
 "self.base_channel_url=":self.base_channel_url
 
            The url which indicates the YT channel ID.
            
 "self.videos=":self.videos
            
            Information about the YT channel given the specifiied YT channel ID.
            
  "self.video_url_list=":self.video_url_list
  
            A list of url which indicates all YT videos of YT channel ID.
            
        
