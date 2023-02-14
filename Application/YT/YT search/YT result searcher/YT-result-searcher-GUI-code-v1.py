import PySimpleGUI as sg
import webbrowser
import urllib3

class YT_results_searcher():
    
    def MainWindow(self):
        
        def ClearAll():
            for k,v in values.items():
                window[k].update(emptyString)
            
        def SearchResults():
            val=values[keyword_key]
            if (not val is None) and val!=emptyString:
                base_query_url=r"https://www.youtube.com/results?search_query="
                url=base_query_url+val
                webbrowser.open(url)                
        
        emptyString=""
        
        keyword_key="--Keyword--"
        searchButton="Search"
        clearButton="Clear"
        closeButton="Close"
        
        
        layout=[
            [
                sg.Text("Keyword:"),
                sg.Input(key=keyword_key)
            ]    
            ,
            [
                sg.Button(searchButton),
                sg.Button(clearButton),
                sg.Button(closeButton)
            ]
        ]
        
        window=sg.Window(title="YT result search Window",layout=layout)
        
        while True:
            event,values=window.read()
            
            if event == sg.WIN_CLOSED or event == closeButton:
                break
            if event == clearButton:
                ClearAll()
                
            if event == searchButton:
                SearchResults()
        window.close()

inst=YT_results_searcher()
inst.MainWindow()
