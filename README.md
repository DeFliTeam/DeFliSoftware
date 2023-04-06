# DeFliSoftware 

The basic aim of the DeFli package is to forward data read from an ADS-B receiver to DeFli Network Servers and DeFli Blockchain

It does this using a program, piaware, aided by some support programs.

    DeFliX - establishes an encrypted session to DeFli and forwards data
    DeFli-Config - used to configure DeFliSOftware like with a DeFli username and password
    DeFli-status - used to check the status of DeFliSoftware
    faup1090 - run by DeFliSoftware to connect to dump1090 or some other program producing beast-style ADS-B data and translate between its format and DeFliSoftware's
    fa-mlat-client - run by DeFliSoftware to gather data for multilateration
