EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "E2_watering - Schématique de l'installation"
Date "2021-05-16"
Rev "1"
Comp "HES-SO Valais/Wallis"
Comment1 "FRUND Tchavo / SANDOZ Valentin"
Comment2 "Informatique 1"
Comment3 "Projet Raspberry PI"
Comment4 ""
$EndDescr
$Comp
L Sensor_Temperature:DS18B20 U1
U 1 1 60A1B3EF
P 7650 1450
F 0 "U1" H 8000 1600 50  0000 R CNN
F 1 "DS18B20" H 8250 1700 50  0000 R CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 6650 1200 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf" H 7500 1700 50  0001 C CNN
	1    7650 1450
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push_LED SW1
U 1 1 60A25088
P 2050 5350
F 0 "SW1" H 2050 5700 50  0001 C CNN
F 1 "Bouton 1" H 2050 5600 50  0000 C CNN
F 2 "" H 2050 5650 50  0001 C CNN
F 3 "~" H 2050 5650 50  0001 C CNN
	1    2050 5350
	-1   0    0    -1  
$EndComp
$Comp
L Sensor_perso:CapacitiveSoilMoistureSensor U3
U 1 1 60A1694C
P 7650 2950
F 0 "U3" H 7950 3050 50  0000 C CNN
F 1 "CapacitiveSoilMoistureSensor" H 8450 3150 50  0000 C CNN
F 2 "" H 7950 3200 50  0001 C CNN
F 3 "" H 7950 3200 50  0001 C CNN
	1    7650 2950
	1    0    0    -1  
$EndComp
$Comp
L Sensor_perso:SoilMoistureSensor U4
U 1 1 60A4B1C6
P 7650 3550
F 0 "U4" H 7878 3596 50  0000 L CNN
F 1 "SoilMoistureSensor" H 7900 3700 50  0000 L CNN
F 2 "" H 7650 3800 50  0001 C CNN
F 3 "" H 7650 3800 50  0001 C CNN
	1    7650 3550
	1    0    0    -1  
$EndComp
$Comp
L Sensor_perso:GrovePi+ U7
U 1 1 60A5B0A8
P 2050 3200
F 0 "U7" H 2075 4265 50  0000 C CNN
F 1 "GrovePi+" H 2075 4174 50  0000 C CNN
F 2 "" H 2050 4150 50  0001 C CNN
F 3 "" H 2050 4150 50  0001 C CNN
	1    2050 3200
	1    0    0    -1  
$EndComp
$Comp
L Sensor_perso:AHT10 U6
U 1 1 60A5BC52
P 3300 4700
F 0 "U6" H 3528 4751 50  0000 L CNN
F 1 "AHT10" H 3528 4660 50  0000 L CNN
F 2 "" H 3450 4950 50  0001 C CNN
F 3 "" H 3400 4850 50  0001 C CNN
	1    3300 4700
	1    0    0    -1  
$EndComp
$Comp
L Sensor_perso:SolenoidValve U5
U 1 1 60A5E512
P 7650 4950
F 0 "U5" H 8028 4846 50  0000 L CNN
F 1 "SolenoidValve" H 8028 4755 50  0000 L CNN
F 2 "" H 7650 4950 50  0001 C CNN
F 3 "" H 7650 4950 50  0001 C CNN
	1    7650 4950
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR0101
U 1 1 60A5F1E2
P 5950 4600
F 0 "#PWR0101" H 5950 4450 50  0001 C CNN
F 1 "+12V" H 5965 4773 50  0000 C CNN
F 2 "" H 5950 4600 50  0001 C CNN
F 3 "" H 5950 4600 50  0001 C CNN
	1    5950 4600
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 60A62D12
P 6200 4450
F 0 "#PWR0102" H 6200 4200 50  0001 C CNN
F 1 "GND" H 6205 4277 50  0000 C CNN
F 2 "" H 6200 4450 50  0001 C CNN
F 3 "" H 6200 4450 50  0001 C CNN
	1    6200 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	6050 5400 6050 5700
Wire Wire Line
	6050 5700 7750 5700
Wire Wire Line
	7750 5700 7750 5300
Wire Wire Line
	7750 4450 7750 4900
Wire Wire Line
	7750 4450 6200 4450
Wire Wire Line
	5950 4600 5950 4800
Wire Notes Line
	5750 4350 8650 4350
Wire Notes Line
	8650 4350 8650 5850
Wire Notes Line
	8650 5850 5750 5850
Wire Notes Line
	5750 5850 5750 4350
Text Notes 6700 4300 0    50   ~ 0
12V Circuit
$Comp
L Switch:SW_Push_LED SW2
U 1 1 60A838A2
P 1650 5350
F 0 "SW2" H 1650 5100 50  0001 C CNN
F 1 "Bouton 2" H 1650 5200 50  0000 C CNN
F 2 "" H 1650 5650 50  0001 C CNN
F 3 "~" H 1650 5650 50  0001 C CNN
	1    1650 5350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 3750 2600 3750
Wire Wire Line
	1850 4400 1850 4800
Wire Wire Line
	1850 4400 2600 4400
Connection ~ 1850 5250
Wire Wire Line
	1850 5250 1850 5350
Wire Wire Line
	1850 4800 1900 4800
Connection ~ 1850 4800
Wire Wire Line
	1850 4800 1850 5250
Wire Wire Line
	2600 3750 2600 4400
Wire Wire Line
	2800 4850 3000 4850
Wire Wire Line
	2500 3500 2800 3500
Wire Wire Line
	2900 4750 3000 4750
Wire Wire Line
	2900 3400 2900 4750
Wire Wire Line
	2500 3400 2900 3400
Connection ~ 2600 3750
Wire Wire Line
	2500 3850 2700 3850
Wire Wire Line
	2700 3850 2700 4650
Wire Wire Line
	2700 4650 3000 4650
Wire Wire Line
	2600 4400 2600 4550
Wire Wire Line
	2600 4550 3000 4550
Connection ~ 2600 4400
Wire Wire Line
	2500 2400 2950 2400
Entry Wire Line
	2950 2400 3050 2300
Wire Wire Line
	2500 2500 2950 2500
Wire Wire Line
	2500 2600 2950 2600
Entry Wire Line
	3050 2500 2950 2600
Entry Wire Line
	3050 2100 2950 2000
Entry Wire Line
	3050 2400 2950 2500
Entry Wire Line
	6700 2100 6800 2000
Wire Wire Line
	2700 5400 5550 5400
Connection ~ 2700 4650
Wire Wire Line
	5550 4800 5550 3200
Wire Wire Line
	5550 3200 2500 3200
Wire Wire Line
	2200 4800 2700 4800
Wire Wire Line
	2700 4650 2700 4800
Connection ~ 2700 4800
Wire Wire Line
	2700 4800 2700 5400
Wire Wire Line
	2800 3500 2800 4850
Wire Wire Line
	2600 3750 2600 2700
Wire Wire Line
	2600 2700 2950 2700
Wire Wire Line
	2700 3850 2700 2800
Wire Wire Line
	2700 2800 2950 2800
Connection ~ 2700 3850
Entry Wire Line
	2950 2800 3050 2700
Entry Wire Line
	2950 2700 3050 2600
$Comp
L Device:LED_ALT D1
U 1 1 60AD2342
P 2050 4800
F 0 "D1" H 2043 4545 50  0001 C CNN
F 1 "LED 1" H 2050 4650 50  0000 C CNN
F 2 "" H 2050 4800 50  0001 C CNN
F 3 "~" H 2050 4800 50  0001 C CNN
	1    2050 4800
	-1   0    0    1   
$EndComp
$Comp
L Device:LED_ALT D2
U 1 1 60AD294A
P 1700 4800
F 0 "D2" H 1693 5017 50  0001 C CNN
F 1 "LED 2" H 1700 4950 50  0000 C CNN
F 2 "" H 1700 4800 50  0001 C CNN
F 3 "~" H 1700 4800 50  0001 C CNN
	1    1700 4800
	1    0    0    -1  
$EndComp
Connection ~ 1850 5350
Text Label 4250 5400 0    50   ~ 0
GND
Text Label 2200 4400 0    50   ~ 0
5V
Entry Wire Line
	6700 2250 6800 2350
Entry Wire Line
	6700 2350 6800 2450
Entry Wire Line
	6700 2450 6800 2550
Entry Wire Line
	6700 2550 6600 2650
Wire Wire Line
	6800 2000 6800 1850
Wire Wire Line
	6800 1850 7950 1850
Wire Wire Line
	7950 1850 7950 1450
Wire Wire Line
	6800 2450 7150 2450
Wire Wire Line
	7150 2450 7150 3050
Wire Wire Line
	7150 3050 7350 3050
Wire Wire Line
	7350 3400 7050 3400
Wire Wire Line
	7050 3400 7050 2550
Wire Wire Line
	7050 2550 6800 2550
Wire Wire Line
	6600 3600 7350 3600
Wire Wire Line
	6600 2950 6600 3600
Wire Wire Line
	7350 2250 7350 2350
Wire Wire Line
	7350 2350 6800 2350
Wire Wire Line
	7350 2050 7250 2050
Wire Wire Line
	7250 2050 7250 2850
Wire Wire Line
	7250 3700 7350 3700
Wire Wire Line
	7350 2850 7250 2850
Connection ~ 7250 2850
Wire Wire Line
	7250 2850 7250 3500
Wire Wire Line
	7650 1750 7250 1750
Wire Wire Line
	7250 1750 7250 2050
Connection ~ 7250 2050
Text Label 6600 2550 1    50   ~ 0
5V
Text Label 7050 3400 1    50   ~ 0
A0
Text Label 7150 3050 1    50   ~ 0
A1
Text Label 7350 2350 1    50   ~ 0
A2
Text Label 6800 1850 0    50   ~ 0
D4-RPI
Entry Wire Line
	6700 2550 6800 2650
Wire Wire Line
	6800 2650 6800 3500
Wire Wire Line
	6800 3500 7250 3500
Connection ~ 7250 3500
Wire Wire Line
	7250 3500 7250 3700
Text Label 6800 2750 3    50   ~ 0
GND
$Comp
L Relay:FINDER-32.21-x000 K1
U 1 1 60A55C5B
P 5750 5100
F 0 "K1" H 6180 5146 50  0000 L CNN
F 1 "Relais" H 6180 5055 50  0000 L CNN
F 2 "Relay_THT:Relay_SPST_Finder_32.21-x300" H 7020 5070 50  0001 C CNN
F 3 "https://gfinder.findernet.com/assets/Series/355/S32EN.pdf" H 5750 5100 50  0001 C CNN
	1    5750 5100
	1    0    0    1   
$EndComp
Wire Wire Line
	1550 4800 1550 3200
Wire Wire Line
	1550 3200 1650 3200
Wire Wire Line
	1450 5250 1450 3100
Wire Wire Line
	1450 3100 1650 3100
Wire Wire Line
	1450 5350 1350 5350
Wire Wire Line
	1350 5350 1350 3000
Wire Wire Line
	1350 3000 1650 3000
Wire Wire Line
	1650 3300 1150 3300
Wire Wire Line
	1150 3300 1150 5600
Wire Wire Line
	1150 5600 2350 5600
Wire Wire Line
	2250 5350 2350 5350
Wire Wire Line
	2350 5350 2350 5600
Wire Wire Line
	2250 5250 2450 5250
Wire Wire Line
	2450 5250 2450 5700
Wire Wire Line
	2450 5700 1050 5700
Wire Wire Line
	1050 5700 1050 3400
Wire Wire Line
	1050 3400 1650 3400
Text Label 2450 5250 2    50   ~ 0
D6
Text Label 1450 5250 1    50   ~ 0
D3
Text Label 1350 5350 1    50   ~ 0
D2
Text Label 2350 5350 2    50   ~ 0
D5
Text Label 1550 4800 1    50   ~ 0
D4
Wire Notes Line
	6500 3900 9100 3900
Wire Notes Line
	9100 3900 9100 1050
Wire Notes Line
	9100 1050 6500 1050
Text Notes 7500 1000 0    50   ~ 0
Circuit de mesure\n
Wire Notes Line
	3900 1750 3900 6050
Wire Notes Line
	3900 6050 900  6050
Wire Notes Line
	900  6050 900  1750
Wire Notes Line
	900  1750 3900 1750
Text Notes 1800 1700 0    50   ~ 0
Boîtier de contrôle
Wire Notes Line
	6500 1050 6500 3900
Connection ~ 6600 2950
Wire Wire Line
	7350 2950 6600 2950
Wire Wire Line
	6600 2150 7350 2150
Wire Bus Line
	3050 2100 6700 2100
Wire Wire Line
	6600 2150 6600 1300
Connection ~ 6600 2150
Wire Wire Line
	7250 1750 7250 1300
Connection ~ 7250 1750
$Comp
L Device:R R1
U 1 1 60BACDAC
P 6750 1300
F 0 "R1" V 6550 1300 50  0000 C CNN
F 1 "110" V 6634 1300 50  0000 C CNN
F 2 "" V 6680 1300 50  0001 C CNN
F 3 "~" H 6750 1300 50  0001 C CNN
	1    6750 1300
	0    1    1    0   
$EndComp
$Comp
L Sensor_perso:CapacitiveSoilMoistureSensor U2
U 1 1 60A15B21
P 7650 2150
F 0 "U2" H 7950 2200 50  0000 C CNN
F 1 "CapacitiveSoilMoistureSensor" H 8450 2300 50  0000 C CNN
F 2 "" H 7950 2400 50  0001 C CNN
F 3 "" H 7950 2400 50  0001 C CNN
	1    7650 2150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 60BAD7CA
P 7100 1300
F 0 "R2" V 6893 1300 50  0000 C CNN
F 1 "220" V 6984 1300 50  0000 C CNN
F 2 "" V 7030 1300 50  0001 C CNN
F 3 "~" H 7100 1300 50  0001 C CNN
	1    7100 1300
	0    1    1    0   
$EndComp
Wire Wire Line
	6950 1300 6900 1300
Wire Wire Line
	6900 1300 6900 1150
Wire Wire Line
	6900 1150 7650 1150
Connection ~ 6900 1300
Text GLabel 2400 2000 0    50   Input ~ 0
D4-Rpi
Wire Wire Line
	2950 2000 2400 2000
Wire Wire Line
	6600 2150 6600 2950
Wire Bus Line
	6700 2100 6700 2550
Wire Bus Line
	3050 2100 3050 2700
$EndSCHEMATC
