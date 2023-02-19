var popIT = document.querySelector('#popUP');
var checkerboard = document.querySelector('#checker');
var header = document.querySelector('#trigger');


function pops(e){
    popIT.style.display = 'block';
    checkerboard.style.display = 'none';
    header.innerText = 'NINJAAA'
}

function popout(e) {
    popIT.style.display = 'none';
    checkerboard.style.display = 'block';
    header.innerText = '***Checkerboard***';
}