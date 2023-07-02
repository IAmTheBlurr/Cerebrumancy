""" ./setup.py """
import setuptools

setuptools.setup(
    name='Cerebrumancy',
    version='0.0.1',
    author='Jonathan Craig',
    author_email='blurr@iamtheblurr.com',
    long_description_content_type='text/markdown',
    long_description=open('README.md', encoding='utf8').read(),
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Artificial Intelligence',
    ],
    python_requires='>=3.7',
    packages=setuptools.find_packages(),
    url='https://github.com/iamtheblurr/cerebrumancy',
    license='MIT',
    install_requires=[
        'openai',
        'pytest',
        'pytest-bdd',
        'requests',
    ],
)
