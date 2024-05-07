function HideShow_01() {
    const toggleButton_01 = document.getElementById('toggleButton_01');
    const info_div_01 = document.getElementById('flyer-div-description');

    try {
        if (info_div_01.style.display === 'flex') {

            info_div_01.classList.remove('div-description-transition-01');
            info_div_01.style.display = 'none'; 
            toggleButton_01.classList.remove('rotated-01');

        } else {
            
            info_div_01.classList.add('div-description-transition-01');
            toggleButton_01.classList.add('rotated-01');
            info_div_01.style.display = 'flex';
        }
    } catch (error) {
        console.error('Error: ', error);
    }
};

function HideShow_02() {
    const toggleButton_02 = document.getElementById('toggleButton_02');
    const info_div_02 = document.getElementById('business-proposal-div-description');

    try {
        if (info_div_02.style.display === 'flex') {

            info_div_02.classList.remove('div-description-transition-02');
            info_div_02.style.display = 'none'; 
            toggleButton_02.classList.remove('rotated-02');

        } else {
            
            info_div_02.classList.add('div-description-transition-02');
            toggleButton_02.classList.add('rotated-02');
            info_div_02.style.display = 'flex';
        }
    } catch (error) {
        console.error('Error: ', error);
    }
};

function HideShow_03() {
    const toggleButton_03 = document.getElementById('toggleButton_03');
    const info_div_03 = document.getElementById('store-advertizing-div-description');

    try {
        if (info_div_03.style.display === 'flex') {

            info_div_03.classList.remove('div-description-transition-03');
            info_div_03.style.display = 'none'; 
            toggleButton_03.classList.remove('rotated-03');

        } else {
            
            info_div_03.classList.add('div-description-transition-03');
            toggleButton_03.classList.add('rotated-03');
            info_div_03.style.display = 'flex';
        }
    } catch (error) {
        console.error('Error: ', error);
    }
};
