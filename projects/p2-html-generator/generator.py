term1 = "HTML"
description1 = "HTML stands for Hypertext Markup Language."
concept1 = [term1, description1]

term2 = "CSS"
description2 = "CSS stands for Cascading Style Sheets."
concept2 = [term2, description2]

concepts = [concept1, concept2]

def add_concept_to_concept_list(term, description, concept_list):
	concept = [term, description]
	concept_list.append(concept)
	return conceptList

def display_all_terms(concept_list, prefix=""):
	for concept in concept_list:
		term = concept[0]
		description = concept[1]
		print prefix + term
		print prefix

def display_all_descriptions(concept_list, prefix=""):
	for concept in concept_list:
		term = concept[0]
		description = concept[1]
		print prefix + description
		print prefix

def generate_question(concept_list):
	description = concept_list[0][1]
	print "What term does the following description apply to?"
	print "| " + description
	print "| " + '#' * len(description)
	print "|"
	display_all_terms(concept_list, prefix = "|   ")
	print "| " + '#' * len(description)


generate_question(concepts)