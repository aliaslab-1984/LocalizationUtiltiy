# LocalizationUtiltiy
A small python library that helps you to generate localization strings for your mobile projects.

This small script aims to help you to manage localization for your cross-platform apps.
To start off you have to configure a .csv file (or generate it using microsoft excell or pages) with this format:

| KEYS        | eng           | ita  |
| ------------- |:-------------:| -----:|
| hello_message      | Hello! |  Ciao! |

Once you have exported the .csv file, all you have to do is open your terminal and type:
```bash
python3 localizationUtility.py ~/Desktop/translation.csv
```
Easy right ? The script will export all the translated strings right where your .csv file is located.

### Notes:
This script depends on [pandas](https://github.com/pandas-dev/pandas) library, so make sure to have the latest version on your machine before running the script.
