import os
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("========================================")
    print("   FFMPEG STREAM GENERATOR (V4 - BASH FIX)")
    print("========================================")
    
    # 1. Inputs
    m3u8_link = input("\n[?] M3U8 Link paste karein: ").strip().replace('\n', '').replace('\r', '')
    referer = input("[?] Referer Link (e.g., https://bhalocast.com): ").strip().replace('\n', '').replace('\r', '')
    origin = input("[?] Origin Link (e.g., https://bhalocast.com): ").strip().replace('\n', '').replace('\r', '')
    
    if not m3u8_link:
        print("Error: Link khali nahi ho sakta!")
        return

    # Default Key
    stream_key = "11523921485458_10535073221266_x3wpukcvda"
    
    # 2. Data/Quality Selection
    print("\n----------------------------------------")
    print("DATA OPTIMIZATION (Slow Internet ke liye)")
    print("1. HAAN: Data chota karo (480p, Low Bitrate)")
    print("2. NAHI: Original Quality (High Data)")
    choice = input("Apna option chunein (1/2): ").strip()

    # --- CONSTRUCTION ZONE ---
    
    # User Agent
    ua_part1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    ua_part2 = "AppleWebKit/537.36 (KHTML, like Gecko) "
    ua_part3 = "Chrome/120.0.0.0 Safari/537.36"
    user_agent = ua_part1 + ua_part2 + ua_part3
    
    # Headers (Bash Syntax)
    headers = f"$'Origin: {origin}\\r\\nReferer: {referer}'"
    
    # Quality Settings
    if choice == '1':
        video_settings = "-c:v libx264 -preset ultrafast -b:v 600k -maxrate 800k -bufsize 1200k -vf \"scale=854:480\" -r 25"
        audio_settings = "-c:a aac -b:a 64k -ar 44100"
        print("\n[+] Mode: Low Data (Optimized)")
    else:
        video_settings = "-c copy"
        audio_settings = ""
        print("\n[+] Mode: Original Quality")

    # Command Construction
    parts = [
        "ffmpeg -re",
        f"-headers {headers}",
        f"-user_agent \"{user_agent}\"",
        f"-i \"{m3u8_link}\"",
        video_settings,
        audio_settings,
        f"-f flv \"rtmp://vsu.okcdn.ru/input/{stream_key}\""
    ]
    
    raw_command = " ".join(parts)
    final_command = raw_command.replace('\n', ' ').replace('\r', ' ').replace('  ', ' ')

    # 4. Result
    print("\n========================================")
    print("COMMAND READY!")
    print("========================================")
    print(final_command)
    print("========================================")
    
    run_now = input("\n[?] Kya main is command ko abhi RUN kar dun? (y/n): ")
    if run_now.lower() == 'y':
        print("\n[+] Starting Stream via BASH... (Ab chalega!)")
        # FIX: Force execution through /bin/bash to support special headers
        subprocess.run(final_command, shell=True, executable='/bin/bash')
    else:
        print("Okay.")

if __name__ == "__main__":
    main()