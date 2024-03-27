
import sys
from typing import List

import click
from loguru import logger

from src.rules import Rules


class Converter:
    
    def __init__(self) -> None:
        self.units = ['un', 'dix', 'cent']

    def convert_to_string(self, number_str: str) -> list:
        """
        Convert a number into a list of strings representing its digits and corresponding units.

        Args:
            number (str): The number to be converted.

        Returns:
            list: A list of strings representing each digit of the number and its unit.
        """
        letters = []

        for i, digit in enumerate(number_str[::-1]):
            letters.append(f'{digit}_x_{self.units[i % len(self.units)]}')

        return letters


    def convert_units(self, lettres: list) -> list:
        """
        Convert the digits into French words using predefined mappings.

        This function takes a list of strings representing each digit and its unit and converts them
        into French words based on predefined mappings for units, tens, and hundreds.

        Args:
            lettres (list): A list of strings representing each digit and its unit.

        Returns:
            list: A list of strings containing the French words representing the numbers.
        """
        processed_lettres = []  
        for x in lettres:  
            digit, unit = x.split('_x_') 
            # if the unit is for units 
            if unit == self.units[0]:  
                processed_lettres.append(Rules.rule_units(digit))  
            # if the unit is for tens
            elif unit == self.units[1]:  
                processed_lettres.append(Rules.rule_tens(digit))  
                processed_lettres.append("x")  
            # If the unit is for hundreds
            else:  
                processed_lettres.append(Rules.rule_hundreds(digit))  

        return processed_lettres  


    def convert_tens(self, lettre: List[str]) -> List[str]:
        """
        Convert the representation of tens into French words.

        Args:
            lettre (list): A list representing the digits and their units.

        Returns:
            list: A list containing French words representing the tens and units.
        """
        processed_lettres = []
        for i, item in enumerate(lettre):
            if item == 'x':
                # process the digits befor and after 'x'
                processed_lettres.remove(lettre[i - 2])
                processed_lettres.remove(lettre[i - 1])
                processed_lettres.extend([Rules.rule_x(digit1=lettre[i - 2], digit2=lettre[i - 1])])
            else:
                processed_lettres.append(item)
        return processed_lettres


    def convert_hundred(self, lettres: List[str]) -> List[str]:
        """
        Convert the representation of hundreds into French words.

        Args:
            lettres (list): A list representing the digits and their units.

        Returns:
            list: A list containing French words representing the hundreds.
        """
        # if zero is in the number (ex. 200>209)
        if lettres[0] == 'zéro':
            # cas of 200 -> deux-cents with 's'
            if len(lettres[1].split('-')) == 2:
                return [lettres[1] + 's']
            else:
                return [lettres[1]]
        else:
            return [f"{lettres[1]}-{lettres[0]}"]


    def convert_thousands(self, lettres: List[str]) -> str:
        """
        Convert the representation of thousands into French words.

        Args:
            lettres (list): A list representing the digits and their units.

        Returns:
            str: French words representing the thousands.
        """
        # < 1000
        if len(lettres) == 1:
            return lettres[0]

        # if zero is in the number
        if lettres[0] == 'zéro' and  lettres[1] == 'un' :
            return 'mille'

        # case of 'un'
        if lettres[1] == 'un':
            return f"mille-{lettres[0]}"
        # case of plural
        elif lettres[0] == 'zéro':
            if lettres[1][-1] == 's' and 'trois' not in lettres[1]:
                return f"{lettres[1][:-1]}-milles"
            return f"{lettres[1]}-milles"

        return f"{lettres[1]}-mille-{lettres[0]}"



    def convert_to_french(self, number:str) -> str:
        """
        Convert a numerical input into its French word representation.

        Args:
            number (str): The numerical input to be converted.

        Returns:
            str: The French word representation of the input number.
        """
        try:
            number = str(int(number))
        except Exception as e:
            # Log the exception and exit if the input cannot be converted to an integer
            logger.exception(e)
            sys.exit(0)

        # Divide the number into parts of three digits each
        parts = [str(int(number[max(0, i-3):i])) for i in range(len(number), 0, -3)]
        final_letters = []

        # Convert each part to French words and combine them
        for part in parts:
            letters = self.convert_to_string(part)
            letters = self.convert_units(letters)
            # > 10
            if len(letters) != 1:
                letters = self.convert_tens(letters)
            # > 100
            if len(letters) != 1:
                letters = self.convert_hundred(letters)
            final_letters.append(letters[0])

        return self.convert_thousands(final_letters)

@click.command()
@click.option("--number", required=True, help="number to be converted")
def main(number:str):
    converter = Converter()
    results = converter.convert_to_french(number=number)
    logger.info(f'{number} in French words is -> {results}')
    

if __name__ == "__main__":
    main()
