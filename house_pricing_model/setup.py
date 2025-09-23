from setuptools import setup, find_packages

setup(
    name="house-pricing-model",
    version="0.1.0",
    description="Modelo de predição de preços de casas",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.21.0", 
        "scikit-learn>=1.1.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "xgboost>=1.6.0",
    ],
    python_requires=">=3.9",
)