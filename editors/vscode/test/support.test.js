const test = require('node:test');
const assert = require('node:assert/strict');
const {parseDiagnostic, words} = require('../support');
test('parse paths including drive colon and Arabic', () => {
  const item = parseDiagnostic('APL-SyntaxError: C:\\مشروع\\main.apl:3:5\nخطأ في الصياغة\n');
  assert.equal(item.line, 2); assert.equal(item.column,4);
  assert.equal(item.file,'C:\\مشروع\\main.apl');
});
test('bounded prefix completion', () => {
  assert.deepEqual(words([{name:'جذر'}], 'ج'), [{name:'جذر'}]);
  assert.equal(words(Array(110).fill({name:'س'}),'س').length,100);
});
test('valid manifest, grammar and generated completion index', () => {
  const manifest = require('../package.json');
  assert.equal(manifest.contributes.languages[0].id,'apl');
  assert.ok(require('../syntaxes/apl.tmLanguage.json').patterns.length);
  assert.ok(require('../completions.json').length > 1000);
});
