import PySimpleGUI as sg
from YTChannelID_class import YTLinkOpener

class MainWindow(YTLinkOpener):
    def __init__(self):
      self.CreateMainWindow()
    def CreateMainWindow(self):
        
        emptyString=""
        whitespace=" "
        tab="\t"
        newline="\n"
        YTChannelIDLink_key="--YT Channel Link--"
        filepath_key="--File Path--"
        
        openYTLinkButton="Open"
        selectPathButton="Browse"
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
            ]
            ,
            [
                sg.Button(openYTLinkButton),
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
                    window[k].update(emptyString)
                
            if event == selectPathButton:
                filepath = sg.popup_get_folder('Select a folder as path:',no_window =True)
                window[filepath_key].update(filepath)
            if event == openYTLinkButton:
                link=values[YTChannelIDLink_key]
                link=link.rstrip(whitespace).rstrip(tab).rstrip(newline)
                super().__init__(link)
                self.OpenYTLink(link)
                
        window.close()
            

inst=MainWindow()
