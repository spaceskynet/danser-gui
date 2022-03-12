@echo off
set langs=en-US zh-CN

for %%l in (%langs%) do (
    if not exist .\langs\%%l (
        md .\langs\%%l
    )
    if not exist .\langs\%%l\lang.txt (
        echo %%l > .\langs\%%l\lang.txt
    )
    pylupdate5 .\ui\setupMainWindow.py .\ui\bindKeyDialog.py .\ui\MainWindow.py .\ui\gui.py .\utils\exception_handling.py .\utils\setup.py -ts .\langs\%%l\lang.ts
    echo %%l is generated.
)