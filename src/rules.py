from src.utils import load_data

# Load the data from the YAML file into a dictionary.
number_to_letter_data = load_data('src/data.yml')

# Create a reverse mapping dictionary where keys and values are swapped for both units and tens.
letter_to_number_data = {
    'units': {v: k for k, v in number_to_letter_data['units'].items()},
    'tens': {v: k for k, v in number_to_letter_data['tens'].items()},
}

class Rules:

    @staticmethod
    def rule_units(digit: str) -> str:
        """
        Convert a digit representing the units place into French words.

        Args:
            digit (str): A string representing the digit.

        Returns:
            str: The French words representing the digit in the units place.
        """
        return number_to_letter_data['units'][digit]

    @staticmethod
    def rule_tens(digit: str) -> str:
        """
        Convert a digit representing the tens place into French words.

        Args:
            digit (str): A string representing the digit.

        Returns:
            str: The French words representing the digit in the tens place.
        """
        digit = str(int(digit) * 10)
        return number_to_letter_data['tens'][digit] if digit in number_to_letter_data['tens'] else "zéro"

    @staticmethod
    def rule_hundreds(digit: str) -> str:
        """
        Convert a digit representing the hundreds place into French words.

        Args:
            digit (str): A string representing the digit.

        Returns:
            str: The French words representing the digit in the hundreds place.
        """
        # case of 100, 200, 900
        if not Rules.rule_units(digit) == 'un':
            return f"{Rules.rule_units(digit)}-cent"
        else:
            return 'cent'

    @staticmethod
    def rule_x(digit1: str, digit2: str)-> str:
        """
        Convert a pair of digits into French words 
        This function takes two digits and converts them into French words
        for units and tens. It handles cases where the digits are combined with hyphens to form compound numbers.

        Args:
            digit1 (str): The first digit to be converted.
            digit2 (str): The second digit to be converted.

        Returns:
            str: The French word representation of the input pair of digits.
        """
        # Case 1: Calculate the sum of the tens and units digits
        number = str((int(letter_to_number_data['tens'][digit2]) + int(letter_to_number_data['units'][digit1])))

        # Case 2: If the sum is in the predefined mappings for units, return its French word
        if number in number_to_letter_data['units']:
            return number_to_letter_data['units'][number]
        
        # Case of 80 with and without 's'
        if digit1 == "zéro":
            if len(digit2.split('-'))==2 and int(letter_to_number_data['tens'][digit2]) == 80:
                return digit2+'s'
            return digit2
        
        # Case 4: If digit2 is a compound number with a hyphen (e.g., "quatre-vingt"), handle it
        if len(digit2.split('-'))==2:
            unit, tens = digit2.split('-')
            number = str((int(letter_to_number_data['tens'][tens]) + int(letter_to_number_data['units'][digit1])))
            if number in number_to_letter_data['units']:
                if digit1 =='un':
                    return f"{unit}-et-{number_to_letter_data['units'][number]}"
                else:
                    return f"{unit}-{number_to_letter_data['units'][number]}"
            
            return f'{digit2}-{digit1}'
        
        # Case 5: If digit2 is a compound number with two hyphens (e.g., "cent-quatre-vingt"), handle it
        if len(digit2.split('-'))==3:
            unit_1, unit_2, tens = digit2.split('-')
            number = str((int(letter_to_number_data['tens'][tens]) + int(letter_to_number_data['units'][digit1])))
            if number in number_to_letter_data['units']:
                    return f"{unit_1}-{unit_2}-{number_to_letter_data['units'][number]}" 
            return f'{digit2}-{digit1}'
        
        # Case 6: If digit1 is "un", handle special case 
        if digit1 == 'un':
            return f"{digit2}-et-{digit1}"
        
        
        return f'{digit2}-{digit1}' 
