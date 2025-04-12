# ISTA_421_Midterm_2
Midterm 2, Part 2 for Introduction to Machine Learning

### Step 1

- [First resource](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011876/)
- [Second resource](https://newsroom.spectrumhealth.org/corewell-health-study-determines-keys-to-reducing-hospital-readmissions/)
- [Third resource](https://pmc.ncbi.nlm.nih.gov/articles/PMC8101040/)

### Step 3

- Facility Name (string): the name of the facility/clinic where data was collected.
- Facility ID (int): the unique id number associated with the facility/clinic where data was collected.
- State (string): the US state abbreviation in which the facility resides.
- Measure Name (string): the measure that the facility is reporting data on.
- Number of Discharges (int): The total number of patients that have been discharged from the facility between the Start Date and End Date and for the given measure. 
- Footnote (int): I cannot find an exact definition on their site, but footnote is generally some kind of additional notes or clarifications made by the facility. The majority of footnotes are blank anyway.
- Excess Readmission Ratio (float): The ratio of a facility's actual readmissions to an expected number of readmissions. A number >1 means there are more readmissions than expected. 
- Predicted Readmission Rate (float): The derived rate (as a percentage) at which readmissions are expected to occur within the reporting period. 
- Expected Readmission Rate (float): The target readmission rate (as a percentage) that the facility's stats are compared against. 
- Number of Readmissions (string): The total number of patient readmissions in the reporting period. This column has to be a string because in some cases, the value is "Too Few to Report" for privacy reasons. 
- Start Date (date): The beginning date of the reporting period in which the data were collected.
- End Date (date): The final date of the reporting period in which the data were collected.

### Step 4

Research question: Are there consistent over or under performing hospitals across multiple readmission measures?

### Step 5

This question is important to the board because they may want to penalize/fine hospitals with excess readmission rates. If a facility consistently underperforms across multiple conditions, it’s likely to repeat penalties, which can translate directly into financial loss. Thus, identifying these patterns here can prioritize prevention and resource allocation, potentially saving the hospital a lot of money and readmissions. On the other end of the spectrum, if a particular facility/hospital is consistently overperforming across multiple conditions, the board can study what this hospital is doing **right** so as to implement/replicate it in other facilities. Finally, from the patients' perspectives, the facilities are only going to improve with this knowledge, resulting in frequently better patient outcomes. 

### Step 9

- Conclusions: 
    - My model correctly classified 95% of all 749 hospitals in the test set
- Predictions: 
- Recommendations: 

## Running the Model

Running my model is very simple. I have a random forest model that will run automatically and print a classification report, assuming you run the file "step_6_chose-algo.py" and the dataset is in your working directory. 

## Disclosures

None