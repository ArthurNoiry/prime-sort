# Prime sorting encryption

This project implements matrix encryption and decryption using prime numbers sorting and provides functionality to process `.png` images.
prime numbers sorting is a sorting method that puts first the number closest to a prime number
  in case of equality the smaller prime number will go first, if the numbers also share their closest prime number the smallest is first

## Features
- Matrix encryption and decryption based on prime sorting.
- Handle `.png` files for encryption and decryption.

## Requirements
- Python 3.7+
- Poetry
- Dependencies: `numpy`1.21.0 or more, `pillow` 8.3 or earlier

## Installation

1. **Clone the repository (if applicable)**:
   If you're working with a repository, first clone it:
   ```bash
   git clone https://your-repository-url.git
   cd prime-sort
   ```
   Create a virtual environment (optional but recommended): You can create a virtual environment using Poetry. If you don\'t have Poetry installed, run:
   ```bash
   pip install poetry
   ```

2. **Create a new environment and install dependencies**:
    ```bash
    poetry install
    ```
    This will automatically create a virtual environment for you.

3. **Activate the virtual environment**:
    ```bash
    poetry shell
    ```
    If you\'re not using Poetry, you can manually activate your environment (if using conda or venv).

4. **Install dependencies: If you are not using Poetry, you can install the dependencies manually with**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Use the package**:
    ```Python
    from prime_sort.utils import encrypt, decrypt, process_image
    process_image("test.png",encrypt)
    process_image("test_encrypt.png",decrypt)
    ```
