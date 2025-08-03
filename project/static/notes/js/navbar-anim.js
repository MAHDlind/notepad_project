document.addEventListener("DOMContentLoaded", function () {
    const toggler = document.querySelector(".navbar-toggler");
    const collapse = document.querySelector(".navbar-collapse");

    if (toggler && collapse) {
        toggler.addEventListener("click", () => {
            collapse.classList.toggle("show");
        });
    }
});
