from setuptools import setup, find_packages

setup(
    name='enhanced-wireless-auth',
    version='1.1.0',
    description='Adds additional wireless authentication and encryption options to NetBox.',
    author='Danny Messano',
    author_email='drmessano@gmail.com',
    min_version='4.2.0',
    max_version='4.2.99',
    packages=find_packages(),  # This automatically includes the enhanced_wireless_auth package
)

