from pyspark.sql import SparkSession
import os
import re

def extract_part_of_filename(file_path):
    # Extract the filename from the full path
    filename = os.path.basename(file_path)
    # Use regex to find the part between '_dataset_' and '.json'
    match = re.search(r'_dataset_(.*?)\.json', filename)
    if match:
        return match.group(1)
    return None

def split_json_with_pyspark(input_path, chunk_size=120000):  # Adjust chunk size as needed
    filename_part = extract_part_of_filename(input_path)
    output_dir = os.path.join('/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/chunks/', filename_part)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Initialize Spark session with adjusted configurations
    spark = SparkSession.builder \
        .appName("Split JSON File") \
        .config("spark.executor.memory", "8g") \
        .config("spark.driver.memory", "8g") \
        .config("spark.executor.cores", "2") \
        .config("spark.executor.instances", "1") \
        .getOrCreate()

    # Read JSON file into DataFrame
    df = spark.read.json(input_path)

    # Get the total number of records
    total_records = df.count()
    print(f"Total records: {total_records}")

    # Calculate the number of partitions to create
    num_partitions = (total_records // chunk_size) + (total_records % chunk_size > 0)

    # Repartition DataFrame to the calculated number of partitions
    df_repartitioned = df.repartition(num_partitions)

    # Write the repartitioned DataFrame to JSON files with overwrite mode
    df_repartitioned.write.mode('overwrite').json(output_dir)
    print(f"Data written to {output_dir}")

    # Stop Spark session
    spark.stop()

# File paths
user_datapath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_academic_dataset_user.json'
checkin_datapath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_academic_dataset_checkin.json'
review_datapath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_academic_dataset_review.json'

if __name__ == "__main__":
    # split_json_with_pyspark(user_datapath)
    split_json_with_pyspark(checkin_datapath)
    split_json_with_pyspark(review_datapath)


# from pyspark.sql import SparkSession
# import os
# import re

# def extract_part_of_filename(file_path):
#     filename = os.path.basename(file_path)
#     match = re.search(r'_dataset_(.*?)\.json', filename)
#     if match:
#         return match.group(1)
#     return None


# def split_json_with_pyspark(input_path, output_dir, chunk_size=240000):
#     # Initialize Spark session
#     spark = SparkSession.builder \
#         .appName("Split JSON File") \
#         .getOrCreate()

#     # Read JSON file into DataFrame
#     df = spark.read.json(input_path)

#     # Get the total number of records
#     total_records = df.count()
#     print(f"Total records: {total_records}")

#     # Calculate number of chunks
#     num_chunks = (total_records // chunk_size) + (total_records % chunk_size > 0)
#     filename = extract_part_of_filename(input_path)
#     for i in range(num_chunks):
#         # Get the start and end indices for the current chunk
#         start = i * chunk_size
#         end = start + chunk_size

#         # Get the chunk DataFrame
#         chunk_df = df.limit(end).subtract(df.limit(start))

#         # Write the chunk DataFrame to a JSON file
#         chunk_file_path = os.path.join(output_dir, f"chunk_{i + 1}.json")
#         chunk_file_path =  chunk_file_path + '_' + filename
#         chunk_df.write.json(chunk_file_path)
#         print(f"Created {chunk_file_path}")

#     # Stop Spark session
#     spark.stop()

# # File paths
# user_datapath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_academic_dataset_user.json'
# user_outpath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_user_data'
# checkin_datapath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_academic_dataset_checkin.json'
# checkin_outpath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_checkin_data'
# review_datapath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_academic_dataset_review.json'
# review_outpath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_review_data'

# if __name__ == "__main__":
#     print(extract_part_of_filename(user_datapath))
#     split_json_with_pyspark(user_datapath, user_outpath)
#     # split_json_with_pyspark(checkin_datapath, checkin_outpath)
#     # split_json_with_pyspark(review_datapath, review_outpath)

#--------------------------------------------------------------------

# import json
# from tqdm import tqdm

# def split_json(file_path, output_dir, chunk_size=245760):
#     with open(file_path, 'r') as f:
#         data = json.load(f)
    
#     # Calculate number of chunks
#     num_chunks = len(data) // chunk_size + (len(data) % chunk_size > 0)
    
#     for i in tqdm(range(num_chunks), desc="Splitting JSON file"):
#         chunk = data[i * chunk_size:(i + 1) * chunk_size]
#         chunk_file_path = f"{output_dir}/chunk_{i + 1}.json"
        
#         with open(chunk_file_path, 'w') as chunk_file:
#             json.dump(chunk, chunk_file)
#         # Print message for each chunk created (optional, since tqdm already shows progress)
#         print(f"Created {chunk_file_path}")

# # File paths
# user_datapath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_academic_dataset_user.json'
# user_outpath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_user_data'
# checkin_datapath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_academic_dataset_checkin.json'
# checkin_outpath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_checkin_data'
# review_datapath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_academic_dataset_review.json'
# review_outpath = '/home/ra-terminal/Desktop/portfolio_projects/udacity_data_architecture_course/designing_data_systems/json_data/yelp_review_data'

# if __name__ == "__main__":
#     split_json(user_datapath, user_outpath)
#     # split_json(checkin_datapath, checkin_outpath)
#     # split_json(review_datapath, review_outpath)

