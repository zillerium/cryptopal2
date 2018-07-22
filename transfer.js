const Sunbeam = require('sunbeam')
const Eos = require('eosjs')

keyProvider= '5Jsoz5kcmKLyYwNgud3C7UHKs3RHi7b4izPpjC9n6yNT8VyUqbc'
httpEndpoint=   'http://35.189.86.89:8888'
chainId=   'cf057bbfb72640471fd910bcb67639c22df9f92470936cddc1ade0e2f2e7dc4f' 

// Localhost Testnet (run ./docker/up.sh)
// Connect to a testnet or mainnet
eos = Eos({httpEndpoint,  keyProvider})

      eos.contract('efinextether').then((contract) => {
      const args = {
      }
      return contract.transfer({ "from": "testuser1122", "to": "efinexchange", "quantity": "1.0000000000 BTC", "memo": "go time"})
     //return contract.cancel(args, this.getAuth())
     })
      .then((res) => {
        console.log(res)
      })
     .catch((err) => { console.log(err) })

