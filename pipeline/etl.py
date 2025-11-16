import pandas as pd
import os

# Path
def load_data_from_local_service_data():
        base_dir =  r"D:\Code 2025\zentel_pipeline\data"
        file_name = "service_data.csv"
        file_path = os.path.join(base_dir, file_name)
        
        df =pd.read_csv(file_path)
        print(df)
load_data_from_local_service_data()


def load_data_from_local_employee():
        base_dir =  r"D:\Code 2025\zentel_pipeline\data"
        file_name = "employee.csv"
        file_path = os.path.join(base_dir, file_name)
        
        df =pd.read_csv(file_path)
        print("Employee",df)
load_data_from_local_employee()

def load_data_from_local_channel_type():
        base_dir =  r"D:\Code 2025\zentel_pipeline\data"
        file_name = "channel_type.csv"
        file_path = os.path.join(base_dir, file_name)
        
        df =pd.read_csv(file_path)
        print(f"Channel", df)
load_data_from_local_channel_type()

def load_data_from_local_service_tpye():
        base_dir =  r"D:\Code 2025\zentel_pipeline\data"
        file_name = "service_data.csv"
        file_path = os.path.join(base_dir, file_name)
        
        df =pd.read_csv(file_path)
        print(df)
load_data_from_local_service_tpye()

def load_data_from_local_location():
        base_dir =  r"D:\Code 2025\zentel_pipeline\data"
        file_name = "location.csv"
        file_path = os.path.join(base_dir, file_name)
        
        df =pd.read_csv(file_path)
        print(f'Location',df)
load_data_from_local_location()

def load_data_from_local_fault():
        base_dir =  r"D:\Code 2025\zentel_pipeline\data"
        file_name = "location.csv"
        file_path = os.path.join(base_dir, file_name)
        
        df =pd.read_csv(file_path)
        print(f'Faults',df)
load_data_from_local_fault()


# Cleaning functions
def clean_service_data(df):
        # Example cleaning steps
        df = df.dropna()  # Remove missing values
        df['service_date'] = pd.to_datetime(df['service_date'])  # Convert to datetime
        return df

print("Data cleaning functions defined.", clean_service_data(df=pd.DataFrame('service_date')))