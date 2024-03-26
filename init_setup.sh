echo [$(date)]: "START"
echo [$(date)]: "Creating virtual env with python 3.8"
conda create --prefix ./cnnclassifier python=3.8 -y
echo [$(date)]: "Activating the environment"
source activate ./cnnclassifier
echo [$(date)]: "Installing the dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"