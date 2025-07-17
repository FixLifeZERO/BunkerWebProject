document.addEventListener('DOMContentLoaded', (event) => {
    // --- Matrix Rain Effect for Main Menu ---
    const canvas = document.getElementById('matrix-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');

        // Set canvas to full screen
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        // Characters to be used - 1s and 0s
        const binary = "10";
        const characters = binary.split('');

        const fontSize = 16;
        const columns = canvas.width / fontSize;

        // Array to store the y-position of each drop
        const drops = [];
        for (let x = 0; x < columns; x++) {
            drops[x] = 1;
        }

        function drawMatrix() {
            // Set a semi-transparent black background to create the fading effect
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Set the color and font for the characters
            ctx.fillStyle = '#0f0'; // Green color
            ctx.font = fontSize + 'px monospace';

            // Loop through each column
            for (let i = 0; i < drops.length; i++) {
                // Get a random character
                const text = characters[Math.floor(Math.random() * characters.length)];
                // Draw the character
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                // Reset drop to the top randomly to make the rain uneven
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }

                // Move the drop down
                drops[i]++;
            }
        }

        // Animate the matrix effect
        setInterval(drawMatrix, 33);

        // Adjust canvas size on window resize
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            // Recalculate columns on resize, though it might not be perfect without a full reset
        });
    }
});

// --- Laptop Modal Toggle Function ---
function toggleLaptop() {
    const modal = document.getElementById('laptop-modal');
    if (modal) {
        modal.classList.toggle('hidden');
    }
}

// --- Laptop Menu Toggle Function ---
function toggleLaptopMenu() {
    const dropdown = document.getElementById('laptop-menu-dropdown');
    if (dropdown) {
        dropdown.classList.toggle('hidden');
    }
}

// --- Search Console Toggle Function ---
function toggleSearchConsole() {
    const console = document.getElementById('search-console');
    console.classList.toggle('hidden');
    if (!console.classList.contains('hidden')) {
        const output = console.querySelector('.console-output');
        output.textContent = 'To activate the "S.F.P.A.I." protocol, write "/start"\n';
        initializeConsole();
    }
}

function initializeConsole() {
    const input = document.getElementById('command-input');
    const output = document.querySelector('.console-output');
    
    input.addEventListener('keypress', async function(e) {
        if (e.key === 'Enter') {
            const command = input.value.trim();
            input.value = '';
            
            if (command === '/start') {
                const response = await fetch('/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ action: 'start_search' })
                });
                
                const data = await response.json();
                if (data.status === 'success') {
                    simulateSearchProcess();
                }
            }
        }
    });
}

async function simulateSearchProcess() {
    const output = document.querySelector('.console-output');
    const searchLines = [
        'Initializing S.F.P.A.I. protocol...',
        'Scanning parallel realities...',
        'Analyzing quantum signatures...',
        'Processing dimensional data...',
        'Checking for compatible entities...',
        'Validating results...'
    ];
    
    output.textContent = '';
    for (const line of searchLines) {
        output.textContent += line + '\n';
        await new Promise(resolve => setTimeout(resolve, 1000));
    }
    
    const response = await fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ action: 'check_search_results' })
    });
    
    const data = await response.json();
    if (data.status === 'success') {
        output.textContent += '\n' + data.message;
    }
}
