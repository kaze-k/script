#! /bin/bash


LANG=zh_CN.UTF-8

# 检测更新的函数
updt(){
    echo -n -e "\n是否执行命令：sudo apt update ？[Y/N]:"
    read sec
    case $sec in
        Y | y)
            sudo apt update;;
        N | n)
            exit 1;;
        *)
            echo "输入无效！" &&updt;;
    esac

    echo -n -e "\n是否执行命令：apt list --upgradable ？[Y/N]:"
    read sec
    case $sec in
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
    read sec
    case $sec in
        Y | y)
            sudo apt upgrade;;
        N | n)
            exit 1;;
        *)
            echo "输入无效！" && upgrp;;
    esac
}


# 主程序
main()
{
    # 获取时间
    hours=$(date +%H)
    week=$(date +%w)
    if [[ $hours == 21 && $week == 5 ]];then
        while true
        do
            echo -e "*系统更新检测" &&
            updt &&
            upgrp &&
            exit 0
        done
    else
        exit 0
    fi
}

# 运行
main
