# Chemical Compounds Filter

#### Video Demo: [FinalProjectCS50](https://youtu.be/XiaaNvEC2qE)

#### Description:

## Table of contents
- Introduction
- Required Files
- Running the Script Requirements
- Example Execution
- project.py
   - project.py Behavoir
   - Code project.py
- test_project.py
   - test_project.py Behavoir
   - Code test_project.py
- Source References

## Introduction
For my Master thesis, I did a screening of 1224 chemical compounds. From this screening I found some interesting compounds that raises the pollen germination in stress conditions and I called them "Hits", but I wasted many time searching this hits in the chemical library data. I have made a program that obtains the position of some interesting compounds from a chemical library, and tries to find their structure and molecular weight. There are some compounds (like 5.H11) that are in the screening but they are not well referenced in the library so its not possible to obtain their structure.

## Required Files
1. **Hit.csv**: Contains information about detected compounds, organized with the following columns:
    - `CNB_plates`: Plate where the compound is located.
    - `position`: Specific position on the plate.
    - `Catalog_number`: Catalog number associated with the compound.

2. **Library.csv**: Contains additional details about compounds, organized with the following columns:
    - `IDNUMBER`: Unique identifier for the compound.
    - `fmla_structure`: Chemical structure of the compound.
    - `mol_weight_structure`: Molecular weight of the compound.

## Running the Script Requirements
The script requires a command-line argument specifying the compound to search for. The correct format is `python project.py [compound]`, where `[compound]` must follow the format `Plate.Position` (e.g., `1.A2`).

## Example Execution:
```bash
python project.py 1.A2
```
## Project.py

### Program Behavior:
1. **Main Function:**
   - It validates the input arguments using `catch_error` and retrieves the compound data using `compound_data`.

2. **`catch_error()` Function:**
   - Validates the number and format of command-line arguments.
   - Ensures the input follows the `[Plate].[Position]` format.
   - Handles errors such as few arguments or too many arguments, printing an appropiate message using `sys.exit`.
   - Call `compound_identifier(compound)` function to identify the catalog number in `Hit.csv`.

3. **`compound_identifier(compound)` Function:**
   - Try to split the prompt into `plate` and `position` components. If can't do it exits the program using `sys.exit` with a message indicating the wrong format.
   - Searches for the compound in the `Hit.csv` file by matching the plate and position.
   - Returns the catalog number if found, or exits the program using `sys.exit` if the compound is not located or `Hit.csv` file is not found.

4. **`compound_data(hit)` Function:**
   - Uses the catalog number (`hit`) to search for compound details in the `Library.csv` file.
   - Retrieves the compound's ID number, formula structure, and molecular weight or exits the program using `sys.exit` if the `Library.csv` file is not found.
   - Formats the retrieved data into a readable output for the user.

5. **Output Example:**
   ```
   Hit info:
       ID Number: P7510350036
       Formula Structure: C20H27NO3
       Molecular Weight: 329,44309
   ```

### Code project.py
```python
import sys
import csv

def main():
    hit = catch_error()
    print(compound_data(hit))

def catch_error():
    if len(sys.argv) == 2:
        compound = sys.argv[1]
        if compound_identifier(compound):
            return compound_identifier(compound)
        else:
            sys.exit("Compound not found. Example of good format: python project.py 1.A2")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments. Example of good format: python project.py 1.A2")
    else:
        sys.exit("Too many command-line arguments. Example of good format: python project.py 1.A2")

def compound_identifier(compound):
    try:
        plate, position = compound.split(".")
        with open("Hit.csv", "r") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                if row["CNB_plates"] == plate and row["position"] == position:
                    return row["\ufeffCatalog_number"]
    except FileNotFoundError:
        sys.exit("Hit.csv not found")
    except ValueError:
        sys.exit("Bad format. Example of good format: python project.py 1.A2")

def compound_data(hit):
    try:
        with open("Library.csv", "r") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                if row["\ufeffIDNUMBER"].endswith(hit):
                    return f"""
Hit info:
    ID Number: {row["\ufeffIDNUMBER"]}
    Formula Structure: {row["fmla_structure"]}
    Molecular Weight: {row["mol_weight_structure"]}"""
    except FileNotFoundError:
        sys.exit("Library.csv not found")

if __name__ == "__main__":
    main()
```
## test_project.py

### test_project.py Behavoir
1. **`test_sys_argv`:**
   - Simulates different scenarios for `sys.argv` using `monkeypatch`.
   - Ensures `catch_error` behaves correctly with valid number of sys.argvs.

2. **`test_Not_in_hit`:**
   - Verifies that `compound_identifier` returns `None` when a compound is not found in `Hit.csv`.

3. **`test_Not_in_library`:**
   - Ensures `compound_identifier` handles cases where the compound is absent in `Library.csv`.

4. **`test_catch_error`:**
   - Confirms `catch_error` raises `SystemExit` for incorrect prompt formats.

5. **`test_compound_identifier`:**
   - Tests that `compound_identifier` correctly identifies catalog numbers for valid inputs.
   - Ensures it raises `SystemExit` for invalid formats like `4,A6` or `4:A6`.

6. **`test_compound_data`:**
   - Checks that `compound_data` retrieves and formats the correct compound details.

### Code test_project.py
```python
import pytest
import sys
from project import catch_error, compound_identifier, compound_data

def test_sys_argv(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["project.py", "4.A6"])
    assert catch_error() == "7210430612"
    monkeypatch.setattr(sys, "argv", ["project.py"])
    with pytest.raises(SystemExit):
        catch_error()
    monkeypatch.setattr(sys, "argv", ["project.py", "4", "A6"])
    with pytest.raises(SystemExit):
        catch_error()

def test_Not_in_hit():
    assert compound_identifier("5.H18") == None
    assert compound_identifier("25.H1") == None

def test_Not_in_library():
    assert compound_identifier("5.H11") == ""

def test_catch_error():
    with pytest.raises(SystemExit):
        compound_identifier("4")
    with pytest.raises(SystemExit):
        compound_identifier("A6")
    with pytest.raises(SystemExit):
        compound_identifier("cat")
    with pytest.raises(SystemExit):
        compound_identifier("4 A6")

def test_compound_identifier():
    assert compound_identifier("4.A6") == "7210430612"
    assert compound_identifier("6.B5") == "7510350036"
    with pytest.raises(SystemExit):
        compound_identifier("4,A6")
    with pytest.raises(SystemExit):
        compound_identifier("4:A6")
def test_compound_data():
    assert compound_data("7210430612") == """
Hit info:
    ID Number: P7210430612
    Formula Structure: C13H12O5
    Molecular Weight: 248,23759"""

    assert compound_data("7510350036") == """
Hit info:
    ID Number: P7510350036
    Formula Structure: C20H27NO3
    Molecular Weight: 329,44309"""
```


## Source References: Reddit for monkeypatch: https://www.reddit.com/r/cs50/comments/18i6af7/pytest_with_sysargv/?rdt=55883
