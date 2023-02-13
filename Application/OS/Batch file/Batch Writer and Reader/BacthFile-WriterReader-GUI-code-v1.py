import PySimpleGUI as sg
import os 

class BatchFile_WriterRunner():
    
    def PopupErrorWindow(self,tb:str,e:str):
        sg.popup_error(f'AN EXCEPTION OCCURRED!',e,tb)
    def MainWindow(self):
        def CreateBatchFile():
            filepathname=values[filepathname_key]
            contentText=values[batchCmd_key]
            f=open(filepathname,"w")
            f.write(contentText)
                
        def ReadBatchFile():
            f=open(filepathname,"r")
            updatedMessage=f.read()
            window[batchCmd_key].update(updatedMessage)
            
        whitespace=" "
        tab="\t"
        blash="/"
         
        filepathname_key="--File Path and Name--"
        
        batchCmd_key="----Batch CMD----"
        
        writeFileButton="Write"
        readFileButton="Read"
        browseFilepathnameButton="Browse"
        
        
        layout=[
            [
                sg.Text("File Path and File name:"),
                sg.Input(key=filepathname_key,readonly=True),
                sg.Button(browseFilepathnameButton)
            ]    
            ,
            [
                sg.Text("Batch file cmd:")
            ]
            ,
            [
                sg.Multiline(size=(120,7),autoscroll=True,key=batchCmd_key)
            ]
            ,
            [
                sg.Button(writeFileButton),
                sg.Button(readFileButton)
            ]
        ]
        
        window=sg.Window(title="BatchFile Writer and Runner Window",layout=layout)
        while True:
            event,values=window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == browseFilepathnameButton:
                
                filepathname=sg.popup_get_folder("Browse",title="Select a folder")
                filepathname=filepathname.rstrip(whitespace).rstrip(tab)
                print(filepathname)
                ok=True
                filepath=blash.join(filepathname.split(blash)[:-1])
                print(filepath)
                if ok and not os.path.exists(filepathname) and not os.path.exists(filepath):
                    ok=False
                    tb="traceback on the input field with key "+filepathname_key
                    e="ERROR!!! The input field does NOT exist!!!"
                    self.PopupErrorWindow(tb,e)
                if ok and os.path.isdir(filepathname) and os.path.isdir(filepath):
                    ok=False
                    tb="traceback on the input field with key "+filepathname_key
                    e="ERROR!!! The input field is a directory!!!"
                    self.PopupErrorWindow(tb,e)
                if ok and not filepathname.endswith(".bat"):
                    ok=False
                    tb="traceback on the input field with key "+filepathname_key
                    e="ERROR!!! The value of input field must ends with .bat!!!"
                    self.PopupErrorWindow(tb,e)
                    
                if ok:
                    window[filepathname_key].update(filepathname)
                    
            if event == writeFileButton:
               CreateBatchFile()
            if event == readFileButton:
                ReadBatchFile()
                
                
            
        window.close()
        
    
inst=BatchFile_WriterRunner()
inst.MainWindow()
