import PySimpleGUI as sg

from FolderOperator_class import FolderOperator
from FileOperator_class import FileOperator
from DirectoryOperation_class import DirectoryOperation

class Folder_Operation_Window():
    def __init__(self):
        self.CreateWindow()
        
    def CreateWindow(self):
        
        absoluteFolderPath_key="--Absolute Folder Path--"
        
        
        createButton="Create"
        listdirAllFoldersAndFilesButton="List files and folders in the directory"
        listdirAllFoldersButton="List folders in the directory"
        listdirAllFilesButton="List files in the directory"
        
        printFolderStatusButton="Print Folder Status"
        findMaxSizeButton="Find the file with max size"
        
        deleteButton="Delete"
        closeButton="Close"
        
        layout=[
            [
                sg.Text("Absolute folder path:"),
                sg.Input(key=absoluteFolderPath_key)
            ]
            ,
            [
                sg.Button(createButton)
            ]
            ,
            [
                sg.Button(listdirAllFoldersAndFilesButton),
                sg.Button(listdirAllFoldersButton),
                sg.Button(listdirAllFilesButton)
            ]
            ,
            [
                sg.Button(printFolderStatusButton),
                sg.Button(findMaxSizeButton),
                sg.Button(deleteButton)
            ]
            ,
            [
                sg.Button(closeButton)    
            ]
            
        ]   
        window=sg.Window(title="Folder Operation Window",layout=layout)
        
        instFolder=FolderOperator(src_folderfilepath="", need_check_filepathname_exists=False, need_prehandling_filepathname=False)
        
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
            
            if values[absoluteFolderPath_key] == "":
                sg.popup_error(f"ERRROR occurs"
                               ,"traceback (from last call): values[absoluteFolderPath_key]"
                               ,"values[absoluteFolderPath_key] is an empty string.")
                continue
            
            instFolder.SetFilepathname(values[absoluteFolderPath_key])
            
            if event == createButton:
                DirectoryOperation.MakeDirectory(path=instFolder.src_file.filepathname)
                
            if event == deleteButton:
                DirectoryOperation.Delete(path=instFolder.src_file.filepathname)
                
            if event == listdirAllFoldersAndFilesButton:
                hasNone,hasException=FolderOperator.PrintAllFoldersAndFiles_InThisLevel(src_folderfilepath=instFolder.src_file.filepathname)
                if hasNone:
                    sg.popup("There are NO results","Thus,the terminal has NO changes.",title="Notice Window")
                    
            if event == listdirAllFoldersButton:
                hasNone,hasException=FolderOperator.PrintAllFolders_InThisLevel(src_folderfilepath=instFolder.src_file.filepathname)
                if hasNone:
                    sg.popup("There are NO results","Thus,the terminal has NO changes.",title="Notice Window")
            if event == listdirAllFilesButton:
                hasNone,hasException=FolderOperator.PrintAllFiles_InThisLevel(src_folderfilepath=instFolder.src_file.filepathname)
                if hasNone:
                    sg.popup("There are NO results","Thus,the terminal has NO changes.",title="Notice Window")
            if event == printFolderStatusButton:
                hasNone,hasException=FolderOperator.PrintFolderStatus(src_folderfilepath=instFolder.src_file.filepathname, only_print_first=False)
                if hasNone:
                    sg.popup("There are NO results","Thus,the terminal has NO changes.",title="Notice Window")
            
            if event == findMaxSizeButton:
                maxFile,maxSize,hasNone,hasException=FolderOperator.GetMaxSize_ForAllSubfiles(src_folderfilepath=instFolder.src_file.filepathname)
                if hasNone:
                    sg.popup("There are NO results","Thus,the terminal has NO changes.",title="Notice Window",)
                else:
                    sg.popup("The file with max size is "+str(maxFile),"The max size is "+str(maxSize),title="Output Window")
                    
        window.close()

def test():
    inst=Folder_Operation_Window()
    
if __name__=='__main__':
    test()
