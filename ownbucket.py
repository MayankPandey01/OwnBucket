import concurrent.futures
import requests
import argparse
import time,sys
from config import *


parser = argparse.ArgumentParser(description="OwnBucket : Bucket Enumeration Tool") 
parser.add_argument("-t","--target", help="Target to search Buckets for",dest='target',required=True)
parser.add_argument('--gcp', dest='scan_gcp', action='store_true')
parser.add_argument('--all', dest='scan_all', action='store_true')
args= parser.parse_args()

scan_gcp=args.scan_gcp
scan_all=args.scan_all
if scan_gcp or scan_all:
    scan_aws=False
if scan_gcp and scan_all:
    banner()
    print(f"{RED} Too many Arguments Provided , Use Either --all or --gcp{RESET}")
    sys.exit()


target=args.target.lower().strip()
final.append(target)
tmp1 = [f"{target}-{i}" for i in bucket_prefix ]
tmp2 = [f"{target}-{i}" for i in env ]
tmp3 = [f"{target}{k}{i}{l}{j}" for i in bucket_prefix for j in env for k in pref for l in suff]
final=final+tmp1+tmp2+tmp3
final=set(final)

def check_aws(bucket):
    try:
        headers = {'User-Agent': f'{ua.random}'}
        resp=requests.get(f"http://{bucket}.s3.amazonaws.com",headers=headers)
        if resp.status_code==200:
            print(f"{GREEN}{bucket:15s} : {resp.status_code}{RESET}")
        if resp.status_code==403:
            print(f"{RED}{bucket:15s} : {resp.status_code}{RESET}")
        if resp.status_code not in [200,403,404]:
            print(f"{YELLOW}{bucket:15s} : {resp.status_code}{RESET}")

    except KeyboardInterrupt:
        sys.exit()

def check_gcp(bucket):
    try:
        headers = {'User-Agent': f'{ua.random}'}
        resp=requests.get(f"https://storage.googleapis.com/{bucket}",headers=headers)
        if resp.status_code==200:
            print(f"{GREEN}{bucket:15s} : {resp.status_code}{RESET}")
        if resp.status_code==403:
            print(f"{RED}{bucket:15s} : {resp.status_code}{RESET}")
        if resp.status_code not in [200,403,404]:
            print(f"{YELLOW}{bucket:15s} : {resp.status_code}{RESET}")
    except KeyboardInterrupt:
        sys.exit()

def main():
    start_time = time.time()
    banner()
    print(f"\n{CYAN}[*] Generated Wordlist of {len(final)} items{RESET}\n")
    if scan_gcp:
        print(f'[+] Checking GCP Buckets for "{target}"\n')
        with concurrent.futures.ThreadPoolExecutor(max_workers=no_of_workers) as executor:
            try:
                executor.map(check_gcp,final)
            except KeyboardInterrupt:
                sys.exit()
    if scan_aws:
        print(f'[+] Checking AWS S3 Buckets for "{target}"\n')
        with concurrent.futures.ThreadPoolExecutor(max_workers=no_of_workers) as executor:
            executor.map(check_aws,final)

    if scan_all:
        print(f'[+] Checking AWS S3 Buckets for "{target}"\n')
        with concurrent.futures.ThreadPoolExecutor(max_workers=no_of_workers) as executor:
            executor.map(check_aws,final)
        print(f'\n[+] Checking GCP Buckets for "{target}"\n')
        with concurrent.futures.ThreadPoolExecutor(max_workers=no_of_workers) as executor:
            try:
                executor.map(check_gcp,final)
            except KeyboardInterrupt:
                sys.exit()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{CYAN}\n[*] Time elapsed: {elapsed_time:.2f} seconds{RESET}\n")

if __name__=="__main__":
    main()