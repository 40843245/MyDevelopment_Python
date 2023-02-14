import PySimpleGUI as sg
import os
#import junk1
# import the module for the function GenerateRandomNestedData()

class LetterGeneratorWindow():
    def __init__(self):
        self.MainWindow()
    def MainWindow(self):
        def ClearAll():
            for k,v in values.items():
                window[k].update(emptyString)
        def PopupErrorWindow(tb:str,e:str):
            sg.popup_error(f"Exception occurs",tb,e)
            
        def BrowseFile():
            filepath=sg.popup_get_folder("Select a folder",title="Select a folder as path for auto-generating files"
                                ,keep_on_top=True)
            ok = True
            
            if ok and not os.path.exists(filepath):
                ok = False
                tb="Traceback (from last call):BrowseFile."
                e = "ERROR!!! The path you selected does NOT exist!!!"
                PopupErrorWindow(tb=tb,e=e)
            if  ok and not os.path.isdir(filepath):
                ok = False
                tb="Traceback (from last call):BrowseFile."
                e = "ERROR!!! The path you selected is NOT a directory!!!"
                PopupErrorWindow(tb=tb,e=e)
                
            if ok:
                return filepath
            return None
        emptyString=""
        
        browseFilePathButton="Browse"
        generateFileButton="Create"
        clearAllButton="Clear"
        
        filePath_key="--File Path--"
        fileName_key="--File Name--"
        numOfGeneratingFile_key="--Number of generated files--"
        
        layout=[
            [
                sg.Text("File path:"),
                sg.Input(key=filePath_key,readonly=True),
                sg.Button(browseFilePathButton)
            ]
            ,
            [
                sg.Text("File name:"),
                sg.Input(key=fileName_key)
            ]
            ,
            [
                sg.Text("Number of file to generate:"),
                sg.Input(key=numOfGeneratingFile_key,default_text="0")
            ]
            ,
            [
                sg.Button(clearAllButton),
                sg.Button(generateFileButton)    
            ]    
        ]
        
        window=sg.Window(title="Letter Generator Window",layout=layout)
        while True:
            event,values=window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == clearAllButton:
                ClearAll()
            if event == browseFilePathButton:
                path=BrowseFile()
                if path is not None:
                    window[filePath_key].update(path)
                    
            if event == generateFileButton:
                
                numOfGeneratingFile=values[numOfGeneratingFile_key]
                if not isinstance(numOfGeneratingFile,(str,int)):
                    raise TypeError
                numOfGeneratingFile=int(numOfGeneratingFile,10)
                maxGenFile=100000
                ok = True
                if ok and numOfGeneratingFile<=0:
                    ok = False
                    tb="Traceback (from last call):generateFileButton."
                    e = "ERROR!!! The number of files to generate must be positive integer and less than "+str(maxGenFile)+"!!!"
                    PopupErrorWindow(tb=tb,e=e)
                if ok and numOfGeneratingFile>=maxGenFile:
                    ok = False
                    tb="Traceback (from last call):generateFileButton."
                    e = "ERROR!!! The number of files to generate must be positive integer and less than "+str(maxGenFile)+"!!!"
                    PopupErrorWindow(tb=tb,e=e)
                if ok:
                    for k in range(1,numOfGeneratingFile+1,1):
                        filepath=values[filePath_key]
                        filename=values[fileName_key]
                        filepathname=os.path.join(filepath,filename).replace("/","\\")+"_"+str(k)+".txt"
                        print(filepathname)
                        randomNestedData=GenerateRandomNestedData(minElem=1, maxElem=100, level=5)
                        f=open(filepathname,"w")
                        f.write(str(randomNestedData))
                        f.close()
        window.close()
        
inst=LetterGeneratorWindow()
