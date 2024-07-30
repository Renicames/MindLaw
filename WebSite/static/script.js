document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll(".navbar nav ul li a");

    links.forEach(link => {
        link.addEventListener("click", function(e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);
            window.scrollTo({
                top: targetElement.offsetTop - document.querySelector(".navbar").offsetHeight,
                behavior: "smooth"
            });
        });
    });
});
