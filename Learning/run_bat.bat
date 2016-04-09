REM This is an example of how to run a python command from a batch file

@python D:\eclipse\workspace\Proiecte\trunk\Learning\Challenge1_function.py %* 
@pause

GOTO:EndComment
This is a comment.
We put @ in front of the python command.
%* means we are forwarding the arguments from the command - if there are any.
We use pause to keep the command line open after running a command.
:EndComment