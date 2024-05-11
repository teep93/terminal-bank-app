#!bin/bash

install() {
    echo "Please wait for verification of virtual environment..."
    if [ -d ".venv" ]; then
        echo "Virtual environment already in directory."
    else
        echo "Installing virtual environment..."
        python3 -m pip install --user virtualenv
        python3 -m venv ".venv"
        echo "Virtual environment installed and created"
    fi

    echo "Activating virtual environment..."
    source ".venv/bin/activate"
    echo "Virtual environment activated."

    launch

}

launch(){
    echo "Activating virtual environment..."
    source ".venv/bin/activate"
    echo "Virtual environment activated."
    echo "Launching program..."
    python3 main.py
}

if [ "$1" = "--install" ]; then
    install
    return 0
fi

if [ "$1" = "--launch" ]; then
    launch
    return 0
fi
