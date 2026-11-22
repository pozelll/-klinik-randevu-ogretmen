/* İş kuralları: DOM, onay penceresi ve localStorage bağımlılığı yoktur. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory(require('./demo-data.js'));
  else root.KlinikRules = factory(root.KlinikDemo);
})(globalThis, function (demo) {
  'use strict';
  function hasConflicts(rows) {
    const occupied = new Set();
    for (const a of rows) {
      if (a.status === 'cancelled') continue;
      const key = [a.doctorId, a.date, a.time].join('|');
      if (occupied.has(key)) return true;
      occupied.add(key);
    }
    return false;
  }
  const validContext = c => c && Object.hasOwn(demo.ROLE_LABELS, c.role) &&
    Object.hasOwn(demo.PATIENTS, c.patientId) && Object.hasOwn(demo.DOCTORS, c.doctorId) && demo.DATES.includes(c.date);
  const canBook = c => validContext(c) && ['patient', 'reception'].includes(c.role);
  const canViewDaily = c => validContext(c) && ['reception', 'doctor'].includes(c.role);
  const canComplete = (a, c) => Boolean(a && validContext(c) && c.role === 'doctor' &&
    a.doctorId === c.doctorId && a.date === c.date && a.status === 'pending');
  function createService(repository) {
    let startupMessage = repository.storageStatus().loadMessage;
    if (hasConflicts(repository.list())) {
      repository.reset();
      startupMessage = 'Önceki demo kaydında çakışma bulundu. Başlangıçtaki sentetik veriler yüklendi.';
    }
    repository.flush();
    function occupiedAt(c, time) {
      return repository.list().find(a => a.doctorId === c.doctorId && a.date === c.date && a.time === time && a.status !== 'cancelled') || null;
    }
    function cancelEligibility(id, c) {
      const appointment = repository.findById(id);
      if (!appointment) return {ok: false, code: 'NOT_FOUND'};
      if (!c || c.role !== 'patient') return {ok: false, code: 'ROLE'};
      if (appointment.patientId !== c.patientId) return {ok: false, code: 'OWNER'};
      if (appointment.status !== 'pending') return {ok: false, code: 'STATUS'};
      return {ok: true, appointment};
    }
    function cancel(id, c) {
      // Onay penceresinden sonra güncel veriyi tekrar denetle.
      const eligibility = cancelEligibility(id, c);
      if (!eligibility.ok) return eligibility;
      const appointment = {...eligibility.appointment, status: 'cancelled'};
      const saved = repository.update(appointment);
      if (!saved.applied) return {ok: false, code: 'WRITE'};
      return {ok: true, appointment, persistent: saved.persistent,
        slotAvailable: !occupiedAt(appointment, appointment.time)};
    }
    function book(c, time) {
      if (!validContext(c)) return {ok: false, code: 'CONTEXT'};
      if (!canBook(c)) return {ok: false, code: 'ROLE'};
      if (!demo.TIMES.includes(time)) return {ok: false, code: 'TIME'};
      if (occupiedAt(c, time)) return {ok: false, code: 'OCCUPIED'};
      if (repository.list().length >= 1000) return {ok: false, code: 'LIMIT'};
      const saved = repository.add({patientId: c.patientId, doctorId: c.doctorId, date: c.date, time, status: 'pending'});
      return saved.applied ? {ok: true, appointment: saved.appointment, persistent: saved.persistent} : {ok: false, code: 'WRITE'};
    }
    function complete(id, c) {
      const appointment = repository.findById(id);
      if (!canComplete(appointment, c)) return {ok: false, code: 'ROLE'};
      const updated = {...appointment, status: 'completed'};
      const saved = repository.update(updated);
      return saved.applied ? {ok: true, appointment: updated, persistent: saved.persistent} : {ok: false, code: 'WRITE'};
    }
    function view(c) {
      const rows = repository.list().filter(a => a.doctorId === c.doctorId && a.date === c.date);
      const daily = canViewDaily(c);
      const appointments = rows.filter(a => daily || a.patientId === c.patientId)
        .sort((a, b) => a.time.localeCompare(b.time) || a.id.localeCompare(b.id));
      const totals = daily ? {pending: 0, completed: 0, cancelled: 0, total: rows.length} : null;
      if (daily) rows.forEach(a => totals[a.status]++);
      return {appointments, totals, canBook: canBook(c), canViewDaily: daily};
    }
    return {startupMessage, cancelEligibility, cancel, book, complete, view, occupiedAt,
      canComplete, storageStatus: () => repository.storageStatus(), reset: () => repository.reset()};
  }
  return {createService, hasConflicts};
});
