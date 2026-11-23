'use strict';
const vscode = require('vscode');
const cp = require('node:child_process');
const index = require('./completions.json');
const {parseDiagnostic, words} = require('./support');
function activate(context) {
  const diagnostics = vscode.languages.createDiagnosticCollection('apl');
  const selector = {language:'apl', scheme:'file'};
  let running;
  function check(document) {
    if (document.languageId !== 'apl') return;
    // Checking invokes the compiler only, never runs the program. Executable
    // configuration and process launch are restricted to trusted workspaces.
    if (!vscode.workspace.isTrusted) return;
    if (document.isDirty) return;
    const version = document.version;
    if (running) running.kill();
    const exe = vscode.workspace.getConfiguration('apl').get('executable', 'apl');
    running = cp.execFile(exe, ['check', document.uri.fsPath], {timeout:10000,maxBuffer:65536}, (error, stdout, stderr) => {
      if (document.isClosed || document.version !== version) return;
      const item = parseDiagnostic(stderr);
      if (item) {
        const position = new vscode.Position(item.line, item.column);
        diagnostics.set(document.uri, [new vscode.Diagnostic(new vscode.Range(position, position.translate(0,1)), item.message, vscode.DiagnosticSeverity.Error)]);
      } else diagnostics.delete(document.uri);
    });
  }
  context.subscriptions.push(diagnostics,
    vscode.languages.registerCompletionItemProvider(selector, {provideCompletionItems(document, position) {
      const range = document.getWordRangeAtPosition(position, /[\w\u0600-\u06FF]+/u);
      const prefix = range ? document.getText(new vscode.Range(range.start, position)) : '';
      if (!prefix) return [];
      return words(index,prefix).map(item => {
        const result = new vscode.CompletionItem(item.name, vscode.CompletionItemKind.Function);
        result.detail = `${item.library}: ${item.target}`;
        return result;
      });
    }}),
    vscode.languages.registerHoverProvider(selector, {provideHover(document, position) {
      const range = document.getWordRangeAtPosition(position, /[\w\u0600-\u06FF]+/u);
      if (!range) return;
      const item = index.find(item => item.name === document.getText(range));
      if (item) return new vscode.Hover(`${item.name}\n\n${item.library}: ${item.target}`);
    }}),
    vscode.workspace.onDidOpenTextDocument(check), vscode.workspace.onDidSaveTextDocument(check),
    {dispose(){if(running)running.kill();}}
  );
  vscode.workspace.textDocuments.forEach(check);
}
module.exports = {activate};
