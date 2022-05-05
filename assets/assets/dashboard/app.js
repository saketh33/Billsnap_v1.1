var lastNewEducationalInfoDiv = 0;

function createTag(parent, content) {
	parent = parent.trim();
	content = content.trim();
	document.getElementById(parent).innerHTML +=
		"<div class='tag' onclick='destroy(\"" +
		parent +
		'", "' +
		content +
		'")\'>' +
		content +
		'</div>';
}

function destroy(parent, content) {
	console.log(parent, content);
	document.getElementById(parent).childNodes.forEach(function (node) {
		if (node.textContent !== undefined) {
			var comparetext = node.textContent.trim();
		} else {
			return;
		}
		if (comparetext === content) {
			node.remove();
		}
	});
}
document.addEventListener('keydown', function (e) {
	if (
		(e.key === ' ' || e.key === 'Enter') &&
		e.target.id === 'skills' &&
		e.target.value !== undefined &&
		e.target.value.trim() !== ''
	) {
		createTag('skillsTags', e.target.value.trim().toUpperCase());
		e.target.value = '';
	}
	if (
		(e.key === ' ' || e.key === 'Enter') &&
		e.target.id === 'spokenLanguages' &&
		e.target.value !== undefined &&
		e.target.value.trim() !== ''
	) {
		createTag('spokenLanguagesTags', e.target.value.trim().toUpperCase());
		e.target.value = '';
	}
});

function addmoreforms() {
	console.log('herer');
	lastNewEducationalInfoDiv += 1;
	document.getElementsByClassName(
		'editProfiletabcontentTwo',
	)[0].innerHTML += `<div class="Educational_edit" id=educationalinfoform-collection_${lastNewEducationalInfoDiv}> <div class="deleteButton" onclick="destroyForm('educationalinfoform-collection_${lastNewEducationalInfoDiv}')\" data-eduformid=educationalinfoform-collection_${lastNewEducationalInfoDiv} >Remove</div> <div class="title">Highest Qualification Details</div> <div class="form__group field"><input type="input" class="form__field" placeholder="Institution" name="Institution" id="Institution" required /> <label for="Email" class="form__label" >Institution </label> </div> <div class="Educational_input_section" ><div class="form__group field"><input type="input" class="form__field" placeholder="YearofPassinge.g.2019" name="YearofPassing" id="YearofPassing" required /> <labelfor="YearofPassing" class="form__label">Year of Passing </label></div><div class="form__group field"> <select name="SelectState" id="SelectState" class="form__field"><option value="" disabled selected hidden >SelectState </option> <option value="SelectState"> Male </option> <option value="SelectState"> Female </option> </select> </div> </div> <div class="Educational_input_section"><div class="Educational_input_radio_buttons custom_radio"><input type="radio" id="featured-1_${lastNewEducationalInfoDiv}" name="featured_${lastNewEducationalInfoDiv}" checked><label for="featured-1_${lastNewEducationalInfoDiv}">Percentage</label><input type="radio" id="featured-2_${lastNewEducationalInfoDiv}" name="featureds_${lastNewEducationalInfoDiv}"><label for="featured-2_${lastNewEducationalInfoDiv}">CGPA </label> </div><div class="form__group field"> <input type="input" class="form__field" placeholder="CGPA" name="CGPA" id="CGPA" required/> <label for="CGPA" class="form__label"> CGPA </label> </div> <div class="form__group field"> <input type="input" class="form__field" placeholder="Scale/Outof" name="Scale/Outof" id="Scale/Outof" required/><label for="Scale/Outof" class="form__label">Scale / Out of </label> </div> </div>  </div>`;
}
function destroyForm(parent, childID) {
	document.getElementById(parent).childNodes.forEach(function (element) {
		if (element.classList !== undefined) {
			if (element.getAttribute('data-eduformid')) {
				document
					.getElementById(element.getAttribute('data-eduformid'))
					.remove();
			}
		}
	});
}
/* const destroyForm = () => {
	console.log(e);
};
 */
function launch_toast() {
	var x = document.getElementById('toast');
	x.className = 'show';
	setTimeout(function () {
		x.className = x.className.replace('show', '');
	}, 5000);
}
const Profile = document.querySelector('.avatar');
const Profile_dropDown = document.querySelector('.profile_dropDown');
Profile.addEventListener('click', () => {
	if (Profile_dropDown.style.opacity === '1') {
		Profile_dropDown.style.opacity = '0';
		Profile_dropDown.style.pointerEvents = 'none';
	} else {
		Profile_dropDown.style.opacity = '1';
		Profile_dropDown.style.pointerEvents = 'all';
	}
});
const notification_bell = document.querySelector('.notification_bell');
const notification_dropDown = document.querySelector('.notification_dropdown');
notification_bell.addEventListener('click', () => {
	console.log('here');
	if (notification_dropDown.style.opacity === '1') {
		notification_dropDown.style.opacity = '0';
		notification_dropDown.style.pointerEvents = 'none';
	} else {
		notification_dropDown.style.opacity = '1';
		notification_dropDown.style.pointerEvents = 'all';
	}
});
//--------------------------------------------------------------------------
const goalsSection = document.querySelector('.goals_DropDown');
const goalButton = document.querySelector('.points');

const goalsDrop = () => {
	if (goalsSection.style.visibility == 'visible') {
		goalsSection.style.visibility = 'hidden';
	} else {
		goalsSection.style.visibility = 'visible';
	}
};
const powerSection = document.querySelector('.power_dropDown');
const coinSection = document.querySelector('.coin_dropDown');

const powerhandler = () => {
	if (powerSection.style.visibility == 'visible') {
		powerSection.style.visibility = 'hidden';
	} else {
		powerSection.style.visibility = 'visible';
	}
};
const Coinhandler = () => {
	if (coinSection.style.visibility == 'visible') {
		coinSection.style.visibility = 'hidden';
	} else {
		coinSection.style.visibility = 'visible';
	}
};
const power = document.querySelector('.shock');
const coin = document.querySelector('.coin');
//--------------------------------
document.addEventListener('click', function (event) {
	var isClickInsideAvatar = Profile.contains(event.target);
	var isClickInsideBell = notification_bell.contains(event.target);
	var isClickInsideDropdown = notification_dropDown.contains(event.target);
	var isClickInsideGoal = goalButton.contains(event.target);
	var isClickInsideGoalSection = goalsSection.contains(event.target);
	let isClickInsideShock = power.contains(event.target);
	let isClickInsideCoin = coin.contains(event.target);

	if (!isClickInsideAvatar) {
		Profile_dropDown.style.opacity = '0';
		Profile_dropDown.style.pointerEvents = 'none';
	}
	if (!isClickInsideShock) {
		powerSection.style.visibility = 'hidden';
	}
	if (!isClickInsideCoin) {
		coinSection.style.visibility = 'hidden';
	}
	if (!isClickInsideGoal && !isClickInsideGoalSection) {
		goalsSection.style.visibility = 'hidden';
	}
	if (!isClickInsideBell && !isClickInsideDropdown) {
		notification_dropDown.style.opacity = '0';
		notification_dropDown.style.pointerEvents = 'none';
	}
});

// ---------leaderboard data------------------------

const slideMenu = () => {
	const sideMenu = document.querySelector('.sideMenu');
	const ham = document.querySelector('#ham_icon');
	if (sideMenu.style.left === '0px') {
		sideMenu.style.left = '-250px';
		ham.src = 'https://img.icons8.com/android/96/000000/menu.png';
	} else {
		ham.src =
			'https://img.icons8.com/material-outlined/24/000000/delete-sign.png';
		sideMenu.style.left = '0';
	}
};
const closeInfo = () => {
	const info = document.querySelector('.info_text');
	info.style.display = 'none';
};