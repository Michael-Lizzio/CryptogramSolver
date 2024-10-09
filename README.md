
# Cryptogram Solver

## Overview
This project is a cryptogram solver created by **YATA Systems**, featuring our mascot, IGOR! The solver takes in a cryptic quote and decodes it using various techniques, including word sorting, letter frequency analysis, and a brute force approach to test potential solutions. The system works by analyzing patterns in the encrypted text and cross-referencing them with known word lists to decode the message.

## How It Works
### 1. **Cryptogram Input**
   - The user provides a cryptogram, which is a string of text where each letter represents another letter.
   - The solver uses a brute force method to test different words from a word list, trying to match the letters and words in the cryptogram.

### 2. **Word Sorting (Using Letter Frequency)**
   - **Sorting Function:** The cryptogram text is first broken into words and sorted. Larger words are prioritized because they often provide more useful letter patterns.
   - **Letter Frequency:** The solver counts the occurrences of each letter in the cryptogram’s longest word and sorts other words by how closely they match this frequency pattern. This strategy helps IGOR focus on more probable letter mappings.

### 3. **Brute Force Solving**
   - The solver loops through possible words from the word list, trying to map encrypted letters to actual letters.
   - For each potential match, it checks whether the letter mappings are consistent across the cryptogram.
   - If a mismatch occurs, the solver resets to the last known good state and continues testing.
   - The process repeats until a solution is found or until all possibilities have been exhausted.

### 4. **Discovery Lists**
   - **Encrypted Letter Discovery List:** Keeps track of which encrypted letters correspond to known letters.
   - **Plain Letter Discovery List:** Tracks the plaintext letters as they are identified.
   - These lists allow the solver to systematically refine the solution as more information becomes available.

### 5. **User Interaction**
   - After decoding the cryptogram, the solver asks the user if they’d like to change any words. The user can adjust specific words and the solver will re-run the decoding process.

## Word Lists
The word lists used for matching are sourced from:
**[Gwick's Dictionaries](http://www.gwicks.net/dictionaries.htm)**, which provides a wide array of word lengths and frequency analyses used in this project.

## Example Output

```plaintext
Created by YATA Systems -- Say Hello to IGOR!!!
MG SMT ZQUQ Z BWGQHFTL FQ Z CTTV CTP CFDG OFLWHGQ MG SMT ETGQ LTH ZQU Z BWGQHFTL PGOZFLQ Z CTTV CTPGDGP
['BWGQHFTL', 'OFLWHGQ', 'PGOZFLQ', 'CTPGDGP', 'ETGQ', 'LTH', 'ZQUQ', 'CTTV', 'CFDG', 'FQ', 'SMT', 'CTP', 'ZQU', 'MG', 'Z']
['BEHAVIOR', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['COMPUTER', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['CONSIDER', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['CONSUMER', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['CUSTOMER', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['DAUGHTER', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['DEMOCRAT', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['DISCOVER', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['HOSPITAL', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['INDUSTRY', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['MAJORITY', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['PERSONAL', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['PHYSICAL', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['QUESTION', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['QUESTION', 'MINUTES', '', '', '', '', '', '', '', '', '', '', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', '', '', '', '', '', '', '', '', '', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', '', '', '', '', '', '', '', '', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', '', '', '', '', '', '', '', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', 'NOT', '', '', '', '', '', '', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', 'NOT', 'ASKS', '', '', '', '', '', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', 'NOT', 'ASKS', 'FOOL', '', '', '', '', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', 'NOT', 'ASKS', 'FOOL', 'FIVE', '', '', '', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', 'NOT', 'ASKS', 'FOOL', 'FIVE', 'IS', '', '', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', 'NOT', 'ASKS', 'FOOL', 'FIVE', 'IS', 'WHO', '', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', 'NOT', 'ASKS', 'FOOL', 'FIVE', 'IS', 'WHO', 'FOR', '', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', 'NOT', 'ASKS', 'FOOL', 'FIVE', 'IS', 'WHO', 'FOR', 'ASK', '', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', 'NOT', 'ASKS', 'FOOL', 'FIVE', 'IS', 'WHO', 'FOR', 'ASK', 'HE', '']
['QUESTION', 'MINUTES', 'REMAINS', 'FOREVER', 'DOES', 'NOT', 'ASKS', 'FOOL', 'FIVE', 'IS', 'WHO', 'FOR', 'ASK', 'HE', 'A']
Done ( ͡⎚ ͜ʖ ͡⎚)
0-BWGQHFTL 1-OFLWHGQ 2-PGOZFLQ 3-CTPGDGP 4-ETGQ 5-LTH 6-ZQUQ 7-CTTV 8-CFDG 9-FQ 10-SMT 11-CTP 12-ZQU 13-MG 14-Z
0-QUESTION 1-MINUTES 2-REMAINS 3-FOREVER 4-DOES 5-NOT 6-ASKS 7-FOOL 8-FIVE 9-IS 10-WHO 11-FOR 12-ASK 13-HE 14-A

crypto-quote - MG SMT ZQUQ Z BWGQHFTL FQ Z CTTV CTP CFDG OFLWHGQ MG SMT ETGQ LTH ZQU Z BWGQHFTL PGOZFLQ Z CTTV CTPGDGP
  solution   - HE WHO ASKS A QUESTION IS A FOOL FOR FIVE MINUTES HE WHO DOES NOT ASK A QUESTION REMAINS A FOOL FOREVER
Difference - 0:00:00.621482
```

## Getting Started
1. **Prerequisites**: Python 3.x.
2. **Running the Solver**:
   - Save the code in a Python file (e.g., `cryptogram_solver.py`).
   - Run the script by entering the cryptogram text in the `crypto_text` variable and executing the file.
3. **Customization**:
   - You can modify the cryptogram text to test different encrypted messages.
   - You can also add your own word lists to the `/word-lists/` directory.

## Conclusion
The Cryptogram Solver uses a combination of word sorting, letter frequency analysis, and brute-force tactics to crack cryptic codes. Feel free to experiment with different cryptograms, and let IGOR help you solve them!
