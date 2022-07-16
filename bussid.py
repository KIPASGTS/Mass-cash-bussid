#NOTE: JUST FOR FUN XD

import requests, json, time, threading
headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '157','Host': '4ae9.playfabapi.com'}

def create_mission():
	try:
		data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["MLG","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
		response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
		js = json.loads(response)
		csession = js['data']['FunctionResult']['careerSession']
		return csession
	except Exception as e:
		pass
	

def skip_mission(token, rec):
		try:
			data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":rec,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
			response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
				
			js = json.loads(response)
			logs = js['data']['Logs']
			cash = logs[len(logs)-1]['Message'].split()[5]
			print(f'Total Balanced -> {cash}')
		except Exception as e:
			pass
			
def pass_mission():
	try:
		csession = create_mission()
		token = csession['token']
		kota = ["MLG","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR"]
		rec = []
		for i in range(0, len(kota)):
			passenger = csession['passenger'][i]
			source = passenger['source']
			dest = passenger['destination']
			max_passenger = passenger['amount']
			rec.append({"Key":{"sourceCity":source,"destinationCity":dest,"routePassed":[dest,source],"activityRewards":None},"Value":int(max_passenger)})
		skip_mission(token, rec)
	except Exception as e:
		pass

auth = input('Auth token: ')
headers['X-Authorization'] = auth	
while True:
	pass_mission()
	time.sleep(4)