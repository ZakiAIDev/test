# French Number Converter

## Overview

This is a Python package designed to convert numerical inputs into their French word representation. The primary aim of this package is to convert numbers into their textual equivalents in French. For example, converting "123" into "cent-vingt-trois."

## Approach

The approach followed in this package is based on the observation that numbers can be segmented into groups of three digits, each representing a different magnitude (ones, tens, hundreds). This segmentation allows us to apply a consistent conversion process to each group, thereby simplifying the overall conversion.

### Segmentation

1. **Three-Digit Segmentation**: Numbers are divided into segments of three digits each. For example, "234567" would be segmented into ["234,567"].

### Conversion Process

1. **Individual Digit Conversion**: Each digit within a segment is converted individually into its corresponding French word representation. For instance, "782" would be represented as ['2_x_un', '8_x_dix', '7_x_cent'], indicating that 2 represents units, 8 represents tens, and 7 represents hundreds.
   
2. **Application of Conversion Rules**: The conversion of each digit is governed by predefined conversion rules. These rules dictate how individual digits are translated into French words based on their position and value.

3. **Combination of Segments**: If the input number consists of multiple segments, such as thousands, millions, etc., a process of combining these segments is applied according to the appropriate rules. For example, combining "mille" (thousand) with the French word representation of the remaining digits.


## Example

Consider the number "654321":

### Segmentation:

Dividing the number into segments results in ["654,321"].

### Conversion:

#### For 321:
- "3" is converted to "trois-cent" (three hundred).
- "2" is converted to "vingt" (twenty).
- "1" is converted to "un" (one).

#### For 654:
- "6" is converted to "six-cent" (six hundred).
- "5" is converted to "cinquante" (fifty).
- "4" is converted to "quatre" (four).

### Combination:

The converted segments are then combined:

- **321**: "trois-cent-vingt-et-un"
- **654**: "six-cent-cinquante-quatre"

### Final Result:

Combining the two segments yields the French word representation of the number:

**French Representation**: "six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un"

## Usage

To convert a numerical input into its French word representation, you can use the command-line interface.


```bash
python -m src.main --number 654321
# Output: "six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un"
```

This will display the French word representation of the provided number.


### Installation

You can install the dependencies using [Poetry](https://python-poetry.org/) or directly from the `requirements.txt` file.

```bash
poetry install
# or
pip install -r requirements.txt
```

### Testing

You can run tests using [pytest](https://docs.pytest.org/en/stable/) by executing the following command:

```bash
pytest test.py
```


---

## Usage of ChatGPT

- Docstrings for each function were generated using ChatGPT with a prompt tailored for function documentation.
- The README file was generated using ChatGPT with a customized prompt.

