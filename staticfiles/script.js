var swiper = new Swiper(".slide-content", {
  slidesPerView: "auto", // Set slidesPerView to "auto" to adjust the number of visible slides dynamically
  spaceBetween: 30,
  loop: true,
  loopFillGroupWithBlank: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    768: {
      slidesPerView: 3, // Show 3 slides per view on screens larger than or equal to 768px
    },
  },
});
