# Readability Analyzer for Web Pages

This Python script analyzes the readability of web-hosted pages using the `textstat` library. It fetches content from URLs listed in a text file, extracts the main text, calculates various readability scores, and outputs the results to the console and a CSV file.

## Features

* **Fetches content from URLs:**  Uses the `requests` library to retrieve HTML content from web pages.
* **Extracts main text:**  Employs `BeautifulSoup4` to parse HTML and extract the main text content, removing script and style elements.
* **Calculates readability scores:**  Leverages `textstat` to compute multiple readability metrics, including:
  * Flesch Reading Ease
  * Flesch-Kincaid Grade Level
  * Gunning Fog Index
  * SMOG Index
  * Automated Readability Index (ARI)
  * Coleman-Liau Index
  * Linsear Write Formula
  * Dale-Chall Readability Score
  * Text Standard (combined metric)
  * Character Count
  * Word Count
* **Loads URLs from a text file:** Reads URLs from a specified text file (default: `urls.txt`), one URL per line.
* **Outputs results:** Displays results on the console and saves them to a CSV file (`readability_results.csv`).
* **Error handling:** Includes error handling for network issues, file I/O, and HTML parsing.
* **Clear output:** Presents results in a readable format, both in the console and the CSV file.

## Requirements

* Python 3.6+
* `requests`
* `beautifulsoup4`
* `lxml` (optional but recommended for better performance with `beautifulsoup4`)
* `textstat`

## Installation

1. **Install Python:** If you don't have Python 3.6 or higher, download and install it from [https://www.python.org/downloads/](https://www.python.org/downloads/). Make sure to add Python to your system's PATH during installation.
2. **Clone the repository:**  Clone this repository to your local machine using Git.
3. **Install Libraries:** Open a terminal or command prompt and install the required libraries using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Create a text file `urls.txt`**  Create a text file containing the URLs of the pages you want to analyze, one URL per line.  Example:

    ```txt
    https://www.example.com/docs/page1
    https://www.example.com/docs/page2
    https://www.example.com/docs/tutorial/getting-started
    ```

2. **Run the script:**  Open a terminal or command prompt in the directory where you saved the script and run:

    ```bash
    python readability_checker.py
    ```

The script will:

* Read URLs from `urls.txt`.
* Fetch the content of each webpage.
* Extract the main text content.
* Calculate readability scores.
* Print the results to the console.
* Save the results to `readability_results.csv`.

## Output

### Console Output

The console will display readability scores for each URL, similar to this:

```plaintext
URL: https://www.example.com/docs/page1
  flesch_reading_ease: 31.48
  flesch_kincaid_grade: 12.4
  gunning_fog: 9.33
  smog_index: 12.3
  automated_readability_index: 17.1
  coleman_liau_index: 19.13
  linsear_write_formula: 20.0
  dale_chall_readability_score: 7.45
  text_standard: 12.0
  character_count: 6786
  word_count: 1020
```

### CSV File

The script will save the results to a CSV file named `readability_results.csv`. The file will contain the following columns:

```plaintext
URL, Flesch Reading Ease, Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Automated Readability Index, Coleman-Liau Index, Linsear Write Formula, Dale-Chall Readability Score, Text Standard, Character Count, Word Count
```
