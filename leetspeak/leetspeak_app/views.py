import re
from typing import Dict, Pattern
from django.http import HttpResponse
from django.shortcuts import render


class LeetspeekConverter:
    TEXT: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LEET: str = "4bcd3f9h1jklmn0pqr57uvwxyz4bcd3f6h1jklmn0pqr57uvwxyz"

    def __init__(self) -> None:
        self.leet_dict: Dict[str, str] = dict(zip(self.TEXT, self.LEET))

    def convert_to_leet(self, text) -> str:
        """ Hack to implement multiple re.sub on the same string in one go
        https://stackoverflow.com/questions/35713540/replace-more-than-one-pattern-python
        """
        regex: Pattern[str] = re.compile(r"(%s)" % "|".join(map(re.escape, self.leet_dict.keys())))
        return regex.sub(lambda x: self.leet_dict[x.string[x.start():x.end()]], text)


def api(request, string):
    converter = LeetspeekConverter()
    converter.convert_to_leet(string)
    return render(request, "leetspeak_app/index.html", {
        'leet_string': converter.convert_to_leet(string),
    })


def index(request):
    return render(request, 'leetspeak_app/index.html')
