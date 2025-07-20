window.addEventListener("load", () => {
  document.querySelectorAll('.fade-in, .fade-in-delay').forEach((el, i) => {
    el.style.opacity = 0;
    el.style.transform = "translateY(20px)";
    el.style.transition = `opacity 0.8s ease ${i * 0.3}s, transform 0.8s ease ${i * 0.3}s`;

    setTimeout(() => {
      el.style.opacity = 1;
      el.style.transform = "translateY(0)";
    }, 50);
  });
});
