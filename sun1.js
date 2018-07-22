'use strict'

const Sunbeam = require('sunbeam')
const Eos = require('eosjs')

const readNodeConf = {
  httpEndpoint: 'http://35.189.86.89:8888',
  keyProvider: [
    '5Jsoz5kcmKLyYwNgud3C7UHKs3RHi7b4izPpjC9n6yNT8VyUqbc'
  ]
}

const writeNodeConf = {
  httpEndpoint: 'http://35.189.86.89:8888', // 'http://writenode.example.com'
  keyProvider: [
    '5Jsoz5kcmKLyYwNgud3C7UHKs3RHi7b4izPpjC9n6yNT8VyUqbc'
  ]
}
const eos = {
  Eos,
  readNodeConf,
  writeNodeConf
}

// dev: true allows one node for read and write
const opts = { dev: true, account: 'testuser1122' }
const sb = new Sunbeam(eos, opts)

sb.withdraw({
  currency: 'BTC',
  amount: '67'
}, {}, (err, res) => {
  if (err) throw err
})
