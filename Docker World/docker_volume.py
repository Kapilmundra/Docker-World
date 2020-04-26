import os
os.system("clear")
while True:
	os.system("tput setaf 1")
	print("\t\t\t Volume")
	os.system("tput setaf 7")
	print("\t\t\t ......")
	print("""
	Press 1: Excess Volumes
	Press 2: Create Volume
	Press 3: Remove Volume
	Press 4: Previos page
	""")
	print("Enter your choice: ",end="")
	ch=int(input())
	if ch==1:
		os.system("docker volume ls")
	elif ch==2:
		print("Enter the name of Volume: ",end="")
		volume_name=input()
		os.system("docker volume create {}".format(volume_name))
	elif ch==3:
		print("Enter the name of removable volume : ",end="")
		volume_name1=input()
		os.system("docker volume rm {}".format(volume_name1))
	elif ch==4:
		break
	else:
		print("Choose correct option....")
	input("Enter to continue...")
	os.system("clear")

