# MULTI-LANGUAGE INVOICE EXTRACTOR USING GEMINI

This is a Streamlit web app that allows users to upload an invoice image and ask questions about it. The app uses **Gemini 1.5 Flash Vision** model by Google to understand and extract information from the image, even if the invoice is in different languages.


## Features

* Upload invoice images (`.jpg`, `.jpeg`, `.png`)
* Ask any question related to the invoice (e.g., "What is the total amount?")
* Supports **multiple languages**
* Uses **Gemini Vision AI** to extract answers from images
* Simple and user-friendly interface built with **Streamlit**

## Requirements

* Python 3.8+
* Google Generative AI API key (set it in `.env` file as `GOOGLE_API_KEY`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/multi-lang-invoice-extractor.git
cd multi-lang-invoice-extractor
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

## How to Run

```bash
streamlit run app.py
```

1. Upload an invoice image.
2. Enter your question (e.g., "What is the due date?").
3. Click the **Get response from invoice** button.
4. View the extracted answer below.

## Example Use Cases

* Extract total amount or tax details
* Get invoice date or due date
* Identify vendor or customer names
* Works with invoices in different languages

##  Model Used

* `gemini-1.5-flash-latest` (vision model)
