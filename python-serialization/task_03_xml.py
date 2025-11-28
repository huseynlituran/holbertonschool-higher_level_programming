#!/usr/bin/python3
"""
This module provides functions to serialize and deserialize a Python dictionary
using XML format.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.
    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename for the output XML file.
    """
    # 1. Kök elementini (Root) yaradırıq: <data>
    root = ET.Element("data")

    # 2. Lüğətdəki hər bir elementi XML uşağı (child) kimi əlavə edirik
    for key, value in dictionary.items():
        # Uşaq element yaradılır: <key>
        child = ET.SubElement(root, key)
        # Elementin mətni təyin edilir: <key>value</key>
        child.text = str(value)

    # 3. XML ağacını yaradırıq və fayla yazırıq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file to a Python dictionary.
    Args:
        filename (str): The filename of the input XML file.
    Returns:
        dict: A dictionary constructed from the XML data.
    """
    try:
        # 1. XML faylını oxuyuruq (parse edirik)
        tree = ET.parse(filename)
        root = tree.getroot()

        # 2. Məlumatları yığmaq üçün boş lüğət yaradırıq
        result_dict = {}

        # 3. Kökün içindəki bütün uşaqları (children) gəzirik
        for child in root:
            # child.tag -> açar (məsələn: 'name')
            # child.text -> dəyər (məsələn: 'John')
            result_dict[child.tag] = child.text

        return result_dict
    except FileNotFoundError:
        return None
