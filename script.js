// This file can be used for future JavaScript interactions, such as:
// - Handling quiz logic for skin type selectio
// - Implementing smooth scrolling for navigation links
// - Adding animations or dynamic content loading

console.log("script.js loaded: Ready for future enhancements!");

document.querySelectorAll('nav ul li a').forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        const targetId = event.target.getAttribute('href').slice(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Suggested navigation links
const navLinks = `
<li><a href="#home">Home</a></li>
<li><a href="#about">About</a></li>
<li><a href="#features">Features</a></li>
<li><a href="#contact">Contact</a></li>
`;

document.querySelector('nav ul').innerHTML += navLinks;

function startQuiz() {
    alert("Quiz functionality coming soon!");
}

document.querySelector('.btn.secondary').addEventListener('click', startQuiz);
