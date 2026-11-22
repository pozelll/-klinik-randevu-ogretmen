/* Sabit sentetik ders verisi. Ürün katmanı değil, ortak veri sözlüğüdür. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.KlinikDemo = factory();
})(globalThis, function () {
  'use strict';
    const STORAGE_KEY = 'ygs-klinik-randevu-demo-v1';
    const PATIENTS = {ece:'Ece Yılmaz',kaan:'Kaan Demir'};
    const DOCTORS = {deniz:'Doktor Deniz Arı',selin:'Doktor Selin Kaya'};
    const DATES = ['2030-11-12','2030-11-13'];
    const TIMES = ['09:00','09:30','10:00','10:30','11:00','11:30','13:00','13:30','14:00','14:30'];
    const STATUS_LABELS = {pending:'Bekliyor',completed:'Tamamlandı',cancelled:'İptal edildi'};
    const ROLE_LABELS = {patient:'Hasta',reception:'Resepsiyon',doctor:'Doktor'};
    function seedData() {
      return {schema:1,nextId:8,appointments:[
        {id:'R001',patientId:'ece',doctorId:'deniz',date:DATES[0],time:'09:00',status:'pending'},
        {id:'R002',patientId:'kaan',doctorId:'deniz',date:DATES[0],time:'10:00',status:'pending'},
        {id:'R003',patientId:'ece',doctorId:'deniz',date:DATES[0],time:'11:00',status:'completed'},
        {id:'R004',patientId:'kaan',doctorId:'deniz',date:DATES[0],time:'13:00',status:'cancelled'},
        {id:'R005',patientId:'ece',doctorId:'selin',date:DATES[0],time:'09:30',status:'pending'},
        {id:'R006',patientId:'kaan',doctorId:'selin',date:DATES[0],time:'11:00',status:'completed'},
        {id:'R007',patientId:'kaan',doctorId:'deniz',date:DATES[1],time:'10:30',status:'pending'}
      ]};
    }

    function validateShape(candidate) {
      if (!candidate || candidate.schema !== 1 || !Number.isSafeInteger(candidate.nextId) || candidate.nextId < 8 || !Array.isArray(candidate.appointments) || candidate.appointments.length > 1000) return false;
      const ids = new Set();
      for (const a of candidate.appointments) {
        if (!a || !/^R\d{3,12}$/.test(a.id) || ids.has(a.id) || !Object.hasOwn(PATIENTS,a.patientId) || !Object.hasOwn(DOCTORS,a.doctorId) || !DATES.includes(a.date) || !TIMES.includes(a.time) || !Object.hasOwn(STATUS_LABELS,a.status)) return false;
        if (Number(a.id.slice(1)) >= candidate.nextId) return false;
        ids.add(a.id);
      }
      return true;
    }

  return {STORAGE_KEY, PATIENTS, DOCTORS, DATES, TIMES, STATUS_LABELS, ROLE_LABELS, seedData, validateShape};
});
