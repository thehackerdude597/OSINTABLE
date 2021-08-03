import colorama
from colorama import Fore, Back, Style
from pyfiglet import Figlet, figlet_format
import time

colorama.init()
figlet = Figlet(font='standard')
print(figlet.renderText("OSINTABLE"))

print(Fore.CYAN + 'v1.1')

print(Fore.LIGHTMAGENTA_EX + 'Tools: Reverse Name, Address, or Phone ex:type "reverse" to start. Find social media accounts ex:"username" to start')



user_prompt = input("Username or Reverse:")

#Username
if user_prompt == "username":
    print(Fore.BLUE + 'OK!')
    username = input("Username:")
    print(Fore.MAGENTA + "facebook.com/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "instagram.com/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "twitter.com/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "tumblr.com/blog/view" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "linkedin.com/in/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "reddit.com/user/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "youtube.com/user/channel/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "quora.com/profile/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "twitch.tv/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "tiktok.com/@" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "wattpad.com/user" + username)
    time.sleep(1)
    print(Fore.MAGENTA + username + ".medium.com")
    time.sleep(1)
    print(Fore.MAGENTA + "giphy.com/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "imgur.com/user/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "crunchyroll.com/groups" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "vimeo.com/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + "github.io/" + username)
    time.sleep(1)
    print(Fore.MAGENTA + username + '.blogger.com')
print(Fore.LIGHTGREEN_EX + 'If ANY Errors please add them so I can fix them')
if user_prompt == "reverse":
    print(Fore.LIGHTYELLOW_EX + 'Put a COMMA between the city and state! or else it will not work')
    name = input('Name:')
    city_state = input("City or state:")
    print(Fore.LIGHTYELLOW_EX + 'https://www.truepeoplesearch.com/results?name=' + name + '&citystatezip=' + city_state)
