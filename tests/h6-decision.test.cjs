'use strict';
const {test, after} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {fixture, context, demo} = require('./helpers.cjs');
const cases = [
  ['DK-K01', 'R999', 'patient', 'ece', 'pending', 'NOT_FOUND'],
  ['DK-K02', 'R001', 'reception', 'ece', 'pending', 'ROLE'],
  ['DK-K03', 'R001', 'doctor', 'ece', 'pending', 'ROLE'],
  ['DK-K04', 'R001', 'patient', 'kaan', 'pending', 'OWNER'],
  ['DK-K05', 'R001', 'patient', 'ece', 'completed', 'STATUS'],
  ['DK-K06', 'R001', 'patient', 'ece', 'cancelled', 'STATUS'],
  ['DK-K07', 'R001', 'patient', 'ece', 'pending', 'OK']
];
const evidence = [];
for (const [id, requestId, role, patientId, status, expected] of cases) {
  test(`${id} | ${expected}`, () => {
    const initialData = demo.seedData(); initialData.appointments[0].status = status;
    const {repository: r, service: s, storage, updateCalls} = fixture({initialData});
    const before = r.snapshot(); const writesBefore = storage.writes;
    const result = s.cancel(requestId, {...context, role, patientId});
    const afterData = r.snapshot();
    assert.equal(result.ok ? 'OK' : result.code, expected);
    if (expected === 'OK') {
      assert.equal(afterData.appointments[0].status, 'cancelled');
      assert.equal(afterData.appointments.length, before.appointments.length);
      assert.equal(afterData.nextId, before.nextId);
      assert.deepEqual(afterData.appointments.slice(1), before.appointments.slice(1));
      assert.equal(result.slotAvailable, true);
      assert.equal(updateCalls(), 1);
      assert.equal(storage.writes - writesBefore, 1);
    } else {
      assert.deepEqual(afterData, before);
      assert.equal(updateCalls(), 0);
      assert.equal(storage.writes - writesBefore, 0);
    }
    evidence.push({id, context: {...context, role, patientId}, requestId, expected,
      actual: result, before, after: afterData, updateCalls: updateCalls(),
      storageWritesDuringRequest: storage.writes - writesBefore, status: 'PASS'});
  });
}
after(() => {
  if (!process.env.EVIDENCE_DIR) return;
  const sources = Object.fromEntries(['index.html','src/demo-data.js','src/repository.js','src/rules.js','src/ui.js'].map(p =>
    [p, crypto.createHash('sha256').update(fs.readFileSync(path.join(__dirname,'..',p))).digest('hex')]));
  fs.mkdirSync(process.env.EVIDENCE_DIR, {recursive:true});
  fs.writeFileSync(path.join(process.env.EVIDENCE_DIR,'karar-tablosu-sonuclari.json'),
    JSON.stringify({executedAt: new Date().toISOString(), node: process.version,
      scope: 'Otomatik kontrollü ders testi; bağımsız kişi incelemesi değildir.', sources, evidence}, null, 2)+'\n');
});
