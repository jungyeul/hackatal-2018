## for full .tsv files: 9-10 columns
Hackathon2Full.java

java Hackathon2Full  storyzy_en_test2_full.tsv  > storyzy_en_test2_full_corrected.tsv

## for test[1|2].tsv files: 3 columns
Hackathon2Test.java

java Hackathon2Test storyzy_en_test2.tsv > storyzy_en_test2_corrected.tsv


## how to make a "fasttext" input file; 
1/ remove head info;
j=`wc -l ./data-train/storyzy_en_train_corrected.tsv  | awk '{print $1}'`; k=`echo "$j - 1" | bc -l`; tail -n $k ./data-train/storyzy_en_train_corrected.tsv  > ./data-train/storyzy_en_train_corrected.tsv.ok;

j=`wc -l ./data-train/storyzy_en_train.text.tok  | awk '{print $1}'`; k=`echo "$j - 1" | bc -l`; tail -n $k ./data-train/storyzy_en_train.text.tok  > ./data-train/storyzy_en_train.text.tok.ok;


2/ extract labels and convert fasttext labels;
cut -f3 ./data-train/storyzy_en_train_corrected.tsv.ok | sed 's/^/__label__/g' > t;

3/ paste label and text;
wc -l t ./data-train/storyzy_en_train.text.tok.ok;
paste t ./data-train/storyzy_en_train.text.tok.ok > storyzy_en_train.text.tok.fasttext
rm -f t; 

4/ run fasttext;
see fasttext.cc 



