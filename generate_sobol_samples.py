import os
import pandas as pd
import sys
from SALib.sample import sobol

def generate_sobol_samples(params_section, params_name, params_id, bounds, num_samples, csv_file_url=None):
    """
    Generate parameter samples using Sobol's method.
    
    Parameters:
    - params_section (list): List of strings specifying the sections of the parameters.
    - params_name (list): List of strings specifying the names of the parameters.
    - params_id (list): List of integers specifying the IDs of the parameters.
    - bounds (list): List of lists specifying the bounds of the parameters.
    - num_samples (int): Number of samples to generate.
    - csv_file_url (str, optional): File path to save the output CSV file. If None, CSV file will be saved in the present working directory.

    Returns:
    - DataFrame: A pandas DataFrame containing the sampled parameter values with column names generated from the input parameters.
    """
    # Check if the lengths of input lists are equal
    if len(params_section) != len(params_name) or len(params_name) != len(params_id):
        sys.exit('"params_section", "params_name", and "params_id" must have the same length')

    # Make labels for each user-defined parameter
    params_label = [f"{params_section[i][:3].upper()}_{params_name[i]}_{params_id[i]}" for i in range(len(params_section))]

    # Define problem
    problem = {
        'num_vars': len(params_section),
        'names': params_label,
        'bounds': bounds
    }

    # Sample parameters
    param_values = sobol.sample(problem, num_samples, calc_second_order=True)
    
    # Create DataFrame with specified column names
    df = pd.DataFrame(param_values, columns=params_label)
    
    # Write DataFrame to CSV file if csv_file_url is provided
    if csv_file_url:
        df.to_csv(csv_file_url, index=True)
    else:
        current_directory = os.getcwd()
        csv_file_path = os.path.join(current_directory, 'X.csv')
        df.to_csv(csv_file_path, index=True)
        print(f"CSV file saved at: {csv_file_path}")
    
    return df
