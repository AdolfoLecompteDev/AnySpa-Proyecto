// Seleccionamos el botón y el menú
const toggleBtn = document.querySelector('.menu-toggle');
const menu = document.querySelector('.menu');
const menuLinks = document.querySelectorAll('.menu a');
const menuIcon = document.getElementById('menu-icon');

// Mostrar/ocultar el menú al hacer clic en el botón hamburguesa
toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('show');

    // Cambiar ícono hamburguesa <-> X
    if (menu.classList.contains('show')) {
        menuIcon.classList.remove('bi-list');
        menuIcon.classList.add('bi-x');
    } else {
        menuIcon.classList.remove('bi-x');
        menuIcon.classList.add('bi-list');
    }
});

// Cerrar el menú cuando se hace clic en cualquier enlace del menú
menuLinks.forEach(link => {
    link.addEventListener('click', () => {
        menu.classList.remove('show');
        menuIcon.classList.remove('bi-x');
        menuIcon.classList.add('bi-list');
    });
});
