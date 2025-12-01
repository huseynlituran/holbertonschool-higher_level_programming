#!/usr/bin/python3
"""
Module to generate invitations from a template.
"""
import os

def generate_invitations(template, attendees):
    """
    Generates invitation files based on a template and a list of attendees.

    Args:
        template (str): The content of the invitation template.
        attendees (list): A list of dictionaries containing attendee details.
    """
    # 1. Check Input Types
    # Template string, attendees isə list olmalıdır.
    if not isinstance(template, str):
        print("Error: Invalid input type for template. Expecting string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Invalid input type for attendees. Expecting list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    # Əgər template boşdursa
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    # Əgər siyahı boşdursa
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process Each Attendee
    # enumerate funksiyası bizə həm index-i (1-dən başlayaraq), həm də datanı verir.
    for index, attendee in enumerate(attendees, start=1):
        # Şablonun surətini çıxarırıq ki, orijinal dəyişməsin
        content = template

        # Dəyişdiriləcək açar sözlər
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for key in placeholders:
            # Məlumatı lüğətdən götürürük.
            value = attendee.get(key)
            # Əgər məlumat yoxdursa (None) və ya açar tapılmırsa, "N/A" edirik
            if value is None:
                value = "N/A"
            # String daxilindəki {key}-i real dəyərlə əvəz edirik.
            # {key} -> məsələn {name}
            placeholder_str = "{" + key + "}"
            content = content.replace(placeholder_str, str(value))

        # 4. Generate Output Files
        # Fayl adını düzəldirik: output_1.txt, output_2.txt ...
        filename = "output_{}.txt".format(index)
        try:
            with open(filename, 'w') as file:
                file.write(content)
        except Exception as e:
            print("Error writing to file {}: {}".format(filename, e))
