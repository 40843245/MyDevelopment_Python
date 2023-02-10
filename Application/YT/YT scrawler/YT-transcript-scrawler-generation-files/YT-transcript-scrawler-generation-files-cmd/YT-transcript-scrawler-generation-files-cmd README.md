# README
## This article talks importance notice. You must have to pay lot of attention on this article before use the YT-transcript-scrawler-generation-files-cmd-code.py
## Preparation
For convenience, I call YT-transcript-scrawler-generation-files-cmd-code.py as this file.

There are some preprations to do before using this file.

### 1) install Python modules (if neccessary) and import them.

#### For third-party modules

Here, I will use these third-party modules. 

Please install them before executing this file.

1.python-docx (For, write data into files with these extensions .docx .docx .html .pptx etc then auto-generate them)

2.youtube_transcript_api (To scrawl the transcript from YT via the specified YT link)

3.googletrans (It translates the language by google translator, more concisely to say, it connects to google translator server and translates)

4. scrapetube (To scrawl the data from YT via the ID of specified YT channel)

To install it, you can use the cmd in some kinds Terminal (such as anaconda Terminal).
  
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

    
### 2) To save you time, you don't have to write codes to import them. Just make sure these statements are written at the top of the code, if NOT, copy and paste these statement at the top of the code. (After the end of section #### 3) )
    
### 3) Make sure the location of my-developed .py files to ensure the module can be correctly found.

    
    
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
