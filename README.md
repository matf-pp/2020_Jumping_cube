# jumping_cube
virtualenv venv --python=python3.7
. venv/bin/activate
echo "$(pwd)" | sudo tee venv/lib/python3.7/site-packages/jumpingcube_app.pth > /dev/null

python jumpingcube_app/game.py

press w to jump and avoid obstacles