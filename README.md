# Python Library Installer

This script is designed to automate the installation of Python libraries and their dependencies. It includes functions to handle failed installations, upgrade PIP, install dependencies, and install libraries across various categories.

## Features

- **Automated Installation**: Simplifies the process of installing multiple libraries.
- **Dependency Management**: Automatically identifies and installs required dependencies.
- **Error Logging**: Logs failed installations to a file for review.
- **Special Handling**: Includes specific installation procedures for libraries like PyTorch.

## Requirements

- Python 3.x
- PIP (latest version recommended)

## Usage

To use this script, simply run the `Install Libs.py` file with administrative priveleges

## Functions

- `display_failed_libs(failed_libs)`: Logs and displays libraries that failed to install.
- `install_pip()`: Installs and upgrades PIP.
- `install_dependencies(libs)`: Installs dependencies for the provided libraries.
- `install_libraries(libs, method='pip')`: Installs specified libraries using PIP or other methods.

## Logging

Failed installations are logged in the `Failed.txt` file, which is created in the same directory as the script.

## Contributing

Contributions to improve the script are welcome. Please ensure to test your changes before submitting a pull request.

## License

This script is released under the MIT License. See the LICENSE file for more details.

## Disclaimer

This script is provided "as is", without warranty of any kind. Use at your own risk.

## Contact

For any queries or issues, please open an issue on the repository's issue tracker.

