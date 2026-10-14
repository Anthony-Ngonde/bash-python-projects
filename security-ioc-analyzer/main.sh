#!/usr/bin/bash


echo "======================"
echo "SECURITY IOC ANALYZER"
echo "======================"

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$BASE_DIR/analyzer.py"


add_ioc() {

echo "=========="
echo "Add IOC"
echo "=========="


echo
read -p "Enter IOC: " ioc


if [[ -z "$ioc"  ]]
   then
     echo "Error. IOC cannot be empty"
     return

fi


python3 "$PYTHON_SCRIPT" add "$ioc"


}


#add_ioc


search_ioc() {

echo "=============="
echo "Search IOC"
echo "============="

echo
read -p "Enter IOC: " ioc


if [[ -z "$ioc"  ]]
   then
     echo "Error. IOC cannot be empty"
     return

fi


python3 "$PYTHON_SCRIPT" search "$ioc"


}

#search_ioc



classify_ioc() {

echo "============="
echo "Classify IOC"
echo "============="


echo
read -p "Enter IOC: " ioc

if [[ -z "$ioc"  ]]
   then
     echo "Error. IOC cannot be empty"
     return

fi


echo
echo -n "Classification: "

python3 "$PYTHON_SCRIPT" classify "$ioc"


}


list_iocs() {

python3 "$PYTHON_SCRIPT" list


}


count_iocs() {


python3 "$PYTHON_SCRIPT" count


}



while true
do


echo
echo "1.Add IOC"
echo "2.Search IOC"
echo "3.Classify IOC"
echo "4.List IOC"
echo "5.Count IOC"
echo "6.Exit"


echo
read -p "Enter your choice: " choice


case $choice in

1)
 add_ioc
 ;;

2)
 search_ioc
 ;;

3)
 classify_ioc
 ;;

4)
 list_iocs
 ;;

5)
 count_iocs
 ;;

6)
 echo
 echo "Exiting..."
 exit 0
 ;;

*)
 echo
 echo "Invalid choice"
 ;;

esac


echo
read -p "Press Enter to Continue..."



done
