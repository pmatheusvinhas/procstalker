# procstalker

procstalker is going to watch a process and when It receive a termination signal it will recreate the process keeping it in a loop.
It's usefull to me as test and productivity in initial codes principily in C when you have a lot of segfaults in early stages. 

## Notes
It's written in Python 3 and for now it supports binaries and .py files.

# How to use:
`nohup python3 procstalker.py -f file &`