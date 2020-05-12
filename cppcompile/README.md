# c++ compile

* a bash script that'll enable you to edit your c++ code and input file, compile it using g++ and run it
* code files are saved as code#.cpp where # is a number and execution files are saved as code#.out
* default code file is code69.cpp, when passed without any argument
* you can pass your file number as an argument in case you wish to work on multiple files
* editor used here is nvim, you can use other editors like vim, emacs, sublime or even vscode as long as they open in wait mode
* new: added template file - edit template file to your desire before running the script

### installation and execution

> git clone https://github.com/lordlabuckdas/skripts.git ; cd skripts/cppcompile ### or just download the script 
>
> chmod +x cppcompile.sh
>
> ./cppcompile.sh