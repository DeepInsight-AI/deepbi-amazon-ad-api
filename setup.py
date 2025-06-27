"""
此文件基于python-amazon-ad-api项目（MIT许可证）
原始版权：Copyright (c) 2021 Michael Primke, Copyright (c) 2021 Daniel Álvaro
修改者：DeepInsight
"""

from setuptools import setup

setup(
    name='deepbi-amazon-ad-api',
    version='0.1.1',
    install_requires=[
        "requests>=2.27.1,<2.33.0",
        "six>=1.16,<1.18",
        "cachetools>=5.0,<6.2",
        "pycryptodome>=3.13,<3.24",
        "pytz>=2021.3,<2026.0",
        "confuse>=1.7,<2.1",
    ],
    packages=[
        'ad_api',
        'ad_api.api',
        'ad_api.auth',
        'ad_api.base',
        'ad_api.api.sp',
        'ad_api.api.sb',
        'ad_api.api.sd',
        'ad_api.api.dsp',
    ],
    url='https://github.com/DeepInsight/deepbi-amazon-ad-api',
    license='MIT',
    author='DeepInsight (基于Daniel Alvaro的工作)',
    author_email='dev@deepbi.com',
    description='Python wrapper for the Amazon Advertising API - DeepInsight定制版本',
)
