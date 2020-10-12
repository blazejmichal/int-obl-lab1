import csv


class Task2a:

    @staticmethod
    def execute():
        with open('miasta.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['Rok'], row['Gdansk'], row['Poznan'], row['Szczecin'])
