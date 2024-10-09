
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
BABNGDZB PTZCU UDWB WTHRSTY UDYMCRDZ CD COBRN VNDKYBW TZF BABNGDZB NBXMUBU CD KBYRBAB RZ WTHRS.
['BABNGDZB', 'KBYRBAB', 'NBXMUBU', 'VNDKYBW', 'COBRN', 'UDWB', 'UDYMCRDZ', 'PTZCU', 'TZF', 'CD', 'RZ', 'WTHRSTY', 'WTHRS']
['EVERYONE', '', '', '', '', '', '', '', '', '', '', '', '']
['EVERYONE', 'BELIEVE', '', '', '', '', '', '', '', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', '', '', '', '', '', '', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', '', '', '', '', '', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', '', '', '', '', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', '', '', '', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', '', '', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'CANTS', '', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'CANTS', 'AND', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'CANTS', 'AND', 'TO', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'CANTS', 'AND', 'TO', 'IN', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'CANTS', 'AND', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'CANTS', 'AND', 'TO', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'CANTS', 'AND', 'TO', 'IN', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'WANTS', '', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'WANTS', 'AND', '', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'WANTS', 'AND', 'TO', '', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'WANTS', 'AND', 'TO', 'IN', '', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'WANTS', 'AND', 'TO', 'IN', 'MAGICAL', '']
['EVERYONE', 'BELIEVE', 'REFUSES', 'PROBLEM', 'THEIR', 'SOME', 'SOLUTION', 'WANTS', 'AND', 'TO', 'IN', 'MAGICAL', 'MAGIC']
Done ( ͡⎚ ͜ʖ ͡⎚)
0-BABNGDZB 1-KBYRBAB 2-NBXMUBU 3-VNDKYBW 4-COBRN 5-UDWB 6-UDYMCRDZ 7-PTZCU 8-TZF 9-CD 10-RZ 11-WTHRSTY 12-WTHRS
0-EVERYONE 1-BELIEVE 2-REFUSES 3-PROBLEM 4-THEIR 5-SOME 6-SOLUTION 7-WANTS 8-AND 9-TO 10-IN 11-MAGICAL 12-MAGIC

crypto-quote - BABNGDZB PTZCU UDWB WTHRSTY UDYMCRDZ CD COBRN VNDKYBW TZF BABNGDZB NBXMUBU CD KBYRBAB RZ WTHRS.
  solution   - EVERYONE WANTS SOME MAGICAL SOLUTION TO THEIR PROBLEM AND EVERYONE REFUSES TO BELIEVE IN MAGIC.
Difference - 0:00:00.340710

Would you like to change any of the words? Enter the number of the word you would like to change, or 'no' to continue.
no
IGOR, was happy to help! (✯‿✯)
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
