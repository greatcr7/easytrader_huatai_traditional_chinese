import easytrader

## Huatai Parameters ##
ht_username = '666639271031'
ht_password = '970411'
ht_comm_password = '183010'
#######################


## JoinQuant Parameters ##
jq_username = '13601787682'
jq_password = 'Jeich970815'
jq_strategy_url = 'https://www.joinquant.com/algorithm/live/index?backtestId=f82682d71e9fa7ebae1c748f49a945a5'
target = 'jq'  # joinquant
##########################


user = easytrader.use('ht_client')

user.prepare(user='666639271031', password='970411', exe_path='D:\\htzqftb\\xiadan.exe', comm_password='183010')

follower = easytrader.follower(target)
follower.login(user=jq_username, password=jq_password)

follower.follow(user, jq_strategy_url, send_interval=5, buy_multiplier=1, sell_multiplier=1)

