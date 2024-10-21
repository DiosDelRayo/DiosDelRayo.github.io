Title: logfile
Tags: qt, pipe, QTextBrowser, QProcess
Summary: Remove watching logfile, use stdin of process to rotate last 1000 lines of log

Remove the file watcher because if file gets to big:
* rest of the logs go to other files and
* it takes to long to render and highlight fucked up UX

* [ ] Remove file watcher
* [ ] Remove parsing from file
* [ ] Add FIFO ~~buffer~~
* [x] Add partial updating ==QTextBrowser==
