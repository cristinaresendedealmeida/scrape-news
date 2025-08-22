# 📰 READ ME: News Web Scraper for Identifying Child Rights Violations

This repository contains a Python project to perform **web scraping** on news websites and identify mentions of **child rights violations**, such as child abuse, child labor, and child exploitation.

## ⚙️ Features

* Makes HTTP requests to news pages using `requests`.
* Extracts the text content from the page paragraphs using `BeautifulSoup`.
* Searches for keywords related to child rights violations.
* Displays the keywords found in the article text.

## 📦 Prerequisites

Python 3 must be installed. The libraries used are:

```bash
pip install requests beautifulsoup4
```

## 📝 Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. Open the Python script and set the URL of a news website:

```python
news_url = 'https://g1.globo.com/'  # Replace with the desired URL
```

3. Run the script:

```bash
python filename.py
```

4. The program will display the keywords found in the article in the terminal:

```
Keywords found in the article: child abuse, child labor
```

or

```
No keywords related to child rights violations were found.
```

## 🛠 Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* Regex (`re`)

## ⚠️ Notes

* Make sure to use URLs of websites that allow web scraping.
* This project is for educational purposes and awareness of child rights violations only.

## 📌 Future Improvements

* Support for multiple URLs automatically.
* Store results in CSV files or a database.
* Automatic notifications when sensitive keywords are detected.

