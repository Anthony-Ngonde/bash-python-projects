#!/usr/bin/bash


echo "======================"
echo "SECURITY IOC ANALYZER"
echo "======================"

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$BASE_DIR/analyzer.py"


add_ioc() {

echo
read -p "Enter IOC: " ioc


if [[ -z "$ioc"  ]]
   then
     echo "Error. IOC cannot be empty"
     return

fi


python3 "$PYTHON_SCRIPT" add "$ioc"


}


add_ioc

