#!/usr/bin/env python3

import os
import argparse
import shutil

from pypdf import PdfReader


def find_article_number(pdf_file, article_number) -> dict | None:
    """
    Search for a given article number.
    :param pdf_file: path to PDF
    :param article_number: the article number you looking for
    :return: a dict with billing-number and date or none if the searched article number not in PDF
    """
    try:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            text = page.extract_text()
            text_splitted = text.split("\n")

            items = {}
            if article_number in text_splitted[38].split(" ")[0]:
                items["billing_number"] = text_splitted[11].split(" ")[1]
                items["date"] = text_splitted[13]
                items["file"] = pdf_file.rsplit("/", 1)[1]

                return items
        return None
    except Exception as e:
        print(f"Kann diese Datei nicht lesen {pdf_file}")
        print(e)
        return

def main():
    parser = argparse.ArgumentParser(description="Suchen Sie nach Artikelnummern in PDF-Rechnungen.")
    parser.add_argument("article_number", type=str, help="Die Artikelnummer, nach der gesucht werden soll.")
    args = parser.parse_args()

    article_number = args.article_number

    main_directory = os.path.dirname(os.path.abspath(__file__))
    bill_directory = main_directory + "/Bills/"
    output_directory = main_directory + "/FoundBills/"

    if not os.path.exists(bill_directory):
        print(f"Das Verzeichnis '{bill_directory}' existiert nicht.")
        return

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    print(f"Suche nach Artikelnummer '{article_number}' in PDF-Rechnungen im Verzeichnis '{bill_directory}':")

    found_bills = []
    for filename in os.listdir(bill_directory):
        if filename.endswith(".pdf"):
            pdf_file = os.path.join(bill_directory, filename)
            scanned_pdf = find_article_number(pdf_file, article_number)
            if scanned_pdf:
                found_bills.append(scanned_pdf)
                shutil.copy(pdf_file, os.path.join(output_directory, filename))

    for items in found_bills:
        print(f"Rechnungsnummer {items['billing_number']} vom {items['date']} Dateinmae: {items['file']}")


if __name__ == "__main__":
    main()
