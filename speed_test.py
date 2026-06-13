import speedtest
from colorama import Fore

def speed_test():
    print("Initialising Speed Test (This may take a while)")
    st = speedtest.Speedtest()

    print(Fore.CYAN, "[+] Getting Best Server")
    st.get_best_server()

    print(Fore.CYAN, "[+] Testing Download Speed")
    download_speed = st.download()

    print(Fore.CYAN, "[+] Testing Upload Speed")
    upload_speed = st.upload()

    print(Fore.CYAN, "[+] Pinging")
    ping_result = st.results.ping

    download_mbps = download_speed / 1024 / 1024
    upload_mbps = upload_speed / 1024 / 1024

    print("\n=== SPEED TEST RESULTS ===")
    print(f"Download Speed: {download_mbps:.2f} Mbps")
    print(f"Upload Speed:   {upload_mbps:.2f} Mbps")
    print(f"Ping (Latency): {ping_result} ms")

if __name__ == "__main__":
    speed_test()


