# fbjsonrobot
A Python robot that transforms bundesliga text files from openfootball in JSON using the required structure.

Scripts with dependencies

Launch file is jsonrobot2.py

In Windows console python jsonrobot2.py and the JSON file is generated

Uses 1-bundesliga-i.txt as origin file but can be adapted to use the raw github Link https://raw.githubusercontent.com/openfootball/de-deutschland/master/2016-17/1-bundesliga-i.txt to it

The generated file is intented to be used in spanish

TODO:

* The generated JSON bundesliga.json is still imperfect, but workable. At the end it still generates an unnecesary ",
{
 "name": "14. Jornada",

"matches": [
{"

to be substituted with "] }"

to result in a validated json

* JSOn is still to be "pretty printed"

* A future version in german is intented, to be used with the original JSON and the link https://raw.githubusercontent.com/openfootball/de-deutschland/master/2016-17/1-bundesliga-i.txt
