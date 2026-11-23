'use strict';
function parseDiagnostic(text) {
  const m = text.match(/APL-([A-Za-z]+): (.*):(\d+):(\d+)\r?\n([^\n]+)/u);
  return m ? {kind: m[1], file: m[2], line: Math.max(0, Number(m[3])-1),
    column: Math.max(0, Number(m[4])-1), message: m[5]} : null;
}
function words(index, prefix) {
  return index.filter(item => item.name.startsWith(prefix)).slice(0, 100);
}
module.exports = {parseDiagnostic, words};
