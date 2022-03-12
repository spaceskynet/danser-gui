#!/usr/bin/env bash
langs=(en-US zh-CN)

for lang in ${langs[*]}; do
    if ! [[ -d "./langs/${lang}" ]]; then
        mkdir "./langs/${lang}"
    fi
    if ! [[ -f "./langs/${lang}/lang.txt" ]]; then
        echo $lang > "./langs/${lang}/lang.txt"
    fi
    pylupdate5 ./ui/setupMainWindow.py ./ui/bindKeyDialog.py ./ui/MainWindow.py ./ui/gui.py ./utils/exception_handling.py ./utils/setup.py -ts "./langs/${lang}/lang.ts"
    echo $lang is generated.
done