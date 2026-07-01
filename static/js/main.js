/* ============================================================
   JobPortal System – Main JavaScript
   ============================================================ */

'use strict';

/* ---------- Auto-dismiss flash alerts after 5s ---------- */
document.addEventListener('DOMContentLoaded', function () {
  const alerts = document.querySelectorAll('.alert.fade.show');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      if (bsAlert) bsAlert.close();
    }, 5000);
  });

  /* ---------- Navbar active link highlight ---------- */
  const currentPath = window.location.pathname;
  document.querySelectorAll('#mainNav .nav-link').forEach(function (link) {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
      link.style.color = '#ffc107';
    }
  });

  /* ---------- Animate stat counters on landing page ---------- */
  const counters = document.querySelectorAll('.counter');
  if (counters.length) {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    });
    counters.forEach(function (c) { observer.observe(c); });
  }

  /* ---------- Character counter for textareas ---------- */
  document.querySelectorAll('textarea[maxlength]').forEach(function (ta) {
    const max  = parseInt(ta.getAttribute('maxlength'));
    const info = document.createElement('small');
    info.className = 'text-muted float-end';
    info.textContent = '0 / ' + max;
    ta.parentNode.insertBefore(info, ta.nextSibling);
    ta.addEventListener('input', function () {
      info.textContent = ta.value.length + ' / ' + max;
      info.style.color = ta.value.length > max * 0.9 ? '#dc3545' : '';
    });
  });

  /* ---------- Confirm delete buttons ---------- */
  document.querySelectorAll('[data-confirm]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      if (!confirm(btn.dataset.confirm)) e.preventDefault();
    });
  });

  /* ---------- Skill tag input helper (comma → badge preview) ---------- */
  const skillsInput = document.querySelector('input[name="skills_required"], input[name="skills"]');
  if (skillsInput) {
    const preview = document.createElement('div');
    preview.className = 'mt-2 skill-preview';
    skillsInput.parentNode.insertBefore(preview, skillsInput.nextSibling);
    skillsInput.addEventListener('input', function () {
      preview.innerHTML = '';
      skillsInput.value.split(',').forEach(function (sk) {
        const s = sk.trim();
        if (s) {
          const badge = document.createElement('span');
          badge.className = 'badge bg-primary bg-opacity-10 text-primary border me-1 mb-1';
          badge.textContent = s;
          preview.appendChild(badge);
        }
      });
    });
  }

  /* ---------- Form validation feedback ---------- */
  const forms = document.querySelectorAll('form.needs-validation');
  forms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      if (!form.checkValidity()) {
        e.preventDefault();
        e.stopPropagation();
      }
      form.classList.add('was-validated');
    });
  });
});

/* ---------- Counter animation ---------- */
function animateCounter(el) {
  const target = parseInt(el.textContent.replace(/\D/g, '')) || 0;
  let current  = 0;
  const step   = Math.max(1, Math.floor(target / 60));
  const timer  = setInterval(function () {
    current += step;
    if (current >= target) { current = target; clearInterval(timer); }
    el.textContent = current;
  }, 20);
}

/* ---------- Password strength indicator ---------- */
function checkPasswordStrength(pwd) {
  let strength = 0;
  if (pwd.length >= 8)           strength++;
  if (/[A-Z]/.test(pwd))        strength++;
  if (/[0-9]/.test(pwd))        strength++;
  if (/[^A-Za-z0-9]/.test(pwd)) strength++;
  return strength;
}

/* ---------- Smooth scroll to top ---------- */
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
