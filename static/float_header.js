//for floating headers
const tableContainer = document.querySelector('.table-container');
const table = document.querySelector('table');
const tableHeader = document.querySelector('thead');

tableContainer.addEventListener('scroll', () => {
    const scrollTop = tableContainer.scrollTop;
    tableHeader.style.transform = `translateY(${scrollTop}px)`;
});