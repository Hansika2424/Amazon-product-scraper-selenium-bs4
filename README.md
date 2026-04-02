# 🛒 Amazon Product Scraper

A Python-based web scraping project that automates the extraction of product listings from Amazon India using **Selenium** for browser automation and **BeautifulSoup** for HTML parsing. Built as a hands-on learning project to explore browser automation, DOM traversal, and data collection pipelines.

---

## 📌 What It Does

- Automates a Chrome browser to navigate Amazon search results
- Scrapes product cards across multiple pages for a given query (e.g., `laptop`)
- Saves raw HTML of each product card to disk
- Parses the saved HTML files to extract **title**, **price**, and **product link**
- Exports the final structured data to a **CSV file**

---

## 🗂️ Project Structure

```
amazon-scraper/
│
├── main.py               # Selenium basics — navigating python.org (learning exercise)
├── locating_single.py    # Locating a single product card on Amazon search page
├── locating_multiple.py  # Locating and printing all product cards
├── project.py            # Core scraper — saves each product card as an HTML file
├── collect.py            # Parser — reads saved HTML files, extracts data, exports CSV
├── data/                 # Folder where raw HTML files are saved (auto-created)
└── data.csv              # Final output with title, price, and product link
```

---

## ⚙️ How It Works

### Step 1 — Scrape (`project.py`)
Selenium opens Chrome and navigates to the Amazon search results page for the query. It finds all product card elements (`.puis-card-container`), saves each one as a separate `.html` file in the `data/` folder, and loops across pages with a delay to avoid rate limiting.

### Step 2 — Parse & Export (`collect.py`)
BeautifulSoup reads each saved HTML file, extracts the product **title** (from `<h2>`), **price** (from `.a-price-whole`), and **link** (from the parent `<a>` tag), and writes everything into a `data.csv` file using pandas.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Google Chrome + [ChromeDriver](https://chromedriver.chromium.org/) (must match your Chrome version)

### Install Dependencies

```bash
pip install selenium beautifulsoup4 pandas
```

### Run the Scraper

```bash
# Step 1: Scrape and save HTML files
python project.py

# Step 2: Parse HTML and generate CSV
python collect.py
```

The output CSV (`data.csv`) will contain columns: `title`, `price`, `link`.

---

## 📊 Sample Output

| title | price | link |
|-------|-------|------|
| Acer Aspire Lite 12th Gen Intel Core i5... | 51,990 | https://amazon.in/... |
| HP 15, 13th Gen Intel Core i3-1315U... | 44,990 | https://amazon.in/... |
| Lenovo V15 G4 AMD Athlon Silver 7120U... | 37,999 | https://amazon.in/... |

---

## 🧠 Concepts Practiced

- Browser automation with **Selenium WebDriver**
- DOM element selection using **CSS class names**
- HTML parsing with **BeautifulSoup**
- File I/O for storing intermediate HTML data
- Data structuring and export with **pandas**
- Handling exceptions gracefully during parsing

---

## 🔮 Possible Improvements

- Add pagination support with dynamic page count
- Add headless browser mode for faster scraping
- Implement retry logic for failed requests
- Extend to multiple product categories

---

## 📝 Notes

- This project is for **educational purposes only**. Always respect a website's `robots.txt` and Terms of Service before scraping.
- A `time.sleep()` delay is used between requests to be courteous to the server.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-orange)
![Pandas](https://img.shields.io/badge/Pandas-CSV-lightgrey?logo=pandas)
