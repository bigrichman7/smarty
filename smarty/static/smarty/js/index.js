

    let index_flex_blocks = document.getElementsByClassName('index-flex-block');

    for (let block of index_flex_blocks) {
        block.addEventListener('mouseover', (event) => {
            block.getElementsByClassName('index-module-name')[0].style.marginTop = "-55px";
        });
        block.addEventListener('mouseleave', (event) => {
            block.getElementsByClassName('index-module-name')[0].style.marginTop = "70px";
        })
    }