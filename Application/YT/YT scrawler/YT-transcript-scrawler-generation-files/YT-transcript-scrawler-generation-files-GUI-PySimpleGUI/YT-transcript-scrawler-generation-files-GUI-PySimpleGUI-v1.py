import PySimpleGUI as sg
import os
import os.path
import json
import ORDER_class
import docx

def main():
    
    def ListElem(o):
        if isinstance(o,str):
            o=o.strip('"').strip("'")
            if o=="True":
                return '1'
            elif o=="False":
                return '0'
            
            return o
        
        #### NOTE that isinstance(o,bool) must be checked before isinstance(o,int)
        #### since if the x is bool type, then x must be a int type.
        if isinstance(o,bool):
            if o==True:
                tf='1'
            else:
                tf='0'
            return tf
    
        if isinstance(o,int):
            return o
        
        if isinstance(o,list):
            return o
        if isinstance(o,tuple):
            return o
        
    def IsHexDigit(c):
        unic=ord(c)
        if (48<=unic and unic<=57) or (65<=unic and unic<=69) or (97<=unic and unic<=101):
            return True
        return False
    
    def SplitDigit(s,many):
        li=[ s[idx:min(idx+many,len(s))] for idx in range(0,len(s),many)]
        return li
    
    def HexString2DecNumber(s,many):
        s=s.lstrip("#")
        numSymbolSign=s[0:2]
        s=s[2:]  
        li=SplitDigit(s=s,many=many)
        n_li=[ int(numSymbolSign+l_elem,0) for l_elem in li ]
        return n_li
    
    def CheckValid_ColorHexString2DecNumber(hexColor):
        if not isinstance(hexColor,str):
            return False
        if len(hexColor)!=9:
            return False
        if hexColor[0]!="#":
            return False
        if hexColor[1]!="0":
            return False
        if hexColor[2]!="x" and hexColor[2]!="X" :
            return False
        for idx in range(3,9,1):
            c=hexColor[idx]
            v=IsHexDigit(c)
            if v==False:
                return False
        n_li=HexString2DecNumber(hexColor,2)     
        return n_li
    
    def IsNullOrEmpty(s):
        if s==None:
            return True
        if isinstance (s,str) and s=="":
            return True
        if isinstance(s,(list,tuple,set)) and len(s)==0:
            return True
        
        return False
    
    def Check_Valid_Before_Generate():
        print(values)
        for k,v in values.items():
            if IsNullOrEmpty(v):
                return False
        
        return True
    
    def OpenErrorWindow(tb,e):
        sg.popup_error(f'AN EXCEPTION OCCURRED!', e,tb)
        
    def GenerateFile(translated_cmd_argv_str):
        print(translated_cmd_argv_str)
        os.system(translated_cmd_argv_str)
         
    def Write_Command():
        whitespace=" "
        emptyString=""
        semicolon=":"
        delim=whitespace
        file_name=r"C:\Users\user\youtube_transcript_command_test3.py"      
        
        translated_cmd_argv=list()
        
        translated_cmd_argv.append('"'+"python"+'"')   
        translated_cmd_argv.append('"'+file_name+'"')
        translated_cmd_argv.append('"'+ORDER_class.ORDER.ASCENDING_FROM_1+'"')
        
        values_list=[
              values[YTChannelLink_key],
              values[FilePath_key],
              values[DocName_key],
              values[DocExt_key],
              ['ja'],
              values[TarLang_key],
              values[NeedHeader_key],
              values[HeaderFormat_Alignment_key],
              values[HeaderFormat_NeedCurrentPage_key],
              values[HeaderFormat_NeedSeperator_key],
              values[HeaderFormat_NeedTotalPage_key],
              values[NeedFooter_key],
              values[FooterFormat_Alignment_key],   
              values[FooterFormat_NeedCurrentPage_key],
              values[FooterFormat_NeedSeperator_key],
              values[FooterFormat_NeedTotalPage_key],
              
              values[FontSize_key],
              values[FontBody_key],
              values[FontTextColor_key],
              values[FontBackgroundColor_key],
              
              values[FontBold_key],
              values[FontUnderline_key],
              values[FontItalic_key],
              values[FontStrike_key]
              
              ]
        
        for v in values_list:
            v=ListElem(v)
            
            """
            print("~~~~")
            print(v)
            print("------")
            print(v)
            print("~~~~")
            """
            
            if isinstance(v,str):
                v=v.strip("\n")
                v=v.strip("\t")
                v=v.rstrip(" ")
                
            translated_cmd_argv.append(v)
        
        print("@@@@Before (translated_cmd_argv)")
        print(translated_cmd_argv)
        
        ## Convert x then strip " and ' for all elements x in the list.
        translated_cmd_argv=[str(x).strip("'").strip('"')for x in translated_cmd_argv]
        
        print("@@@@After (translated_cmd_argv)")
        print(translated_cmd_argv)
        
        ## Join the list into string.
        translated_cmd_argv_str=str(translated_cmd_argv[0])+' "'+'" "'.join(translated_cmd_argv[1:])+'"'
        
        print("@@@@After (translated_cmd_argv_str)")
        print(translated_cmd_argv_str)
        ## command with string type
        return translated_cmd_argv_str
    
    def FontWindow():
       ###
       submitButton="Submit"
       cancelSubmitButton="Cancel"
       
       FontTextColor_key="--FONT TEXT COLOR--"
       FontBackgroundColor_key="--FONT BACKGROUND COLOR--"
       ###
       layout=[
           [
               sg.Text("Font Size:"),
               sg.Input(key="--FONT SIZE--",size=(10,1)),
               sg.Text("Font BODY:"),
               sg.Input(key="--FONT BODY--",size=(20,1)),
               sg.Text("Font text color:"),
               sg.Input(key=FontTextColor_key,size=(10,1)),
               sg.Text("Font background color:"),
               sg.Input(key=FontBackgroundColor_key,size=(10,1))
           ],
           [
               sg.Button(submitButton),
               sg.Button(cancelSubmitButton)
           ]
       ]
       fontWindow = sg.Window('Font Title', layout,modal=True)
       while True:
           event, values = fontWindow.read()
           
           if event == sg.WIN_CLOSED:       
               break
           
           if event == cancelSubmitButton:
               
               ret_val=tuple("" for _ in range(0,len(values.keys()),1))
               fontWindow.close()
               return ret_val
           
           if event == submitButton:
               ok=True if CheckValid_ColorHexString2DecNumber(values[FontTextColor_key]) and CheckValid_ColorHexString2DecNumber(values[FontBackgroundColor_key]) else False
                               
               if ok:
                   ret_val=tuple(v for v in values.values())   
                   fontWindow.close()
                   return ret_val
               else:
                   OpenErrorWindow(tb="traceback on the last: fontWindow",
                                   e="There are invalid value in the field about colors. Valid format such as #0x112233.")
                   
           
       fontWindow.close()
       return tuple(k for k in range(0,4,1))    
   
    def Select_ScrollBar_Window(li):
        submitButton="Submit"
        checkbox_key="SELECTED"
        if isinstance(li,list)==False:
            raise TypeError
        
        column1 = [
            [sg.Checkbox(c,key=c)] for c in li 
        ]
        layout = [
            [
                sg.Column(column1, scrollable=True,  vertical_scroll_only=True),
            ]
            ,
            [
                sg.Button(submitButton)
            ]
        ]
        
        window = sg.Window('Scrollable', layout)
        while True:
            event,values=window.read()
            
            if event == sg.WIN_CLOSED:
                window.close()
                break
            
            if event == submitButton:
                ret_val=list(k for k in values.keys() if bool(values[k])==True)
                ret_val=str(ret_val)
                ret_val=ret_val.replace(" ","")
                ret_val=json.dumps(ret_val)
                ret_val=ret_val.strip('"')
                ret_val=ret_val.strip("'")
                window.close()
                return ret_val
            
        return list() 
    
    ####
    def FetchData():
        ###
        emptyString=""
        whitespace=" "
        ###
        
        updateMessage=emptyString
        
        updateMessage=updateMessage+"YT channel link:"
        updateMessage=updateMessage+"\n"
        updateMessage=updateMessage+values[YTChannelLink_key]
        updateMessage=updateMessage+"\n"
        updateMessage=updateMessage+"Document name:"
        updateMessage=updateMessage+"\n"
        updateMessage=updateMessage+values[DocName_key]
        updateMessage=updateMessage+"\n"
        updateMessage=updateMessage+"Document extension:"
        updateMessage=updateMessage+"\n"
        updateMessage=updateMessage+values[DocExt_key]
        updateMessage=updateMessage+"\n"
        updateMessage=updateMessage+"Language list:"
        updateMessage=updateMessage+"\n"
        updateMessage=updateMessage+values[TarLang_key]
        updateMessage=updateMessage+"\n"
        
        updateMessage=updateMessage+"Need Header:"+(("True,"+"Header Cuurent Page:"+ str(values[HeaderFormat_NeedCurrentPage_key])
                                                     +",Header Seperator:"+str(values[HeaderFormat_NeedSeperator_key])
                                                     +",Header Total Page:"+str(values[HeaderFormat_NeedTotalPage_key])
                                                     +",Header Alignment:"+str(values[HeaderFormat_Alignment_key])
                                                     ) if values[NeedHeader_key]==True else "False")
        updateMessage=updateMessage+"\n"
        
        updateMessage=updateMessage+"Need Footer:"+(("True,"+"Footer Cuurent Page:"+ str(values[FooterFormat_NeedCurrentPage_key])
                                                     +",Footer Seperator:"+str(values[FooterFormat_NeedSeperator_key])
                                                     +",Footer Total Page:"+str(values[FooterFormat_NeedTotalPage_key])
                                                     +",Footer Alignment:"+str(values[FooterFormat_Alignment_key])
                                                     ) if values[NeedFooter_key]==True else "False")
        updateMessage=updateMessage+"\n"
        updateMessage=updateMessage+"About the font:"
        updateMessage=updateMessage+"\n"
        updateMessage=updateMessage+"Bold?"+str(values[FontBold_key])
        updateMessage=updateMessage+whitespace
        updateMessage=updateMessage+"Underline?"+str(values[FontUnderline_key])
        updateMessage=updateMessage+whitespace
        updateMessage=updateMessage+"Italic?"+str(values[FontItalic_key])
        updateMessage=updateMessage+whitespace
        updateMessage=updateMessage+"Strike?"+str(values[FontStrike_key])
        updateMessage=updateMessage+"\n"
        
        window[OutputMessage_key].update(updateMessage)
        
        updateMessage=emptyString
        window.refresh()    
    ####
    
    #### driver code
    ###
    ext_list=['.docx','.doc','.html','.txt','.pptx','.ppt']
    tar_list=['en','zh-tw','ja','ko']
    WD_ALIGN_PARAGRAPH_list=[docx.enum.text.WD_ALIGN_PARAGRAPH.LEFT
                             ,docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
                             ,docx.enum.text.WD_ALIGN_PARAGRAPH.RIGHT]
    emptyString="" 
    ###
    submitButton="Submit"
    generationFileButton="Generate File"
    browseFilePathButton="Browse"
    clearSubmitButton="Clear Submit"
    clearDocNameButton="Clear Doc Name"
    selectDocExtButton="Doc Extension"
    clearAllButton="Clear All"
    closeButton="Close"
    selectFont="Font"
    selectTarLangButton="Target Language"
    selectHeaderAlignmentButton="Header Alignment"
    selectFooterAlignmentButton="Footer Alignment"
    
    
    
    YTChannelLink_key="--YT channel link--"
    FilePath_key="--File Path--"
    
    DocName_key="--Document name--"
    DocExt_key="-Document extension-"
    TarLang_key="--Target Language--"

    FontSize_key="--FONT SIZE--"
    FontBody_key="--FONT BODY--"
    FontTextColor_key="--FONT TEXT COLOR--"
    FontBackgroundColor_key="--FONT BACKGROUND COLOR--"
    OutputMessage_key="-OUTPUT MESSAGE-"
    
    NeedHeader_key="--NEED HEADER--"
    HeaderFormat_Alignment_key="--Header Format Alignment--"
    HeaderFormat_NeedCurrentPage_key="--HEADER FORMAT Need Current Page--"
    HeaderFormat_NeedSeperator_key="--HEADER FORMAT Need Seperator Page--"
    HeaderFormat_NeedTotalPage_key="--HEADER FORMAT Need Total Page--"
    
    NeedFooter_key="--NEED FOOTER--"
    FooterFormat_Alignment_key="--Footer Format Alignment--"
    FooterFormat_NeedCurrentPage_key="--Footer FORMAT Need Current Page--"
    FooterFormat_NeedSeperator_key="--Footer FORMAT Need Seperator Page--"
    FooterFormat_NeedTotalPage_key="--Footer FORMAT Need Total Page--"
    
    FontBold_key="--Font Bold--"
    FontUnderline_key="--Font Underline--"
    FontItalic_key="--Font Italic--"
    FontStrike_key="--Font Strike--"
    
    layout = [  
        [
            sg.Text("YT channel link:"),    
            sg.Input(key=YTChannelLink_key,size=(150,1)),
            sg.Button(submitButton),
            sg.Button(clearSubmitButton)
        ],
        [
             sg.Text("Path where auto-generation file locates:"),
             sg.Input(key=FilePath_key,size=(60,1),readonly=True,use_readonly_for_disable=False,change_submits=True),
             sg.Button(browseFilePathButton)
        ],
        [
            sg.Text("Document name:"),
            sg.Input(key=DocName_key,size=(20,1)),
            sg.Button(clearDocNameButton),
            sg.Text("Document extension:"),
            sg.Input(key=DocExt_key,size=(60,1),readonly=True,use_readonly_for_disable=False,change_submits=True),
            sg.Button(selectDocExtButton)
        ],
        [
            sg.Text("Language for transcript"),
            sg.Input(key=TarLang_key,size=(120,1),readonly=True,use_readonly_for_disable=False,change_submits=True),
            sg.Button(selectTarLangButton)
        ],
        [
            sg.Text("Need footer?"),
            sg.Checkbox("Yes",key=NeedFooter_key),
            sg.Text("Format:"),
            sg.Checkbox("Current Page?",key=FooterFormat_NeedCurrentPage_key),
            sg.Checkbox("Seperator?",key=FooterFormat_NeedSeperator_key),
            sg.Checkbox("Total Page?",key=FooterFormat_NeedTotalPage_key),
            sg.Input(key=FooterFormat_Alignment_key,readonly=True,use_readonly_for_disable=False,change_submits=True),
            sg.Button(selectFooterAlignmentButton)
        ],
        [
            sg.Text("Need header?"),
            sg.Checkbox("Yes",key=NeedHeader_key),
            sg.Text("Format:"),
            sg.Checkbox("Current Page?",key=HeaderFormat_NeedCurrentPage_key),
            sg.Checkbox("Seperator?",key=HeaderFormat_NeedSeperator_key),
            sg.Checkbox("Total Page?",key=HeaderFormat_NeedTotalPage_key),
            sg.Input(key=HeaderFormat_Alignment_key,readonly=True,use_readonly_for_disable=False,change_submits=True),
            sg.Button(selectHeaderAlignmentButton)
        ],
        [
            sg.Button(selectFont),
            sg.Text("Font Size:"),
            sg.Input(key=FontSize_key,size=(10,1),readonly=True,use_readonly_for_disable=False,change_submits=True),
            sg.Text("Font BODY:"),
            sg.Input(key=FontBody_key,size=(20,1),readonly=True,use_readonly_for_disable=False,change_submits=True),
            sg.Text("Font text color:"),
            sg.Input(key=FontTextColor_key,size=(10,1),readonly=True,use_readonly_for_disable=False,change_submits=True),
            sg.Text("Font background color:"),
            sg.Input(key=FontBackgroundColor_key,size=(10,1),readonly=True,use_readonly_for_disable=False,change_submits=True),
            sg.Checkbox("Bold?",key=FontBold_key),
            sg.Checkbox("Underline?",key=FontUnderline_key),
            sg.Checkbox("Italic?",key=FontItalic_key),
            sg.Checkbox("Strike?",key=FontStrike_key)
        ],
        [
            sg.Button(generationFileButton),
            sg.Button(closeButton),
            sg.Button(clearAllButton)
        ],
        [
            sg.HSeparator()
        ],
        [
            sg.Text("message",key=OutputMessage_key,size=(200,20))
        ]
    ]

    window = sg.Window('Window Title', layout=layout,location=(10,10))      


    while True:
        event,values = window.read(timeout=10)
        
        if event == closeButton or event==sg.WIN_CLOSED:
            break
        
        if event == clearSubmitButton:
            window[YTChannelLink_key].update(emptyString)
            
        if event == clearDocNameButton:
            window[DocName_key].update(emptyString)    
            
        if event == selectDocExtButton:
            ret_val=Select_ScrollBar_Window(ext_list)    
            updateMessage=str(ret_val)
            window[DocExt_key].update(updateMessage)
            
        if event == clearAllButton:
            for v in values:
                window[v].update(emptyString)
           
        if event == selectFont:
            fonts=FontWindow()
            window[FontSize_key].update(fonts[0])
            window[FontBody_key].update(fonts[1])
            window[FontTextColor_key].update(fonts[2])
            window[FontBackgroundColor_key].update(fonts[3])

        if event == selectTarLangButton:
            ret_val=Select_ScrollBar_Window(tar_list)
            updateMessage=str(ret_val)
            window[TarLang_key].update(updateMessage)
        
        if event == selectFooterAlignmentButton:
            ret_val=Select_ScrollBar_Window(WD_ALIGN_PARAGRAPH_list)
            updateMessage=str(ret_val)
            window[FooterFormat_Alignment_key].update(updateMessage)
            
        if event == selectHeaderAlignmentButton:
            ret_val=Select_ScrollBar_Window(WD_ALIGN_PARAGRAPH_list)
            updateMessage=str(ret_val)
            window[HeaderFormat_Alignment_key].update(updateMessage)
        
        if event == generationFileButton:
            ok=Check_Valid_Before_Generate()
            if ok:
                translated_cmd_argv_str=Write_Command()
                GenerateFile(translated_cmd_argv_str)
            else:
                OpenErrorWindow(tb="Traceback (most recent call last): Check_Valid_Before_Generate",e="There exist one or some fields that are empty or invalid.")
        if event == browseFilePathButton:
            filename = sg.popup_get_file('Please enter a file name',save_as=True)
            sg.popup('Results', 'The value returned from popup_get_file', filename)
            ok=True
            print(filename)
            if (not filename is None )and filename!=emptyString:
                if os.path.exists(filename)!=True:
                    OpenErrorWindow(tb="Traceback (most recent call last): browseFilePathButton",e="The selected text does NOT exist!!!")
                    ok=False
                
                if os.path.isdir(filename)!=True:
                    OpenErrorWindow(tb="Traceback (most recent call last): browseFilePathButton",e="The selected text is NOT a directory!!!")
                    ok=False
            
                if ok==True:
                    sg.popup('YA!!', 'The value is store in the input field', filename)
                    window[FilePath_key].update(filename)
            
        FetchData()  
        window.refresh()

    window.close()
    
if __name__=='__main__':
    main()
