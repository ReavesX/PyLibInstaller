import subprocess  as sp 
import sys         
import platform    

# Dictionary containing libraries grouped by category
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
            try:                
                sp.check_call([sys.executable, "-m", "pip", "install", "--upgrade", lib])
                print(f"Successfully installed {lib}.")
            except sp.CalledProcessError as e:
                print(f'Error installing the {lib} library')
                failed_libs.append(lib)
    print(failed_libs)

#MAIN:
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