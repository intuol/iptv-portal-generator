import requests

# Script by intuol

# General info
portal = input("Input IPTV Portal URL here: \n")
username = input("Input Username: \n")
password = input("Input Password: \n")

# m3u_plus or m3u?
questionaire = input("m3u_plus or m3u: \n")

# Download commence!!!
def print_m3u_link():
    if questionaire == "m3u_plus":
        print(f'{portal}/get.php?username={username}&password={password}&type=m3u_plus&output=ts')
    elif questionaire == "m3u":
        print(f'{portal}/get.php?username={username}&password={password}&type=m3u&output=ts')
    else:
        print("it's either or. Idk what to tell you.")
        exit()
       

print_m3u_link()