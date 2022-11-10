COPY world_data
FROM 's3://{bucket_name}/{file_name}'
credentials 'aws_access_key_id={access_key};aws_secret_access_key={secret_key}'
CSV;