import speedtest, pyperclip

st = speedtest.Speedtest(secure=False) # secure=False to avoid SSL issues on some systems and return http instead of https

print("Finding best server...")
bestServer = st.get_best_server()
# print(bestServer)   # For debugging

print("Testing download speed...")

# To get download speed
download_speed = st.download() / 1_000_000  # To convert to Mbps

# To get upload speed
upload_speed = st.upload() / 1_000_000      # To convert to Mbps

# To get ping
ping = st.results.ping

print(f"Download Speed: {download_speed:.2f} Mbps") #.2f for 2 decimal places
print(f"Upload Speed: {upload_speed:.2f} Mbps") #.2f for 2 decimal places
print(f"Ping: {ping} ms")
print("Speed test completed.")



# Copy to clipboard option
copy = input("Copy results to clipboard? (y/n): ").lower()
while True:
    if copy == 'y':
        pyperclip.copy(f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps\nPing: {ping} ms")  
        print("Results copied to clipboard.")
        break
    elif copy == 'n':
        print("Results not copied to clipboard.")
        break   
    else:
        copy = input("Invalid input. Please enter 'y' or 'n': ").lower() 



input("Press any Key to Exit")