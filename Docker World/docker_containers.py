import os
os.system("clear")
while True:
	os.system("tput setaf 1")
	print("\t\t\t Container")
	os.system("tput setaf 7")
	print("\t\t\t .........")
	print("""
	Press 1: Excess Containers
	Press 2: Create Container
	Press 3: Remove Container
	Press 4: Excess the terminal of Container
	Press 5: Previos page
	""")
	print("Enter your choice: ",end="")
	ch=int(input())
	if ch==1:
		os.system("docker ps -a")
	elif ch==2:
		print("Enter the name of Container: ",end="")
		container_name=input()
		print("Enter the name of (Image:version): ",end="")
		image_name=input()
		print("Enter the network name: ",end="")
		network_name=input()
		os.system("docker container run -it --name {} --network {} {}".format(container_name,network_name,image_name))
	elif ch==3:
		print("Enter the name of removable container : ",end="")
		container_name1=input()
		os.system("docker container rm {} -f".format(container_name1))
	elif ch==4:
		container_name1=input("Enter the name of Container: ")
		os.system("docker start {}".format(container_name1))
		os.system("docker attach {}".format(container_name1))
	elif ch==5:
		break
	else:
		print("Choose correct option....")
	input("Enter to continue...")
	os.system("clear")

