function toggleVocabDescriptionOnClick() {
	description = this.getElementsByClassName('vocab-description')[0];
	disp = description.style.display;
	console.log(disp);
	if (disp == '') {
		description.style.display = 'inline-block';
	} else {
		description.style.display = '';
	}
}

var vocabTerms = document.getElementsByClassName('vocab');
var term, description;
for (var i=0; i<vocabTerms.length; i++){
	term = vocabTerms[i];
	description = term.getElementsByClassName('vocab-description')[0];
	console.log(description);
	term.addEventListener('click', toggleVocabDescriptionOnClick)
}