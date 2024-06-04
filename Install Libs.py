import subprocess  as sp 
import os
import sys         


def display_failed_libs(failed_libs):
    """
    Displays the contents of the file containing all failed libraries.
    
    Args:
        failed_libs (list): List of python libraries that failed to install.
    """
    try:
        with open("Failed.txt", 'a+') as myFile:
            myFile.seek(0)  # Move the cursor to the start of the file
            content = myFile.read()
            print(content)  # Print the current contents of the file
            myFile.truncate(0)  # Clear the file contents
            for lib in failed_libs:
                myFile.write(f"{lib} installation failed\n")
    except FileNotFoundError:
        with open("Failed.txt", 'w') as myFile:
            myFile.write("Failed Libraries:\n")
        display_failed_libs(failed_libs)
    except PermissionError:
        print("Permission denied")
    except OSError:
        print("Unsupported operation")

def install_pip():
    """
    installs PIP and forces an upgrade
    """

    print("Forcing config and installation of pip...")
    try:
        sp.check_call([sys.executable, '-m', 'ensurepip'])
        sp.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        print("Pip successfully installed and configured.")
    except sp.CalledProcessError as e:
        print(f"An error occurred while installing pip: {e}")

def install_dependencies(libs):
    """
    Installs required dependencies for the provided libraries and logs any failures.
    
    Args:
        libs (dict): Dictionary of libraries grouped by category.
    """
    
    # List to keep track of all dependencies
    all_dependencies = set()
    failed_libs = []  # List to keep track of failed installations

    # Collect dependencies
    for category, libraries in libs.items():
        for lib in libraries:
            try:
                # Use pip show to get the dependencies of the package
                result = sp.check_output([sys.executable, '-m', 'pip', 'show', lib], universal_newlines=True)
                # Extract dependencies from the result
                for line in result.split('\n'):
                    if line.startswith('Requires:'):
                        dependencies = line.split(': ')[1].split(', ')
                        all_dependencies.update(dependencies)
            except sp.CalledProcessError:
                print(f"Failed to get dependencies for {lib}.")
                failed_libs.append(lib)  # Append the failed library to the list

    # Install each dependency
    for dep in all_dependencies:
        if dep:  
            try:
                sp.check_call([sys.executable, '-m', 'pip', 'install', dep])
                print(f"{dep} successfully installed.")
            except sp.CalledProcessError:
                print(f"Failed to install {dep}.")
                failed_libs.append(dep)  # Append the failed dependency to the list

    # Display and log the failed installations
    display_failed_libs(failed_libs)

    if not failed_libs:
        print("All dependencies installed successfully.")
    else:
        print("Some dependencies failed to install. Check Failed.txt for details.")



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
    print("Installing requested packages...")
    failed_libs = []
    for category, libraries in libs.items():
        for lib in libraries: 
            try:
                sp.check_call([sys.executable, "-m", "pip", "install", "--upgrade", lib])
                print(f"Successfully installed {lib}.")
            except sp.CalledProcessError as e:
                failed_libs.append(lib)
            if lib == 'pytorch' or lib == 'pytezos':
                sp.check_call([sys.executable,'pip3', 'install','torch', 'torchvision', 'torchaudio', '--index-url', 'https://download.pytorch.org/whl/cu118'])
                sp.check_call([sys.executable,'pip', 'install', 'torch==1.8.1+cu102', 'torchvision==0.9.1+cu102', 'torchaudio===0.8.1', '-f', 'https://download.pytorch.org/whl/torch_stable.html'])

        display_failed_libs(failed_libs)
    


#MAIN:


def main():
    # Clear screen and write welcome message:
    os.system('cls')  
    print("Welcome to the package installer!")
    

    # Installation begins
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