touch data.txt
echo -e "apple\nbannana\ncherry\ndate\nelderberry" > data.txt
touch result.txt
cat data.txt | grep "bannana" > result.txt
