'use strict';
const {test} = require('node:test');
const assert = require('node:assert/strict');
const {fixture, context} = require('./helpers.cjs');

test('H5-S01 | Onaylı iptal kaydı silmez, nextId korunur', () => {
  const {repository: r, service: s} = fixture();
  const before = r.snapshot();
  assert.equal(s.cancel('R001', context).ok, true);
  assert.equal(r.findById('R001').status, 'cancelled');
  assert.equal(r.list().length, before.appointments.length);
  assert.equal(r.snapshot().nextId, before.nextId);
});
test('H5-S02 | Yalnız kopyayı değiştirmek depoyu değiştirmez', () => {
  const {repository: r} = fixture();
  r.findById('R001').status = 'cancelled';
  const rows = r.list(); rows[0].status = 'completed'; rows.pop();
  assert.equal(r.findById('R001').status, 'pending');
  assert.equal(r.list().length, 7);
});
test('H5-S03 | BR-01 dolu saate ikinci kayıt açtırmaz', () => {
  const {repository: r, service: s} = fixture();
  const before = r.snapshot();
  assert.equal(s.book(context, '09:00').code, 'OCCUPIED');
  assert.deepEqual(r.snapshot(), before);
});
test('H5-S04 | İptal, yeniden oluşturma ve tamamlama aynı veriyi kullanır', () => {
  const {repository: r, service: s} = fixture();
  s.cancel('R001', context);
  const created = s.book(context, '09:00');
  assert.equal(created.ok, true);
  assert.equal(created.appointment.id, 'R008');
  assert.equal(s.complete('R008', {...context, role: 'doctor'}).ok, true);
  assert.equal(r.findById('R001').status, 'cancelled');
  assert.equal(r.findById('R008').status, 'completed');
  assert.equal(s.occupiedAt(context, '09:00').id, 'R008');
});
test('H5-S05 | Hasta filtresi ve günlük toplamların kapsamı korunur', () => {
  const {service: s} = fixture();
  assert.deepEqual(s.view(context).appointments.map(a => a.id), ['R001', 'R003']);
  assert.equal(s.view(context).totals, null);
  assert.deepEqual(s.view({...context, role: 'reception'}).totals,
    {pending: 2, completed: 1, cancelled: 1, total: 4});
});
test('H5-S06 | Yazma başarısızsa değişiklik bellekte, kalıcılık false', () => {
  const {repository: r, service: s, storage} = fixture();
  storage.fail = true;
  const result = s.cancel('R001', context);
  assert.equal(result.ok, true);
  assert.equal(result.persistent, false);
  assert.equal(r.findById('R001').status, 'cancelled');
  assert.equal(s.storageStatus().persistent, false);
});
test('H5-S07 | Resepsiyon iptal isteğinde güncelleme yapılmaz', () => {
  const {repository: r, service: s, updateCalls} = fixture();
  const before = r.snapshot();
  assert.equal(s.cancel('R001', {...context, role: 'reception'}).code, 'ROLE');
  assert.equal(updateCalls(), 0);
  assert.deepEqual(r.snapshot(), before);
});
test('H5-S08 | Onaydan önce uygun olan kayıt işlem anında yeniden denetlenir', () => {
  const {service: s, repository: r, updateCalls} = fixture();
  assert.equal(s.cancelEligibility('R001', context).ok, true);
  s.complete('R001', {...context, role: 'doctor'});
  const count = updateCalls();
  assert.equal(s.cancel('R001', context).code, 'STATUS');
  assert.equal(r.findById('R001').status, 'completed');
  assert.equal(updateCalls(), count);
});
