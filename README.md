# Kaggle_Competition_1
Data Science's In-Class Kaggle Competition 1: Predicting Tabletennis players' Attributes

## Installation

1. Navigate to the directory containing the `Kaggle_Competition_1` folder:  
```bash
cd [DownloadFolder]
```  
2. Install the required packages:  
```bash
pip install pandas
pip install numpy
pip install scikit-learn
```

## Implement

1. Run `RF4GenderHand.py`  
This step generates predictions for `genger` & `hold racket handed`.  

2. Run `mergeGH.py` to merge results from step 1 and sample submission:  
This step outputs the predictions in the correct format.  

### Post-processing

- Check 30 rows at a time in the `gender` and `hold racket handed` columns.
- Identify the majority value for these rows in each column.
- Replace all values in the group of 30 rows with the identified majority value.
- There are three possibilities for `play years` and `level`. We can try at most 6 times to get the right answer.  

I got a 99.5% correction rate in late submission in order to improve my second competition's score.