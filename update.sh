#! /bin/bash


check_update(){
    if [[ $(checkupdates | wc -l) > 0 ]];then
        DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus dunstify "可更新: $(checkupdates | wc -l)";
        exit 0
    else
        exit 0
    fi
}

check_update
