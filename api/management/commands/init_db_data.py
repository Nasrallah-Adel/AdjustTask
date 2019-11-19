import csv

from django.core.management.base import BaseCommand

from api.models import Logs


class Command(BaseCommand):

    def handle(self, *args, **options):
        count = len(Logs.objects.all())
        if count == 0:
            with open('dataset.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count != 0:

                        Logs(
                            date=row[0],
                            channel=row[1],
                            country=row[2],
                            os=row[3],
                            impressions=int(row[4]),
                            clicks=int(row[5]),
                            installs=int(row[6]),
                            spend=float(row[7]),
                            revenue=float(row[8])
                        ).save()
                        line_count += 1
                    else:
                        line_count += 1
                print(f'Processed {line_count} lines.')
        else:
            print("Database Already have data")
