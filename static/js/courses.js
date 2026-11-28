// Show the selected meeting days in each dropdown.
function setupDayDropdowns() {
    document.querySelectorAll('.days-dropdown').forEach(function (dropdown) {
        const summary = dropdown.querySelector('.days-summary');
        const boxes = dropdown.querySelectorAll('input[type="checkbox"]');

        function updateSummary() {
            const picked = [];
            boxes.forEach(function (box) {
                if (box.checked) picked.push(box.value);
            });
            if (picked.length > 0) {
                summary.textContent = picked.join(', ');
            } else {
                summary.textContent = 'Pick days';
            }
            summary.classList.toggle('days-summary-empty', picked.length === 0);
        }

        boxes.forEach(function (box) {
            box.addEventListener('change', updateSummary);
        });
        document.addEventListener('click', function (event) {
            if (!dropdown.contains(event.target)) dropdown.removeAttribute('open');
        });
        updateSummary();
    });
}

setupDayDropdowns();
