import requests, uuid, os
from concurrent.futures import ThreadPoolExecutor	


def main():
	os.system("clear")
	print(""" _____ _____ _____    _____ _____ __\n| __  |     |_   _|  |   | |   __|  |     bot nglink\n| __ -|  |  | | |    | | | |  |  |  |__   rozhbasxyz\n|_____|_____| |_|    |_|___|_____|_____|  free for public\n"""+"─"*32)
	apa = input("[1] brutal spam\n[2] slow spam\n[?] pilih : ")
	print("─"*10)
	if apa in ["1","01"]: brutal()
	elif apa in ["2","02"]: slow()
	else: exit("[!] buta kah matamu")
	
def slow():
	link = input("[?] link : ")
	chat = input("[?] chat : ")
	max = int(input("[?] jumlah : ")); print("─"*10)
	if "https" in str(link): link = link.split("/")[3]
	else: link = link.split("/")[1]
	for x in range(max):
		try:
			date = {"username": link, "question": chat, "deviceId": str(uuid.uuid4()), "gameSlug": "", "referrer": ""}
			post = requests.post("https://ngl.link/api/submit", data=date).json()
			if "questionId" in str(post):
				print("[!] status : sukses {}\n[!] target : {}\n[!] pesan  : {}\n[!] token  : {}".format(x, "ngl.link/"+link, chat, post["questionId"])); print("─"*10)
		except Exception as e: exit(e)
	
def brutal():
	link = input("[?] link : ")
	chat = input("[?] chat : "); print("─"*10)
	if "https" in str(link): link = link.split("/")[3]
	else: link = link.split("/")[1]
	with ThreadPoolExecutor (max_workers=10) as babas:
		while True: babas.submit(send, link, chat)
		
def send(link, chat):
	try:
		date = {"username": link, "question": chat, "deviceId": str(uuid.uuid4()), "gameSlug": "", "referrer": ""}
		post = requests.post("https://ngl.link/api/submit", data=date).json()
		if "questionId" in str(post): print("[!] status : sukses\n[!] target : {}\n[!] pesan  : {}\n[!] token  : {}".format("ngl.link/"+link, chat, post["questionId"])); print("─"*10)
	except Exception as e: exit()		

main()
#{"questionId":"ST1dsQVn2MBrj5ttoUTO"}
