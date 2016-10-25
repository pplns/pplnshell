#/bin/sh
#---------------------------------------------------------------------------------------------------
#FileName        tomcatkiller.sh
#Version         1.0
#Date            2016/10/25
#Author          Neal Zhang
#Email           Loong@pplns.com
#Website         www.pplns.com
#Description     Shell used to check whether the tomcat process is started,then kill the process.
#Copyright (c) 2015--2016 www.pplns.com All rights reserved.
#----------------------------------------------------------------------------------------------------
TomcatID=$(ps -ef |grep tomcat |grep java | awk ' { print $2 } ')
echo "tomcat的pid为$TomcatID"
Monitor(){  
        echo "[info]开始监控tomcat...[$(date +'%F %H:%M:%S')]"  
        if [[ $TomcatID ]] 
           then  
                echo "tomca启动正常"
        echo "kill -9" $TomcatID  
                kill -9 $TomcatID  
                tempTomcatID=$(ps -ef |grep tomcat |grep java | awk ' { print $2 } ')  
                if [[ $tempTomcatID ]]  
                        then  
                        echo "停止失败"  
                else   
                        echo "成功停止"  
                fi  
        else  
            echo "tomcat没有启动"  
        fi  
}
Monitor
