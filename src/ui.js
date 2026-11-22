/* Arayüz: olaylar, onay, metinler ve çizim. Randevu verisine doğrudan yazmaz. */
(() => {
  'use strict';
  const {PATIENTS,DOCTORS,DATES,TIMES,STATUS_LABELS,ROLE_LABELS} = KlinikDemo;
  let storage = null;
  try { storage = window.localStorage; } catch (_) { /* Oturum belleğinde devam. */ }
  const repository = KlinikRepository.createRepository({storage});
  const service = KlinikRules.createService(repository);
  const state = {role:'patient',patientId:'ece',doctorId:'deniz',date:DATES[0],selectedTime:null};
  const $ = id => document.getElementById(id);
    function renderStorage() {
      const storageAvailable = service.storageStatus().persistent;
      $('storage-label').textContent = storageAvailable ? 'Kaydetme: Bu tarayıcıda yerel kayıt.' : 'Kaydetme: Yalnız bu oturumun belleği.';
      $('storage-description').textContent = storageAvailable
        ? 'Sunucuya veri gönderilmez. Aynı dosya ve tarayıcıda kayıt korunabilir; tarayıcı verisi silinirse kaybolur. Sekmeler/cihazlar arasında eşzamanlama yoktur.'
        : 'Tarayıcı kalıcı kayda izin vermedi. Sayfa yenilenince değişiklikler kaybolur. İncelemeye devam edebilir ve bulgularınızı belgelere yazabilirsiniz.';
    }

    function dateLabel(date) { return date === DATES[0] ? '12 Kasım 2030' : '13 Kasım 2030'; }
    function view() { return service.view(state); }
    function canBook() { return view().canBook; }
    function canViewDaily() { return view().canViewDaily; }
    function occupiedAt(time) { return service.occupiedAt(state, time); }
    function canCancel(a) { return service.cancelEligibility(a.id, state).ok; }
    function canComplete(a) { return service.canComplete(a, state); }

    function notify(message,tone='info') {
      $('notice').dataset.tone = tone;
      $('notice').querySelector('.status-symbol').textContent = tone === 'success' ? '✓' : tone === 'error' ? '!' : 'i';
      $('notice-text').textContent = message;
    }

    function renderControls() {
      document.querySelectorAll('[data-role]').forEach(button => button.setAttribute('aria-pressed',String(button.dataset.role === state.role)));
      $('patient-select').value = state.patientId;
      $('patient-select').disabled = state.role === 'doctor';
      $('doctor-select').value = state.doctorId;
      $('date-select').value = state.date;
      $('patient-help').textContent = state.role === 'patient' ? 'Bu hastanın rolünü canlandırıyorsunuz.' : state.role === 'reception' ? 'Bu hasta adına randevu oluşturabilirsiniz.' : 'Hasta seçimi doktor rolünde kullanılmaz.';
      $('doctor-label').textContent = state.role === 'doctor' ? 'Görevli doktor (simülasyon)' : 'Doktor';
      $('doctor-help').textContent = state.role === 'doctor' ? 'Bu doktorun günlük listesini inceliyorsunuz.' : 'Saatler seçili doktora aittir.';
    }

    function renderSlots() {
      $('slots-subtitle').textContent = DOCTORS[state.doctorId] + ' · ' + dateLabel(state.date) + ' · FR-01';
      const fragment = document.createDocumentFragment();
      TIMES.forEach(time => {
        const existing = occupiedAt(time);
        const selected = state.selectedTime === time && !existing;
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'slot';
        button.dataset.time = time;
        button.dataset.testid = 'slot-' + time.replace(':','');
        button.disabled = Boolean(existing) || !canBook();
        button.setAttribute('aria-pressed',String(selected));
        const label = existing ? (existing.status === 'completed' ? 'Kapalı' : 'Dolu') : selected ? 'Seçili' : 'Uygun';
        button.setAttribute('aria-label',time + ', ' + label + (canBook() ? '' : ', doktor rolünde kayıt oluşturulmaz'));
        const strong = document.createElement('strong'); strong.textContent = time;
        const small = document.createElement('small'); small.textContent = label;
        button.append(strong,small);
        fragment.append(button);
      });
      $('slots').replaceChildren(fragment);
      if (state.selectedTime && occupiedAt(state.selectedTime)) state.selectedTime = null;
      $('book-appointment').disabled = !canBook() || !state.selectedTime;
      $('booking-summary').textContent = !canBook()
        ? 'Doktor rolü saatleri inceler. Randevu oluşturmak için Hasta veya Resepsiyon rolünü seçin.'
        : state.selectedTime
          ? PATIENTS[state.patientId] + ' · ' + DOCTORS[state.doctorId] + ' · ' + dateLabel(state.date) + ', ' + state.selectedTime
          : 'Randevu oluşturmak için uygun bir saate tıklayın.';
    }

    function renderAppointments() {
      const rows = view().appointments;
      $('appointments-title').textContent = canViewDaily() ? 'Günlük randevu listesi' : 'Randevularım';
      $('appointments-subtitle').textContent = canViewDaily()
        ? DOCTORS[state.doctorId] + ' · ' + dateLabel(state.date) + ' · FR-04 / FR-05'
        : PATIENTS[state.patientId] + ' · ' + dateLabel(state.date) + ' · FR-03';
      $('list-note').textContent = state.role === 'patient'
        ? 'Seçili doktor ve tarihteki kendi kayıtlarınız gösterilir. Yalnız Bekliyor durumundaki kendi randevunuzu iptal edebilirsiniz.'
        : state.role === 'doctor'
          ? 'Yalnız görevli doktorun Bekliyor durumundaki randevuları Tamamlandı yapılabilir. Tamamlanmış saat tekrar açılmaz.'
          : 'Seçili doktor ve tarihin bütün örnek kayıtları gösterilir. Resepsiyon bu prototipte iptal veya tamamlama yapamaz.';
      const fragment = document.createDocumentFragment();
      if (!rows.length) {
        const empty = document.createElement('p'); empty.className = 'empty'; empty.textContent = 'Bu seçimde henüz randevu yok. Diğer doktoru veya tarihi inceleyebilirsiniz.'; fragment.append(empty);
      }
      rows.forEach(a => {
        const row = document.createElement('article'); row.className = 'appointment'; row.dataset.appointmentId = a.id;
        const time = document.createElement('div'); time.className = 'time-block'; time.textContent = a.time;
        const details = document.createElement('div');
        const name = document.createElement('p'); name.className = 'appointment-name'; name.textContent = PATIENTS[a.patientId];
        const meta = document.createElement('p'); meta.className = 'appointment-meta'; meta.textContent = DOCTORS[a.doctorId] + ' · ' + a.id;
        details.append(name,meta);
        const actions = document.createElement('div'); actions.className = 'appointment-actions';
        const pill = document.createElement('span'); pill.className = 'status-pill ' + a.status; pill.textContent = STATUS_LABELS[a.status]; actions.append(pill);
        if (canCancel(a)) {
          const button = document.createElement('button'); button.type = 'button'; button.className = 'small-button cancel'; button.dataset.action = 'cancel'; button.dataset.id = a.id; button.textContent = 'İptal et'; button.setAttribute('aria-label',a.time + ' saatindeki ' + a.id + ' randevusunu iptal et'); actions.append(button);
        }
        if (canComplete(a)) {
          const button = document.createElement('button'); button.type = 'button'; button.className = 'small-button'; button.dataset.action = 'complete'; button.dataset.id = a.id; button.textContent = 'Tamamlandı'; button.setAttribute('aria-label',a.time + ' saatindeki ' + a.id + ' randevusunu tamamlandı yap'); actions.append(button);
        }
        row.append(time,details,actions); fragment.append(row);
      });
      $('appointments').replaceChildren(fragment);
    }

    function renderSummary() {
      const allowed = canViewDaily();
      $('summary-lock').hidden = allowed;
      $('summary-metrics').hidden = !allowed;
      $('summary-note').hidden = !allowed;
      const totals = view().totals;
      ['pending','completed','cancelled'].forEach(status => $('metric-' + status).textContent = String(totals ? totals[status] : 0));
      $('metric-total').textContent = String(totals ? totals.total : 0);
    }

    function render() { renderControls(); renderSlots(); renderAppointments(); renderSummary(); renderStorage(); }

    function showError(result) {
      const messages = {
        NOT_FOUND: 'Randevu bulunamadı.',
        ROLE: 'Bu rol istenen işlemi yapamaz.',
        OWNER: 'Yalnız kendi randevunuzu iptal edebilirsiniz.',
        STATUS: 'Yalnız Bekliyor durumundaki randevu değiştirilebilir.',
        CONTEXT: 'Hasta, doktor ve tarih seçimini kontrol edin.',
        TIME: 'Önce uygun bir saat seçin.',
        OCCUPIED: 'BR-01: Bu doktor ve saatte iptal edilmemiş bir randevu zaten var. Farklı saat seçin.',
        LIMIT: 'Bu küçük demo en fazla 1.000 kayıt saklar. Bulgularınızı kaydedip örnek veriyi sıfırlayabilirsiniz.',
        WRITE: 'İşlem oturum verisine uygulanamadı.'
      };
      notify(messages[result.code] || 'İşlem uygulanamadı.', 'error');
      return false;
    }
    function bookAppointment() {
      const result = service.book(state, state.selectedTime);
      if (!result.ok) {
        if (result.code === 'OCCUPIED') { state.selectedTime = null; render(); }
        return showError(result);
      }
      const appointment = result.appointment;
      state.selectedTime = null; render();
      notify(appointment.id + ' oluşturuldu: ' + PATIENTS[appointment.patientId] + ', ' + dateLabel(appointment.date) + ' saat ' + appointment.time + '. B2 alanında kaydı inceleyin.','success');
      return true;
    }
    function cancelAppointment(id) {
      const eligibility = service.cancelEligibility(id, state);
      if (!eligibility.ok) return showError(eligibility);
      const appointment = eligibility.appointment;
      if (!window.confirm(
        appointment.id + ' — ' + dateLabel(appointment.date) + ' saat ' + appointment.time + '\n\n' +
        'Tamam: Randevuyu iptal eder. İptal edilen kayıt listede kalır. Aynı doktor, tarih ve saatte başka iptal edilmemiş kayıt yoksa saat yeniden uygun olur.\n\n' +
        'İptal: İşlemden vazgeçer; randevunuz Bekliyor durumunda kalır.\n\n' +
        'Randevunuzu iptal etmek istiyor musunuz?'
      )) return false;
      const result = service.cancel(id, state);
      if (!result.ok) return showError(result);
      render();
      const slotMessage = result.slotAvailable ? 'İlgili saat yeniden uygun.' : 'Bu saatte başka iptal edilmemiş kayıt var; saat uygun değil.';
      notify(appointment.id + ' iptal edildi. ' + slotMessage + ' İptal kaydı geçmişte görünmeye devam eder.','success');
      return true;
    }
    function completeAppointment(id) {
      const result = service.complete(id, state);
      if (!result.ok) return showError(result);
      render();
      notify(id + ' Tamamlandı durumuna geçti. Günlük toplamlar güncellendi; bu saat yeniden açılmaz.','success');
      return true;
    }

    document.querySelectorAll('[data-role]').forEach(button => button.addEventListener('click',() => {
      state.role = button.dataset.role; state.selectedTime = null; render();
      notify(ROLE_LABELS[state.role] + ' rolüne geçildi. Görünen liste ve izin verilen işlemleri karşılaştırın.');
    }));
    ['patient','doctor','date'].forEach(field => $(field + '-select').addEventListener('change',event => {
      if (field === 'patient') state.patientId = event.target.value;
      else if (field === 'doctor') state.doctorId = event.target.value;
      else state.date = event.target.value;
      state.selectedTime = null; render(); notify('Seçim güncellendi. Saatler ve kayıtlar seçili doktor ve tarihe göre gösteriliyor.');
    }));
    $('slots').addEventListener('click',event => {
      const button = event.target.closest('button[data-time]');
      if (!button || button.disabled || !canBook()) return;
      state.selectedTime = button.dataset.time; renderSlots();
      notify(state.selectedTime + ' seçildi. Randevuyu onaylamadan önce hasta, doktor ve tarihi kontrol edin.');
    });
    $('book-appointment').addEventListener('click',bookAppointment);
    $('appointments').addEventListener('click',event => {
      const button = event.target.closest('button[data-action]');
      if (!button) return;
      if (button.dataset.action === 'cancel') cancelAppointment(button.dataset.id);
      if (button.dataset.action === 'complete') completeAppointment(button.dataset.id);
    });
    $('reset-data').addEventListener('click',() => {
      if (!window.confirm('Bu prototipte yaptığınız yerel randevu değişiklikleri silinecek ve başlangıçtaki örnek kayıtlar yüklenecek. Devam edilsin mi?')) return;
      service.reset(); Object.assign(state,{role:'patient',patientId:'ece',doctorId:'deniz',date:DATES[0],selectedTime:null});
      render(); notify('Başlangıçtaki sentetik veriler yüklendi. Hasta rolü, Ece Yılmaz ve 12 Kasım 2030 seçili.','success');
    });
    render(); if (service.startupMessage) notify(service.startupMessage);
})();
