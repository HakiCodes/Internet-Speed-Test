import speedtest as st

#Set best server
server = st.Speedtest()
server.get_best_server()

#Test Download Speed
print("Testing......")
download = server.download()
download /= 1000000
print(f"Download Speed: {download} Mb/s")

#Test Upload Speed
upload = server.upload()
upload /= 1000000
print(f"Upload Speed: {upload} Mb/s")

#Test Ping
ping = server.results.ping
print(f"Ping: {ping}")
