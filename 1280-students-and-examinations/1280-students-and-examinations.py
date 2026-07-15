import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects,how='cross')

    exams = examinations.groupby(['student_id','subject_name'])['subject_name'].size().reset_index(name='attended_exams')

    new_df = df.merge(exams,how='left',on=['student_id','subject_name'],suffixes=('_subject_name', '_attended_exams'))

    new_df['attended_exams'] = new_df['attended_exams'].fillna(0)
    return new_df.sort_values(by=['student_id','subject_name'])