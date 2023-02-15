import os 
import PySimpleGUI as sg

from Letter_ENUM_class import Letter_ENUM
from WriteStream_class import WriteStream
from YTChannelID_class import YTLinkOpener

class MainWindow(YTLinkOpener):
    def __init__(self):
      self.CreateMainWindow()
    def CreateMainWindow(self):
              
        YTChannelIDLink_key="--YT Channel Link--"
        filepath_key="--File Path--"
        filename_key="--File Name--"
        
        selectPathButton="Browse"
        writeInitialDataToFileButton="Write the initial data of YT channel link"
        writeFileButton="Write info of YT channel link"
        clearAllButton="Clear All"
        
        layout=[
            [
                sg.Text("YT channel ID link:"),
                sg.Input(key=YTChannelIDLink_key)
            ]
            ,
            [
                sg.Text("File path:"),
                sg.Input(key=filepath_key,readonly=True),
                sg.Button(selectPathButton)
            ],
            [
                sg.Text("File name:"),
                sg.Input(key=filename_key),
            ]
            ,
            [
                sg.Button(writeFileButton),
                sg.Button(writeInitialDataToFileButton),
                sg.Button(clearAllButton)
            ]
        ]
        
        window=sg.Window(title="YT Link Opener",layout=layout)
        while True:
            event,values=window.read()
            if event==sg.WIN_CLOSED:
                break
            if event == clearAllButton:
                for k in values.keys():
                    window[k].update(Letter_ENUM.emptyString)
                
            if event == selectPathButton:
                filepath = sg.popup_get_folder('Select a folder as path:',no_window =True)
                window[filepath_key].update(filepath)
            if event == writeFileButton:
                filename=values[filename_key]
                filepath=values[filepath_key]
                
                link=values[YTChannelIDLink_key]
                link=link.rstrip(Letter_ENUM.whitespace).rstrip(Letter_ENUM.tab).rstrip(Letter_ENUM.newline)
                super().__init__(link)
                
                textContent=self.__dict__()
                ws=WriteStream()
                ws.SetPath(filepath, filename, fileExt=".txt")
                ws.WriteData(textContent)
                
            if event == writeInitialDataToFileButton:
                 filename=values[filename_key]
                 filepath=values[filepath_key]
                 
                 link=values[YTChannelIDLink_key]
                 link=link.rstrip(Letter_ENUM.whitespace).rstrip(Letter_ENUM.tab).rstrip(Letter_ENUM.newline)
                 super().__init__(link)
                 
                 textContent=self.GetInitialData()
                 ws=WriteStream()
                 ws.SetPath(filepath, filename, fileExt=".txt")
                 ws.WriteData(textContent)
                 
        window.close()
            
if __name__=='__main__':
    inst=MainWindow()
