#!/usr/bin/sh

# Here is an image mask that we will use to generate the grid
# completely transparent pixels will not be included as features
mask="/home/vanessa/Documents/Dropbox/Code/Python/imageSearch/img/empty.png"
dataset="img/"

# First index the dataset and generate the feature output file
python index.py --dataset $dataset --mask $mask --index index.csv --gridsize 60

# Now run a search with some image
python search.py --index index.csv --mask $mask --query "img/0755.png" --result-path $dataset --gridsize 60

# Similar image 0 is 0755.png, score: 5.01683098279e-12
# Similar image 1 is 0758.png, score: 0.753928549838
# Similar image 2 is 0735.png, score: 1.49185219648
# Similar image 3 is 0575.png, score: 1.57747888024
# Similar image 4 is 2531.png, score: 1.58183379819
# Similar image 5 is 2577.png, score: 1.65715516378
# Similar image 6 is 1102.png, score: 1.69818982149
# Similar image 7 is 0573.png, score: 1.82857227454
# Similar image 8 is 1100.png, score: 1.83202124991
# Similar image 9 is 0090.png, score: 1.86576392466
