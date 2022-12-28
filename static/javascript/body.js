//text-effects
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    console.log(entry);
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    } else {
      entry.target.classList.remove("show");
    }
  });
});
const hiddenElements = document.querySelectorAll(
  ".centered , .left , .right , .up , .glow-on-hover , .small-left"
);
hiddenElements.forEach((el) => observer.observe(el));

//varloader
var loader = document.getElementById("preloader");
window.addEventListener("load", function () {
  loader.style.display = "none";
});

// const text = document.querySelector(".beauty");
// const strText = text.textContent;
// const splitText = strText.split(" ");
// text.textContent = " ";
// for (let i = 0; i < splitText.length; i++) {
//   text.innerHTML += "<span>" + splitText[i] + "</span>";
// }
// let char = 0;
// let timer = setInterval(onTick, 50);

// function onTick() {
//   const span = text.querySelectorAll("span")[char];
//   span.classList.add("fade");
//   char++;
//   if (char === splitText.length) {
//     complete();
//     return;
//   }
// }//

// function complete() {
//   clearInterval(timer);
//   timer = null;
// }
// //owl carasoul
// $(document).ready(function () {
//   $(".owl-carousel").owlCarosuel({
//     items:1,
//     loop:Infinity,
//     nav: true,
//     dots:true,
//     autoplay:true,
//     autospeed:1000,
//     smartSpeed:15000,
//   });
// });

window.addEventListener("load", function () {
  this.setTimeout(function open(event) {
    document.querySelector(".popup").style.display = "block;";
  }, 1000);
});

document.querySelector("#close").addEventListener("click", function () {
  document.querySelector(".popup").style.display = "none";
});

//
$.letItSnow('main', {
  stickyFlakes: 'lis-flake--js',
  makeFlakes: true,
  sticky: true
});