#---------------------------------------------------------------------------------------------------
#FileName        shellcommand.py
#Version         1.0
#Date            2017/11/10
#Author          Neal Zhang
#Email           Loong@pplns.com
#Website         www.pplns.com
#Description     Python shell used to list btc unspent parts and do something for that;nohup python3 shellcommand.py 2>&1 >/dev/null &
#Copyright (c) 2015--2017 www.pplns.com All rights reserved.
#----------------------------------------------------------------------------------------------------
import os
import json
import time
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',filename='YOUR_LOG_FILE_NAME.log',filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-8s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
while 1==1:
    time.sleep(1)
    try:
        unspents_str=os.popen('/YOUR_BTC_INSTALL_PATH/bin/bitcoin-cli -datadir=/YOUR_BTC_DATA_PATH listunspent').read()
        unspents_list=json.loads(unspents_str)
        for unspent in unspents_list:
            now_account=unspent["account"]
            now_amount=unspent["amount"]
            now_confirmations=unspent["confirmations"]
            if "YOUR BTC WALLET ACCOUNT NAME"==now_account and now_amount>0.001 and now_confirmations>10:
                logging.info('account:%s***txid:%s***amount:%s***confirmations:%s '%(now_account,unspent['txid'],now_amount,now_confirmations))
                response= os.popen('curl http://YOUR IP:PORT/PATH?PARA1=1\&PARA2='+unspent['txid']).read()
                time.sleep(0.01)
            else:
                continue
        time.sleep(3*60*60)
    except:
        print("couldn't connect to server....")
