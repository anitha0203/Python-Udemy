// JavaScript for Chess Game
function handleMove(src_row, src_col) {
    var validMoves = getValidMoves(src_row, src_col);
    var selectedCell = document.getElementById('cell-' + src_row + '-' + src_col);

    if (selectedCell.classList.contains('selected')) {
        // Deselect the piece
        selectedCell.classList.remove('selected');
    } else {
        // Select the piece and highlight valid moves
        document.querySelectorAll('.selected').forEach(function(cell) {
            cell.classList.remove('selected');
        });

        selectedCell.classList.add('selected');

        validMoves.forEach(function(move) {
            var destCell = document.getElementById('cell-' + move[0] + '-' + move[1]);
            destCell.classList.add('valid-move');
        });
    }
}

function getValidMoves(src_row, src_col) {
    // Send an AJAX request to the server to get the valid moves for the selected piece
    // You need to implement the server-side logic for this
    // ...

    // For now, let's assume all moves are valid for demonstration purposes
    var validMoves = [];
    for (var row = 0; row < 8; row++) {
        for (var col = 0; col < 8; col++) {
            validMoves.push([row, col]);
        }
    }
    return validMoves;
}

function playMove(dest_row, dest_col) {
    var srcCell = document.querySelector('.selected');
    if (!srcCell) return; // No piece selected, ignore

    var src_row = parseInt(srcCell.getAttribute('data-row'));
    var src_col = parseInt(srcCell.getAttribute('data-col'));

    // Send an AJAX request to the server to make the move
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = JSON.parse(this.responseText);
            if (response.status === 'success') {
                // Move the piece on the frontend
                var destCell = document.getElementById('cell-' + dest_row + '-' + dest_col);
                destCell.innerText = srcCell.innerText;
                srcCell.innerText = '';
                destCell.classList.remove('valid-move');
                srcCell.classList.remove('selected');
            } else if (response.status === 'invalid_move') {
                alert('Invalid move! Try again.');
            }
        }
    };

    xhttp.open('POST', '/', true);
    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.send('src_row=' + src_row + '&src_col=' + src_col + '&dest_row=' + dest_row + '&dest_col=' + dest_col);
}
