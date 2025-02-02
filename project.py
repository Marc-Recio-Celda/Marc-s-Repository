import sys
import csv

def main():
    hit = catch_error()
    print(compound_data(hit))

def catch_error():
    #debe comprobar que se ha introducido de manera correcta el compuesto y que se han introducido 2 argumentos command-line de manera correcta
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
    #debe recojer como argumento la posicion en la que se ha encontrado el compuesto de interés en hit.CSV y devolver su Catalog Number
    try:
        plate, position = compound.split(".")
        with open("Hit.csv", "r") as file:
            #especificar que las variables estan separadas por punto y coma
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                if row["CNB_plates"] == plate and row["position"] == position:
                    #when i print row this is the name of the Catalog_number key
                    return row["\ufeffCatalog_number"]

    except FileNotFoundError:
        sys.exit("Hit.csv not found")
    except ValueError:
        sys.exit("Bad format. Example of good format: python project.py 1.A2")

def compound_data(hit):
    #Debe devolver el ID, la estructura química y el peso molecular del compuesto de interés
    try:
        with open("Library.csv", "r") as file:
            #especificar que las variables estan separadas por punto y coma
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                if row["\ufeffIDNUMBER"].endswith(hit):
                    #when i print row this is the name of the Catalog_number key
                    return f"""
Hit info:
    ID Number: {row["\ufeffIDNUMBER"]}
    Formula Structure: {row["fmla_structure"]}
    Molecular Weight: {row["mol_weight_structure"]}"""

    except FileNotFoundError:
        sys.exit("Library.csv not found")


if __name__ == "__main__":
    main()

