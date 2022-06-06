#! /bin/bash

# shc -r -f update.sh 将该脚本变为c语言文件和c语言二进制文件

LANG=zh_CN.UTF-8

# 检测更新的函数
updt(){
    echo -n -e "\n是否执行命令：sudo apt update ？[Y/N]:"
    read input
    case $input in
        Y | y)
            sudo apt update;;
        N | n)
            exit 1;;
        *)
            echo "输入无效！" &&updt;;
    esac

    echo -n -e "\n是否执行命令：apt list --upgradable ？[Y/N]:"
    read input
    case $input in
        Y | y)
            apt list --upgradable;;
        N | n)
            exit 0;;
        *)
            echo "输入无效！" && updt;;
    esac
}

# 执行更新的函数
upgrp(){
    echo -n -e "\n是否进行更新？[Y/N]:"
    read input
    case $input in
        Y | y)
            sudo apt upgrade;;
        N | n)
            exit 1;;
        *)
            echo "输入无效！" && upgrp;;
    esac
}

# 清除缓存的函数
clr() {
    echo -n -e "\n是否清除缓存？[Y/N]:"
    read input
    case $input in
        Y | y)
            sudo apt clean
            sudo apt autoclean;;
        N | n)
            exit 1;;
        *)
            echo "输入无效！" && clr;;
    esac
}

# 执行系统更新检查的函数
enterUpdate() {
    while true
    do
        echo -e "*系统更新检测"
        updt
        upgrp
        clr
        exit 0
    done
}

# 主程序
main()
{
    # 获取时间
    hours=$(date +%H)
    day=$(date +%w)
    if [[ $hours == 21 && $day == 5 ]];then
        enterUpdate
    elif [[ $* == "now" ]];then
        enterUpdate
    else
        exit 0
    fi
}

# 运行
main $*
