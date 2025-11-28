#!/usr/bin/python3
"""
This module contains a function to convert CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and converts it into a JSON file named 'data.json'.
    Args:
        csv_filename (str): The name of the input CSV file.
    Returns:
        bool: True if conversion was successful, False if file not found.
    """
    try:
        # CSV faylini oxumaq ucun aciriq
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # Burda 4 bosluq (tab) olmalidir
            reader = csv.DictReader(csv_file)
            data_list = list(reader)

        # JSON faylini yazmaq ucun aciriq
        with open('data.json', 'w', encoding='utf-8') as json_file:
            # Burda da 4 bosluq olmalidir
            json.dump(data_list, json_file)

        return True

    except FileNotFoundError:
        return False
