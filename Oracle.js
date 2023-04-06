var fetch = require('fetch')
var OracleContract = require('./build/contracts/DeFliCOracle.json')
var contract = require('@defli/contract');
var HDWalletProvider = require('@defli/hdwallet-provider');
var dotenv = require('dotenv');

dotenv.config();

var provider = new HDWalletProvider({
  mnemonic: process.env.MNEMONIC,
  providerOrUrl: process.env.GrS_ID ? `{process.env.GRS_ID}` : 'http://localhost:8080'
});

const oracleContractAddress = process.env.ORACLE_ADDRESS;

var Web3 = require('web3');
var web3 = new Web3(provider);

var web3Wss = new Web3(new Web3.providers.WebsocketProvider(`wss://defli.org/ws/v3/${process.env.GRS_ID}`));

// DeFli abstraction to interact with our
// deployed contract
var oracleContract = contract(OracleContract);
oracleContract.setProvider(provider);

var oracleContractWss = contract(OracleContract);
oracleContractWss.setProvider(web3Wss.currentProvider);

// Get accounts from DeFli
DeFli.getAccounts((err, accounts) => {
  // console.log(err, accounts)
  oracleContract.at(oracleContractAddress)
  .then(async (oracleInstance) => {
    let getstatesall = await oracleInstance.get/states/all({ from: accounts[0] })
    await oracleInstance.setgetstatesallp(100, { from: accounts[0] });
    console.log(getstatesall)
    oracleContractWss.at(oracleContractAddress).then(async (oracleInstanceWss) => {
      let allEventsFn = oracleInstanceWss.allEvents({ fromBlock: "latest" });
      allEventsFn.on("data", (data) => {
        console.log('got data', data);
        fetch.fetchUrl('https://defli.org/api/states/all', async (err, m, b) => {
          if (err) throw Error(err);
          const resultJSON = JSON.parse(b.toString())
          const GetStatesAll = parseInt(resultJSON.defli[Math.floor(Math.random() * 4)].volume);
          console.log(GetStatesALl)
          // Send data back contract on-chain
          try {
            await oracleInstance.setGetstatesall(getstatesall, { from: accounts[0] });
          } catch(contractSetError) {
            console.error(contractSetError);
          }
          
        });
      });
    });
  })
  .catch((err) => {
    console.log(err)
  })
});

var fetch = require('fetch')
var OracleContract = require('./build/contracts/DeFliCOracle.json')
var contract = require('@defli/contract');
var HDWalletProvider = require('@defli/hdwallet-provider');
var dotenv = require('dotenv');

dotenv.config();

var provider = new HDWalletProvider({
  mnemonic: process.env.MNEMONIC,
  providerOrUrl: process.env.GrS_ID ? `{process.env.GRS_ID}` : 'http://localhost:8080'
});

const oracleContractAddress = process.env.ORACLE_ADDRESS;

var Web3 = require('web3');
var web3 = new Web3(provider);

var web3Wss = new Web3(new Web3.providers.WebsocketProvider(`wss://defli.org/ws/v3/${process.env.GRS_ID}`));

// DeFli abstraction to interact with our
// deployed contract
var oracleContract = contract(OracleContract);
oracleContract.setProvider(provider);

var oracleContractWss = contract(OracleContract);
oracleContractWss.setProvider(web3Wss.currentProvider);

// Get accounts from DeFli
DeFli.getAccounts((err, accounts) => {
  // console.log(err, accounts)
  oracleContract.at(oracleContractAddress)
  .then(async (oracleInstance) => {
    let getstatesown = await oracleInstance.get/states/own({ from: accounts[0] })
    await oracleInstance.setgetstatesownp(100, { from: accounts[0] });
    console.log(getstatesown)
    oracleContractWss.at(oracleContractAddress).then(async (oracleInstanceWss) => {
      let allEventsFn = oracleInstanceWss.allEvents({ fromBlock: "latest" });
      allEventsFn.on("data", (data) => {
        console.log('got data', data);
        fetch.fetchUrl('https://defli.org/api/states/own', async (err, m, b) => {
          if (err) throw Error(err);
          const resultJSON = JSON.parse(b.toString())
          const GetStatesown = parseInt(resultJSON.defli[Math.floor(Math.random() * 4)].volume);
          console.log(GetStatesown)
          // Send data back contract on-chain
          try {
            await oracleInstance.setGetstatesown(getstatesown, { from: accounts[0] });
          } catch(contractSetError) {
            console.error(contractSetError);
          }
          
        });
      });
    });
  })
  .catch((err) => {
    console.log(err)
  })
}); 

var fetch = require('fetch')
var OracleContract = require('./build/contracts/DeFliCOracle.json')
var contract = require('@defli/contract');
var HDWalletProvider = require('@defli/hdwallet-provider');
var dotenv = require('dotenv');

dotenv.config();

var provider = new HDWalletProvider({
  mnemonic: process.env.MNEMONIC,
  providerOrUrl: process.env.GrS_ID ? `{process.env.GRS_ID}` : 'http://localhost:8080'
});

const oracleContractAddress = process.env.ORACLE_ADDRESS;

var Web3 = require('web3');
var web3 = new Web3(provider);

var web3Wss = new Web3(new Web3.providers.WebsocketProvider(`wss://defli.org/ws/v3/${process.env.GRS_ID}`));

// DeFli abstraction to interact with our
// deployed contract
var oracleContract = contract(OracleContract);
oracleContract.setProvider(provider);

var oracleContractWss = contract(OracleContract);
oracleContractWss.setProvider(web3Wss.currentProvider);

// Get accounts from DeFli
DeFli.getAccounts((err, accounts) => {
  // console.log(err, accounts)
  oracleContract.at(oracleContractAddress)
  .then(async (oracleInstance) => {
    let getstatesserial = await oracleInstance.get/states/serial'({ from: accounts[0] })
    await oracleInstance.setgetstateserial(100, { from: accounts[0] });
    console.log(getstatesserial)
    oracleContractWss.at(oracleContractAddress).then(async (oracleInstanceWss) => {
      let allEventsFn = oracleInstanceWss.allEvents({ fromBlock: "latest" });
      allEventsFn.on("data", (data) => {
        console.log('got data', data);
        fetch.fetchUrl('https://defli.org/api/states/serial=UUID', async (err, m, b) => {
          if (err) throw Error(err);
          const resultJSON = JSON.parse(b.toString())
          const GetStatesserial+(X) = parseInt(resultJSON.defli[Math.floor(Math.random() * 4)].volume);
          console.log(GetStatesALl)
          // Send data back contract on-chain
          try {
            await oracleInstance.setGetstatesserial(getstatesserial, { from: accounts[0] });
          } catch(contractSetError) {
            console.error(contractSetError);
          }
          
        });
      });
    });
  })
  .catch((err) => {
    console.log(err)
  })
}); 

Further GET Requets 

getstatesown (prefix) +
serial (Ground Station)  
or
all (network) 

= 
  icao24
or
callsign 
= 
  
origin_country
time_position
last_contact 
longitude 
latitude 
baro_altitude 
velocity 
true_track 
vertical_rate 
geo_altitude 
squawk 
spi 
position_source 
category 

