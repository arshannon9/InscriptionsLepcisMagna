// Sorts tables in indices

document.addEventListener("DOMContentLoaded", function () {
    // Get the table rows and convert them to an array
    var rows = Array.from(document.querySelectorAll('tbody tr'));

    // Sort the array based on multiple columns
    rows.sort(function (a, b) {
      // Compare values in each column sequentially
      for (var i = 0; i < a.cells.length; i++) {
        var keyA = a.cells[i].innerText.toUpperCase();
        var keyB = b.cells[i].innerText.toUpperCase();

        if (keyA !== keyB) {
          // If values are different, return the comparison result
          return keyA.localeCompare(keyB);
        }
      }

      // If all values are equal, no change in order
      return 0;
    });

    // Remove existing rows and append the sorted rows
    var tbody = document.querySelector('tbody');
    rows.forEach(function (row) {
      tbody.appendChild(row);
    });
  });