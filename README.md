# LocalizationUtiltiy
A small python library that helps you to generate localization strings for your mobile projects and to merge iOS and Android localization files into a single .csv file.

### localizationUtility.py

This small script aims to help you to manage localization for your cross-platform apps.
To start off you have to configure a .csv file (or generate it using microsoft excell or pages) with this format:

| KEYS          | en          | it          |
| ------------- |:-----------:| -----------:|
| hello_message | Hello!      | Ciao!       |
| second_message| God Morning!| Buongiorno! |

Once you have exported the .csv file, all you have to do is open your terminal and type:
```bash
python3 localizationUtility.py ~/Desktop/translation.csv
```
Easy right ? The script will export all the translated strings right where your .csv file is located.

### fromiOStocsv.py and fromAndroidTocsv.py

This script aims to convert your existing .strings/.xml files into a structured .csv file. If the output .csv file already exists, it appends the new one to the old one.

>**Usage:** 
>```shell
> python3 fromiOStocsv.py firstFile.strings en
>```

The second parameter is the *language identifier*, which identifies the column name that is going to be used for the provided file. 

It's also possible to specify a third parameter into the script to specify the path for the outputfile (remember to assign a name to it).
Here's the usage with the third parameter:

>```shell
> python3 fromiOStocsv.py firstFile.strings en ../Output/translation.csv
>```

### mergeCSV.py

This script aims to merge multiple localization csvs into one.

>**Usage:** 
>```shell
>python3 mergeCSV.py firstFile.csv secondFile.csv
>```

### Notes:

- This script depends on [pandas](https://github.com/pandas-dev/pandas) library, so make sure to have the latest version on your machine before running the script.
- Feel free to contribute and to improve the scripts.
