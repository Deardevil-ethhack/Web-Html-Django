let body = document.querySelector('body');
let progress = document.getElementById('progressbar');
let totalHeight = document.body.scrollHeight - window.innerHeight;
let dark_btn = document.getElementsByClassName('dark-btn')

window.onscroll= function () {
    let progressHeight = (window.pageYOffset / totalHeight) *100;
    progress.style.width = progressHeight + "%";
}

dark_btn.onclick = ()=>{
    body.classList.toggle("dark");
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.top = "0px";
  modal.style.backgroundColor = "rgba(0,0,0,0.4)";
  modal.style.height = "200%";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.top = "-400px";
    modal.style.backgroundColor = "rgba(0,0,0,0.4)";
    modal.style.height = "0%";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.top = "-400px";
    modal.style.backgroundColor = "rgba(0,0,0,0.4)";
    modal.style.height = "0%";
  }
}

let slider_link = document.getElementById("slider-links");
let slider_check = document.getElementById("slider-check");
let nav_cross = document.getElementById("nav-cross");
let slider = document.querySelector(".slider");
let section = document.querySelector("section");
let slider_style = getComputedStyle(slider);

if (window.innerWidth <= 700){

    slider_check.onclick = function() {
    section.style.marginLeft = "0px";
    slider.style.left = "0px";
  }
  
  slider_check.onclick = function() {
      slider.style.left = "-600px";
      section.style.marginLeft = "0px";
  }
  
  nav_cross.onclick = function() {
    slider.style.left = "-600px";
    section.style.marginLeft = "0px";
  }
} else  {
  
  slider_check.onclick = function() {
    section.style.marginLeft = "250px";
    slider.style.left = "0px";
  }
  
  slider_link.onclick = function() {
      slider.style.left = "-500px";
      section.style.marginLeft = "0px";
  }
  
  nav_cross.onclick = function() {
    slider.style.left = "-500px";
    section.style.marginLeft = "0px";
  }
}




