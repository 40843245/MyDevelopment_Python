import PySimpleGUI as sg

from FolderOperator_class import FolderOperator
from FileOperator_class import FileOperator
from DirectoryOperation_class import DirectoryOperation

class File_Operation_Window():
    def __init__(self):
        self.CreateWindow()
        
    def CreateWindow(self):
        
        absoluteFile1Path_key="--Absolute File1 Path--"
        absoluteFile2Path_key="--Absolute File2 Path--"
        
        createButton="Create"
        moveButton="Move"
        deleteButton="Delete"
        closeButton="Close"
        
        layout=[
            [
                sg.Text("Absolute file1 path:"),
                sg.Input(key=absoluteFile1Path_key)
            ]
            ,
            [
                sg.Text("Absolute file2 path:"),
                sg.Input(key=absoluteFile2Path_key)
            ]
            ,
            [
                sg.Button(createButton),
                sg.Button(moveButton),
                sg.Button(deleteButton)
            ]
            ,
            [
                sg.Button(closeButton)    
            ]
            
        ]   
        window=sg.Window(title="Folder Operation Window",layout=layout)
        
        instFile=FileOperator(src_filepathname=None
                              , dest_filepathname=None
                              , need_check_filepathname_exists=[False,False]
                              , need_prehandling_filepathname=[False,False])
        while True:
            event,values=window.read()
            
            
            
            if event == sg.WIN_CLOSED:
                break
            if event == closeButton:
                break
            
            if values[absoluteFile1Path_key] == "":
                sg.popup_error(f"ERRROR occurs"
                               ,"traceback (from last call): values[absoluteFile1Path_key]"
                               ,"values[absoluteFile1Path_key] is an empty string.")
                continue
            
            instFile.SetSrcFilepathname(src_filepathname=values[absoluteFile1Path_key]
                                        ,need_check_filepathname_exists=False
                                        ,need_prehandling_filepathname=False)
            
            if event == createButton:
                DirectoryOperation.MakeDirectory(path=instFile.src_file.filepathname)
                
            if event == deleteButton:
                DirectoryOperation.Delete(path=instFile.src_file.filepathname)
            
            if values[absoluteFile2Path_key] == "":
                sg.popup_error(f"ERRROR occurs"
                               ,"traceback (from last call): values[absoluteFile2Path_key]"
                               ,"values[absoluteFile2Path_key] is an empty string.")
                continue
            
            instFile.SetDestFilepathname(dest_filepathname=values[absoluteFile2Path_key]
                                        ,need_check_filepathname_exists=False
                                        ,need_prehandling_filepathname=False)
            if event == moveButton:
                instFile.MoveFile(follow_symlinks=False)
                
            
            
        window.close()

def test():
    inst=File_Operation_Window()
    
if __name__=='__main__':
    test()
