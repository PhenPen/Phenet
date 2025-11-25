import speedtest

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