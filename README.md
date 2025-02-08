# PDF Search Script

This Python script allows you to search for a specific word within PDF files in a given directory. It recursively scans all PDFs in the directory and prints the paths of the files that contain the search word.

## Use Case

This script is useful when you need to quickly find PDF files that contain a specific word or phrase, such as searching for terms across a collection of documents. It can be helpful for:

- Searching through large numbers of reports, research papers, or articles stored as PDFs.
- Locating a specific keyword in legal, academic, or technical documents.
- Quickly identifying PDFs containing specific information, such as terms of service, regulations, or legal references.

## Prerequisites
- `Python 3.x`
- `PyPDF2` library for PDF text extraction.

### Installation Instructions
To get started with this script, you need to install the necessary dependencies. Here are the steps:

1. Clone this repository to your local machine and move to directory.
```
git clone git@github.com:Chintan45/pdf-search-script
.git
cd pdf-search-script
```
2. Install dependencies using pip
```
pip install -r requirements.txt
```
Alternatively, you can install the necessary library directly:
```
pip install PyPDF2
```

## Usage

### Command Line Arguments

- -p, --path (optional): The directory path where the PDF files are located. If not provided, it defaults to the current directory (./).
- -w, --word (mandatory): The word you want to search for in the PDF files. This argument is required and the word must be at least 3 characters long.

### Example Usage

To search for the word "finance" in all PDF files within the current directory:

```
python pdf_search.py -w finance
```

To search for the word "health" in PDFs inside a specific directory (/path/to/your/folder):
```
python pdf_search.py -p /path/to/your/folder -w health
```

If the word is found in any of the PDF files, the script will output the path to the PDF file containing the word.


### Dependencies
- Python 3.x
- PyPDF2