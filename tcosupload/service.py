# -*- coding=utf-8
"""This file is services for views.py"""
import configparser
import sys
import os
import re

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


def uploadFiles(file_path):
    """upload files to tencent cos
    :param file_path(string): path to the upload files 
    :return(string): url of uploaded file
    """
    # 加载配置信息
    config = configparser.ConfigParser()
    config.read(os.path.abspath(
        os.path.dirname(__file__)) + '\\qcloud_cos.ini')
    config_qcloud = config['qcloud']

    # 设置用户属性, 包括secret_id, secret_key, region
    secret_id = config_qcloud['secret_id']
    secret_key = config_qcloud['secret_key']
    REGION = 'ap-chongqing'  # 替换为用户的region
    TOKEN = None  # 使用临时密钥需要传入Token，默认为空,可不填

    config = CosConfig(Region=REGION, SecretId=secret_id,
                       SecretKey=secret_key, Token=TOKEN)  # 获取配置对象
    client = CosS3Client(config)

    bucket = config_qcloud['bucket_name']

    # get file name and file path

    # 遍历图片进行上传
    file_name = config_qcloud['upload_path'] + \
        re.split('[/\\\\]', file_path)[-1]
    response = client.upload_file(
        Bucket=bucket,
        LocalFilePath=file_path,
        Key=file_name,
        PartSize=10,
        MAXThread=10,
        EnableMD5=True
    )
    print(config_qcloud['url'] + file_name)
    return config_qcloud['url'] + file_name
