'use strict';
const {test} = require('node:test');
const assert = require('node:assert/strict');
const {fixture, memoryStorage, context, demo} = require('./helpers.cjs');

test('H6-R01 | Kalıcı veri tekrar açıldığında korunur', () => {
  const f = fixture(); f.service.cancel('R001', context);
  const reopened = fixture({storage: f.storage});
  assert.equal(reopened.repository.findById('R001').status, 'cancelled');
});
test('H6-R02 | Bozuk JSON bilinen sentetik veriye döner', () => {
  const f = fixture({storage: memoryStorage({[demo.STORAGE_KEY]:'{bad'})});
  assert.deepEqual(f.repository.snapshot(), demo.seedData());
  assert.match(f.service.startupMessage, /okunamadı/);
});
test('H6-R03 | Geçersiz veri şeması reddedilir', () => {
  const data = demo.seedData(); data.schema = 99;
  const f = fixture({storage: memoryStorage({[demo.STORAGE_KEY]:JSON.stringify(data)})});
  assert.equal(f.repository.snapshot().schema, 1);
});
test('H6-R04 | Başlangıç BR-01 çakışması iş katmanında saptanır', () => {
  const data = demo.seedData(); data.appointments[1].time = '09:00';
  const f = fixture({storage: memoryStorage({[demo.STORAGE_KEY]:JSON.stringify(data)})});
  assert.deepEqual(f.repository.snapshot(), demo.seedData());
  assert.match(f.service.startupMessage, /çakışma/);
});
test('H6-R05 | Depo bulunmayan kimlikte kayıt oluşturmaz', () => {
  const f = fixture(); const before = f.repository.snapshot();
  assert.equal(f.repository.update({...before.appointments[0],id:'R999'}).applied, false);
  assert.deepEqual(f.repository.snapshot(), before);
});
test('H6-R06 | Yazma hatası son kalıcı kopyayı değiştirmez', () => {
  const f = fixture(); const saved = f.storage.getItem(demo.STORAGE_KEY);
  f.storage.fail = true; f.service.cancel('R001', context);
  assert.equal(f.storage.getItem(demo.STORAGE_KEY), saved);
  f.storage.fail = false;
  assert.equal(fixture({storage:f.storage}).repository.findById('R001').status, 'pending');
});
test('H6-R07 | localStorage yoksa uygulama oturum belleğinde çalışır', () => {
  const f = fixture({storage:null});
  assert.equal(f.service.book(context, '09:30').ok, true);
  assert.equal(f.service.storageStatus().persistent, false);
});
test('H6-R08 | Doktor ve resepsiyon dışındaki görünüm toplamları açmaz', () => {
  const f = fixture();
  assert.equal(f.service.view(context).totals, null);
  assert.equal(f.service.view({...context,role:'doctor'}).totals.total, 4);
});
test('H6-R09 | İptal günlük toplamı korur, durum sayılarını değiştirir', () => {
  const f = fixture(); f.service.cancel('R001', context);
  assert.deepEqual(f.service.view({...context,role:'reception'}).totals,
    {pending:1,completed:1,cancelled:2,total:4});
});
test('H6-R10 | Doktor kayıt oluşturamaz; resepsiyon oluşturabilir', () => {
  const f = fixture();
  assert.equal(f.service.book({...context,role:'doctor'}, '09:30').code, 'ROLE');
  assert.equal(f.service.book({...context,role:'reception'}, '09:30').ok, true);
});
test('H6-R11 | Farklı doktor/tarih ve resepsiyon tamamlama isteği reddedilir', () => {
  const f = fixture(); const before = f.repository.snapshot();
  for (const c of [{...context,role:'reception'}, {...context,role:'doctor',doctorId:'selin'},
    {...context,role:'doctor',date:demo.DATES[1]}]) assert.equal(f.service.complete('R001', c).ok, false);
  assert.deepEqual(f.repository.snapshot(), before);
});
test('H6-R12 | Geçersiz saat ve hasta yeni kayıt oluşturmaz', () => {
  const f = fixture(); const before = f.repository.snapshot();
  assert.equal(f.service.book(context, '04:00').code, 'TIME');
  assert.equal(f.service.book({...context,patientId:'unknown'}, '09:30').code, 'CONTEXT');
  assert.deepEqual(f.repository.snapshot(), before);
});
test('H6-R13 | 1000 kayıt sınırı nextId değerini artırmaz', () => {
  const data = demo.seedData();
  while (data.appointments.length < 1000) {
    data.appointments.push({...data.appointments[0],id:'R'+String(data.nextId++).padStart(3,'0'),status:'cancelled'});
  }
  const f = fixture({initialData:data}); const before=f.repository.snapshot();
  assert.equal(f.service.book(context,'09:30').code,'LIMIT');
  assert.deepEqual(f.repository.snapshot(),before);
});
test('H6-R14 | Çakışan başka kayıt varsa iptal saati uygun göstermez', () => {
  const f = fixture();
  // Dayanıklılık deneyi: normal ürün akışının reddettiği veri, depo sınırında kontrollü eklenir.
  f.repository.update({...f.repository.findById('R002'),time:'09:00'});
  const result = f.service.cancel('R001',context);
  assert.equal(result.ok,true); assert.equal(result.slotAvailable,false);
  assert.equal(f.repository.findById('R002').status,'pending');
});
test('H6-R15 | Sıfırlama tek ortak depoyu başlangıca döndürür', () => {
  const f = fixture(); f.service.cancel('R001',context); f.service.book(context,'09:30');
  f.service.reset(); assert.deepEqual(f.repository.snapshot(),demo.seedData());
});
