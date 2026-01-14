# SIMPLE DIGITS GENERATION

simple Python script to generate a text file containing a sequence of numbers with a customizable length and an optional prefix

## FEATURES
- **customizable length**: set exactly how many digits you need (e.g., 8 digits).
- **optional Prefix**: add a starting number (e.g., `89` -> `8900000000`) or leave it empty for clean generation.
- **fast Output**: writes directly to a `.txt` file.

## USAGE

1. open the script and configure the variables at the top:

```python
digits = 8          # number of random digits (e.g., 00000000 to 99999999)
prefix = "11"       # prefix to add before the digits (set to "" for none)
filename = "8.txt"  # output filename