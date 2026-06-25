// quantity.js
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.quantity-control').forEach(function(control) {
        const input = control.querySelector('input[type="number"]');
        const minusBtn = control.querySelector('.qty-minus');
        const plusBtn = control.querySelector('.qty-plus');
        
        if (!input) return;
        
        const min = parseInt(input.getAttribute('min')) || 1;
        const max = parseInt(input.getAttribute('max')) || 10;
        
        function updateValue(change) {
            let value = parseInt(input.value) || min;
            value = Math.max(min, Math.min(max, value + change));
            input.value = value;
        }
        
        if (minusBtn) {
            minusBtn.addEventListener('click', function() {
                updateValue(-1);
            });
        }
        
        if (plusBtn) {
            plusBtn.addEventListener('click', function() {
                updateValue(1);
            });
        }
        
        input.addEventListener('change', function() {
            let value = parseInt(this.value) || min;
            if (value < min) this.value = min;
            if (value > max) this.value = max;
        });
        
        // Запрет ввода букв
        input.addEventListener('keydown', function(e) {
            if (e.key === 'e' || e.key === 'E' || e.key === '-' || e.key === '+') {
                e.preventDefault();
            }
        });
    });
});