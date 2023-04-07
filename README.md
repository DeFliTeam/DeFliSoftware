# DeFliSoftware 

The basic aim of the DeFli package is to forward data read from an ADS-B receiver to DeFli Network Servers and DeFli Blockchain

It does this using a program, DeFliSoftware, aided by some support programs.

    DeFliX - establishes an encrypted session to DeFli and forwards data
    DeFli-Config - used to configure DeFliSOftware like with a DeFli username and password
    DeFli-status - used to check the status of DeFliSoftware
    faup1090 - run by DeFliSoftware to connect to dump1090 or some other program producing beast-style ADS-B data and translate between its format and DeFliSoftware's
    fa-mlat-client - run by DeFliSoftware to gather data for multilateration


# Building From Source 

This repository provides the entire DeFli package including fa-mlat-client and faup1090. 

# DeFliSoftware Program 

The DeFliSoftware program establishes a compressed, encrypted TLS connection to DeFli and authenticates either by MAC address, or by a registered DeFli username (or email address) and password.

It then starts faup1090 to translate ADS-B data from a raw Beast-format feed on port 30005 to a filtered ADS-B format. The filtered data is uploaded to DeFli over the previously established TLS connection.

Every five minutes DeFliSoftware also sends a message containing basic health information about the local machine such as system clock, CPU temperature, CPU load, basic filesystem capacity and system uptime.

DeFliSoftware will start the multilateration client fa-mlat-adept on request. fa-mlat-client extracts raw messages from port 30005 and selectively forwards them by UDP to the DeFli servers. UDP is used as this message forwarding is time-sensitive, but it's not too important if some messages get dropped. Multilateration control messages are sent over the main DeFliSoftware TCP connection.

DeFliSoftware uses several techniques to keep the connection established and disconnect and reconnect if something goes wrong.

# Configuring Multilateration Results 

By default, multilateration positions resulting from the data that you feed to DeFli are returned to you by sending them to the local dump1090 process on port 30104; dump1090 will then include them on the web map it generates. 

# DeFli-Status-Program 

DeFli-status will examine your system and try to figure out what's going on. It will report on whether dump1090, faup1090 and DeFliSoftware are running or not and it will identify what program, if any, is producing data on port 30005 and whether or not DeFliSoftware is connected to DeFli. 

