
const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelector(".nav-links");

    burger.addEventListener('click', () => {
    //Toggle links
        nav.classList.toggle('nav-active');

    //Animate links
        Array.prototype.forEach.call(navLinks.children, children => {
        console.log(children);
        if (children.style.animation){
            children.style.animation = '';

        }
        else {
            children.style.animation = 'navLinkFade .5s ease forwards 0.5s';


        }




        });
        //Burger Animation
        burger.classList.toggle('toggle');

    });

}

navSlide();






