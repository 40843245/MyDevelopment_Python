# Release Notes
## In version 1 (v1)

### Release Date
2023/02/10 morning.

### Functionality:
To see my previous articles.

## In version 2 (v2)
### Release Date
2023/02/11 18:11 p.m.

### Difference
There are some difference between them.
#### Contents
1. I fix some bugs. 
2. I add some functions.
3. I change the orders of parameters in DOS cmd.
4. Delete some NOT necessary outputs.
5. Add comments to explain the code.
#### Details
1. I fix some bugs.

        There are many issues I found and solved. While these days, I spent time on reading articles, learning new things and try to solve it with other different way. Such as I spent about 90 minutes to find the XML tags which are used in Micorsoft word, trying to set the text color with different way -- by creating a new XML element . Thus, it was late to release the new version (total spent about 8 hours on finishing learning and debugging.). I sorry to those who has used my codes.
        
        I found these issues in v1.
        1) Unexpected type due to unexpected types between conversion parameters of DOS cmd to code so that there are exceptions at runtime due to mismatched types.
                I spent lots of time on type conversion.
        2) Some unknown error which says the language is NOT supported while translation of transcript. 
                I found why causes the error, the error is due to type conversion.
        3) Errors due to the different order of parameters between pass fron DOS cmd to Python code.
        
2. I add some functions.
                
         While these two days, I added some functionalities.
         1) One can determine the text color, text background color, text font (including font size, bold, italic, font family, underline, strike).
         2) One can add header or footers in many different places. Unlike the v1, we can only place texts at one place for a header in these three columns, and so is for footer.
         3) About strings that represent hex color, 
           it can be converted to a list of elements with int type.
         4) one can see the information by the function Print_Info().
         5) Functions between conversion type.
         6) Type check.
         7) one can set the maximum number of records to fetch.
         8) one can set the YT channel link.
         9) one can determine the location of auto generated file.
         10) one can determine to open the webbroswer with YT channel url during runtime by the parameters of DOS cmd.
     
4. I change the orders of parameters in DOS cmd.
                
         I changed the orders of parameters in DOS cmd to make it more understandable.
         
5. Delete some NOT necessary outputs.
        
        I deleted some NOT necessary outputs after development and before releasing to make the DOS cmd looks more neatly after running.
     
        
7. Add comments to explain the code.
        
        I added some comments to explain what the code can do and what the methods can be used for. 
        
        Also, I make the code looks more formal and seems to like the code is written by a big company.

### Issues can NOT be solved.
#### Contents
1. HTTPRequestsError when there are many records are needed to be translated by googltrans.

2. Unknown exceptions with given some invalid parameters.
 
#### Details 
1. HTTPRequestsError when there are many records are needed to be translated by googltrans.
       
       Since there are maximum requests between google servers, thus, this issue can NOT be solved at present.
       
2. Unknown exceptions with given some invalid parameters.
        
        Such as invalid font size, font family, document extension, document path, document name.
  
        I will NOT solve this issue. Especially to check the input of font family exists in word since it is troublesome to list all available fonts in word. 
        
        NOTE that I just check all types of input and some common invalid input for specified parameter.
        
        But I ensure that these invalid parameters will NOT cause unexpected results.
        
        When one of them are given, the exceptions occur at runtime. (It is I desired for.)
        
        1)text color
        2)text background color

## In version 3 (v3)
### Release Date
2023/02/11 21:00 p.m.
### Issue
#### Contents:
1. Fix several bugs.
2. Delete unnecessary outputs.
#### Details:
1. Fix several bugs.
        
        I fix some several bugs.
        There is a bug in version 2.
        The runtime error due to mismatched type.
2. Delete unnecessary outputs.
