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

To install it, you can use the cmd in some kinds Terminal (such as anaconda Terminal)
  pip install [<parameter>] <package-to-install>
  
  
Before installing it, check the requirements and visit the documents.

Here, I will use these built-in modules. 
1. re
2. sys
3. webbrowser

Here, I will use my-developed module (The .py file with is written by myself)
1. ORDER_class

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
