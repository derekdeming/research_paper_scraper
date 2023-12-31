# research_paper_scraper
Scrapes elsevier website yields a summarized output of all the papers you tell GPT to cover 


This Python script allows you to search for scholarly articles using the Elsevier Scopus API and generate summaries of the articles using OpenAI's GPT-4 model.

## Installation

1. Install the required Python packages using `pip`:

   ```
   pip install argparse requests tqdm concurrent.futures openai
   ```

2. Set up your Elsevier API key and OpenAI API key as environment variables:

   ```
   export ELSEVIER_API_KEY=your_elsevier_api_key
   export OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the script from the command line with the following arguments:

- `keyword`: The keyword to search for in the articles.
- `-n`, `--num_papers`: The number of papers to retrieve (default: 10).
- `-o`, `--output`: The output CSV file (default: papers.csv).
- `-s`, `--subject`: The subject area (e.g., AGRI, ARTS, BIOC, etc.) (optional).

Example:

```
python main.py "machine learning" -n 10 -o results.csv -s COMP
```

This will search for 10 papers related to machine learning in the computer science subject area and save the summaries in the `results.csv` file.

## Output

The output CSV file will contain the following columns:

- Title: The title of the paper.
- Authors: The authors of the paper.
- Publication Name: The name of the publication where the paper was published.
- Publication Date: The date when the paper was published.
- DOI: The DOI of the paper.
- Summary: A summary of the paper generated by the GPT-3 model.
- Hypotheses: Hypotheses in the paper as interpreted by the GPT-3 model.
- Methods: Methods used in the paper as interpreted by the GPT-3 model.
- Findings: Findings in the paper as interpreted by the GPT-3 model.

## Note

This script uses GPT-3 to generate summaries, which may not always be perfectly accurate. Use the generated summaries as a starting point for further investigation and always refer to the original articles for accurate information.
