# FDE-Technical-Screen

This project classifies packages as "STANDARD", "SPECIAL", or "REJECTED" based on their dimensions and mass.

## Requirements

- Python 3.10+
- [pytest](https://pytest.org/) for running tests
- [coverage](https://coverage.readthedocs.io/) (optional, for test coverage)

## Installation

Clone the repository and install dependencies:


git clone https://github.com/camposvi/FDE-Technical-Screen.git

cd FDE-Technical-Screen

pip install -r requirements.txt

## Usage
You can use the sort function from main.py to classify packages:

from main import sort

# Example usage:
result = sort(width, height, length, mass)

print(result)  # Output: "STANDARD", "SPECIAL", or "REJECTED"

Replace width, height, length, and mass with your package's values.

## Running Tests
To run the test suite:

python -m pytest

Project Structure
main.py: Contains the package classification logic.
tests/: Contains unit tests for the project.
requirements.txt: Lists Python dependencies.
README.md: Project documentation.
License
This project is for technical screening and educational purposes.

