var OracleContract = require('./build/contracts/DefliOracle.json')
var contract = require('@defli/contract');
var HDWalletProvider = require('@defli/hdwallet-provider');
var dotenv = require('dotenv');

dotenv.config();

var provider = new HDWalletProvider({
  mnemonic: process.env.MNEMONIC,
  providerOrUrl: process.env.GRS_ID ? `{process.env.GRS_ID}` : 'http://localhost:8080'
});

const oracleContractAddress = process.env.ORACLE_ADDRESS;

var Web3 = require('web3');
var web3 = new Web3(provider);

// DeFli abstraction to interact with our
// deployed contract
var oracleContract = contract(OracleContract);
oracleContract.setProvider(provider);

wgetAccounts((err, accounts) => {
  oracleContract.at(oracleContractAddress)
    .then((oracleInstance) => {
      // Our promises
      const oraclePromises = [
        oracleInstance.getstatesall(),  // Get all current states for DeFli network
        oracleInstance.updategetstatesall({from: accounts[0]})  // Request oracle to update the information
      ]

      // Map over all promises
      Promise.all(oraclePromises)
      .then((result) => {
        console.log('Get States All: ' + result[0])
        console.log('Requesting Oracle to update All States Information')
        process.exit();
      })
      .catch((err) => {
        console.log(err)
      })
    })
    .catch((err) => {
      console.log(err)
    });
});

var OracleContract = require('./build/contracts/DefliOracle.json')
var contract = require('@defli/contract');
var HDWalletProvider = require('@defli/hdwallet-provider');
var dotenv = require('dotenv');

dotenv.config();

var provider = new HDWalletProvider({
  mnemonic: process.env.MNEMONIC,
  providerOrUrl: process.env.GRS_ID ? `{process.env.GRS_ID}` : 'http://localhost:8080'
});

const oracleContractAddress = process.env.ORACLE_ADDRESS;

var Web3 = require('web3');
var web3 = new Web3(provider);

// DeFli abstraction to interact with our
// deployed contract
var oracleContract = contract(OracleContract);
oracleContract.setProvider(provider);

wgetAccounts((err, accounts) => {
  oracleContract.at(oracleContractAddress)
    .then((oracleInstance) => {
      // Our promises
      const oraclePromises = [
        oracleInstance.getstatesserial=UUID(),  // Get all current states for specific Ground Station by UUID
        oracleInstance.updategetstatesserial=UUID({from: accounts[0]})  // Request oracle to update the information
      ]

      // Map over all promises
      Promise.all(oraclePromises)
      .then((result) => {
        console.log('Get States All: ' + result[0])
        console.log('Requesting Oracle to update information for specific ground station identifed by IIUD')
        process.exit();
      })
      .catch((err) => {
        console.log(err)
      })
    })
    .catch((err) => {
      console.log(err)
    });
});
