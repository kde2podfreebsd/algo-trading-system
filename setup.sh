#!/usr/bin/env bash
#encoding=utf8

function echo_block() {
    echo "----------------------------"
    echo $1
    echo "----------------------------"
}

function check_installed_pip() {
   ${PYTHON} -m pip > /dev/null
   if [ $? -ne 0 ]; then
        echo_block "Installing Pip for ${PYTHON}"
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        ${PYTHON} get-pip.py
        rm get-pip.py
   fi
}

function check_installed_python() {
    if [ -n "${VIRTUAL_ENV}" ]; then
        echo "Please deactivate your virtual environment before running setup.sh."
        echo "You can do this by running 'deactivate'."
        exit 2
    fi

    for v in 10 9 8
    do
        PYTHON="python3.${v}"
        which $PYTHON
        if [ $? -eq 0 ]; then
            echo "using ${PYTHON}"
            check_installed_pip
            return
        fi
    done

    echo "No usable python found. Please make sure to have python3.8 or newer installed."
    exit 1
}

function install_talib(){
  if [ -f /home/donqhomo/Desktop/Crypto-TA/ta-lib-0.4.0-src ]; then
        echo "ta-lib already installed, skipping"
        return
  fi

  cd build_helpers && ./install_ta-lib.sh

  if [ $? -ne 0 ]; then
      echo "Quitting. Please fix the above error before continuing."
      cd ..
      exit 1
  fi;

  cd ..
}
