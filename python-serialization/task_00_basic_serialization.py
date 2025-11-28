#!/usr/bin/python3
"""
Bu modul Python lüğətini JSON faylına serializasiya etmək v�
JSON faylını deserializasiya etmək funksiyalarını ehtiva edir.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Python lüğətini (data) götürür və onu verilən ada (filename) sa
    JSON faylına yazır. Əgər fayl varsa, üzərinə yazır.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Verilən JSON faylını (filename) oxuyur və
    Python lüğəti kimi geri qaytarır.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
