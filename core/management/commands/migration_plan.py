import os
import csv
import ast  # Import ast for safe evaluation
from django.core.management.base import BaseCommand
from django.conf import settings

'''
Rules of CSV

Actors come form credits

Actors can be linked to a movie by the credits id 

Movies do NOT contain actor info


Migration plan 
1: populate movie values from movie_csv
    - save the id from the csv as a field csv_id
    - actors and crew can not be populated yet

2: populate people (Person, Cast and Crew) from credits.csv
    - look at Person app models.py for definition info on each
    - Do not worry about linking users on the Person field, that can be done later

3: populate movies actor and crew fields
    - using credits.csv again, use the movie id to populate the movies actor and crew fields
'''

class Command(BaseCommand):
    help = "Runs a one-time script to import data from a CSV file"

    def handle(self, *args, **kwargs):
        print("Executing script1...")

        # Get the absolute path to the CSV file
        csv_path = os.path.join(settings.BASE_DIR, "csv", "credits.csv")

        if not os.path.exists(csv_path):
            print(f"Error: CSV file not found at {csv_path}")
            return

        # Open and read the CSV file
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)  # Use DictReader for named columns

            for row in reader:
                try:
                    # Convert the 'cast' string into a real Python list
                    row["cast"] = ast.literal_eval(row["cast"]) if row["cast"] else []

                    print("Parsed Cast:", row["cast"][0])  # Should print a list of dictionaries
                except (SyntaxError, ValueError) as e:
                    print(f"Error parsing row['cast']: {e}")

                break  # Stop after first row for debugging

        print("Script completed!")
