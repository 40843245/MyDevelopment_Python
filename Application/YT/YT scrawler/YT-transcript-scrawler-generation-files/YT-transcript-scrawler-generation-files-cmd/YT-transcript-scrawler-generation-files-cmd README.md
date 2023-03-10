# README
## This article talks importance notice. You must have to pay lot of attention on this article before use the YT-transcript-scrawler-generation-files-cmd-code.py
## Preparation
For convenience, I call YT-transcript-scrawler-generation-files-cmd-code.py as this file.

There are some preprations to do before using this file.

### 1) Check google translator can translate words.

Link:
https://translate.google.com/

Since when using the googletrans module, the google server is connected.

### 2) Turn on either Wifi or Hotspot of your device while running and check it is stable.

If the connection is NOT stable or is disconnected, the an exception will be thrown at runtime.

The googletrans requires connection while running since it uses google translators at runtime.

### 3) install Python modules (if neccessary) and import them.

#### For third-party modules

Here, I will use these third-party modules. 

Please install them before executing this file.

    1.python-docx (For, write data into files with these extensions .docx .docx .html .pptx etc then auto-generate them)

    2.youtube_transcript_api (To scrawl the transcript from YT via the specified YT link)

    3.googletrans (It translates the language by google translator, more concisely to say, it connects to google translator server and translates)

    4. scrapetube (To scrawl the data from YT via the ID of specified YT channel)

To install it, you can use the cmd in some kinds Terminal (such as anaconda Terminal). Use the pip cmd.
  
    pip install {<parameter>} <package-to-install> {<parameter>}

where 
  
  {} refers it is NOT required.
  
  <parameter> refers the parameters of the cmd.
    
  For more details, google it. I will skip the technique of cmd.

To install it with newer version of Python IDE. Use pip3.
    
    pip3 install {<parameter>} <package-to-install> {<parameter>}
  
Before installing it, check the requirements and visit the documents.

#### For built-in modules
    
Here, I will use these built-in modules. 
    
    1. re
    
    2. sys
    
    3. webbrowser (To open the webbrowser via the link)
    
#### For my-developed modules
    
Here, I will use my-developed module (The .py file with is written by myself)
    
    1. ORDER_class (called ORDER_class.py)

    
### 4) To save you time, you don't have to write codes to import them. Just make sure these statements are written at the top of the code, if NOT, copy and paste these statement at the top of the code. (After the end of section #### 3) )
    
### 5) Make sure the location of my-developed .py files to ensure the module can be correctly found.

Here is the top of the codes.
    
    from __future__ import absolute_import

    from lxml import etree

    import re

    import docx

    from docx.compat import Unicode
    
    from docx.oxml import OxmlElement
    
    from docx.oxml.exceptions import InvalidXmlError
    
    from docx.oxml.ns import NamespacePrefixedTag, nsmap, qn
    
    from docx.shared import lazyproperty

    from docx.oxml import ns

    import sys

    import json

    import docx

    from docx import shared

    from docx import Document

    from docx.shared import Inches

    from docx import section

    from docx.enum.section import WD_SECTION

    from youtube_transcript_api import YouTubeTranscriptApi

    from googletrans import Translator

    import scrapetube

    import webbrowser

    import ORDER_class

 Here is the code of ORDER_class.py (it only contains an enum class.)
    
    class ORDER():
    
        ASCENDING="ASCENDING"
    
        ASCENDING_FROM_1="ASCENDING_FROM_1"
    
        DESCENDING="DESCENDING" 
    
        DESCENDING_BRACKET_WHEN_NEED="DESCENDING_BRACKET_WHEN_NEED"
    
        ARBIRTARY="ARBIRTARY" #Specify the name
    
        RANDOM="RANDOM"
    
## When Testing,
### 1) Don't translate too many lines at once with the module googletrans. Otherwise,the exception throws. I remembered the exception is called HTTPSERVERERROR.
    
I guess the reason is uses google translators and the google translators can NOT translate too many letters at once.
    
I still remembered that I copied lots of texts from a website and pasted it to the google translates, then it tells me that 
    
it can NOT translate at most 3900 word. (I forgot it is 3900 words).
    
## Tested data of the variable lines.

The variable in this file named lines indicates the maximum number of records of transcript (for each videos) will be fetched (from top to down)
    
 For example, if I set the variable lines = 10.
    
 My code will fetch at most top 10 records of transcript for each video (even though there are 1000 records of transcript of the video).
    
I have tested that in my notebook in spyder, at runtime, there are NO any exceptions when I set the variable lines to 
    
    1 and 10
 
 And there are exceptions when I set the variable lines to
    
    100 , 1000 , 10000 , 100000
    
  For error message, see the figure in the Github.
    
    
  ## Ref to Python module
    
  I really appreciate these attributors developes these third-party modules.
    
  So that, I can easily understand and use. Also, it saves me lots of time. (Though, I spent lots of time and writes lots of lines of the code.)
    
  scrapetube
    
    https://pypi.org/project/scrapetube/
    
  youtube-transcript-api
    
    https://pypi.org/project/youtube-transcript-api/
    
  python-docx
    
    https://pypi.org/project/python-docx/
    
  ## Thought to attributor of python-docx.
    
  The python-docx module provides lots of functionality to help me to achieve my code.
    
   Although, the documentation does NOT offer many examples and outputs so that 
    
   I spent some time on finding the way how to use it (,especially how to set the font and color of the text.).
    
   I must really appreciate it.
    
   And I think the attributor is very expertised at Python.
   
    

