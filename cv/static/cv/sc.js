const menu = document.querySelector('.menu');
const ouvrir = document.querySelector('.open');
const fermer = document.querySelector('.close');
const logo = document.querySelector('.logo')

ouvrir.addEventListener('click', () =>{
    menu.style.display = 'flex';
    menu.style.height = '100vh'

})

fermer.addEventListener('click', () =>{
    menu.style.display = 'none';
    menu.style.height = '0vh'

})


if(screen.width == 320) {
    logo.style.marginLeft = '0px';
}else {
    logo.style.marginLeft = '30px'
}