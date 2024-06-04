import subprocess  as sp 
import os
import sys         


def display_failed_libs(failed_libs):
    """
    Displays the contents of the file containing all failed libraries
    
    Args: libs (list): list of python libraries. Ex: [numpy, pytorch, pygame, ..., etc]
    
    
    Raises:
        Permission Error: if the program doesn't have permission to write to the file
        FileNotFound: if the file is not found -> create file
        OSError: if the operation is not supported 
    """
    try:
        with open("Failed.txt", 'a+') as myFile:
            for lib in failed_libs:
                myFile.write(f"{lib} installation failed\n")
    except FileNotFoundError:
        with open("Failed.txt", 'w') as myFile:
            pass
    except PermissionError:
        print("Permission denied")
    except OSError:
        print("Unsupported operation")

    os.system('cls')
    print(myFile.read())


def install_libraries(libs, method='pip'):
    """
    Install specified libraries using the specified method.

    Args:
        libs (dict): Key: Category, Value: List of library names to be installed. Ex: {Category of Module, [List of Modules]}

        method (str, optional): Method of installation. Default is 'pip'.
                                Other options may be added in the future.

                                
    Raises:
        ValueError: If an unsupported method is specified.
    """

    failed_libs = []
    for category, libraries in libs.items():
        for lib in libraries: 
            if method == 'pip':
                try:
                    sp.check_call([sys.executable, "-m", "pip", "install", "--upgrade", lib])
                    print(f"Successfully installed {lib}.")
                except sp.CalledProcessError as e:
                    failed_libs.append(lib)
            else:
                raise ValueError("Unsupported installation method")
    display_failed_libs(failed_libs)

#MAIN:


# Dictionary containing libraries grouped by category
libs = {
    'Prerequisites': [
        'wheel', 'setuptools', 'pip', 'cython'
    ],
    'Data Analysis and Manipulation': [
        'polars', 'numpy', 'pandas', 'datatable', 'modin'
    ],

    'Visualization': [
        'plotly', 'seaborn', 'matplotlib', 'pygal', 'altair', 'bokeh', 'folium'
    ],

    'Statistical Analysis and Machine Learning': [
        'scipy', 'pystan', 'pingouin', 'lifelines', 'pymc3', 'statsmodels',
        'pyflux', 'sktime', 'prophet', 'darts', 'tsfresh', 'kats', 'autots'
    ],

    'Big Data and Distributed Computing': [
        'dask', 'pyspark', 'ray', 'koalas', 'hadoop'
    ],

    'Messaging and Web Scraping': [
        'kafka-python', 'beautifulsoup4', 'octoparse', 'scrapy', 'selenium', 'mechanicalsoup'
    ],

    'Machine Learning Frameworks': [
        'scikit-learn', 'tensorflow', 'keras', 'xgboost', 'pytorch', 'jax'
    ],

    'Natural Language Processing': [
        'bert', 'textblob', 'polyglot', 'spaCy', 'nltk', 'gensim'
    ],

    'Game Development': [
        'pygame', 'arcade', 'pyglet', 'renpy', 'tcod' 
    ],

    'Web Development': [
        'flask', 'django', 'fastapi'
    ],

    'API Requests': [
        'requests', 'httpx'
    ],

    'Web Scraping': [
        'beautifulsoup4', 'scrapy', 'selenium', 'mechanicalsoup'
    ],

    'Encryption and Decryption': [
        'cryptography', 'pycryptodome'
    ],

    'Cybersecurity': [
        'owaspzap', 'scapy'
    ],

    'GUI Development': [
        'tkinter', 'pyqt5', 'pygtk'
    ],

    'Additional Libraries': [
        'paramiko', 'pyopenssl', 'pyarmor', 'pyinstaller'
    ],

    'Blockchain Development': [
        'web3', 'pytezos', 'fabric-sdk-py'
    ]
}

if __name__ == "__main__":
    install_libraries(libs)