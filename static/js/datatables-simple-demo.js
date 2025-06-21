// window.addEventListener('DOMContentLoaded', event => {
//     // Simple-DataTables
//     // https://github.com/fiduswriter/Simple-DataTables/wiki

//     const datatablesSimple = document.getElementById('datatablesSimple');
//     if (datatablesSimple) {
//         new simpleDatatables.DataTable(datatablesSimple, {
//             perPage: 50, // Default rows per page
//             perPageSelect: [50, 100, 200, 500] // Dropdown options for rows per page
//         });
//     }
// });

document.addEventListener('DOMContentLoaded', function () {
    // Ensure the script runs after the table is available
    const datatablesSimple = document.querySelector('#datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple, {
            perPage: 10, // Adjust the default rows per page
            perPageSelect: [10, 25, 50, 100], // Allow users to select rows per page
            searchable: true, // Enable search functionality
            sortable: true, // Enable sorting
            fixedHeight: false
        });
    }
});