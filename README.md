# Stroke prediction project

The project contains these files: 

'stroke_prediction.ipynb" - a Jupyter notebook with all calculations and explanations; 

'stroke.csv" - the stroke prediction dataset which was used for the analysis; 

'stroke_utils.py" - functions that were imported into the Jupyter notebook file;

'XgBoost.joblib' - the XgBoost classifier trained on 14 feature variables: 'age', 'avg_glucose_level', 'bmi', 'gender_Female', 
'ever_married_Yes', 'work_type_Govt_job', 'work_type_Private', 'work_type_Self-employed', 'Residence_type_Urban', 'smoking_status_formerly smoked', 'smoking_status_never smoked', 'smoking_status_smokes', 'hypertension', 'heart_disease'. The classifier is used for the prediction of the probability of stroke based on the input values presented by an user.
