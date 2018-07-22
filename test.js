const Sunbeam = require('sunbeam')
const Eos = require('eosjs')
const YOUR_PRIVATE_KEY = '5Jsoz5kcmKLyYwNgud3C7UHKs3RHi7b4izPpjC9n6yNT8VyUqbc'

const conf = {
	httpEndpoint: 'http://35.189.86.89:8888', // http://localhost:8888
  keyProvider: [
    YOUR_PRIVATE_KEY
  ]
}

const eos = {
  Eos,
  readNodeConf: conf,
  writeNodeConf: conf
}

const opts = { dev: true, account: 'testuser1122' }
const sb = new Sunbeam(eos, opts)
sb.orderbook('BTCUSD', {}, (err, res) => {
  if (err) throw err

  console.log('orderbook: raw')
  console.log(JSON.stringify(res, null, '  '))
})

