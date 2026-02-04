
if [ -f .env ]; then
    source .env
    echo "$APP_ENV"
else
    echo ".env does not exist."
fi


