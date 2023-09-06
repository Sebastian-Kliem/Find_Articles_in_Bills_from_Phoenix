#!/usr/bin/env python3

import os
import argparse
from pypdf import PdfReader


def find_article_number(pdf_file, article_number) -> dict | None:
    """
    Search for a given article number.
    :param pdf_file: path to PDF
    :param article_number: the article number you looking for
    :return: a dict with billing-number and date or none if the searched article number not in PDF
    """
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        text = page.extract_text()
        text_splitted = text.split("\n")

        items = {}
        if article_number in text_splitted[38].split(" ")[0]:
            items["billing_number"] = text_splitted[11].split(" ")[1]
            items["date"] = text_splitted[13]

            return items
        return None


def main():
    parser = argparse.ArgumentParser(description="Suchen Sie nach Artikelnummern in PDF-Rechnungen.")
    parser.add_argument("article_number", type=str, help="Die Artikelnummer, nach der gesucht werden soll.")
    args = parser.parse_args()

    article_number = args.article_number

    main_directory = os.path.dirname(os.path.abspath(__file__))
    directory = main_directory + "/Bills/"

    if not os.path.exists(directory):
        print(f"Das Verzeichnis '{directory}' existiert nicht.")
        return

    print(f"Suche nach Artikelnummer '{article_number}' in PDF-Rechnungen im Verzeichnis '{directory}':")

    found_bills = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_file = os.path.join(directory, filename)
            scanned_pdf = find_article_number(pdf_file, article_number)
            if scanned_pdf:
                found_bills.append(scanned_pdf)

    for items in found_bills:
        print(f"Rechnungsnummer {items['billing_number']} vom {items['date']}")


if __name__ == "__main__":
    main()
