fruits=( "apple" "bannana" "cherry")

for index in "${!fruits[@]}"; do
    echo "Item $index: ${fruits[$index]}"
done