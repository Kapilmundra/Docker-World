import os
os.system("clear")
while True:
	os.system("tput setaf 1")
	print("\t\t\t Images")
	os.system("tput setaf 7")
	print("\t\t\t ......")
	print("""
	Press 1: Excess Images
	Press 2: Download Image
	Press 3: Remove Image
	Press 4: Previos page
	""")
	print("Enter your choice: ",end="")
	ch=int(input())
	if ch==1:
		os.system("docker images")
	elif ch==2:
		print("Enter the name of Image and version(Image:version): ",end="")
		image_name=input()
		os.system("docker image pull {}".format(image_name))
	elif ch==3:
		print("Enter the name of removable (Image:version): ",end="")
		image_name1=input()
		os.system("docker image rm {}".format(image_name1))
	elif ch==4:
		break
	else:
		print("Choose correct option....")
	input("Enter to continue...")
	os.system("clear")

