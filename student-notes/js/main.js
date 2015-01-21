function toggleVocabDescriptionOnClick() {
	var description = this.getElementsByClassName('vocab-description')[0];
	var disp = description.style.display;
	if (disp == '') {
		description.style.display = 'inline-block';
	} else {
		description.style.display = '';
	}
}

var vocabTerms = document.getElementsByClassName('vocab-term-container');
var term;
for (var i=0; i<vocabTerms.length; i++){
	term = vocabTerms[i];
	term.addEventListener('click', toggleVocabDescriptionOnClick);
}