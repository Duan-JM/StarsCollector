import os

import semver
import setuptools


def versioning(version: str) -> str:
    """
    version to specification
    Author: Huan <zixia@zixia.net> (https://github.com/huan)

    X.Y.Z -> X.Y.devZ

    """
    sem_ver = semver.parse(version)

    major = sem_ver['major']
    minor = sem_ver['minor']
    patch = str(sem_ver['patch'])

    if minor % 2:
        patch = 'dev' + patch

    fin_ver = '%d.%d.%s' % (
        major,
        minor,
        patch,
    )

    return fin_ver


def get_version() -> str:
    """
    read version from VERSION file
    """
    version = '0.0.0'

    with open(
            os.path.join(
                os.path.dirname(__file__),
                'VERSION'
            )
    ) as version_fh:
        # Get X.Y.Z
        version = version_fh.read().strip()
        # versioning from X.Y.Z to X.Y.devZ
        version = versioning(version)

    return version


def get_long_description() -> str:
    """get long_description"""
    with open('README.md', 'r') as readme_fh:
        return readme_fh.read()


def get_install_requires() -> list:
    """get install_requires"""
    with open('requirements.txt', 'r') as requirements_fh:
        return requirements_fh.read().splitlines()


setuptools.setup(
    name='stars_collecter',
    license='MIT',
    version=get_version(),
    description='Github Stars Collector',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/Duan-JM/StarsCollector',
    author='Duan-JM (段嘉铭)',
    author_email='vincent.duan95@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: MIT',
        'Operating System :: OS Independent',
    ],
    packages=['stars_collecter'],
    install_requires=get_install_requires(),
    entry_points={
        'console_scripts': ['sc=stars_collecter:main'],
    },
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.4',
)
