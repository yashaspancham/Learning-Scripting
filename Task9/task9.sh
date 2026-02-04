USER_NAME=$USER_NAME

if [ -z "$USER_NAME" ]; then
    USER_NAME="Guest"
fi

echo "Hello, $USER_NAME"