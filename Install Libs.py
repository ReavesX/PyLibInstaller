import subprocess as sp
import os
import sys

# Function to display and log failed library installations
def display_failed_libs(failed_libs):
    """
    Displays and logs the libraries that failed to install.
    
    Args:
        failed_libs (list): List of python libraries that failed to install.
    """
    try:
        # Open or create the file to log failed installations
        with open("Failed.txt", 'a+') as myFile:
            myFile.seek(0)  # Go to the beginning of the file to read content
            content = myFile.read()
            print(content)  # Display current failed installations
            myFile.truncate(0)  # Clear the file for new entries
            # Write new failed installations to the file
            for lib in failed_libs:
                myFile.write(f"{lib} installation failed\n")
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        with open("Failed.txt", 'w') as myFile:
            myFile.write("Failed Libraries:\n")
        display_failed_libs(failed_libs)
    except PermissionError:
        # Handle errors related to file permissions
        print("Permission denied")
    except OSError:
        # Handle other OS-related errors
        print("Unsupported operation")

# Function to install and upgrade PIP
def install_pip():
    """
    Installs and upgrades PIP, the Python package installer.
    """
    print("Forcing config and installation of pip...")
    try:
        # Ensure pip is installed
        sp.check_call([sys.executable, '-m', 'ensurepip'])
        # Upgrade pip to the latest version
        sp.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        print("Pip successfully installed and configured.")
    except sp.CalledProcessError as e:
        # Handle errors during pip installation
        print(f"An error occurred while installing pip: {e}")

# Function to install dependencies for the libraries
def install_dependencies(libs):
    """
    Installs dependencies for the provided libraries and logs any failures.
    
    Args:
        libs (dict): Dictionary of libraries grouped by category.
    """
    # Set to keep track of all unique dependencies
    all_dependencies = set()
    failed_libs = []  # List to track failed installations

    # Collect dependencies for each library
    for category, libraries in libs.items():
        for lib in libraries:
            try:
                # Get dependencies using pip show
                result = sp.check_output([sys.executable, '-m', 'pip', 'show', lib], universal_newlines=True)
                # Parse and add dependencies to the set
                for line in result.split('\n'):
                    if line.startswith('Requires:'):
                        dependencies = line.split(': ')[1].split(', ')
                        all_dependencies.update(dependencies)
            except sp.CalledProcessError:
                # Log failed attempts to get dependencies
                print(f"Failed to get dependencies for {lib}.")
                failed_libs.append(lib)

    # Install each collected dependency
    for dep in all_dependencies:
        if dep:  # Skip empty dependency names
            try:
                # Install the dependency using pip
                sp.check_call([sys.executable, '-m', 'pip', 'install', dep])
                print(f"{dep} successfully installed.")
            except sp.CalledProcessError:
                # Log failed installations
                print(f"Failed to install {dep}.")
                failed_libs.append(dep)

    # Log and display failed installations
    display_failed_libs(failed_libs)

    # Provide feedback on the installation process
    if not failed_libs:
        print("All dependencies installed successfully.")
    else:
        print("Some dependencies failed to install. Check Failed.txt for details.")

# Function to install libraries using pip
def install_libraries(libs, method='pip'):
    """
    Installs specified libraries using pip or other methods if specified.
    
    Args:
        libs (dict): Libraries to install, grouped by category.
        method (str, optional): Installation method (default is 'pip').
    """
    print("Installing requested packages...")
    failed_libs = []  # Track libraries that fail to install

    # Install each library using pip
    for category, libraries in libs.items():
        for lib in libraries:
            try:
                # Attempt to install the library
                sp.check_call([sys.executable, "-m", "pip", "install", "--upgrade", lib])
                print(f"Successfully installed {lib}.")
            except sp.CalledProcessError as e:
                # Log failed installations
                failed_libs.append(lib)
            # Special handling for pytorch and pytezos
            if lib == 'pytorch' or lib == 'pytezos':
                # Install pytorch with specific version and URL
                sp.check_call([sys.executable, 'pip3', 'install', 'torch', 'torchvision', 'torchaudio', '--index-url', 'https://download.pytorch.org/whl/cu118'])
                sp.check_call([sys.executable, 'pip', 'install', 'torch==1.8.1+cu102', 'torchvision==0.9.1+cu102', 'torchaudio===0.8.1', '-f', 'https://download.pytorch.org/whl/torch_stable.html'])

        # Log and display failed installations
        display_failed_libs(failed_libs)

# Main function to orchestrate the installation process
def main():
    # Clear the console screen
    os.system('cls')
    print("Welcome to the package installer!")

    # Begin the installation process
    install_pip()
    install_dependencies(libs)
    install_libraries(libs)



# Dictionary containing libraries grouped by category

libs = {
    'Data Analysis and Manipulation': [
        'polars', 'numpy', 'pandas', 'datatable', 'modin'
    ],

    'Visualization': [
        'plotly', 'seaborn', 'matplotlib', 'pygal', 'altair', 'bokeh', 'folium'
    ],

    'Statistical Analysis and Machine Learning': [
        'scipy', 'pystan', 'pingouin', 'lifelines', 'pymc3', 'statsmodels',
        'sktime', 'prophet', 'tsfresh', 'autots'
    ],

    'Big Data and Distributed Computing': [
        'dask', 'pyspark', 'koalas'
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
        'beautifulsoup4', 'Scrapy', 'selenium', 'mechanicalsoup'
    ],

    'Encryption and Decryption': [
        'cryptography', 'pycryptodome'
    ],

    'Cybersecurity': [
        'scapy'
    ],

    'GUI Development': [
        'pyqt5', 'pygtk'
    ],

    'Additional Libraries': [
        'paramiko', 'pyopenssl', 'pyarmor', 'pyinstaller'
    ],

    'Blockchain Development': [
        'web3', 'pytezos', 'fabric-sdk-py'
    ]
}


if __name__ == "__main__":
    main()