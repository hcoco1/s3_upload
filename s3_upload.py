# Import necessary modules
import os
import boto3
import sys

# Configuration dictionary containing the S3 bucket name
config = {
   'bucket_name': 'python3-boto3-hcoco1-test-bucket'
}

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the directory where the CSV files are located
csv_dir = os.path.join(script_dir, 'csv_files')

# Print the current working directory
print(os.getcwd())

# Add the CSV directory to the configuration dictionary
config['csv_dir'] = csv_dir
print(config)

# Uncomment the following line if you want to exit the script here
# sys.exit()

try:
    # Check if there are any files in the CSV directory
    if os.listdir(config['csv_dir']):
        print(f"Files found in the {config['csv_dir']} directory.")
        
        # List all files in the CSV directory
        csv_list = os.listdir(config['csv_dir'])
        print(csv_list)
        
        # Initialize the S3 resource using boto3
        s3 = boto3.resource('s3')
        
        # Iterate over each file in the CSV list
        for file in csv_list:
            try:
                # Split the file name into root and extension
                root, ext = os.path.splitext(file)
                
                # Check if the file has a .csv extension
                if ext != '.csv':
                    print(f"\n{file} is incorrect file type '{ext}'. Expecting: '.csv'.")
                else:
                    # Define the local file path
                    local_filepath = f"{config['csv_dir']}/{file}"
                    # Replace underscores with slashes for the S3 file path
                    s3_filename = file.replace('_', '/')
                
                    # Upload the file to the specified S3 bucket
                    s3.Bucket(config['bucket_name']).upload_file(local_filepath, s3_filename)
                    print(f"\nThe {file} file was uploaded to {config['bucket_name']} at {s3_filename}.")
                
                    # Uncomment the following line if you want to remove the local file after upload
                    # os.remove(local_filepath)
            except PermissionError as pe:
                print(f"Error in {__file__}.\n{pe}.")
    else:
        print(f"No files found in the {config['csv_dir']}.")
        print(f"list: {csv_list}")
except FileNotFoundError as fne:
    print(f"\nError in {__file__}.\n{fne}\nThe current working directory is: {os.getcwd()}.")

    
    
    


    