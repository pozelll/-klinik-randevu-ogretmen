'use strict';
const {createRepository} = require('../src/repository.js');
const {createService} = require('../src/rules.js');
const demo = require('../src/demo-data.js');
const context = {role: 'patient', patientId: 'ece', doctorId: 'deniz', date: demo.DATES[0]};
function memoryStorage(initial = {}) {
  const data = new Map(Object.entries(initial));
  return {fail: false, writes: 0,
    getItem(key) { return data.get(key) ?? null; },
    setItem(key, value) { if (this.fail) throw new Error('Kota / izin hatası'); data.set(key, value); this.writes++; },
    removeItem(key) { data.delete(key); }
  };
}
function fixture(options = {}) {
  const storage = options.storage === undefined ? memoryStorage() : options.storage;
  const repository = createRepository({...options, storage});
  let updates = 0;
  const original = repository.update;
  repository.update = a => { updates++; return original(a); };
  const service = createService(repository);
  return {repository, service, storage, updateCalls: () => updates};
}
module.exports = {fixture, memoryStorage, context, demo};
