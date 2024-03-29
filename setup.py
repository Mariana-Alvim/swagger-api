# -*- encoding: utf-8 -*-
# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
import re

from setuptools import find_packages, setup

dev_requirements = [
    'flake8',
    'pytest',
]
unit_test_requirements = [
    'pytest',
    'pandas'
]
integration_test_requirements = [
    'pytest',
    'pandas'
]
run_requirements = [
    'flask==1.1.2',
    'itsdangerous==2.0.1',
    'Flask-Cors==3.0.7',
    'flask-restplus==0.13.0',
    'werkzeug==0.16.1',
    'loguru==0.4.1',
    'gunicorn==19.10.0',
    'requests==2.22.0',
    'loguru==0.4.1',
    'numpy==1.20.3',
    'prometheus_client==0.8.0',
    'jinja2==3.0.0',
    'pycep_correios==5.0.0',
    'geopy==2.1.0',
    'timezonefinder==6.0.1',
    'datetime==4.5.0'
]

with io.open('./service/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="service",
    version=version,
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    description="API Timezone arq 3.0",
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
         'dev': dev_requirements,
         'unit': unit_test_requirements,
         'integration': integration_test_requirements,
    },
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=(),
    entry_points={
        'console_scripts': [
            'service = service.__main__:app'
        ],
    },
)
