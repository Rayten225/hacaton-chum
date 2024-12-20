// burger menu
const burgerButton = document.querySelector('.burger-button');
const burgerMenu = document.querySelector('.burger-menu')
let body = document.querySelector('body');

function toggleBurger() {
    burgerButton.classList.toggle('active')
    burgerMenu.classList.toggle('active')
    body.classList.toggle('lock');
}

burgerButton.addEventListener('click', toggleBurger)

