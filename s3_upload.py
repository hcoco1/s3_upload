import os
import boto3
import sys

config = {
    'bucket_name' : 'python3-boto3-hcoco1-test-bucket'
}
print(config['bucket_name'])

csv_dir = 'csv_files'

config['csv_dir'] = csv_dir
print(config)

# sys.exit()

if os.listdir(config['csv_dir']):
    print(f"Files found in the {config['csv_dir']} directory.")

    csv_list = os.listdir(config['csv_dir'])
    print(csv_list)   

    s3 = boto3.resource('s3')
    for file in csv_list:      
        root, ext = os.path.splitext(file)
        
        if ext != '.csv':
            print(f"\n{file} is incorrect file type '{ext}'. Expecting: '.csv'.")
        else:
            local_filepath = f"{config['csv_dir']}/{file}"
            s3_filename = file.replace('_', '/')
        
            s3.Bucket(config['bucket_name']).upload_file(local_filepath, s3_filename)
            print(f"\nThe {file} file was uploaded to {config['bucket_name']} at {s3_filename}.")
        
else:
    print(f"No files found in the {config['csv_dir']}.")
    print(f"list: {csv_list}")
    
    
    
    


    