import PySimpleGUI as sg
import os

from ReaderStream_class import ReaderStream
from WriteStream_class import WriteStream


from PythonCMDAdder_class import PythonCMDAdder

class PythonCMDHandlerWindow():
    
    def __init__(self):
        self.MainWindow()
        
    def MainWindow(self):
        
        def GetFilepathnameInfo(filepathname):
            pass
        filepathname1_key="--File Path Name--"
        CMDMultiline_key="-CMD Multiline-"
        
        browseButton="Browse"
        readFileButton="Read"        
        writeFileButton="Write"
        
        pythonExt=[".py",".pym"]
        
        
        layout=[
            [
                 sg.Text("File path name:")
                 ,sg.Input(key=filepathname1_key,readonly=True)
                 ,sg.Button(browseButton)
                 ,sg.Button(readFileButton)
                 ,sg.Button(writeFileButton)
            ]
            ,
            [
                sg.Multiline(expand_x=True
                             ,expand_y=True
                             ,horizontal_scroll=True
                             ,key=CMDMultiline_key
                             )
            ]
            
            
            
        ]
        
        rs=ReaderStream()
        ws=WriteStream()
        
        window=sg.Window(title="Python CMD Handler Window",layout=layout,resizable=True)
        while True:
            event,values=window.read()
            if event==sg.WIN_CLOSED:
                break
            if event == browseButton:
                filepathname=sg.popup_get_file(message="File name",title="Get a file",no_window=True)
                window[filepathname1_key].update(filepathname)
            if event == readFileButton:
                val=values[filepathname1_key]
                if (not val is None) and len(val)!=0:
                    filepath=os.path.dirname(val)
                    filename=''.join(os.path.splitext(os.path.basename(val))[:-1])
                    fileExt=os.path.splitext(val)[-1]
                    if fileExt in pythonExt:
                        rs.SetPath(filepath=filepath, filename=filename, fileExt=fileExt)
                        textContent=rs.ReadData()
                        window[CMDMultiline_key].update(textContent)
                        
            if event == writeFileButton:
                val=values[filepathname1_key]
                print(val)
                if (not val is None) and len(val)!=0:
                    filepath=os.path.dirname(val)
                    filename=''.join(os.path.splitext(os.path.basename(val))[:-1])
                    fileExt=os.path.splitext(val)[-1]
                    print(filepath)
                    print(filename)
                    print(fileExt)
                    if fileExt in pythonExt:
                        ws.SetPath(filepath=filepath, filename=filename, fileExt=fileExt)
                        textContent=values[CMDMultiline_key]
                        ws.WriteData(textContent=textContent)
                        print(ws.textContent)
                    
                    
                 
        window.close()
    
def test():
    inst=PythonCMDHandlerWindow()

if __name__=='__main__':
    test()
