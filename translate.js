const csv = require('csv-parser')
const fs = require('fs-extra')
const _ = require('lodash')
const { Translate } = require('@google-cloud/translate').v2;

const translate = new Translate({ key: 'xxxxx' });

let results = require('./raw_sci.json');

const start = async () => {
  console.log('count:', results.length)

  for (let i = 0; i < results.length; i++) {
    const [data] = await translate.detect(results[i].text)
    const [translation] = await translate.translate(results[i].text, { to: 'en' });
    results[i].text_lang = data.language
    results[i].text_en = translation
    console.log('translate', i, `[${results[i].text_lang}]`, results[i].text, translation)
  }

  const content = ['[']
  results.forEach((obj, index) => {
    if (index === results.length - 1) {
      content.push(JSON.stringify(obj))
    } else  {
      content.push(JSON.stringify(obj) + ',')
    }
  })
  content.push(']')
  fs.outputFileSync('raw_sci.json', content.join('\n'))
}

start()
