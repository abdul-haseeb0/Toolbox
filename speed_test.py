import speedtest
from colorama import Fore, Style


def speed_test():
    print("Initialising Speed Test (This may take a while)")
    st = speedtest.Speedtest()

    print(Fore.GREEN, "[+] Getting Best Server", Style.RESET_ALL)
    st.get_best_server()

    print(Fore.MAGENTA, "[+] Testing Download Speed", Style.RESET_ALL)
    download_speed = st.download()

    print(Fore.MAGENTA, "[+] Testing Upload Speed", Style.RESET_ALL)
    upload_speed = st.upload()

    print(Fore.YELLOW, "[+] Pinging", Style.RESET_ALL)
    ping_result = st.results.ping

    download_mbps = download_speed / 1024 / 1024
    upload_mbps = upload_speed / 1024 / 1024

    print("\n=== SPEED TEST RESULTS ===")
    print(f"Download Speed: {download_mbps:.2f} Mbps")
    print(f"Upload Speed:   {upload_mbps:.2f} Mbps")
    print(f"Ping (Latency): {ping_result} ms")

if __name__ == "__main__":
    speed_test()


