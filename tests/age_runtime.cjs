// Execute the rendered page with a minimal DOM and record observable chart output.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const script = fs.readFileSync(0, 'utf8');
const stats = {};
const charts = {};
const resize = [];
const document = {
  getElementById(id) {
    if (!id.endsWith('Chart')) return stats[id] ??= {};
    const output = charts[id] ??= {bars: 0, labels: []};
    const finite = (...args) => args.forEach(value => {
      if (typeof value === 'number') assert.ok(Number.isFinite(value), `${id}: ${value}`);
    });
    const context = {
      scale: finite,
      clearRect(...args) { finite(...args); output.bars = 0; output.labels = []; },
      beginPath() {}, moveTo: finite, lineTo: finite, stroke() {}, fill() {},
      roundRect(...args) { finite(...args); output.bars++; },
      fillText(label, ...args) { finite(...args); output.labels.push(String(label)); },
      createLinearGradient(...args) { finite(...args); return {addColorStop() {}}; },
    };
    return {
      style: {},
      parentElement: {getBoundingClientRect: () => ({width: 800, height: 320})},
      getContext: () => context,
    };
  },
};
vm.runInNewContext(script, {
  document,
  window: {devicePixelRatio: 2, addEventListener(event, callback) {
    assert.equal(event, 'resize'); resize.push(callback);
  }},
}, {timeout: 1000});
resize.forEach(callback => callback());
console.log(JSON.stringify({stats, charts}));
