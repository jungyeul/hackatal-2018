GOLD_FR = $1
PRED_FR = $2
GOLD_EN = $3
PRED_EN = $4

echo 'FRENCH'
python3 eval-hackathon2018.py GOLD_FR PRED_FR
echo 'ENGLISH'
python3 eval-hackathon2018.py GOLD_EN PRED_EN
