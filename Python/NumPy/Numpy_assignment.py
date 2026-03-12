import logging
import pandas as pd


# Logger Setup
def setup_logger(log_file: str = 'logs.log') -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s')

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Add handlers if not already added
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

logger = setup_logger()
logger.info("Pipeline started")





# TASK - 1
# Load Data
def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, parse_dates=['Joining_Date'], dayfirst=True)
    logger.info(f"Loaded {len(df)} records with columns: {df.dtypes.to_dict()}")
    return df

record = load_data('employees.csv')






# TASK - 2
# Data Cleaning
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Data cleaning started")

    # Standardize column names
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
    logger.info(f"Standardized columns: {df.columns.tolist()}")

    # Fill missing salary with mean
    if df['salary'].isnull().any():
        mean_salary = df['salary'].mean()
        df['salary'].fillna(mean_salary, inplace=True)
        logger.info(f"Filled missing salaries with mean: {mean_salary:.2f}")

    # Fill missing age with median
    if df['age'].isnull().any():
        median_age = df['age'].median()
        df['age'].fillna(median_age, inplace=True)
        logger.info(f"Filled missing ages with median: {median_age:.0f}")

    # Remove duplicates based on employee_id
    duplicates_count = df.duplicated(subset=['employee_id']).sum()
    if duplicates_count > 0:
        df.drop_duplicates(subset=['employee_id'], inplace=True)
        logger.info(f"Removed {duplicates_count} duplicate records based on employee_id")

    # Ensure correct data types
    df['resigned'] = df['resigned'].astype(bool)

    logger.info("Data cleaning completed")
    return df

record = clean_data(record)






# TASK - 3
# Data Manipulation
def manipulate_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Data manipulation started")
    initial_count = len(df)

    # Filter employees: age > 25 OR salary > 40000, and not resigned
    filtered = df[((df['age'] > 25) | (df['salary'] > 40000)) & (~df['resigned'])]
    filtered_count = len(filtered)
    logger.info(f"Records before filtering: {initial_count}, after filtering: {filtered_count}")

    # Add years_in_company
    today = pd.to_datetime("today")
    filtered = filtered.copy()  # Avoid SettingWithCopyWarning
    filtered['years_in_company'] = (today - filtered['joining_date']).dt.days // 365

    logger.info("Data manipulation completed")
    return filtered

record_filtered = manipulate_data(record)






# TASK - 4
# Aggregation & Analysis
def analyze_data(df: pd.DataFrame, department_to_increment: str = 'Sales') -> pd.DataFrame:
    logger.info("Aggregation & analysis started")

    # Department-level stats
    dept_stats = df.groupby('department').agg(
        avg_salary=('salary', 'mean'),
        median_age=('age', 'median')
    ).reset_index()
    logger.info(f"Department-level stats:\n{dept_stats}")

    # Apply 10% increment to a department
    increment_mask = df['department'] == department_to_increment
    df.loc[increment_mask, 'salary'] *= 1.10
    logger.info(f"Applied 10% salary increment to department: {department_to_increment}")

    logger.info("Aggregation & analysis completed")
    return df

record_filtered = analyze_data(record_filtered)

# TASK - 5
# Transformation & Export
def export_data(df: pd.DataFrame, file_path: str = 'cleaned_employees.json') -> None:
    logger.info("Data transformation & export started")

    # Keep relevant fields & sort
    final_df = df[['employee_id', 'name', 'age', 'department', 'salary', 'years_in_company']]
    final_df = final_df.sort_values(by='employee_id')

    # Export to JSON
    final_df.to_json(file_path, orient='records', date_format='iso')
    logger.info(f"Exported cleaned dataset to {file_path} with {len(final_df)} records")
    logger.info("Data transformation & export completed")

export_data(record_filtered)