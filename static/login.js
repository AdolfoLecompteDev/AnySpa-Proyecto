// NAV toggle (mobile)
const navToggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav');

if (navToggle && nav) {
  navToggle.addEventListener('click', () => {
    const expanded = navToggle.getAttribute('aria-expanded') === 'true' || false;
    navToggle.setAttribute('aria-expanded', !expanded);
    nav.classList.toggle('mobile-open');
  });
}

// Login form validation (existing, mejorado un poquito)
const form = document.getElementById('loginForm');
if (form) {
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    if (!email || !password) {
      // mejor feedback que alert (aunque alert sirve en demo)
      window.alert('Por favor completa todos los campos.');
      return;
    }

    // aquí iría el fetch al backend; demo:
    window.alert('Login exitoso (demo). Aquí se conectaría con el backend.');
    // form.submit(); // descomentar si quieres enviar a un servidor real
  });
}
