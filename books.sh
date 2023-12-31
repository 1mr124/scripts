#!/usr/bin/env bash

# Directory where your PDF books are stored
booksDirectory="/home/mr124/Documents/currentReading"

# Use find to locate PDF files in subfolders
BooksNames=$(find "$booksDirectory" -iname '*.pdf' | rev | cut -d '/' -f 1 | rev | cut -d '.' -f 1)

# Use dmenu to create a dynamic menu from the list of PDF files
selectedFile=$(echo "$BooksNames" | dmenu -i -p "Select a book:")

# Check if the user selected a book
if [ -n "$selectedFile" ]; then
    PdfPath=$(find "$booksDirectory" -type f -iname "$selectedFile*" )
    echo $PdfPath 
    zathura "$PdfPath" &
fi
