# word-pw - simple passphrase generator

### Usage

1. **Download the EFF Large Wordlist for Passphrases**
   - Download the wordlist from [EFF Large Wordlist for Passphrases](https://www.eff.org/document/passphrase-wordlists).

2. **File Placement**
   - Make sure that the downloaded file is placed in the same directory as the scripts.
   - Ensure the downloaded file is named `eff.org_files_2016_07_18_eff_large_wordlist.txt`. You can change the filename if needed, but follow any specific naming conventions required by the scripts.

3. **Run `make.py`**
   - Execute the `./make.py` script in your terminal.
   - This script will create a file named `words.pkl` containing a pickled array from the EFF word list (numbers are excluded) with gzip compression.

4. **Run `pw.py`**
   - Execute the `./pw.py` script in your terminal.
   - This script will open `words.pkl` and randomly print out 8 words as a passphrase.
   - Note that the downloaded EFF text file is not used by this script.
