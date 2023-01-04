import colorama
from fake_useragent import UserAgent
from _version import __version__
colorama.init()
ua = UserAgent()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
CYAN = colorama.Fore.CYAN
YELLOW = colorama.Fore.YELLOW
DIM=colorama.Style.BRIGHT
DIM_RESET=colorama.Style.RESET_ALL
MAGENTA=colorama.Fore.MAGENTA
RESET2 = colorama.Back.RESET
no_of_workers=10
def banner():
    banner=rf'''{RED}  
   ___                 ____             _        _   
  / _ \__      ___ __ | __ ) _   _  ___| | _____| |_ 
 | | | \ \ /\ / / '_ \|  _ \| | | |/ __| |/ / _ \ __|
 | |_| |\ V  V /| | | | |_) | |_| | (__|   <  __/ |_ 
  \___/  \_/\_/ |_| |_|____/ \__,_|\___|_|\_\___|\__| v{__version__} 


   '''


    print(banner)
    print(f"{MAGENTA}\t OwnBucket : Bucket Enumeration Tool {RESET} [BY : @mayank_pandey01]{DIM_RESET}\n\n\n")

final=[]
scan_aws=True
env = ["dev", "development", "stage", "s3", "staging", "prod", "production", "test", "frontend", "backend"]
bucket_prefix=[]
suff =["-", "."]
pref =["-","."]
with open("bucket_prefixes.txt","r") as f:
    bucket_prefix = [line.strip() for line in f]
