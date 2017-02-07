
window.onload = function(){
  const mainNav = document.querySelector(".main-nav");
  let stickingPoint = mainNav.offsetTop;


  function stickyNav(){
    if(window.scrollY >= stickingPoint){
      document.body.style.paddingTop = mainNav.offsetHeight;
      document.body.classList.add("sticky-nav");
      document.querySelector(".main-nav").style.position = "fixed";

    }else{
      document.body.style.paddingTop = 0;
      document.body.classList.remove("sticky-nav");
      document.querySelector(".main-nav").style.position = "relative";
    }
  }

  window.addEventListener("scroll", stickyNav);

  /* ----- Smooth-Scroll */

   smoothScroll.init({
     offset: 120
   });

  /* --- Hamburger Menu Code */
   const hamburgerButton = document.querySelector(".fa-bars");
   const xButton = document.querySelector(".fa-times");
   const nav = document.querySelector(".header-nav-items");
   const socialIcons = document.querySelector(".social-icon-wrapper");

   function hamburgerMenu(){
     nav.style.display = "flex";
     xButton.style.display = "flex";
     socialIcons.style.display = "flex";
     hamburgerButton.style.display = "none";
   }
   function xButtonMenu(){
    hamburgerButton.style.display = "flex";
    xButton.style.display = "none";
    nav.style.display = "none";
    socialIcons.style.display = "none";

   }
   function navBarLoaded(){
     nav.style.display = "flex";
     socialIcons.style.display = "flex";
   }

   function windowSize(){
     if(window.innerWidth >= 650){
       nav.style.display = "flex";
       socialIcons.style.display = "flex";

     }else{
       nav.style.display = "none";
       socialIcons.style.display = "none";
     }


   }

   hamburgerButton.addEventListener('click', hamburgerMenu);
   xButton.addEventListener('click', xButtonMenu);
   window.addEventListener("load", navBarLoaded);
   window.addEventListener('resize', windowSize);


}
