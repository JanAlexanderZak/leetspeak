from typing import Dict, Pattern
import re


class LeetspeekConverter:
    TEXT: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LEET: str = "4bcd3f9h1jklmn0pqr57uvwxyz4bcd3f6h1jklmn0pqr57uvwxyz"

    def __init__(self) -> None:
        self.leet_dict: Dict[str, str] = dict(zip(self.TEXT, self.LEET))

    def convert_to_leet(self, text) -> str:
        """ ...
        https://stackoverflow.com/questions/35713540/replace-more-than-one-pattern-python
        """
        regex: Pattern[str] = re.compile(r"(%s)" % "|".join(map(re.escape, self.leet_dict.keys())))
        return regex.sub(lambda x: self.leet_dict[x.string[x.start():x.end()]], text)


if __name__ == "__main__":
    input_string = input("Please enter a string: \n")

    # catch mby binary or raw strings?
    if not isinstance(input_string, str):
        print("Your input was not a string")
        exit(0)

    converter = LeetspeekConverter()
    leet_string = converter.convert_to_leet(input_string)
    print(leet_string)
