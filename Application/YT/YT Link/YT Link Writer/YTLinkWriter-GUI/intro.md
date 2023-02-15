# Intro
In this code, one can write some datas of YT channel to a text file and generate it (if it does NOT exist) with specified url of YT channel ID.

At beginning of running this code, you will see a GUI window.

The input field with left text field with text "YT channel ID link" indicates you to enter the url of YT channel ID.

The input field with left text field with text "File path" determines the location of auto-generated file.

The input field with left text field with text "File name" determines the file name of auto-generated file.

The absolute path and filename will be 

    <filepathname>=(<filepath>+"\"+<filename>).replace("/","\\")+".txt" 
  
 in Windows 11.
  
For example, if <filepath> is set to "C:/Users/user/Desktop/Demo_Test/Test_Output" and <filename> is set to "YT_demo2".

Then <filepathname> will be 
  
  C:\Users\user\Desktop\Demo_Test\Test_Output\YT_demo2.txt
  

