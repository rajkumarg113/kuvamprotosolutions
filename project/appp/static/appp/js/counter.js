document.addEventListener('DOMContentLoaded', function() {
    const counters = document.querySelectorAll('.counter');
    
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight)
        );
    }

    function startCount(counter) {
        const target = parseInt(counter.getAttribute('data-target'));
        let count = 0;
        const duration = 2000; // 2 seconds to count up
        const steps = 50;
        const increment = target / steps;
        const stepTime = duration / steps;

        const timer = setInterval(() => {
            count += increment;
            if (count >= target) {
                counter.innerText = target;
                clearInterval(timer);
            } else {
                counter.innerText = Math.round(count);
            }
        }, stepTime);
    }

    // Initialize all counters to 0
    counters.forEach(counter => {
        counter.innerText = '0';
    });

    // Check counters on scroll
    window.addEventListener('scroll', function() {
        counters.forEach(counter => {
            if (isElementInViewport(counter) && counter.innerText === '0') {
                startCount(counter);
            }
        });
    });
});
