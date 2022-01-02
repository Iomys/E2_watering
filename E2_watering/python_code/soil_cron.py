"""
Ce script a été utilisé pour récupérer les mesures par le biais d'un cronjob
"""

from datetime import datetime
import csv
from classes import Measures
mes = Measures()
print("Init")
def save_to_csv(filepath, state=None):
    with open(filepath, 'a', newline='') as csvfile:

        output = [datetime.now().isoformat(), mes.soil_hum_cap0(), mes.soil_hum_cap1(), mes.soil_hum_cap2(), mes.ds18b20.get_temperature(), mes.aht10_temp(), mes.aht10_hum(), mes.humidity_to_percent(mes.soil_hum_cap2()), state]
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(output)
        print(output)

save_to_csv("/home/pi/E2_watering/report/report_cron.csv")
