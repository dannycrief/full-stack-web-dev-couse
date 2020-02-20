let button = document.querySelector('.popup-button');

    	button.addEventListener('mouseover', showPopup);

    	function showPopup() {
        	document.querySelector('.popup').classList.add('visible');
    	}

    	button.addEventListener('mouseout', hidePopup);

    	function hidePopup() {
        	document.querySelector('.popup').classList.remove('visible');
    	}