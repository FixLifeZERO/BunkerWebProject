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
    const notificationMarker = document.querySelector('.notification-marker');
    
    if (modal) {
        modal.classList.toggle('hidden');
        if (!modal.classList.contains('hidden')) {
            checkSearchResults();
            // Remove notification marker when opening laptop
            if (notificationMarker) {
                notificationMarker.remove();
            }
        }
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
    const input = document.getElementById('command-input');
    const output = document.querySelector('.console-output');

    if (console.classList.contains('hidden')) {
        console.classList.remove('hidden');
        // Only initialize if there's no active search
        if (!output.dataset.searchAnimation && !output.dataset.hasResult) {
            output.textContent = 'To activate the "S.F.P.A.I." protocol, write "/start"\n';
            input.style.display = 'block';
            initializeConsole();
        }
    } else {
        console.classList.add('hidden');
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
                try {
                    const response = await fetch('/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ 
                            action: 'start_search',
                            command: '/start'
                        })
                    });
                    
                    const data = await response.json();
                    if (data.success) {
                        simulateSearchProcess();
                    }
                } catch (error) {
                    console.error('Error:', error);
                }
            }
        }
    });
}

async function simulateSearchProcess() {
    const output = document.querySelector('.console-output');
    const input = document.getElementById('command-input');
    const searchLines = [
        'Initializing S.F.P.A.I. protocol...',
        'Scanning parallel realities...',
        'Analyzing quantum signatures...',
        'Processing dimensional data...',
        'Checking for compatible entities...',
        'Validating results...',
        'Scanning...'
    ];
    
    // Hide input
    input.style.display = 'none';
    
    // Clear and start animation
    output.textContent = '';
    let currentLine = 0;
    
    // Create repeating animation
    const animation = setInterval(() => {
        output.textContent = searchLines.slice(0, currentLine + 1).join('\n');
        currentLine = (currentLine + 1) % searchLines.length;
    }, 1000);

    // Store animation ID in data attribute
    output.dataset.searchAnimation = animation;
}

// Add function to check search results when reopening laptop
async function checkSearchResults() {
    const output = document.querySelector('.console-output');
    const input = document.getElementById('command-input');
    
    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ action: 'check_search_results' })
        });
        
        const data = await response.json();
        if (data.status === 'success') {
            if (data.message) {
                // If we have a result, show it and clean up
                if (output.dataset.searchAnimation) {
                    clearInterval(parseInt(output.dataset.searchAnimation));
                    delete output.dataset.searchAnimation;
                }
                output.textContent = data.message;
                output.dataset.hasResult = 'true';
                input.style.display = 'none';
            } else if (output.dataset.searchAnimation) {
                // If search is in progress, continue animation
                input.style.display = 'none';
            } else if (!output.dataset.hasResult) {
                // Only show initial message if we don't have a result
                output.textContent = 'To activate the "S.F.P.A.I." protocol, write "/start"\n';
                input.style.display = 'block';
                initializeConsole();
            }
        }
    } catch (error) {
        console.error('Error checking search results:', error);
    }
}

// --- Modules Panel Toggle Function ---
function toggleModulesPanel() {
    const panel = document.getElementById('modules-panel');
    if (panel) {
        panel.classList.toggle('hidden');
    }
}

// --- Diary Panel Toggle Function ---
function toggleDiary() {
    const panel = document.getElementById('diary-panel');
    const notificationMarker = document.querySelector('#diaryButton .notification-marker');
    
    if (panel) {
        panel.classList.toggle('hidden');
        // Remove notification marker when opening diary
        if (notificationMarker) {
            notificationMarker.remove();
        }
    }
}

// --- Day Transition Animation ---
function showDayTransition(dayNumber) {
    const overlay = document.getElementById('dayTransition');
    
    // Show overlay
    overlay.classList.add('visible');
    
    // Hide after 2 seconds
    setTimeout(() => {
        overlay.classList.remove('visible');
    }, 2000);
}

// Modify the existing form submissions to handle day transitions
document.addEventListener('DOMContentLoaded', () => {
    // Check if we need to show day transition
    const urlParams = new URLSearchParams(window.location.search);
    const newDay = urlParams.get('new_day');
    if (newDay === 'true') {
        showDayTransition();
        // Clean up URL
        window.history.replaceState({}, document.title, window.location.pathname);
    }
});
