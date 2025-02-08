"""
Author: Chintan Dobariya
Date: 2025-02-07
Description: This script searches for a specified word in PDF files within a given directory, including nested directories.
"""


import os
import sys
import argparse
from PyPDF2 import PdfReader


# ANSI escape codes for coloring text
RED = "\033[31m"
RESET = "\033[0m"


def search_pdfs(directory, search_word):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"{RED}Error: Directory '{directory}' does not exist.{RESET}")
        return

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".pdf"):
                file_path = os.path.join(root, file)
                try:
                    # Extract text from PDF
                    with open(file_path, "rb") as f:
                        reader = PdfReader(f)
                        pdf_content = ""
                        for page in reader.pages:
                            pdf_content += page.extract_text()

                    # Search for the word in the content
                    if search_word.lower() in pdf_content.lower():
                        print(f"Found '{search_word}' in: {file_path}")
                except Exception as e:
                    print(f"{RED}Error processing file '{file_path}': {e}{RESET}")

def validate_word(word):
    # Ensure the word has a minimum length of 3 characters
    if len(word) < 3:
        print(f"{RED}Error: Search word must be at least 3 characters long.{RESET}")
        sys.exit(1)
    return word


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Search for a word in PDF files within a directory.")
    
    # optional path argument
    parser.add_argument("-p", "--path", type=str, default="./", 
                        help="Directory path to search for PDF files (default: './')")
    # mandatory word argument            
    parser.add_argument("-w", "--word", type=validate_word, required=True, 
                        help="Word to search for in the PDFs (must be at least 3 characters long)")
                        
    args = parser.parse_args()

    search_pdfs(args.path, args.word)
