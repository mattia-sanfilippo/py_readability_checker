import requests
from bs4 import BeautifulSoup
import textstat
import csv

def get_text_from_url(url):
    """
    Fetches a webpage, extracts the main text content, and returns it.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        soup = BeautifulSoup(response.content, 'lxml')  # Use 'lxml' for faster parsing

        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Get text and remove extra whitespace
        text = soup.get_text(separator=" ", strip=True)
        return text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None

def analyze_readability(url, text):
    """
    Calculates readability scores using textstat and returns a dictionary.
    """
    if text is None:
        return None

    textstat.set_lang("en_US")  # Set to your documentation language

    scores = {
        "url": url,
        "flesch_reading_ease": textstat.flesch_reading_ease(text),
        "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text),
        "gunning_fog": textstat.gunning_fog(text),
        "smog_index": textstat.smog_index(text),
        "automated_readability_index": textstat.automated_readability_index(text),
        "coleman_liau_index": textstat.coleman_liau_index(text),
        "linsear_write_formula": textstat.linsear_write_formula(text),
        "dale_chall_readability_score": textstat.dale_chall_readability_score(text),
        "text_standard": textstat.text_standard(text, float_output=True),
        "character_count": textstat.char_count(text, ignore_spaces=True),
        "word_count": textstat.lexicon_count(text, removepunct=True),
    }
    return scores

def load_urls_from_file(filepath):
    """
    Loads URLs from a text file, one URL per line.
    """
    urls = []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                url = line.strip()  # Remove leading/trailing whitespace and newline characters
                if url:  # Ignore empty lines
                    urls.append(url)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None  # Return None to indicate an error
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None
    return urls


def main():
    """
    Main function to process URLs from a file and output readability scores.
    """
    url_file = "urls.txt"  # Name of the file containing URLs
    urls = load_urls_from_file(url_file)

    if urls is None:
        return  # Exit if there was an error loading URLs

    results = []
    for url in urls:
        text = get_text_from_url(url)
        scores = analyze_readability(url, text)
        if scores:
            results.append(scores)

    # Output to console
    print("Readability Scores:")
    for result in results:
        print(f"URL: {result['url']}")
        for metric, score in result.items():
            if metric != "url":
                print(f"  {metric}: {score}")
        print("-" * 20)

    # Output to CSV
    if results:
        with open("readability_results.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = results[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(results)
        print("Results saved to readability_results.csv")

if __name__ == "__main__":
    main()