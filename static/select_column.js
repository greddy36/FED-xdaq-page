        // Function to handle column selection
        function handleColumnSelection() {
            const checkboxes = document.querySelectorAll('.column-selector');
            checkboxes.forEach(checkbox => {
                const columnKey = checkbox.getAttribute('data-column');
                const cells = document.querySelectorAll(`td[data-column="${columnKey}"]`);
                const headers = document.querySelectorAll(`th[data-column="${columnKey}"]`);
                
                checkbox.addEventListener('change', () => {
                    if (checkbox.checked) {
                        cells.forEach(cell => {
                            cell.style.display = ''; // Show the cell
                        });
                        headers.forEach(header => {
                            header.style.display = ''; // Show the header
                        });
                    } else {
                        cells.forEach(cell => {
                            cell.style.display = 'none'; // Hide the cell
                        });
                        headers.forEach(header => {
                            header.style.display = 'none'; // Hide the header
                        });
                    }
                });
            });
        }
        // Call the function to initialize column selection
        handleColumnSelection();