const Sunbeam = require('sunbeam')
const Eos = require('eosjs')
keyProvider: '5Jsoz5kcmKLyYwNgud3C7UHKs3RHi7b4izPpjC9n6yNT8VyUqb'

httpEndpoint: 'http://35.189.86.89:8888'
 chainId: 'cf057bbfb72640471fd910bcb67639c22df9f92470936cddc1ade0e2f2e7dc4f' 

// Localhost Testnet (run ./docker/up.sh)
eos = Eos({keyProvider})

// Connect to a testnet or mainnet
eos = Eos({httpEndpoint, chainId, keyProvider})

// Cold-storage
eos = Eos({httpEndpoint: null, chainId, keyProvider})

// Read-only instance when 'eosjs' is already a dependency
eos = Eos.modules.api({/*config*/})


      eos.contract('eosio.token').then((contract) => {
      const args = {
      }
      contract.transfer('testuser1122', 'testuser1234', '0.1 BTC', '', options)
      return contract.cancel(args, this.getAuth())
    })
      .then((res) => {
        return cb(null, res)
      })
      .catch((err) => { cb(err) })

