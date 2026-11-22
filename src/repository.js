/* Veri erişimi: tek oturum verisi, bağımsız kopyalar, kalıcılık sonucu. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory(require('./demo-data.js'));
  else root.KlinikRepository = factory(root.KlinikDemo);
})(globalThis, function (demo) {
  'use strict';
  const copy = value => JSON.parse(JSON.stringify(value));
  function createRepository({storage = null, initialData = demo.seedData()} = {}) {
    if (!demo.validateShape(initialData)) throw new Error('Geçersiz başlangıç veri biçimi');
    let data = copy(initialData);
    let persistent = false;
    let loadMessage = '';
    if (storage) {
      try {
        const probe = demo.STORAGE_KEY + '-probe';
        storage.setItem(probe, '1'); storage.removeItem(probe);
        persistent = true;
        const saved = storage.getItem(demo.STORAGE_KEY);
        if (saved) {
          try {
            const candidate = JSON.parse(saved);
            if (!demo.validateShape(candidate)) throw new Error('Geçersiz biçim');
            data = copy(candidate);
          } catch (_) { loadMessage = 'Önceki demo kaydı okunamadı. Başlangıçtaki sentetik veriler yüklendi.'; }
        }
      } catch (_) { persistent = false; }
    }
    if (!persistent) loadMessage = 'Tarayıcı kalıcı kayda izin vermiyor. Demo bu oturumda çalışır; sayfa yenilenince son kalıcı kayıt veya örnek veriler yüklenir.';
    function persist() {
      if (persistent) {
        try { storage.setItem(demo.STORAGE_KEY, JSON.stringify(data)); }
        catch (_) { persistent = false; }
      }
      return {applied: true, persistent};
    }
    function replace(candidate) {
      if (!demo.validateShape(candidate)) return {applied: false, persistent, code: 'SHAPE'};
      data = copy(candidate);
      return persist();
    }
    return {
      findById: id => copy(data.appointments.find(a => a.id === id) || null),
      list: () => copy(data.appointments),
      snapshot: () => copy(data),
      storageStatus: () => ({persistent, loadMessage}),
      flush: persist,
      update(appointment) {
        const index = data.appointments.findIndex(a => a.id === appointment.id);
        if (index < 0) return {applied: false, persistent, code: 'NOT_FOUND'};
        const candidate = copy(data);
        candidate.appointments[index] = copy(appointment);
        return replace(candidate);
      },
      add(fields) {
        const candidate = copy(data);
        const appointment = {...copy(fields), id: 'R' + String(candidate.nextId++).padStart(3, '0')};
        candidate.appointments.push(appointment);
        return {...replace(candidate), appointment: copy(appointment)};
      },
      reset: () => replace(demo.seedData())
    };
  }
  return {createRepository};
});
