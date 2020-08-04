from boto3.session import Session
import yaml
import pandas as pd
import datetime
from sqlalchemy import create_engine
from io import StringIO


def env_loading():
    with open(file="env.yaml", mode="rt") as f:
        env_config = yaml.safe_load(f.read())
    return env_config


def create_db_engine():
    env_config = env_loading()
    ai_forecast_mysql_config = env_config.get("ai_forecast_mysql")
    return create_engine(
        f'mysql+pymysql://{ai_forecast_mysql_config["user"]}:{ai_forecast_mysql_config["password"]}@{ai_forecast_mysql_config["host"]}'
        f':{ai_forecast_mysql_config["port"]}/{ai_forecast_mysql_config["database"]}')


def get_df_from_db(table_name):
    db_engine = create_db_engine()
    result_df = pd.read_sql_table(table_name, con=db_engine)
    db_engine.dispose()
    return result_df


def get_format_filename(source_system_name, table_name):
    filename = "{source_system_name}_{table_name}_{timestamp}.csv".format(
        source_system_name=source_system_name, table_name=table_name.replace("_", "-"),
        timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    )
    return filename


def upload_df_to_s3(bucket_name, df, file_name):
    env_config = env_loading()
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, header=None, index=False)

    session = Session(
        aws_access_key_id=env_config['aws_s3']['access_key'],
        aws_secret_access_key=env_config['aws_s3']['secret_access_key'],
        region_name='cn-north-1')
    s3_resource = session.resource("s3")
    s3_resource.Object(bucket_name, file_name).put(Body=csv_buffer.getvalue())


def upload_file_to_s3(bucket_name, file_name, local_file):
    env_config = env_loading()

    session = Session(
        aws_access_key_id=env_config['aws_s3']['access_key'],
        aws_secret_access_key=env_config['aws_s3']['secret_access_key'],
        region_name='cn-north-1')
    s3 = session.client("s3")
    s3.upload_file(Filename=local_file, Key=file_name, Bucket=bucket_name)


def download_file_from_s3(bucket_name, file_name, local_file):
    env_config = env_loading()

    session = Session(
        aws_access_key_id=env_config['aws_s3']['access_key'],
        aws_secret_access_key=env_config['aws_s3']['secret_access_key'],
        region_name='cn-north-1')
    s3 = session.client("s3")
    s3.download_file(Filename=local_file, Key=file_name, Bucket=bucket_name)


def upload_db_object_to_s3(bucket_name, source_system_name, s3_path, table_name):
    df = get_df_from_db(table_name)
    saved_filename = get_format_filename(source_system_name, table_name)
    print(f"Starting to upload data in table {table_name} to S3...")
    upload_df_to_s3(bucket_name, df, f"{s3_path}/{saved_filename}")
    print(f"Finish uploading data in table {table_name} to S3...")


if __name__ == "__main__":
    #upload_db_object_to_s3("ulsc-test-raw", "aidp", "aidp/fcst_sop", "fcst_sop_2020_07")
    #upload_db_object_to_s3("ulsc-test-raw", "aidp", "aidp/fcst_sop", "fcst_2020_wk31")
    upload_db_object_to_s3("ulsc-test-raw", "aidp", "aidp/plant", "plant_2020_WK31")